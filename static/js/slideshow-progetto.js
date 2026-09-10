/* =========================================================================
   slideshow-progetto.js — slideshow della pagina progetto + pannello "Info".

   Slideshow:
     [data-slide]        ogni immagine; quella visibile ha la classe "is-attiva"
     [data-slide-prec]   freccia "precedente"
     [data-slide-succ]   freccia "successiva"
     [data-contatore]    la pillola "1 / N"

   Pannello Info:
     [data-info-toggle]  il bottone "Info"
     [data-pannello-info] il pannello (il contenuto e' gia' nell'HTML, per la SEO)
     la classe "is-info-aperto" sul contenitore [data-slideshow] apre il pannello
   ========================================================================= */

(function () {
  "use strict";

  var slideshow = document.querySelector("[data-slideshow]");
  if (!slideshow) {
    return;
  }

  // ---------------------------------------------------------- TORNA INDIETRO
  // Il link "Torna a ..." punta di default alla pagina categoria. Ma se
  // l'utente arriva da un'altra pagina del sito (Portfolio, Home, un'altra
  // categoria, un altro progetto), il link lo riporta a QUELLA pagina, nel
  // punto in cui era (history.back).
  (function gestisciRitorno() {
    var ritorno = slideshow.querySelector("[data-ritorno]");
    if (!ritorno || !document.referrer) {
      return;
    }

    var provenienza;
    try {
      provenienza = new URL(document.referrer);
    } catch (errore) {
      return;
    }

    // Solo se arriva da questo stesso sito e da una pagina diversa da questa.
    if (provenienza.origin !== window.location.origin) {
      return;
    }
    if (provenienza.pathname === window.location.pathname) {
      return;
    }

    var etichetta = "Indietro";
    var percorso = provenienza.pathname;
    if (percorso === "/portfolio") {
      etichetta = "Torna al portfolio";
    } else if (percorso.indexOf("/categoria/") === 0) {
      etichetta = "Torna alla categoria";
    } else if (percorso === "/") {
      etichetta = "Torna alla home";
    } else if (percorso.indexOf("/progetto/") === 0) {
      etichetta = "Torna al progetto";
    }

    var testo = ritorno.querySelector("[data-ritorno-testo]") || ritorno;
    testo.textContent = "← " + etichetta;

    // Fallback (se il JS del click non parte): l'href diventa la pagina di provenienza.
    ritorno.setAttribute("href", provenienza.pathname + provenienza.search);

    ritorno.addEventListener("click", function (evento) {
      evento.preventDefault();
      window.history.back();
    });
  })();

  // ---------------------------------------------------------------- SLIDESHOW
  var slides = slideshow.querySelectorAll("[data-slide]");
  var frecciaPrec = slideshow.querySelector("[data-slide-prec]");
  var frecciaSucc = slideshow.querySelector("[data-slide-succ]");
  var contatore = slideshow.querySelector("[data-contatore]");

  var indiceAttivo = 0;

  function mostraSlide(nuovoIndice) {
    // Indice "circolare": dopo l'ultima si torna alla prima e viceversa.
    if (nuovoIndice < 0) {
      nuovoIndice = slides.length - 1;
    } else if (nuovoIndice >= slides.length) {
      nuovoIndice = 0;
    }

    // Se sto lasciando una slide con un video in riproduzione, lo metto in pausa.
    var videoUscente = slides[indiceAttivo].querySelector("video");
    if (videoUscente) {
      videoUscente.pause();
    }

    slides[indiceAttivo].classList.remove("is-attiva");
    slides[nuovoIndice].classList.add("is-attiva");
    indiceAttivo = nuovoIndice;

    if (contatore) {
      contatore.textContent = (indiceAttivo + 1) + " / " + slides.length;
    }
  }

  if (frecciaPrec) {
    frecciaPrec.addEventListener("click", function () {
      mostraSlide(indiceAttivo - 1);
    });
  }
  if (frecciaSucc) {
    frecciaSucc.addEventListener("click", function () {
      mostraSlide(indiceAttivo + 1);
    });
  }

  // ------------------------------------------------------------- PANNELLO INFO
  var bottoneInfo = slideshow.querySelector("[data-info-toggle]");
  var maniglia = slideshow.querySelector("[data-chiudi-info]");
  var pannello = slideshow.querySelector("[data-pannello-info]");

  // Durata e curva del movimento "accompagnato" (apertura, chiusura, ritorno).
  // Il TRASCINAMENTO invece segue il puntatore 1:1, senza transizione.
  var DURATA = 420; // millisecondi
  var CURVA = "cubic-bezier(0.22, 1, 0.36, 1)"; // curva morbida "tipo Smart Animate"

  function pannelloAperto() {
    return slideshow.classList.contains("is-info-aperto");
  }

  // Dopo l'apertura/chiusura ripulisce gli stili inline e sistema la classe.
  function nascondiPannello() {
    slideshow.classList.remove("is-info-aperto");
    if (pannello) {
      pannello.style.transition = "";
      pannello.style.transform = "";
    }
  }

  function apriPannello() {
    if (pannelloAperto()) {
      return;
    }
    slideshow.classList.add("is-info-aperto");
    if (bottoneInfo) {
      bottoneInfo.setAttribute("aria-expanded", "true");
    }
    if (!pannello) {
      return;
    }
    // Parte da sotto (fuori dalla card) e sale con una transizione morbida.
    pannello.style.transition = "none";
    pannello.style.transform = "translateY(100%)";
    void pannello.offsetWidth; // forza il browser a "vedere" lo stato di partenza
    pannello.style.transition = "transform " + DURATA + "ms " + CURVA;
    pannello.style.transform = "translateY(0)";
  }

  function chiudiPannello() {
    if (!pannelloAperto()) {
      return;
    }
    if (bottoneInfo) {
      bottoneInfo.setAttribute("aria-expanded", "false");
    }
    if (!pannello) {
      nascondiPannello();
      return;
    }
    // Scivola giù (accompagnato) e poi sparisce davvero, ritagliato dalla card.
    pannello.style.transition = "transform " + DURATA + "ms " + CURVA;
    pannello.style.transform = "translateY(100%)";
    setTimeout(nascondiPannello, DURATA);
  }

  if (bottoneInfo) {
    bottoneInfo.addEventListener("click", function () {
      if (pannelloAperto()) {
        chiudiPannello();
      } else {
        apriPannello();
      }
    });
  }

  // ----------------------------------------------------------------------------
  // La maniglia in alto al pannello e' uno SLIDER: mentre la si tiene premuta
  // e si trascina, il pannello segue ESATTAMENTE il puntatore. Al rilascio:
  //   - se e' stato tirato giu' oltre una soglia -> scivola via e si chiude;
  //   - altrimenti -> torna su dolcemente (nessuna chiusura).
  // Un semplice "tocco" senza trascinamento NON chiude (torna su e basta).
  // ----------------------------------------------------------------------------
  if (maniglia && pannello) {
    var trascinando = false;
    var yPartenza = 0;
    var spostamento = 0;

    function muovi(evento) {
      if (!trascinando) {
        return;
      }
      spostamento = evento.clientY - yPartenza;
      // Verso l'alto il pannello "resiste" (non deve salire oltre la sua posizione).
      if (spostamento < 0) {
        spostamento = spostamento / 4;
      }
      // Nessuna transizione: il pannello sta dove lo porta il puntatore.
      pannello.style.transform = "translateY(" + spostamento + "px)";
    }

    function rilascia() {
      if (!trascinando) {
        return;
      }
      trascinando = false;
      document.removeEventListener("pointermove", muovi);
      document.removeEventListener("pointerup", rilascia);
      document.removeEventListener("pointercancel", rilascia);

      // Serve un trascinamento deciso (~1/3 del pannello, max 180px) per chiudere.
      var soglia = Math.min(180, pannello.offsetHeight * 0.33);
      pannello.style.transition = "transform " + DURATA + "ms " + CURVA;

      if (spostamento > soglia) {
        pannello.style.transform = "translateY(100%)";
        setTimeout(nascondiPannello, DURATA);
        if (bottoneInfo) {
          bottoneInfo.setAttribute("aria-expanded", "false");
        }
      } else {
        // Torna al suo posto, accompagnato.
        pannello.style.transform = "translateY(0)";
      }
    }

    maniglia.addEventListener("pointerdown", function (evento) {
      if (!pannelloAperto()) {
        return;
      }
      trascinando = true;
      yPartenza = evento.clientY;
      spostamento = 0;
      pannello.style.transition = "none"; // il drag deve seguire il puntatore 1:1
      if (maniglia.setPointerCapture) {
        try {
          maniglia.setPointerCapture(evento.pointerId);
        } catch (errore) {
          /* alcuni browser lo rifiutano: non e' un problema */
        }
      }
      document.addEventListener("pointermove", muovi);
      document.addEventListener("pointerup", rilascia);
      document.addEventListener("pointercancel", rilascia);
    });

    // Accessibilità da tastiera: Invio / Spazio sulla maniglia chiude il pannello.
    maniglia.addEventListener("keydown", function (evento) {
      if (evento.key === "Enter" || evento.key === " ") {
        evento.preventDefault();
        chiudiPannello();
      }
    });
  }

  // Click fuori dal pannello (e fuori dal bottone Info): chiude.
  document.addEventListener("click", function (evento) {
    if (!pannelloAperto()) {
      return;
    }
    var dentroPannello = pannello && pannello.contains(evento.target);
    var sulBottone = bottoneInfo && bottoneInfo.contains(evento.target);
    if (!dentroPannello && !sulBottone) {
      chiudiPannello();
    }
  });

  // ESC: chiude il pannello.
  document.addEventListener("keydown", function (evento) {
    if (evento.key === "Escape" && pannelloAperto()) {
      chiudiPannello();
    }
  });

  // Frecce della tastiera: scorrono le immagini del progetto (come i bottoni).
  // Solo se ci sono piu' media e il pannello Info e' chiuso. Non intercetta le
  // frecce quando il focus e' su un video (servono a scorrerlo).
  document.addEventListener("keydown", function (evento) {
    if (slides.length < 2 || pannelloAperto()) {
      return;
    }
    if (evento.target && evento.target.tagName === "VIDEO") {
      return;
    }
    if (evento.key === "ArrowRight") {
      mostraSlide(indiceAttivo + 1);
    } else if (evento.key === "ArrowLeft") {
      mostraSlide(indiceAttivo - 1);
    }
  });
})();
