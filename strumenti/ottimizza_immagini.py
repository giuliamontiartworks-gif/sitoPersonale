# -*- coding: utf-8 -*-
"""
Prepara le immagini del sito: dalle foto ORIGINALI (grandi, pesanti) crea le
versioni LEGGERE che il sito mostra davvero.

PERCHE' SERVE
  Le foto originali (anche 30 MB e 70 megapixel) rendono il sito lentissimo e
  Safari, soprattutto su iPhone/iPad, si rifiuta di mostrare le piu' grandi.
  Questo script le ridimensiona e le comprime SENZA cambiare l'aspetto:
    - rotazione: applicata (le foto da telefono non ruotano di colpo)
    - colori: il profilo colore incorporato (sRGB, Display P3...) viene conservato
    - trasparenza: se una PNG e' davvero trasparente resta PNG
    - proporzioni: invariate (si riduce soltanto la risoluzione)

COME SI USA
  1. Metti le foto ORIGINALI in una cartella FUORI dal progetto, una
     sottocartella per progetto con lo stesso nome della cartella del sito:
         Desktop/curriculum/originali-progetti/eme/01.jpg
  2. Dalla cartella del progetto, con l'ambiente virtuale attivo:
         python strumenti/ottimizza_immagini.py            (tutti i progetti)
         python strumenti/ottimizza_immagini.py eme avsi   (solo questi)
  3. Le versioni leggere finiscono in static/img/progetti/<progetto>/ e la
     miniatura della copertina in static/img/progetti/<progetto>/miniature/.
  Gli originali NON vengono mai modificati.

Serve la libreria Pillow:  pip install pillow   (solo per questo script: il
sito vero non la usa, quindi non sta in requirements.txt).
"""

import argparse
import io
import os
import shutil
import sys

from PIL import Image, ImageCms, ImageOps

# Alcune foto sono enormi (70+ megapixel): Pillow di default ha paura e rifiuta.
Image.MAX_IMAGE_PIXELS = None

# ------------------------------------------------------------------ IMPOSTAZIONI
LATO_MAX = 2400          # px del lato piu' lungo per le immagini del sito
MINIATURA_LATO = 1200    # px del lato piu' lungo per la miniatura delle card
QUALITA_FOTO = 90        # JPEG per le foto: alta, per non alterare colori e dettagli
QUALITA_GRAFICA = 92     # JPEG per ex-PNG (mockup, schermate, testi: servono bordi netti)
QUALITA_MINIATURA = 85

ESTENSIONI_IMMAGINE = (".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif")
ESTENSIONI_VIDEO = (".mp4", ".webm")

# Cartelle di default (rispetto alla cartella del progetto).
CARTELLA_PROGETTO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGINALI_DEFAULT = os.path.join(os.path.dirname(CARTELLA_PROGETTO), "originali-progetti")
USCITA_DEFAULT = os.path.join(CARTELLA_PROGETTO, "static", "img", "progetti")

# Profilo sRGB "standard" (588 byte), usato quando si converte da CMYK.
_SRGB = ImageCms.ImageCmsProfile(ImageCms.createProfile("sRGB"))


# ------------------------------------------------------------------- FUNZIONI
def _con_trasparenza(immagine):
    """True solo se l'immagine ha trasparenza VERA (tante PNG hanno un canale
    alfa completamente opaco, inutile e pesante)."""
    if immagine.mode in ("RGBA", "LA"):
        minimo, _ = immagine.getchannel("A").getextrema()
        return minimo < 250
    if immagine.mode == "P":
        return "transparency" in immagine.info
    return False


def _prepara(percorso):
    """
    Apre un'immagine e la porta in uno stato "pulito":
    ruotata, in RGB (o RGBA se davvero trasparente), con il suo profilo colore.
    Restituisce (immagine, profilo_icc_in_byte, ha_trasparenza, era_png).
    """
    originale = Image.open(percorso)
    era_png = originale.format == "PNG"
    icc = originale.info.get("icc_profile")

    immagine = ImageOps.exif_transpose(originale)  # applica la rotazione salvata nella foto

    if immagine.mode == "CMYK":
        # CMYK (stampa) -> sRGB (schermo), usando il profilo incorporato se c'e'.
        if icc:
            try:
                sorgente = ImageCms.ImageCmsProfile(io.BytesIO(icc))
                immagine = ImageCms.profileToProfile(
                    immagine, sorgente, _SRGB, outputMode="RGB",
                    # Impostazioni scelte confrontando il risultato con come il
                    # browser mostra l'originale CMYK (senza compensazione del nero).
                    renderingIntent=ImageCms.Intent.RELATIVE_COLORIMETRIC,
                )
            except Exception:
                immagine = immagine.convert("RGB")
        else:
            immagine = immagine.convert("RGB")
        icc = _SRGB.tobytes()

    trasparente = _con_trasparenza(immagine)
    if trasparente:
        immagine = immagine.convert("RGBA")
    else:
        immagine = immagine.convert("RGB")
    return immagine, icc, trasparente, era_png


def _riduci(immagine, lato_max):
    """Riduce (mai ingrandisce) in modo che il lato piu' lungo sia <= lato_max."""
    larghezza, altezza = immagine.size
    lato = max(larghezza, altezza)
    if lato <= lato_max:
        return immagine
    fattore = lato_max / lato
    nuova = (max(1, round(larghezza * fattore)), max(1, round(altezza * fattore)))
    return immagine.resize(nuova, Image.LANCZOS)


def _salva(immagine, destinazione, icc, trasparente, qualita, grafica):
    """Salva in JPEG (foto) oppure PNG (solo se davvero trasparente)."""
    os.makedirs(os.path.dirname(destinazione), exist_ok=True)
    extra = {"icc_profile": icc} if icc else {}
    if trasparente:
        immagine.save(destinazione, "PNG", optimize=True, **extra)
    else:
        # subsampling=0 (4:4:4): il colore resta a risoluzione piena. Il default dei
        # JPEG (4:2:0) dimezza la risoluzione dei colori: invisibile su molte foto,
        # ma smorza i rossi saturi dei poster e i bordi netti di testi e mockup.
        immagine.save(
            destinazione, "JPEG", quality=qualita, optimize=True, progressive=True,
            subsampling=0, **extra
        )


def _file_di_progetto(cartella):
    """Nomi dei file immagine/video di un progetto, ordinati come fa il sito."""
    nomi = []
    for nome in sorted(os.listdir(cartella)):
        if nome.startswith(".") or not os.path.isfile(os.path.join(cartella, nome)):
            continue
        if nome.lower().endswith(ESTENSIONI_IMMAGINE + ESTENSIONI_VIDEO):
            nomi.append(nome)
    return nomi


def ottimizza_progetto(slug, originali, uscita):
    """Ottimizza tutte le immagini di un progetto. Restituisce un riepilogo."""
    sorgente = os.path.join(originali, slug)
    cartella_uscita = os.path.join(uscita, slug)
    nomi = _file_di_progetto(sorgente)
    if not nomi:
        return []

    # Due file con lo stesso nome base (01.png e 01.jpg) finirebbero sullo
    # stesso file di uscita: meglio fermarsi che sovrascrivere.
    basi = [os.path.splitext(n)[0] for n in nomi]
    doppi = {b for b in basi if basi.count(b) > 1}
    if doppi:
        sys.exit("ERRORE in '%s': nomi duplicati (stessa base, estensioni diverse): %s" % (slug, sorted(doppi)))

    righe = []
    primo = True   # la copertina e' la prima IMMAGINE (un video non puo' esserlo)
    for nome in nomi:
        base, estensione = os.path.splitext(nome)
        percorso_in = os.path.join(sorgente, nome)

        if nome.lower().endswith(ESTENSIONI_VIDEO):          # video: copiato cosi' com'e'
            os.makedirs(cartella_uscita, exist_ok=True)
            shutil.copy2(percorso_in, os.path.join(cartella_uscita, nome))
            righe.append((slug, nome, nome, os.path.getsize(percorso_in), os.path.getsize(percorso_in), None))
            continue

        if nome.lower().endswith((".gif", ".avif", ".webp")):  # formati rari: copiati
            os.makedirs(cartella_uscita, exist_ok=True)
            shutil.copy2(percorso_in, os.path.join(cartella_uscita, nome))
            righe.append((slug, nome, nome, os.path.getsize(percorso_in), os.path.getsize(percorso_in), None))
            primo = False
            continue

        with Image.open(percorso_in) as controllo:
            gia_a_posto = (
                controllo.format == "JPEG" and controllo.mode == "RGB"
                and max(controllo.size) <= LATO_MAX
                and controllo.getexif().get(274, 1) == 1      # nessuna rotazione da applicare
            )

        immagine, icc, trasparente, era_png = _prepara(percorso_in)
        grande = _riduci(immagine, LATO_MAX)
        estensione_uscita = ".png" if trasparente else ".jpg"
        nome_uscita = base + estensione_uscita
        qualita = QUALITA_GRAFICA if era_png else QUALITA_FOTO
        destinazione = os.path.join(cartella_uscita, nome_uscita)
        _salva(grande, destinazione, icc, trasparente, qualita, grafica=era_png)

        # Un JPEG gia' della misura giusta e' gia' stato compresso: ricomprimerlo
        # aggiunge solo una perdita di qualita'. Se risparmiamo meno del 15%,
        # teniamo il file ORIGINALE identico.
        if gia_a_posto and os.path.getsize(destinazione) > 0.85 * os.path.getsize(percorso_in):
            shutil.copy2(percorso_in, destinazione)

        if primo:   # miniatura della copertina, per le card (molto piu' leggera)
            piccola = _riduci(immagine, MINIATURA_LATO)
            _salva(piccola, os.path.join(cartella_uscita, "miniature", nome_uscita),
                   icc, trasparente, QUALITA_MINIATURA, grafica=era_png)
            primo = False

        righe.append((slug, nome, nome_uscita, os.path.getsize(percorso_in),
                      os.path.getsize(destinazione), grande.size))
    return righe


def main():
    parser = argparse.ArgumentParser(description="Ottimizza le immagini dei progetti.")
    parser.add_argument("progetti", nargs="*", help="slug dei progetti (default: tutti)")
    parser.add_argument("--originali", default=ORIGINALI_DEFAULT, help="cartella con le foto originali")
    parser.add_argument("--uscita", default=USCITA_DEFAULT, help="cartella di destinazione")
    argomenti = parser.parse_args()

    if not os.path.isdir(argomenti.originali):
        sys.exit("Cartella degli originali non trovata: %s" % argomenti.originali)

    slug_da_fare = argomenti.progetti or sorted(
        d for d in os.listdir(argomenti.originali)
        if os.path.isdir(os.path.join(argomenti.originali, d)) and not d.startswith(".")
    )

    prima = dopo = 0
    for slug in slug_da_fare:
        righe = ottimizza_progetto(slug, argomenti.originali, argomenti.uscita)
        p = sum(r[3] for r in righe)
        d = sum(r[4] for r in righe)
        prima += p
        dopo += d
        print("%-26s %3d file   %7.1f MB -> %6.1f MB" % (slug, len(righe), p / 1048576, d / 1048576))
    print("\nTOTALE: %.1f MB -> %.1f MB" % (prima / 1048576, dopo / 1048576))


if __name__ == "__main__":
    main()
