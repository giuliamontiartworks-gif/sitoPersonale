/* =========================================================================
   popup-certificazioni.js — apre il popup con i dettagli di una certificazione.

   I badge ([data-badge-certificazione]) portano i dati negli attributi data-*.
   Al click copiamo quei dati dentro il popup (#popup-certificazione) e lo
   mostriamo aggiungendo la classe "is-aperto".
   ========================================================================= */

(function () {
  "use strict";

  var popup = document.getElementById("popup-certificazione");
  if (!popup) {
    return;
  }

  var badge = document.querySelectorAll("[data-badge-certificazione]");
  var bottoneChiudi = popup.querySelector("[data-chiudi-popup]");

  // Riferimenti agli elementi del popup da riempire.
  var campoNome = popup.querySelector("[data-cert-nome]");
  var campoDescrizione = popup.querySelector("[data-cert-descrizione]");
  var campoEnte = popup.querySelector("[data-cert-ente]");
  var campoData = popup.querySelector("[data-cert-data]");
  var campoDurata = popup.querySelector("[data-cert-durata]");
  var campoId = popup.querySelector("[data-cert-id]");

  // Elemento che aveva il focus prima di aprire il popup: ci torniamo alla chiusura.
  var elementoPrecedente = null;

  function apriPopup(datiBadge) {
    campoNome.textContent = datiBadge.getAttribute("data-nome");
    campoDescrizione.textContent = datiBadge.getAttribute("data-descrizione");
    campoEnte.textContent = datiBadge.getAttribute("data-ente");
    campoData.textContent = datiBadge.getAttribute("data-data");
    campoDurata.textContent = datiBadge.getAttribute("data-durata");
    campoId.textContent = datiBadge.getAttribute("data-id-verifica");

    elementoPrecedente = datiBadge;
    popup.hidden = false;
    popup.classList.add("is-aperto");
    document.body.style.overflow = "hidden";
    if (bottoneChiudi) {
      bottoneChiudi.focus();
    }
  }

  function chiudiPopup() {
    popup.classList.remove("is-aperto");
    popup.hidden = true;
    document.body.style.overflow = "";
    if (elementoPrecedente) {
      elementoPrecedente.focus();
    }
  }

  badge.forEach(function (unBadge) {
    unBadge.addEventListener("click", function () {
      apriPopup(unBadge);
    });
  });

  if (bottoneChiudi) {
    bottoneChiudi.addEventListener("click", chiudiPopup);
  }

  // Click sullo sfondo scuro (fuori dal contenuto): chiude.
  popup.addEventListener("click", function (evento) {
    if (evento.target === popup) {
      chiudiPopup();
    }
  });

  // ESC: chiude.
  document.addEventListener("keydown", function (evento) {
    if (evento.key === "Escape" && popup.classList.contains("is-aperto")) {
      chiudiPopup();
    }
  });
})();
