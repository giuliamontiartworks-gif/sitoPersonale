# -*- coding: utf-8 -*-
"""
Applicazione Flask del sito portfolio di Giulia Monti.

Qui vivono SOLO le rotte (quale URL mostra quale pagina) e il collegamento
con i dati. Tutta la presentazione sta nei template Jinja in templates/,
tutti i contenuti stanno nei file in data/.

Per avviarlo in locale:
    pip install -r requirements.txt
    python app.py
poi apri http://127.0.0.1:5000

Invio email del form Contatti: le credenziali stanno nel file ".env"
(non committato). Vedi ".env.example" per le variabili richieste.
"""

import os
import time

from flask import Flask, render_template, abort, redirect, url_for, request
from flask_mail import Mail, Message
from dotenv import load_dotenv

# Carica le variabili del file .env (se presente) in os.environ.
load_dotenv()

# Import dei dati. Ogni modulo espone funzioni "di accesso" (elenco_*, *_da_slug...)
# cosi' che un domani si possa sostituire la sorgente dati senza toccare le rotte.
from data.categorie import elenco_categorie, categoria_da_slug, nome_categoria
from data.progetti import (
    elenco_progetti,
    progetto_da_slug,
    progetti_per_categoria,
    progetti_in_evidenza,
    progetti_correlati,
)
from data.certificazioni import elenco_certificazioni
from data import contenuti


app = Flask(__name__)

# In sviluppo: non far tenere in cache al browser i file statici (CSS/JS),
# cosi' ogni modifica si vede subito senza dover svuotare la cache.
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

# --- Configurazione email (Gmail via SMTP) --------------------------------
# I valori arrivano dal file .env. Se manca, MAIL_USERNAME/PASSWORD restano
# None e il form continua a funzionare senza inviare nulla (vedi invia_email).
app.config.update(
    MAIL_SERVER="smtp.gmail.com",
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME=os.environ.get("MAIL_USERNAME"),
    MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD"),
    MAIL_DEFAULT_SENDER=os.environ.get("MAIL_USERNAME"),
    # A chi arrivano i messaggi del form (default: la stessa email mittente).
    MAIL_TO=os.environ.get("MAIL_TO") or os.environ.get("MAIL_USERNAME"),
)

mail = Mail(app)


# ---------------------------------------------------------------------------
# "Cache busting": a ogni URL di file statico aggiungiamo ?v=<data-modifica>,
# cosi' quando cambi un CSS o un JS il browser scarica per forza la versione
# nuova (l'URL cambia). Sostituisce url_for solo per i file statici.
# ---------------------------------------------------------------------------
@app.context_processor
def _url_for_con_versione():
    def url_for_statico(endpoint, **valori):
        if endpoint == "static":
            nome_file = valori.get("filename")
            if nome_file:
                percorso = os.path.join(app.static_folder, nome_file)
                if os.path.isfile(percorso):
                    valori["v"] = int(os.stat(percorso).st_mtime)
        return url_for(endpoint, **valori)

    return {"url_for": url_for_statico}


# ---------------------------------------------------------------------------
# Contesto condiviso da tutti i template.
# Cosi' header e footer possono usare persona/social/servizi senza che ogni
# rotta li passi a mano.
# ---------------------------------------------------------------------------
@app.context_processor
def variabili_globali():
    return {
        "persona": contenuti.persona,
        "social": contenuti.social,
        "footer": contenuti.footer,
        "categorie": elenco_categorie(),
        "url_portfolio_pdf": _url_portfolio_pdf(),
        "anno_corrente": 2026,
    }


# ---------------------------------------------------------------------------
# PDF del portfolio + curriculum (link nella pagina Portfolio).
# Basta mettere UN file .pdf dentro static/documenti/ (con qualsiasi nome):
# il sito lo trova da solo e il link diventa un download automatico.
# Se la cartella non c'e' o e' vuota, torniamo il valore di ripiego da
# contenuti.py (di solito "#") e il template nasconde il link.
# ---------------------------------------------------------------------------
def _url_portfolio_pdf():
    cartella = os.path.join(app.static_folder, "documenti")
    try:
        nomi = sorted(os.listdir(cartella))
    except OSError:
        return contenuti.url_portfolio_pdf

    for nome in nomi:
        if nome.startswith(".") or not nome.lower().endswith(".pdf"):
            continue
        return url_for("static", filename="documenti/" + nome)

    return contenuti.url_portfolio_pdf


# Helper disponibile nei template: dice se un file statico esiste davvero.
# Serve per mostrare un segnaposto colorato al posto delle immagini mancanti.
@app.template_global()
def file_statico_esiste(percorso_relativo):
    percorso_assoluto = os.path.join(app.static_folder, percorso_relativo)
    return os.path.isfile(percorso_assoluto)


# Estensioni accettate nelle cartelle dei progetti.
_ESTENSIONI_IMMAGINE = (".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif")
_ESTENSIONI_VIDEO = (".mp4", ".webm")


# Helper disponibile nei template: legge immagini E video di un progetto
# direttamente dalla cartella static/img/progetti/<slug>/, ordinati per nome
# file (01.jpg, 02.mp4, 03.jpg, ...). Cosi' basta aggiungere/togliere file
# nella cartella: non serve toccare data/progetti.py.
# Restituisce una lista di dizionari:
#   [{"percorso": "img/progetti/eme/01.jpg", "video": False},
#    {"percorso": "img/progetti/eme/02.mp4", "video": True}, ...]
@app.template_global()
def media_progetto(slug):
    cartella = os.path.join(app.static_folder, "img", "progetti", slug)
    if not os.path.isdir(cartella):
        return []
    elementi = []
    for nome in sorted(os.listdir(cartella)):
        if nome.startswith("."):
            continue
        estensione = os.path.splitext(nome)[1].lower()
        percorso = "img/progetti/{}/{}".format(slug, nome)
        if estensione in _ESTENSIONI_IMMAGINE:
            elementi.append({"percorso": percorso, "video": False})
        elif estensione in _ESTENSIONI_VIDEO:
            elementi.append({"percorso": percorso, "video": True})
    return elementi


# Helper: solo le IMMAGINI di un progetto (usato per la copertina delle card,
# che non puo' essere un video). Percorsi relativi a static/. La prima e' la
# copertina/thumbnail.
@app.template_global()
def immagini_progetto(slug):
    return [m["percorso"] for m in media_progetto(slug) if not m["video"]]


# Helper disponibile nei template: trova la foto della pagina "Chi sono" in
# static/img/. Accetta il nome "giulia", "chi-sono" o "chi_sono" con qualsiasi
# estensione immagine e maiuscole/minuscole (es. "chi_sono.JPG" va bene).
# Restituisce il percorso relativo a static/ (es. "img/chi_sono.JPG") o None.
@app.template_global()
def foto_chi_sono():
    cartella = os.path.join(app.static_folder, "img")
    if not os.path.isdir(cartella):
        return None
    nomi_ammessi = ("giulia", "chi-sono", "chi_sono")
    for nome in sorted(os.listdir(cartella)):
        base, estensione = os.path.splitext(nome)
        if base.lower() in nomi_ammessi and estensione.lower() in _ESTENSIONI_IMMAGINE:
            return "img/" + nome
    return None


# Helper disponibile nei template: dato uno slug categoria restituisce il nome
# leggibile (es. "agenzia" -> "Lavori d'agenzia").
@app.template_global()
def nome_disciplina(slug_categoria):
    return nome_categoria(slug_categoria)


# ---------------------------------------------------------------------------
# Invio dell'email del form Contatti.
# ---------------------------------------------------------------------------
def invia_email_contatto(dati):
    """
    Manda a Giulia un'email con i dati del form.

    Restituisce True se l'email e' partita, False altrimenti.
    NON solleva eccezioni: se le credenziali mancano (nessun .env) o l'invio
    fallisce, logga il problema e lascia comunque proseguire l'utente.
    """
    if not app.config.get("MAIL_USERNAME") or not app.config.get("MAIL_PASSWORD"):
        app.logger.warning(
            "Email non configurata (manca il file .env): messaggio del form NON inviato."
        )
        return False

    corpo = (
        "Nuovo messaggio dal form del sito.\n\n"
        "Nome e cognome: {nome}\n"
        "Email: {email}\n"
        "Telefono: {telefono}\n"
        "Servizio: {servizio}\n\n"
        "Messaggio:\n{messaggio}\n"
    ).format(**dati)

    messaggio = Message(
        subject="Sito — nuovo contatto da {}".format(dati["nome"] or "Anonimo"),
        recipients=[app.config["MAIL_TO"]],
        body=corpo,
        # Cosi' Giulia puo' rispondere direttamente al visitatore.
        reply_to=dati["email"] or None,
    )

    try:
        mail.send(messaggio)
        return True
    except Exception as errore:  # noqa: BLE001 - vogliamo comunque non bloccare l'utente
        app.logger.error("Invio email del form fallito: %s", errore)
        return False


# ---------------------------------------------------------------------------
# Rotte
# ---------------------------------------------------------------------------

@app.route("/")
def home():
    """Pagina Home."""
    return render_template(
        "index.html",
        progetti_evidenza=progetti_in_evidenza(),
        servizi=contenuti.servizi,
        certificazioni=elenco_certificazioni(),
        testi=contenuti.home,
        esperienze=contenuti.esperienze,
    )


@app.route("/portfolio")
def portfolio():
    """Elenco di tutte le categorie, ognuna con un'anteprima di 3 progetti."""
    # Per ogni categoria prepariamo i primi 3 progetti da mostrare nel carosello.
    categorie_con_progetti = []
    for categoria in elenco_categorie():
        progetti_categoria = progetti_per_categoria(categoria["slug"])
        categorie_con_progetti.append(
            {
                "categoria": categoria,
                "anteprima": progetti_categoria[:3],
            }
        )
    return render_template(
        "portfolio.html",
        categorie_con_progetti=categorie_con_progetti,
    )


@app.route("/categoria/<slug_categoria>")
def categoria(slug_categoria):
    """Pagina di una singola categoria con tutti i suoi progetti."""
    categoria_scelta = categoria_da_slug(slug_categoria)
    if categoria_scelta is None:
        abort(404)
    return render_template(
        "categoria.html",
        categoria=categoria_scelta,
        progetti=progetti_per_categoria(slug_categoria),
    )


@app.route("/progetto/<slug_progetto>")
def progetto(slug_progetto):
    """Pagina di un singolo progetto, generata dai suoi dati."""
    progetto_scelto = progetto_da_slug(slug_progetto)
    if progetto_scelto is None:
        abort(404)

    # Nome della prima categoria del progetto: serve per la pillola "Torna a ...".
    slug_prima_categoria = progetto_scelto["categorie"][0]
    prima_categoria = categoria_da_slug(slug_prima_categoria)

    return render_template(
        "progetto.html",
        progetto=progetto_scelto,
        prima_categoria=prima_categoria,
        correlati=progetti_correlati(slug_progetto, quanti=3),
    )


@app.route("/chi-sono")
def chi_sono():
    """Pagina Chi sono."""
    return render_template(
        "chi-sono.html",
        testi=contenuti.chi_sono,
        esperienze=contenuti.esperienze,
        formazione=contenuti.formazione,
        lingue=contenuti.lingue,
        certificazioni=elenco_certificazioni(),
        interessi=contenuti.interessi,
    )


@app.route("/contatti", methods=["GET", "POST"])
def contatti():
    """
    Pagina Contatti.

    GET  -> mostra il form.
    POST -> invia a Giulia l'email con i dati del form, poi reindirizza a /grazie.
            (Se l'email non e' configurata o l'invio fallisce, l'utente vede
            comunque la pagina "grazie": vedi invia_email_contatto.)
    """
    if request.method == "POST":
        # Se il messaggio sembra spam (vedi _sembra_spam), mostriamo comunque
        # "grazie" come se fosse andato tutto bene: cosi' chi/cosa lo manda
        # non capisce che e' stato scartato e non insiste per aggirarci.
        if not _sembra_spam(request.form):
            # "servizio" e' multi-selezione: getlist() restituisce tutti i valori.
            servizi_scelti = [s.strip() for s in request.form.getlist("servizio") if s.strip()]
            dati_modulo = {
                "nome": request.form.get("nome", "").strip(),
                "email": request.form.get("email", "").strip(),
                "telefono": request.form.get("telefono", "").strip(),
                "servizio": ", ".join(servizi_scelti),
                "messaggio": request.form.get("messaggio", "").strip(),
            }
            invia_email_contatto(dati_modulo)
        return redirect(url_for("grazie"))

    return render_template(
        "contatti.html",
        opzioni_servizio=contenuti.opzioni_servizio,
        testi=contenuti.chi_sono,
        ora_corrente_timestamp=time.time(),
    )


# Tempo minimo (in secondi) tra l'apertura della pagina e l'invio del form.
# Una persona vera impiega sempre piu' di qualche secondo a scrivere un
# messaggio; un bot lo compila e invia quasi istantaneamente.
_SECONDI_MINIMI_COMPILAZIONE = 3


def _sembra_spam(dati_form):
    """
    Controlli anti-spam invisibili sul form Contatti (vedi contatti.html):
      1) il campo esca "sito_web" e' compilato -> quasi certamente un bot
      2) il form e' stato inviato troppo poco tempo dopo l'apertura pagina
    Nessuno dei due si vede o disturba una persona che compila il form.
    """
    if request.form.get("sito_web", "").strip():
        return True

    try:
        aperto_alle = float(dati_form.get("aperto_alle", 0))
    except (TypeError, ValueError):
        return False  # campo mancante o manomesso: non blocchiamo per questo

    return (time.time() - aperto_alle) < _SECONDI_MINIMI_COMPILAZIONE


@app.route("/grazie")
def grazie():
    """Pagina di conferma dopo l'invio del form."""
    return render_template("grazie.html")


@app.route("/robots.txt")
def robots():
    """
    Dice ai motori di ricerca che possono leggere tutto il sito e dove
    trovare la mappa completa delle pagine (sitemap.xml). E' il primo file
    che Google va a cercare quando scopre il dominio.
    """
    righe = [
        "User-agent: *",
        "Allow: /",
        "Sitemap: " + url_for("sitemap", _external=True),
    ]
    return "\n".join(righe), 200, {"Content-Type": "text/plain; charset=utf-8"}


@app.route("/sitemap.xml")
def sitemap():
    """
    Elenco di TUTTE le pagine del sito, in XML, cosi' Google le trova e le
    indicizza tutte (anche quelle non linkate direttamente dalla home).
    Costruita automaticamente dai dati: aggiungere un progetto o una
    categoria basta, non serve toccare questa funzione.
    """
    pagine = [
        {"loc": url_for("home", _external=True), "priorita": "1.0"},
        {"loc": url_for("portfolio", _external=True), "priorita": "0.9"},
        {"loc": url_for("chi_sono", _external=True), "priorita": "0.7"},
        {"loc": url_for("contatti", _external=True), "priorita": "0.7"},
    ]
    for categoria in elenco_categorie():
        pagine.append({
            "loc": url_for("categoria", slug_categoria=categoria["slug"], _external=True),
            "priorita": "0.8",
        })
    for progetto in elenco_progetti():
        pagine.append({
            "loc": url_for("progetto", slug_progetto=progetto["slug"], _external=True),
            "priorita": "0.6",
        })

    corpo = render_template("sitemap.xml", pagine=pagine)
    return corpo, 200, {"Content-Type": "application/xml; charset=utf-8"}


@app.errorhandler(404)
def pagina_non_trovata(errore):
    """Pagina 404 semplice, con lo stesso layout del sito."""
    return render_template("404.html"), 404


if __name__ == "__main__":
    # La porta si puo' cambiare con la variabile d'ambiente PORT
    # (di default 5000). Su macOS la 5000 e' spesso occupata da
    # "AirPlay Receiver": in quel caso usa un'altra porta, es.
    #     PORT=5050 python app.py
    porta = int(os.environ.get("PORT", 5000))
    # debug=True ricarica il server a ogni salvataggio: comodo in sviluppo,
    # da togliere in produzione.
    app.run(debug=True, port=porta)
