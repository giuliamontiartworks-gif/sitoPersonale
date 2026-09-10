# -*- coding: utf-8 -*-
"""
Elenco dei progetti del portfolio.

FONTE UNICA E VINCOLANTE: il documento "progetti-DEFINITIVO-per-claude-code.md"
di Giulia. Nome, categoria, contesto, cliente, anno, uso AI, strumenti,
overview, insight e target NON vanno modificati senza il suo ok.

Sono ESATTAMENTE 19 progetti. Le immagini sono ancora tutte da caricare
(vanno in static/img/progetti/<slug>/): finché mancano il sito mostra un
segnaposto lilla col nome del progetto.

Chiavi di ogni progetto:
  - "slug"          identificativo per l'URL /progetto/<slug>
  - "nome"          titolo mostrato a schermo
  - "categorie"     lista di slug categoria (vedi data/categorie.py)
  - "contesto"      com'è nato il progetto (università, agenzia, personale...)
  - "cliente"       stringa, oppure None
  - "anno"          intero
  - "ai_used"       True/False
  - "ai_strumenti"  (opzionale) lista degli strumenti AI usati
  - "strumenti"     lista di software/strumenti
  - "overview"      paragrafo di presentazione
  - "insight"       l'insight di partenza
  - "target"        a chi si rivolge
  - "risultato"     (opzionale) risultato concreto del progetto
  (le immagini NON sono qui: si leggono a runtime dalla cartella
   static/img/progetti/<slug>/, ordinate per nome file. Vedi immagini_progetto in app.py.)
  - "in_evidenza"   True se compare nella sezione "Progetti in evidenza" (Home)
  - "ordine_evidenza" (solo per i 4 in evidenza) ordine in Home, 1 = primo
  - "vetrina"       True solo per la card grande della Home
"""

progetti = [
    # ------------------------------------------------------------- ILLUSTRAZIONE
    {
        "slug": "craze-beer-bravery-bar",
        "nome": "Craze Beer × Bravery Bar",
        "categorie": ["illustrazione"],
        "contesto": "Contest universitario",
        "cliente": "Craze Beer × Bravery Bar",
        "anno": 2026,
        "ai_used": False,
        "strumenti": ["Illustrator"],
        "overview": "Un progetto per celebrare il Made in Italy — non solo l'Italia come luogo, ma attraverso easter egg nascosti nelle illustrazioni che citano pezzi di design italiano, pensati per essere riconosciuti e scovati da occhi esperti.",
        "insight": "Chi lavora nel design nota i dettagli che agli altri sfuggono, e trova soddisfazione nel riconoscerli. Un piccolo gioco di scoperta rende la lattina memorabile proprio per un pubblico come quello di Bravery Bar.",
        "target": "Designer italiani e appassionati di design che hanno partecipato all'evento Bravery Bar, dove le lattine sono state vendute.",
        "in_evidenza": False,
    },
    {
        "slug": "mani-per-gaza",
        "nome": "Mani per Gaza",
        "categorie": ["illustrazione"],
        "contesto": "Lavoro personale",
        "cliente": "Evento Mani per Gaza, Fondazione Tito Tocca Colore",
        "anno": 2025,
        "ai_used": False,
        "strumenti": ["InDesign"],
        "overview": "Un pattern ispirato alle trame geometriche della kefiah, dove le mani si trasformano in fiori e aquiloni, richiamando il simbolo della Mano di Fatima — per l'illustrazione della locandina dell'evento \"Mani per Gaza\".",
        "insight": "C'era il bisogno di un'illustrazione leggera, correlata al contesto politico ma che non riportasse subito alla pesantezza della questione.",
        "target": "Famiglie torinesi sensibili alla questione palestinese, persone frequentanti la Casa del Quartiere di San Salvario.",
        "in_evidenza": False,
    },
    {
        "slug": "the-torineser",
        "nome": "The Torineser",
        "categorie": ["illustrazione"],
        "contesto": "Personale",
        "cliente": None,
        "anno": 2026,
        "ai_used": False,
        "strumenti": ["Illustrator"],
        "overview": "Un'illustrazione omaggio a Torino con protagonista la stazione di Porta Nuova — icona architettonica e cuore pulsante della città — trattata con linee pulite e un'estetica editoriale contemporanea.",
        "insight": "Porta Nuova viene attraversata ogni giorno con distrazione da chi la vive: trattarla come protagonista di un poster editoriale, quasi una copertina da collezione, la fa guardare con occhi nuovi.",
        "target": "Torinesi doc, appassionati d'architettura.",
        "in_evidenza": False,
    },
    {
        "slug": "rear-window",
        "nome": "Rear Window",
        "categorie": ["illustrazione"],
        "contesto": "Personale",
        "cliente": None,
        "anno": 2025,
        "ai_used": False,
        "strumenti": ["Illustrator"],
        "overview": "Per questo omaggio al capolavoro di Alfred Hitchcock, ho voluto tradurre l'essenza voyeuristica del film in due poster concettuali.",
        "insight": "Il bisogno di raccontare i due aspetti del film: la finestra come strumento per osservare le vite altrui — dalle più belle e spensierate alle più solitarie — e il lato dell'indagine e della preoccupazione.",
        "target": "Amanti dei grandi classici del cinema iconici.",
        "in_evidenza": False,
    },

    # ---------------------------------------------------------- LAVORI D'AGENZIA
    {
        "slug": "mupa-actionaid",
        "nome": "MUPA × ActionAid",
        "categorie": ["lavori-agenzia"],
        "contesto": "Agenzia (Hello Tomorrow)",
        "cliente": "ActionAid / MUPA — Museo del Patriarcato",
        "anno": 2026,
        "ai_used": False,
        "strumenti": ["InDesign"],
        "overview": "Il MUPA (Museo del Patriarcato) racconta le statistiche di oggi presentandole come reperti da museo, con tanto di date e didascalie — un espediente che mette subito in chiaro il cortocircuito tra la forma (il passato, il museo) e il contenuto (dati di oggi).",
        "insight": "Molti pensano che il patriarcato sia un tema superato, roba da libri di storia — ma i dati raccontano una realtà ancora attualissima.",
        "target": "Chi pensa che la parità di genere sia ormai un traguardo raggiunto: un pubblico trasversale, non necessariamente ostile al tema, ma distaccato.",
        "risultato": "Oltre 10.000 visite al museo temporaneo alla Fabbrica del Vapore, Milano.",
        "in_evidenza": True,
        "ordine_evidenza": 1,
        "vetrina": True,
    },
    {
        "slug": "un-mare-di-gocce",
        "nome": "Un mare di gocce",
        "categorie": ["lavori-agenzia"],
        "contesto": "Agenzia (Hello Tomorrow)",
        "cliente": "Evento interno Hello Tomorrow",
        "anno": 2025,
        "ai_used": False,
        "strumenti": ["Photoshop"],
        "overview": "Ognuno di noi può fare la differenza, come una goccia nel mare: possiamo far cambiare la corrente delle cose che ci circondano, con piccoli o grandi gesti della nostra quotidianità.",
        "insight": "Un tema difficile da affrontare a parole si presta a un linguaggio visivo astratto: un intreccio continuo di segni che si muovono insieme, senza immagini esplicite, lasciando spazio alla riflessione di chi guarda.",
        "target": "Community di Hello Tomorrow, interessata ad approfondire il tema attraverso il racconto e il confronto.",
        "in_evidenza": False,
    },
    {
        "slug": "avsi",
        "nome": "AVSI",
        "categorie": ["lavori-agenzia"],
        "contesto": "Agenzia (Hello Tomorrow)",
        "cliente": "AVSI",
        "anno": 2025,
        "ai_used": False,
        "strumenti": ["InDesign"],
        "overview": "Una brochure editoriale per raccontare il lascito solidale ad AVSI: informare su un tema delicato con chiarezza, senza perdere il calore umano.",
        "insight": "Parlare di lascito testamentario significa parlare di fine vita: un tema che si evita. La chiave è spostare il focus dal \"dopo di te\" al \"cosa puoi ancora rendere possibile\" — non una perdita, ma un gesto che continua a fare del bene.",
        "target": "Donatori storici AVSI, generalmente over 60, già sensibili alla causa ma da accompagnare con delicatezza verso una decisione così personale.",
        "in_evidenza": False,
    },

    # ---------------------------------------------------------------- STRATEGIA
    {
        "slug": "wizzair-ooh",
        "nome": "WizzAir OOH",
        "categorie": ["strategia"],
        "contesto": "Progetto universitario",
        "cliente": "WizzAir (esercizio)",
        "anno": 2024,
        "ai_used": False,
        "strumenti": ["Photoshop", "InDesign"],
        "overview": "Una campagna OOH per WizzAir che trasforma un difetto in un pregio: graffi e ammaccature dei bagagli diventano ricordi di viaggio, con la headline \"Every bump is an experience\" e sticker souvenir da applicare alle valigie danneggiate.",
        "insight": "Le recensioni negative su WizzAir parlano spesso di bagagli rovinati — invece di negare il problema, l'ironia lo trasforma in una prova di quanto si è viaggiato.",
        "target": "Viaggiatori low-cost abituali, spesso critici verso la compagnia ma comunque fedeli per il prezzo — un pubblico che apprezza l'autoironia più delle scuse.",
        "in_evidenza": False,
    },
    {
        "slug": "torino-smartphone",
        "nome": "Città di Torino — dipendenza da smartphone",
        "categorie": ["strategia"],
        "contesto": "Progetto universitario, di gruppo",
        "cliente": None,
        "anno": 2026,
        "ai_used": True,
        "ai_strumenti": ["Gemini"],
        "strumenti": ["Photoshop", "InDesign"],
        "overview": "Una campagna di comunicazione di pubblica utilità sull'uso eccessivo dello smartphone, declinata in più soggetti: diverse situazioni quotidiane in cui si potrebbe essere più presenti, e invece ci si isola dietro lo schermo. Headline: \"Più ti connetti, più ti allontani.\"",
        "insight": "I dati mostrano come la dipendenza da smartphone danneggi proprio le relazioni più quotidiane e vicine — il paradosso di essere sempre \"connessi\" online mentre ci si allontana da chi si ha accanto, in tanti momenti diversi della giornata.",
        "target": "Chiunque riconosca nel proprio quotidiano almeno una delle situazioni rappresentate, proprio perché il comportamento è ormai diffuso.",
        "in_evidenza": False,
    },
    {
        "slug": "big-sis",
        "nome": "Big Sis",
        "categorie": ["strategia"],
        "contesto": "Brief universitario",
        "cliente": None,
        "anno": 2026,
        "ai_used": True,
        "ai_strumenti": ["Gemini", "Claude"],
        "strumenti": ["Illustrator", "InDesign", "Photoshop", "Figma"],
        "overview": "Un brief universitario chiedeva di creare brand identity e strategia per un'app di grading degli ex: è nata così Big Sis, pensata per proteggere le persone tra loro da situazioni scomode o pericolose nel dating — con un impatto fortemente femminista, non da gossip, ma orientato a proteggere davvero la community.",
        "insight": "Il mondo del dating attuale è percepito come \"rotto\" (broken world): manca uno strumento che trasformi le esperienze di chi è già passato per situazioni difficili in una protezione concreta per chi viene dopo.",
        "target": "Donne che vivono il dating online come un terreno da attraversare con cautela, non da evitare. Il progetto identifica tre profili principali: la \"Protector\", che usa l'app non solo per sé ma per proteggere amiche e community; la \"Recovering Heart\", reduce da un'esperienza negativa che cerca strumenti concreti per ricostruire fiducia prima di tornare a uscire; e l'\"Efficiency Dater\", che vuole ottimizzare il proprio tempo evitando situazioni rischiose o una perdita di tempo già in partenza. Un pubblico trasversale per età, accomunato dal bisogno di sicurezza attiva — non passiva — nel dating.",
        "in_evidenza": False,
    },
    {
        "slug": "origine",
        "nome": ".Origine",
        "categorie": ["strategia"],
        "contesto": "Progetto universitario, di gruppo",
        "cliente": None,
        "anno": 2026,
        "ai_used": True,
        "ai_strumenti": ["Gemini", "ChatGPT", "Claude"],
        "strumenti": ["Illustrator", "Figma", "Photoshop"],
        "overview": "Il brief chiedeva un rebranding della fiducia applicato a un settore specifico: abbiamo scelto il cibo, immaginando un futuro in cui la sfiducia diventa totale — prima verso i supermercati, poi persino verso il cibo preparato da altre persone, fino a un isolamento diffuso (orti privati in casa, ristoranti falliti per mancanza di clienti). .Origine nasce in questo scenario come un brand che, attraverso spazi dedicati, percorsi di accompagnamento e un'app, lavora per far tornare le persone a mangiare insieme.",
        "insight": "La vera posta in gioco non è la sicurezza alimentare in sé, ma la fiducia reciproca che si perde quando smettiamo di condividere il cibo con gli altri — recuperarla significa prima di tutto ricreare occasioni di socialità attorno alla tavola.",
        "target": "Persone che vivono (o rischiano di vivere) questo isolamento alimentare — chi ha smesso di fidarsi abbastanza da rinunciare a mangiare fuori o con altri, e cerca un modo sicuro per tornare a farlo.",
        "in_evidenza": False,
    },
    {
        "slug": "eoliann",
        "nome": "Eoliann",
        "categorie": ["strategia"],
        "contesto": "Progetto accademico IAAD",
        "cliente": "Eoliann — brand di progetto, tecnologia predittiva per la resilienza ai disastri naturali",
        "anno": 2026,
        "ai_used": True,
        "ai_strumenti": ["Gemini", "ChatGPT", "Claude"],
        "strumenti": ["Photoshop", "Figma", "Illustrator", "InDesign"],
        "overview": "\"I volontari non servono\": una campagna provocatoria per Eoliann, un brand di tecnologia AI predittiva contro i disastri naturali — perché il vero intervento è prevenirli, non gestirli. La headline sembra un attacco, ma è in realtà un elogio della prevenzione: se la tecnologia funzionasse davvero, l'intervento in emergenza non servirebbe più.",
        "insight": "Le persone associano gli eroi delle emergenze ai volontari che intervengono quando il danno è già fatto — ma nessuno si chiede perché quel danno debba accadere per forza.",
        "target": "Cittadini e comunità in aree a rischio idrogeologico, enti pubblici e potenziali investitori in tecnologie di prevenzione.",
        "in_evidenza": True,
        "ordine_evidenza": 2,
        "vetrina": False,
    },

    # -------------------------------------------------------------------- BRAND
    {
        "slug": "eme",
        "nome": "EME",
        "categorie": ["brand"],
        "contesto": "Esercizio universitario",
        "cliente": "Azienda food bio/naturale immaginata, Corciano (Umbria), in espansione verso il foodtech vegetale",
        "anno": 2026,
        "ai_used": True,
        "ai_strumenti": ["Gemini", "Claude"],
        "strumenti": ["Photoshop", "Illustrator", "InDesign", "Figma"],
        "overview": "Un progetto di rebranding per la carne vegetale, pensata come prodotto desiderabile e non come compromesso — dalla ricerca fino al packaging, dal sito al pop-up store. Il nome nasce dall'Eme, la molecola che dà alla carne il suo sapore e colore, ritrovata anche nei legumi fermentati: packaging e palette richiamano il rosso e il ferro, restando sofisticati nonostante il prodotto sia 100% vegetale.",
        "insight": "Chi sceglie di non mangiare carne non vuole rinunciare a niente — né al sapore, né alla completezza nutrizionale. EME nasce per rispondere esattamente a questo bisogno di \"zero compromessi\".",
        "target": "Amanti dell'alimentazione naturale, disposti a un costo leggermente superiore alla carne tradizionale per un prodotto sano e gluten-free.",
        "in_evidenza": True,
        "ordine_evidenza": 3,
        "vetrina": False,
    },
    {
        "slug": "molecular-bites-fanzine",
        "nome": "Molecular Bites",
        "categorie": ["brand"],
        "contesto": "Universitario",
        "cliente": "Molecular Bites",
        "anno": 2025,
        "ai_used": False,
        "strumenti": ["Photoshop", "InDesign"],
        "overview": "Una fanzine dedicata alla cucina molecolare, impaginata editorialmente pensando a rubriche e layout dedicati.",
        "insight": "La cucina molecolare rischia di sembrare fredda e tecnica sulla carta quanto lo è nei suoi strumenti — la sfida era impaginarla come una vera fanzine di tendenza, con rubriche e layout che ne raccontassero il lato più curioso e visivo, non solo scientifico.",
        "target": "Amanti della cucina e della scienza.",
        "in_evidenza": False,
    },
    {
        "slug": "cioccolato-calcagno",
        "nome": "Cioccolato Calcagno",
        "categorie": ["brand"],
        "contesto": "Universitario, ma progetto reale",
        "cliente": "Cioccolato Calcagno — marchio storico torinese",
        "anno": 2024,
        "ai_used": False,
        "strumenti": ["Photoshop", "Illustrator"],
        "overview": "Un sistema di packaging per lo storico marchio torinese Cioccolato Calcagno, costruito attorno alla stella a otto punte — elemento architettonico simbolo della città (San Lorenzo, Cappella della Sindone, Teatro Regio) — che si trasforma di stagione in stagione: stella a Natale, fiore a Pasqua, cuori a San Valentino.",
        "insight": "Un marchio storico come Calcagno vive del legame con la sua città: rendere un simbolo architettonico torinese il cuore del sistema visivo rafforza quel senso di appartenenza, invece di affidarsi solo al logo o al nome.",
        "target": "Torinesi affezionati alla tradizione dolciaria locale, e chi cerca un regalo che racconti un legame autentico con la città, più che un cioccolato qualsiasi.",
        "in_evidenza": False,
    },
    {
        "slug": "passayoun",
        "nome": "Passayoun",
        "categorie": ["brand"],
        "contesto": "Contest universitario",
        "cliente": "Brand nascente Passayoun",
        "anno": 2026,
        "ai_used": True,
        "ai_strumenti": ["Gemini"],
        "strumenti": ["Figma", "Illustrator", "Photoshop"],
        "overview": "Un'identità di brand per Passayoun, sportswear pensata per il mercato MENA, che unisce l'eredità geometrica dell'arte islamica all'istinto crudo dello sport urbano. Il logo nasce dalla \"Court Vision\": la mappa mentale totale che un playmaker ha del campo, tradotta nei vettori taglienti e scattanti del \"No-Look Pass\" — un passaggio fulmineo e imprevedibile che disorienta le difese.",
        "insight": "Nel basket, i giocatori più forti non sono quelli che guardano dove tirano, ma quelli che \"vedono\" l'intero campo prima ancora di agire — un'intelligenza tattica che l'arte geometrica islamica racconta da secoli attraverso pattern che rappresentano una conoscenza totale e assoluta.",
        "target": "Giovani atleti e appassionati di sport urbano nell'area MENA, alla ricerca di un brand che parli sia alla propria identità culturale sia alla cultura sportiva globale (basket, streetwear).",
        "in_evidenza": False,
    },

    # ------------------------------------------------------- UX/UI E WEB DESIGN
    {
        "slug": "grella-grella-sito",
        "nome": "Grella Grella — sito web",
        "categorie": ["ux-ui-web-design"],
        "contesto": "Freelance, progetto reale",
        "cliente": "Grella Grella — laboratorio artigianale di biscotti e pasta fresca, Mercato Civico di Santa Chiara, Cagliari",
        "anno": 2026,
        "ai_used": True,
        "ai_strumenti": ["Claude", "Claude Code"],
        "strumenti": ["Figma"],
        "overview": "Il sito per Grella Grella: un'esperienza calda e familiare, pensata per raccontare la persona e la storia dietro al prodotto.",
        "insight": "Chi cerca un piccolo laboratorio artigianale non vuole un e-commerce anonimo: vuole sentire chi c'è dietro. Il sito racconta prima la storia di Cristina e la sua famiglia, poi i prodotti — non il contrario.",
        "target": "Abitanti e visitatori di Cagliari alla ricerca di cibo e persone autentiche, oltre ai clienti storici che vogliono un modo semplice per trovare orari, indirizzo e novità.",
        "in_evidenza": True,
        "ordine_evidenza": 4,
        "vetrina": False,
    },

    # ---------------------------------------------------------------- FOTOGRAFIA
    {
        "slug": "laltra-isola",
        "nome": "L'altra isola",
        "categorie": ["fotografia"],
        "contesto": "Personale",
        "cliente": None,
        "anno": 2026,
        "ai_used": False,
        "strumenti": ["Sony Alpha 5000", "Lightroom"],
        "overview": "Un reportage fotografico sulla Sicilia, raccontata attraverso volti, abbracci, momenti condivisi e paesaggi — un ritratto del paradosso tra la bellezza assoluta dell'isola e le ferite dell'abbandono (cantieri aperti da decenni, strutture che divorano i panorami). Bianco e nero per i ritratti e i momenti umani, colore per i paesaggi.",
        "insight": "Da sarda, credevo che la mia terra fosse l'unica a portare il peso dell'abbandono. In Sicilia ho ritrovato lo stesso legame viscerale con la terra e la stessa ferita — non un progetto per denunciare, ma per capire, e forse per riconoscermi.",
        "target": "Chi ha un legame profondo con la propria terra d'origine e ne conosce il peso dell'abbandono; appassionati di fotografia documentaristica interessata al Sud Italia e ai suoi paradossi.",
        "in_evidenza": False,
    },
    {
        "slug": "viaggio-canali-francesi",
        "nome": "Reportage di un viaggio in Francia",
        "categorie": ["fotografia"],
        "contesto": "Personale",
        "cliente": None,
        "anno": 2026,
        "ai_used": False,
        "strumenti": ["iPhone 14"],
        "overview": "Un reportage fotografico in bianco e nero su un viaggio in famiglia lungo i canali francesi, scattato interamente con iPhone 14 per la sua discrezione — meno \"peso sociale\" di una fotocamera, più naturalezza negli scatti alle persone incontrate lungo il percorso.",
        "insight": "Il bisogno di sperimentare, raccontando una vacanza in famiglia con lo sguardo e il rigore di un reportage, non come semplici foto ricordo.",
        "target": "Amanti della fotografia.",
        "in_evidenza": False,
    },
]


# ---------------------------------------------------------------------------
# Funzioni di accesso ai dati. Sono l'unico punto da cui i template leggono
# i progetti: se un domani arrivassero da un database, basta riscrivere queste.
# ---------------------------------------------------------------------------

def elenco_progetti():
    """Restituisce tutti i progetti, nell'ordine definito sopra."""
    return progetti


def progetto_da_slug(slug):
    """Restituisce il progetto con lo slug richiesto, oppure None se non esiste."""
    for progetto in progetti:
        if progetto["slug"] == slug:
            return progetto
    return None


def progetti_per_categoria(slug_categoria):
    """Restituisce tutti i progetti che appartengono alla categoria indicata."""
    return [p for p in progetti if slug_categoria in p["categorie"]]


def progetti_in_evidenza():
    """
    Restituisce i progetti da mostrare nella Home ("Progetti in evidenza"),
    ordinati per la chiave "ordine_evidenza" (1 = primo). Il primo e' la vetrina.
    """
    evidenza = [p for p in progetti if p.get("in_evidenza")]
    evidenza.sort(key=lambda p: p.get("ordine_evidenza", 999))
    return evidenza


def progetti_correlati(slug_progetto, quanti=3):
    """
    Restituisce `quanti` progetti per la sezione "Altri progetti".

    1) prima i progetti della/e stessa/e categoria/e (escluso quello corrente);
    2) se non bastano (es. progetto unico nella sua categoria), completa con
       progetti di Strategia e Brand.
    Cosi' la sezione ha sempre una riga piena e non sparisce mai.
    """
    progetto = progetto_da_slug(slug_progetto)
    if progetto is None:
        return []

    categorie_progetto = set(progetto["categorie"])
    gia_presi = {slug_progetto}
    correlati = []

    # 1) stessa categoria
    for p in progetti:
        if p["slug"] not in gia_presi and categorie_progetto.intersection(p["categorie"]):
            correlati.append(p)
            gia_presi.add(p["slug"])

    # 2) se mancano, riempi con Strategia e Brand
    if len(correlati) < quanti:
        for p in progetti:
            if len(correlati) >= quanti:
                break
            if p["slug"] not in gia_presi and {"strategia", "brand"}.intersection(p["categorie"]):
                correlati.append(p)
                gia_presi.add(p["slug"])

    return correlati[:quanti]
