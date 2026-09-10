/* =========================================================================
   menu-mobile.js — apertura/chiusura del pannello di navigazione mobile.

   Elementi coinvolti (vedi partials/header.html):
     - [data-apri-menu]   : bottone hamburger
     - [data-chiudi-menu] : bottone X dentro il pannello
     - #nav-mobile        : il pannello a schermo intero
   ========================================================================= */

(function () {
  "use strict";

  var bottoneApri = document.querySelector("[data-apri-menu]");
  var bottoneChiudi = document.querySelector("[data-chiudi-menu]");
  var pannello = document.getElementById("nav-mobile");

  // Se manca uno dei pezzi non facciamo nulla (es. pagina senza header).
  if (!bottoneApri || !pannello) {
    return;
  }

  function apriMenu() {
    pannello.classList.add("is-aperto");
    pannello.setAttribute("aria-hidden", "false");
    bottoneApri.setAttribute("aria-expanded", "true");
    // Blocca lo scroll della pagina dietro al pannello.
    document.body.style.overflow = "hidden";
  }

  function chiudiMenu() {
    pannello.classList.remove("is-aperto");
    pannello.setAttribute("aria-hidden", "true");
    bottoneApri.setAttribute("aria-expanded", "false");
    document.body.style.overflow = "";
  }

  bottoneApri.addEventListener("click", apriMenu);

  if (bottoneChiudi) {
    bottoneChiudi.addEventListener("click", chiudiMenu);
  }

  // Chiude il menu con il tasto ESC.
  document.addEventListener("keydown", function (evento) {
    if (evento.key === "Escape" && pannello.classList.contains("is-aperto")) {
      chiudiMenu();
    }
  });

  // Chiude il menu quando si clicca un link al suo interno (cambio pagina).
  var linkInterni = pannello.querySelectorAll("a");
  linkInterni.forEach(function (link) {
    link.addEventListener("click", chiudiMenu);
  });
})();
