/* =========================================================================
   carosello-portfolio.js — "tira ancora per vedere tutti".

   Sulla pagina Portfolio, ogni categoria ha un carosello orizzontale di 3
   progetti. Su MOBILE, se l'utente arriva in fondo al carosello e continua
   a trascinare verso destra (come per cercare altri progetti), viene portato
   direttamente alla pagina di quella categoria.

   C'e' una RESISTENZA voluta: la freccia all'inizio si muove pochissimo e
   bisogna trascinare parecchio piu' del previsto per far scattare la
   navigazione. Cosi' non succede per sbaglio.

   Elementi (vedi portfolio.html):
     [data-carosello]      il contenitore che scorre in orizzontale
     [data-vai-categoria]  il link (freccia) verso /categoria/<slug>
   ========================================================================= */

(function () {
  "use strict";

  // Il comportamento vale solo per la vista mobile (sotto i 960px).
  var vistaMobile = window.matchMedia("(max-width: 959px)");

  // Pixel di trascinamento OLTRE il bordo necessari per entrare nella categoria.
  // Volutamente alto: dev'essere un gesto deciso, non un movimento naturale.
  var SOGLIA_PIXEL = 190;

  var caroselli = document.querySelectorAll("[data-carosello]");

  caroselli.forEach(function (carosello) {
    var link = carosello.querySelector("[data-vai-categoria]");
    if (!link) {
      return;
    }
    var urlCategoria = link.getAttribute("href");

    var oltreBordo = 0;             // px di trascinamento accumulati oltre il bordo
    var ultimaX = null;             // ultima posizione X del dito
    var navigazionePartita = false;
    var timerRitorno = null;

    // Il carosello e' scrollato fino in fondo a destra? (con 2px di tolleranza)
    function alBordoDestro() {
      return carosello.scrollLeft + carosello.clientWidth >= carosello.scrollWidth - 2;
    }

    // Feedback con RESISTENZA: la curva ^1.8 fa muovere la freccia pochissimo
    // all'inizio (si "sente" di dover tirare di piu'), poi accelera verso la soglia.
    function aggiornaFreccia() {
      var lineare = Math.min(oltreBordo / SOGLIA_PIXEL, 1);
      var conResistenza = Math.pow(lineare, 1.8);
      link.style.transform =
        "translateX(" + (conResistenza * 16) + "px) scale(" + (1 + conResistenza * 0.28) + ")";
    }

    // Riporta la freccia a riposo in modo morbido (classe .is-tornando -> CSS).
    function tornaARiposo() {
      oltreBordo = 0;
      if (!link.style.transform) {
        return;
      }
      link.classList.add("is-tornando");
      link.style.transform = "";
      clearTimeout(timerRitorno);
      timerRitorno = setTimeout(function () {
        link.classList.remove("is-tornando");
      }, 400);
    }

    // delta > 0 = si sta trascinando verso destra (verso "altri progetti").
    function accumula(delta) {
      if (!vistaMobile.matches || navigazionePartita) {
        return;
      }
      if (delta > 0 && alBordoDestro()) {
        oltreBordo += delta;
        aggiornaFreccia();
        if (oltreBordo >= SOGLIA_PIXEL) {
          navigazionePartita = true;
          window.location.href = urlCategoria;
        }
      } else if (delta < 0 && oltreBordo > 0) {
        // si torna indietro: annulla l'accumulo (senza animazione, segue il gesto)
        oltreBordo = 0;
        link.style.transform = "";
      }
    }

    // --- Touch (mobile) ---
    carosello.addEventListener("touchstart", function (evento) {
      ultimaX = evento.touches[0].clientX;
      oltreBordo = 0;
    }, { passive: true });

    carosello.addEventListener("touchmove", function (evento) {
      if (ultimaX === null) {
        return;
      }
      var x = evento.touches[0].clientX;
      // dito che va verso sinistra = contenuto che scorre verso destra
      var delta = ultimaX - x;
      ultimaX = x;
      accumula(delta);
    }, { passive: true });

    carosello.addEventListener("touchend", function () {
      ultimaX = null;
      if (!navigazionePartita) {
        tornaARiposo();
      }
    }, { passive: true });

    // --- Trackpad: scroll orizzontale ---
    var timerWheel = null;
    carosello.addEventListener("wheel", function (evento) {
      // solo gesti prevalentemente orizzontali
      if (Math.abs(evento.deltaX) <= Math.abs(evento.deltaY)) {
        return;
      }
      accumula(evento.deltaX);
      // poco dopo che si smette di scrollare, la freccia torna a riposo
      clearTimeout(timerWheel);
      timerWheel = setTimeout(tornaARiposo, 220);
    }, { passive: true });
  });
})();
