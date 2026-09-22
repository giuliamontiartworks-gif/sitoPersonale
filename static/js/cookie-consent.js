/* =========================================================================
   cookie-consent.js — banner cookie + attivazione di Google Analytics.

   Regola importante per la privacy: Google Analytics NON deve mai partire
   prima che il visitatore abbia accettato. Per questo il tag gtag.js non è
   più in base.html: viene aggiunto alla pagina SOLO da questo script, solo
   dopo un click su "Accetta" (o subito, se aveva già accettato in passato).

   La scelta viene ricordata nel browser (localStorage), non sul server:
   nessun dato del visitatore arriva a noi prima del consenso.
   ========================================================================= */

(function () {
  "use strict";

  var ID_GOOGLE_ANALYTICS = "G-Z60DQ3VLJF";
  var CHIAVE_MEMORIA = "consenso-cookie-analytics"; // valori: "concesso" | "rifiutato"

  // ------------------------------------------------------ CARICA GOOGLE ANALYTICS
  function caricaGoogleAnalytics() {
    // Se per caso e' gia' stato caricato (es. doppio click), non lo rifacciamo.
    if (window._gaCaricato) {
      return;
    }
    window._gaCaricato = true;

    var script = document.createElement("script");
    script.async = true;
    script.src = "https://www.googletagmanager.com/gtag/js?id=" + ID_GOOGLE_ANALYTICS;
    document.head.appendChild(script);

    window.dataLayer = window.dataLayer || [];
    function gtag() {
      window.dataLayer.push(arguments);
    }
    window.gtag = gtag;
    gtag("js", new Date());
    // anonymize_ip: l'indirizzo IP del visitatore viene troncato prima di
    // essere inviato a Google, come raccomandato dal Garante Privacy.
    gtag("config", ID_GOOGLE_ANALYTICS, { anonymize_ip: true });
  }

  // ------------------------------------------------------------- LETTURA SCELTA
  function leggiScelta() {
    try {
      return window.localStorage.getItem(CHIAVE_MEMORIA);
    } catch (errore) {
      // Se localStorage non e' disponibile (privacy del browser, ecc.) non
      // ricordiamo nulla: il banner ricomparira' ad ogni visita, ma il sito
      // continua a funzionare.
      return null;
    }
  }

  function salvaScelta(valore) {
    try {
      window.localStorage.setItem(CHIAVE_MEMORIA, valore);
    } catch (errore) {
      /* non blocchiamo il sito se non si puo' salvare */
    }
  }

  // Scelta gia' fatta in passato: applichiamola subito, senza banner.
  var sceltaSalvata = leggiScelta();
  if (sceltaSalvata === "concesso") {
    caricaGoogleAnalytics();
  }

  // -------------------------------------------------------------------- BANNER
  var banner = document.querySelector("[data-banner-cookie]");
  if (!banner) {
    return;
  }

  // Nessuna scelta salvata: mostriamo il banner e aspettiamo un click.
  if (!sceltaSalvata) {
    banner.hidden = false;
  }

  var bottoneAccetta = banner.querySelector(".js-cookie-accetta");
  var bottoneRifiuta = banner.querySelector(".js-cookie-rifiuta");

  if (bottoneAccetta) {
    bottoneAccetta.addEventListener("click", function () {
      salvaScelta("concesso");
      caricaGoogleAnalytics();
      banner.hidden = true;
    });
  }

  if (bottoneRifiuta) {
    bottoneRifiuta.addEventListener("click", function () {
      salvaScelta("rifiutato");
      banner.hidden = true;
    });
  }

  // Link "Cookie" nel footer: permette di riaprire il banner per cambiare
  // idea in qualsiasi momento (vedi partials/footer.html).
  var linkRiapri = document.querySelector("[data-riapri-banner-cookie]");
  if (linkRiapri) {
    linkRiapri.addEventListener("click", function (evento) {
      evento.preventDefault();
      banner.hidden = false;
    });
  }
})();
