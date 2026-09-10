# -*- coding: utf-8 -*-
"""
Certificazioni di Giulia (mostrate in Home e nella pagina Chi sono).

Sono tutte rilasciate da LEARNN ("LEARNN VERIFIED").

Ogni certificazione è un dizionario con:
  - "nome"          : titolo del corso (testo del badge e titolo del popup)
  - "ente"          : chi l'ha rilasciata
  - "data_verifica" : data di verifica (stringa, come sull'attestato)
  - "durata"        : durata del corso (stringa: "4 ore, 35 lezioni")
  - "id_verifica"   : codice di verifica pubblico
  - "descrizione"   : breve frase mostrata nel popup
"""

_FRASE = "Giulia Monti ha superato con successo il test finale del corso."

certificazioni = [
    {
        "nome": "Presentation Design",
        "ente": "LEARNN",
        "data_verifica": "16/03/2026",
        "durata": "4 ore, 35 lezioni",
        "id_verifica": "14bf6d40-19c9-4a36-8c30-6d23a6b3ad38",
        "descrizione": _FRASE,
    },
    {
        "nome": "Fotografia Creativa",
        "ente": "LEARNN",
        "data_verifica": "25/03/2026",
        "durata": "2 ore, 31 lezioni",
        "id_verifica": "d8fb72fe-f16d-4e6e-ab10-cfa31891dfb3",
        "descrizione": _FRASE,
    },
    {
        "nome": "Social Media Strategy",
        "ente": "LEARNN",
        "data_verifica": "1/03/2026",
        "durata": "4 ore, 30 lezioni",
        "id_verifica": "7ab52258-941e-426a-a098-2dd494717c58",
        "descrizione": _FRASE,
    },
    {
        "nome": "SEO per canali social",
        "ente": "LEARNN",
        "data_verifica": "12/08/2026",
        "durata": "57 minuti, 9 lezioni",
        "id_verifica": "4c5ec9db-46de-4f01-b8ec-cb7a7e6c0af3",
        "descrizione": _FRASE,
    },
    {
        "nome": "Social Media Branding",
        "ente": "LEARNN",
        "data_verifica": "5/08/2026",
        "durata": "3 ore, 33 lezioni",
        "id_verifica": "ed08ba54-5a23-4da2-a164-73e0e7cde3de",
        "descrizione": _FRASE,
    },
]


def elenco_certificazioni():
    """Restituisce tutte le certificazioni, nell'ordine definito sopra."""
    return certificazioni
