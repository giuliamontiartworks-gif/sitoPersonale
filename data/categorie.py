# -*- coding: utf-8 -*-
"""
Elenco delle categorie del portfolio.

Ogni categoria è un dizionario con:
  - "slug": identificativo usato negli URL (es. /categoria/illustrazione)
  - "nome": etichetta mostrata a schermo
  - "descrizione": 1-2 righe di testo specifiche per la pagina categoria

Gli SLUG e i NOMI qui sotto seguono il documento "progetti definitivi" di Giulia.
Le DESCRIZIONI sono ancora testo di bozza: # TODO (Giulia) rivedile.

L'ordine di questa lista è l'ordine in cui le categorie compaiono
nella pagina Portfolio e nei tab-filtro.
"""

categorie = [
    {
        "slug": "lavori-agenzia",
        "nome": "Lavori d'agenzia",
        "descrizione": (
            "Progetti sviluppati in Hello Tomorrow, per brand e organizzazioni no profit: "
            "dalla campagna ai materiali editoriali, fino alla declinazione sui vari formati."
        ),
    },
    {
        "slug": "strategia",
        "nome": "Strategia",
        "descrizione": (
            "Strategie di comunicazione, campagne OOH e posizionamento: analisi del target, "
            "insight e concept creativo al servizio di un obiettivo preciso."
        ),
    },
    {
        "slug": "brand",
        "nome": "Brand",
        "descrizione": (
            "Progetti di brand identity e sistemi visivi completi: naming, logo, palette, "
            "packaging e applicazioni, con attenzione alla coerenza tra estetica e messaggio."
        ),
    },
    {
        "slug": "ux-ui-web-design",
        "nome": "UX/UI e Web Design",
        "descrizione": (
            "Struttura, wireframe e interfaccia di siti e app: dall'architettura dei "
            "contenuti al design visivo, coerente con l'identità del progetto."
        ),
    },
    {
        "slug": "illustrazione",
        "nome": "Illustrazione",
        "descrizione": (
            "Illustrazioni editoriali, poster e progetti visivi in cui il segno racconta "
            "un punto di vista. Lavori personali e su commissione."
        ),
    },
    {
        "slug": "fotografia",
        "nome": "Fotografia",
        "descrizione": (
            "Reportage e progetti di ricerca visiva, usati come linguaggio autonomo "
            "o come base per lavori di art direction e illustrazione."
        ),
    },
]


def elenco_categorie():
    """Restituisce la lista completa delle categorie, nell'ordine definito sopra."""
    return categorie


def categoria_da_slug(slug):
    """
    Restituisce il dizionario della categoria con lo slug richiesto,
    oppure None se lo slug non esiste.
    """
    for categoria in categorie:
        if categoria["slug"] == slug:
            return categoria
    return None


def nome_categoria(slug):
    """Scorciatoia: restituisce il nome leggibile di una categoria dato lo slug."""
    categoria = categoria_da_slug(slug)
    if categoria is None:
        return slug
    return categoria["nome"]
