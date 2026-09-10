/* =========================================================================
   mostra-altro.js — bottone "Mostra altro" per le certificazioni (Chi sono).

   Di base si vedono 3 certificazioni; il bottone rivela le altre e cambia
   testo in "Mostra meno".

   Elementi (vedi chi-sono.html):
     [data-elenco-certificazioni]  il contenitore dei badge
     [data-mostra-altro]           il bottone
   ========================================================================= */

(function () {
  "use strict";

  var bottone = document.querySelector("[data-mostra-altro]");
  var elenco = document.querySelector("[data-elenco-certificazioni]");
  if (!bottone || !elenco) {
    return;
  }

  bottone.addEventListener("click", function () {
    var espanso = elenco.classList.toggle("is-espanso");
    bottone.setAttribute("aria-expanded", espanso ? "true" : "false");
    bottone.textContent = espanso ? "Mostra meno" : "Mostra altro";
  });
})();
