# Sito portfolio — Giulia Monti

Sito personale di Giulia Monti (art director junior, illustratrice, strategist — Torino).
Backend **Flask** + template **Jinja2**, **HTML/CSS puro** e **JavaScript vanilla**.
Nessun database: i contenuti vivono in file Python dentro `data/`.

## Come far girare il sito in locale

Serve **Python 3.10+**.

> ⚠️ Su questo Mac Python non è ancora installato. Apri il Terminale e lancia
> `xcode-select --install` (parte un installer grafico, ci vogliono un paio di
> minuti). Da lì in poi i comandi qui sotto funzionano.

```bash
# 1. (consigliato) crea un ambiente virtuale isolato
python3 -m venv .venv
source .venv/bin/activate

# 2. installa Flask
pip install -r requirements.txt

# 3. avvia il sito
python app.py
```

Poi apri **http://127.0.0.1:5000** nel browser.
Il server si riavvia da solo a ogni salvataggio (`debug=True` in `app.py`).

> Su macOS la porta 5000 è spesso occupata da "AirPlay Receiver"
> (Impostazioni di Sistema → Generali → AirDrop e Handoff). In quel caso:
> ```bash
> PORT=5050 python app.py
> ```
> e apri http://127.0.0.1:5050.

## Dov'è cosa

| Cartella / file        | Contenuto                                                        |
|------------------------|-----------------------------------------------------------------|
| `app.py`               | Le rotte (quale URL → quale pagina). Solo logica, niente HTML.  |
| `data/progetti.py`     | Elenco dei progetti (una lista di dizionari).                    |
| `data/categorie.py`    | Le 5 categorie del portfolio.                                    |
| `data/certificazioni.py` | Le certificazioni (per ora segnaposto).                        |
| `data/contenuti.py`    | Testi di Home/Chi sono, servizi, esperienze, lingue, interessi. |
| `templates/`           | I template Jinja. `base.html` è lo scheletro comune.            |
| `templates/partials/`  | Pezzi riutilizzabili e macro (bottone, card, form…).            |
| `static/css/`          | `tokens.css` (variabili) → `base.css` → `componenti.css` → `pagine.css`. |
| `static/js/`           | Un file per interazione, JavaScript vanilla.                     |
| `static/img/progetti/` | Una sottocartella per progetto con le immagini (`01.jpg`, …).   |

## Cose ancora da fare (cerca `TODO` nel codice)

- **Immagini e video dei progetti**: metti i file in `static/img/progetti/<slug>/`
  nominati `01.jpg`, `02.jpg`, `03.mp4`… (c'è già una cartella per ogni progetto,
  con un `.gitkeep`). Il sito li legge **automaticamente** dalla cartella
  (ordinati per nome file). Non serve toccare `data/progetti.py`.
  - Immagini: `.jpg .jpeg .png .webp .gif .avif`
  - Video: `.mp4` (consigliato, H.264) o `.webm` — appaiono nello slideshow con
    i controlli di riproduzione
  - La **copertina** delle card è sempre la prima *immagine* (`01.jpg`): un video
    non può fare da copertina, mettilo dalla `02` in poi
  - Cartella vuota → segnaposto lilla col nome
- I **testi dei 19 progetti** (`data/progetti.py`) sono quelli definitivi dal
  documento di Giulia: NON modificarli senza il suo ok.
- Le **descrizioni delle categorie** (`data/categorie.py`) sono ancora bozza (`TODO`).
- **Foto Chi sono**: metti il file in `static/img/` chiamandolo `giulia`,
  `chi-sono` o `chi_sono` (qualsiasi estensione, anche maiuscola: `chi_sono.JPG`
  va bene). Il sito la trova da solo; senza foto mostra un segnaposto.
- Link social veri in `data/contenuti.py`.
- **PDF curriculum e portfolio**: metti DUE file `.pdf` in `static/documenti/`
  — uno con "cv" nel nome (es. `CV.pdf`) e uno con "portfolio" nel nome (es.
  `portfolio.pdf`). Il sito li trova da soli e mostra due bottoni di download
  separati nella pagina Portfolio. Se manca uno dei due, sparisce solo il suo
  bottone (l'altro resta).
- Certificazioni reali in `data/certificazioni.py` (per ora segnaposto).

## Invio del form contatti (email)

Il form invia un'email a Giulia (via Gmail SMTP + Flask-Mail) con i dati
compilati, poi mostra la pagina `/grazie`.

Le credenziali stanno nel file **`.env`** (non committato, è nel `.gitignore`).
Per configurarlo su una nuova macchina:

1. `cp .env.example .env`
2. apri `.env` e metti:
   - `MAIL_USERNAME` = l'indirizzo Gmail mittente
   - `MAIL_PASSWORD` = una **password per le app** di Gmail (16 caratteri, da
     <https://myaccount.google.com/apppasswords> — serve la verifica in due
     passaggi attiva), non la password normale
   - `MAIL_TO` = a chi arrivano i messaggi (di solito la stessa email)

Se il `.env` manca, il form **funziona lo stesso**: reindirizza a `/grazie`
senza inviare nulla (e scrive un warning nel log). Comodo in sviluppo.

Codice: config in cima ad `app.py`, invio nella funzione `invia_email_contatto`.
