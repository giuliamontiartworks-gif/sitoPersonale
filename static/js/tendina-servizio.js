/* =========================================================================
   tendina-servizio.js — dropdown custom "Servizio" del form contatti.

   Cosa fa:
     1. apre/chiude il pannello al click sul campo;
     2. le chip sono a SELEZIONE MULTIPLA: se ne possono scegliere piu' di una,
        e cliccare una chip gia' scelta la deseleziona. ECCEZIONE: "Non lo so"
        e' esclusivo (sceglierlo annulla tutte le altre scelte, e viceversa);
     3. il pannello NON si chiude quando si sceglie: resta aperto finche' non
        lo chiude l'utente (click sul campo, click fuori, Tab, ESC);
     4. tiene aggiornato il testo del campo e mantiene un
        <input type="hidden" name="servizio"> per ogni chip scelta
        (lato server: request.form.getlist("servizio")).

   Elementi (vedi partials/dropdown_servizio.html):
     [data-dropdown-servizio]   contenitore
     [data-apri-pannello]       il "campo" cliccabile
     [data-testo-selezione]     lo <span> con il testo del campo
     [data-chip-servizio]       ogni chip (ha data-valore)
     [data-contenitore-hidden]  il div dove mettiamo gli <input hidden>
   ========================================================================= */

(function () {
  "use strict";

  var dropdown = document.querySelector("[data-dropdown-servizio]");
  if (!dropdown) {
    return;
  }

  var campo = dropdown.querySelector("[data-apri-pannello]");
  var testoSelezione = dropdown.querySelector("[data-testo-selezione]");
  var chips = dropdown.querySelectorAll("[data-chip-servizio]");
  var contenitoreHidden = dropdown.querySelector("[data-contenitore-hidden]");

  var TESTO_VUOTO = "Di che servizio hai bisogno?";

  function apriChiudiPannello() {
    var eraAperto = dropdown.classList.toggle("is-aperto");
    campo.setAttribute("aria-expanded", eraAperto ? "true" : "false");
  }

  function chiudiPannello() {
    dropdown.classList.remove("is-aperto");
    campo.setAttribute("aria-expanded", "false");
  }

  // Ricostruisce il testo del campo e gli input nascosti in base alle chip scelte.
  function aggiornaStato() {
    var scelti = [];
    chips.forEach(function (chip) {
      if (chip.getAttribute("aria-pressed") === "true") {
        scelti.push(chip.getAttribute("data-valore"));
      }
    });

    // Testo del campo.
    if (scelti.length === 0) {
      testoSelezione.textContent = TESTO_VUOTO;
      testoSelezione.classList.add("placeholder");
    } else {
      testoSelezione.textContent = scelti.join(", ");
      testoSelezione.classList.remove("placeholder");
    }

    // Un input nascosto per ogni servizio scelto.
    contenitoreHidden.innerHTML = "";
    scelti.forEach(function (valore) {
      var input = document.createElement("input");
      input.type = "hidden";
      input.name = "servizio";
      input.value = valore;
      contenitoreHidden.appendChild(input);
    });
  }

  // --- Collegamento eventi ---

  campo.addEventListener("click", apriChiudiPannello);

  function deselezionaNonLoSo() {
    chips.forEach(function (chip) {
      if (chip.getAttribute("data-valore") === "Non lo so") {
        chip.setAttribute("aria-pressed", "false");
      }
    });
  }

  function deselezionaTutte() {
    chips.forEach(function (chip) {
      chip.setAttribute("aria-pressed", "false");
    });
  }

  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      var eraAttiva = chip.getAttribute("aria-pressed") === "true";
      var eNonLoSo = chip.getAttribute("data-valore") === "Non lo so";

      if (eraAttiva) {
        // stavo deselezionando questa chip
        chip.setAttribute("aria-pressed", "false");
      } else if (eNonLoSo) {
        // "Non lo so" e' esclusivo: annulla tutte le altre scelte
        deselezionaTutte();
        chip.setAttribute("aria-pressed", "true");
      } else {
        // un servizio normale: se "Non lo so" era scelto, va tolto
        deselezionaNonLoSo();
        chip.setAttribute("aria-pressed", "true");
      }

      aggiornaStato();
      // Il pannello resta APERTO: si sceglie e si continua a scegliere.
    });
  });

  // Click fuori dal dropdown (es. su un altro campo): il pannello si chiude.
  document.addEventListener("click", function (evento) {
    if (!dropdown.contains(evento.target)) {
      chiudiPannello();
    }
  });

  // Il focus va su un altro elemento (Tab o click in un altro campo): si chiude.
  document.addEventListener("focusin", function (evento) {
    if (!dropdown.contains(evento.target)) {
      chiudiPannello();
    }
  });

  // ESC chiude il pannello.
  document.addEventListener("keydown", function (evento) {
    if (evento.key === "Escape") {
      chiudiPannello();
    }
  });

  // Stato iniziale.
  aggiornaStato();
})();
