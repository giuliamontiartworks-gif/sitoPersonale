/* =========================================================================
   modulo-contatti.js — tiene disabilitato il bottone "Invia messaggio"
   finché TUTTI i campi non sono compilati (sono tutti obbligatori):
     - Nome e cognome
     - Email (non vuota e in un formato valido)
     - Numero di telefono
     - Servizio (una chip selezionata)
     - Messaggio

   Elementi (vedi contatti.html / partials/):
     [data-modulo-contatti]   il <form>
     .js-invia                il bottone di invio
     #campo-nome / #campo-email / #campo-messaggio   i campi di testo
     [data-chip-servizio]     le chip del campo "Servizio"
   ========================================================================= */

(function () {
  "use strict";

  var form = document.querySelector("[data-modulo-contatti]");
  if (!form) {
    return;
  }

  var bottoneInvia = form.querySelector(".js-invia");
  if (!bottoneInvia) {
    return;
  }

  var campoNome = form.querySelector("#campo-nome");
  var campoEmail = form.querySelector("#campo-email");
  var campoTelefono = form.querySelector("#campo-telefono");
  var campoMessaggio = form.querySelector("#campo-messaggio");
  var chipsServizio = form.querySelectorAll("[data-chip-servizio]");

  function compilato(campo) {
    return !!campo && campo.value.trim() !== "";
  }

  function emailValida() {
    return compilato(campoEmail) && campoEmail.checkValidity();
  }

  function almenoUnServizio() {
    for (var i = 0; i < chipsServizio.length; i++) {
      if (chipsServizio[i].getAttribute("aria-pressed") === "true") {
        return true;
      }
    }
    return false;
  }

  function aggiornaBottone() {
    var tuttoOk =
      compilato(campoNome) &&
      emailValida() &&
      compilato(campoTelefono) &&
      compilato(campoMessaggio) &&
      almenoUnServizio();
    bottoneInvia.disabled = !tuttoOk;
  }

  // Ricontrolla a ogni digitazione...
  form.addEventListener("input", aggiornaBottone);
  // ...e dopo ogni click nel form (le chip "Servizio" cambiano al click:
  // le leggiamo dopo il tick, quando tendina-servizio.js le ha aggiornate).
  form.addEventListener("click", function () {
    setTimeout(aggiornaBottone, 0);
  });

  // Stato iniziale: bottone disabilitato.
  aggiornaBottone();
})();
