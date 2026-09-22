# -*- coding: utf-8 -*-
"""
Contenuti testuali del sito che non sono progetti né certificazioni:
- dati di contatto e link social
- testi di presentazione (Home, Chi sono)
- elenco dei servizi
- esperienze lavorative e formazione
- lingue
- aree di interesse ("Fuori dal lavoro")

Tenuti qui per non sparpagliarli nei template. Stessa logica degli altri
file in data/: se un domani servisse un CMS, questa è la parte da sostituire.

# TODO (Giulia): controllare e completare esperienze, formazione, lingue e bio.
"""

# --- Dati identità / contatto -------------------------------------------------

persona = {
    "nome": "Giulia Monti",
    "ruolo": "Art director junior · Illustratrice · Strategist",
    "citta": "Torino",
    "email": "giuliamontiartworks@gmail.com",
}

# I link social sono usati in header (menu mobile), footer e pagina contatti.
social = [
    {"nome": "Instagram", "url": "https://www.instagram.com/giuliamontidesign/"},
    {"nome": "LinkedIn", "url": "https://www.linkedin.com/in/giulia-monti-090925266/"},
    {"nome": "Behance", "url": "https://www.behance.net/giuliamonti7"},
]

# I link ai PDF (CV e portfolio, nella pagina Portfolio) sono trovati in
# automatico da app.py dentro static/documenti/: non c'e' niente da mettere
# qui (vedi app.py -> _url_documento).

# Testo del footer, su due righe (a capo dopo il punto interrogativo).
footer = {
    "titolo_riga1": "Hai un progetto in mente?",
    "titolo_riga2": "Costruiamolo insieme.",
}


# --- Testi Home --------------------------------------------------------------

home = {
    "eyebrow": "Torino · Art direction · Strategia · Illustrazione",

    # Il titolo della hero è su DUE righe (come nel Figma): l'a-capo è
    # esattamente dopo "illustrazione". Per questo lo teniamo diviso in due
    # stringhe: il template le separa con un <br>.
    "titolo_riga1": "Art direction, strategia e illustrazione,",
    "titolo_riga2": "dove il bello e il funzionale coincidono.",

    # Paragrafo della hero, su due righe (a capo dopo "illustratrice.").
    "presentazione_riga1": "Sono Giulia, art director junior e illustratrice.",
    "presentazione_riga2": (
        "Vivo a Torino, studio Communication Design a IAAD e ho già iniziato "
        "a muovere i primi passi in agenzia."
    ),

    # Banner "Esperienza in agenzia" + "Certificazioni" in fondo alla Home.
    "esperienza_titolo": "Esperienza in agenzia",
    "esperienza_testo": (
        "In Hello Tomorrow, agenzia a impatto positivo, ho lavorato su brand "
        "identity, locandine, impaginazioni editoriali e digitali."
    ),
    "certificazioni_titolo": "Certificazioni",
}


# --- Testi Chi sono ----------------------------------------------------------

chi_sono = {
    "sottotitolo": "Art director junior, illustratrice e stratega — Torino",
    "bio": (
        "Studio Communication Design a IAAD e mi muovo tra art direction, strategia "
        "e illustrazione senza sentire il bisogno di scegliere un solo campo — mi piace "
        "pensare a un progetto e poi anche disegnarlo. Sono curiosa, precisa e porto lo "
        "stesso rigore sia su un brand che su un'illustrazione."
    ),
    # Etichetta sopra le icone social. L'asterisco tiene il testo neutro.
    "social_label": "Rimaniamo conness*",
}

# Esperienze lavorative (pagina Chi sono).
# Ogni voce: il titolo mostrato e' "ruolo — azienda", poi il "contesto" in rosso,
# poi la descrizione. "mostra_link_agenzia": True aggiunge il link ai lavori d'agenzia.
esperienze = [
    {
        "ruolo": "Junior Art Director",
        "azienda": "Hello Tomorrow",
        "contesto": "Agenzia a impatto positivo, Torino",
        "descrizione": (
            "Ho lavorato su brand identity, locandine e impaginazioni editoriali e "
            "digitali — tra i progetti, una campagna per ActionAid arrivata nella metro di Milano."
        ),
        "mostra_link_agenzia": True,
    },
    {
        "ruolo": "Social Media Manager",
        "azienda": "Grella Grella",
        "contesto": "Bottega artigiana, Cagliari",
        "descrizione": (
            "Ho seguito l'instagram di Grella Grella, facendo crescere la pagina di "
            "circa 150 follower in un anno."
        ),
        "mostra_link_agenzia": False,
    },
]

# Formazione (Chi sono). Stesso formato: titolo "ruolo — azienda" + "contesto" in rosso.
formazione = [
    {
        "ruolo": "IAAD Torino",
        "azienda": "Communication Design",
        "contesto": "In corso - Secondo anno",
        "descrizione": "",
    },
    {
        "ruolo": "Liceo Artistico",
        "azienda": "Indirizzo Grafica",
        "contesto": "Diploma 100 e lode",
        "descrizione": "",
    },
    {
        "ruolo": "Anno di studio all'estero",
        "azienda": "North Carolina, USA",
        "contesto": "Scambio culturale",
        "descrizione": (
            "Un anno che mi ha aperto il punto di vista su culture diverse e mi ha "
            "portata a un inglese di livello C2."
        ),
    },
]

# Lingue (Chi sono).
lingue = [
    {"lingua": "Italiano", "livello": "Madrelingua"},
    {"lingua": "Inglese", "livello": "C2"},
    {"lingua": "Spagnolo", "livello": "A1"},
]


# --- Servizi ("Cosa posso fare per te") -------------------------------------
# La lista `servizi` (nome + descrizione) e' usata SOLO nella sezione Home.
# Le opzioni del campo "Servizio" nel form contatti sono in `opzioni_servizio`
# qui sotto: gli stessi servizi + "Non lo so" come ultima voce.

servizi = [
    {
        "nome": "Art Direction",
        "descrizione": "Direzione creativa e coerenza visiva per campagne e progetti di brand.",
    },
    {
        "nome": "Illustrazione",
        "descrizione": "Illustrazioni editoriali e su misura, con uno stile riconoscibile e giocoso.",
    },
    {
        "nome": "Strategia",
        "descrizione": "Posizionamento e ragionamento strategico dietro ogni scelta creativa.",
    },
    {
        "nome": "Brand Identity",
        "descrizione": "Identità visive complete, dal naming alla palette, per marchi profit e no profit.",
    },
    {
        "nome": "UX/UI e Web Design",
        "descrizione": "Siti web per professionisti, personal brand e aziende.",
    },
    {
        "nome": "Fotografia",
        "descrizione": "Fotografia editoriale e di reportage, per raccontare prodotti, spazi e persone.",
    },
    {
        "nome": "Impaginazioni editoriali",
        "descrizione": "Layout e impaginazione per riviste, editoriali e pubblicazioni cartacee e digitali.",
    },
    {
        "nome": "Packaging",
        "descrizione": "Design di packaging che comunica il brand anche fuori dallo schermo.",
    },
]

# Opzioni del campo "Servizio" nel form contatti: i servizi + "Non lo so" in fondo.
opzioni_servizio = [servizio["nome"] for servizio in servizi] + ["Non lo so"]


# --- "Fuori dal lavoro" (Chi sono) ----------------------------------------
# Testi da usare esattamente così come sono (richiesta esplicita di Giulia).

interessi = [
    {
        "nome": "Cinema e serie tv",
        "descrizione": (
            "Amo vedere un film anche più volte: alla prima lo scopro, alla seconda ne "
            "noto i dettagli. Le serie tv mi aiutano a restare al passo con il mondo e a "
            "staccare la spina."
        ),
    },
    {
        "nome": "Arte, mostre e musei",
        "descrizione": (
            "Mi perdo volentieri nei musei, soprattutto quelli d'arte: mi affascina la "
            "storia dell'arte, dall'avanguardia al contemporaneo."
        ),
    },
    {
        "nome": "Attualità e trend",
        "descrizione": (
            "Mi piace restare connessa con quello che succede nel mondo: mi aiuta ad avere "
            "una visione d'insieme e a capire meglio target diversi dal mio."
        ),
    },
    {
        "nome": "Disegno",
        "descrizione": (
            "Quando trovo il tempo, disegno e faccio schizzi: un modo per tenermi "
            "impegnata, ma anche per dare sfogo alle emozioni."
        ),
    },
    {
        "nome": "Passeggiate",
        "descrizione": "Adoro stare in mezzo alla natura, fare trekking e scoprire posti nuovi.",
    },
    {
        "nome": "Viaggi e nuove culture",
        "descrizione": (
            "Viaggiare è una delle mie più grandi passioni: mi rilassa, mi apre la mente "
            "e mi aiuta a capire culture diverse senza pregiudizi, senza giudicare ciò "
            "che non conosco."
        ),
    },
]
