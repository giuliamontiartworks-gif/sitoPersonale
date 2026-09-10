/* =========================================================================
   toast-copia.js — copia l'email negli appunti e mostra il toast "Email copiata!".

   Elementi:
     .js-copia-email   il bottone "Copia" (pagina Contatti)
     [data-email]       la pillola che contiene l'indirizzo email
     #toast-copia       la notifica (vedi partials/toast.html)
   ========================================================================= */

(function () {
  "use strict";

  var bottoneCopia = document.querySelector(".js-copia-email");
  var pillolaEmail = document.querySelector("[data-email]");
  var toast = document.getElementById("toast-copia");

  if (!bottoneCopia || !pillolaEmail || !toast) {
    return;
  }

  var timerNascondi = null;

  function mostraToast() {
    toast.hidden = false;
    // Forza un reflow cosi' la transizione di opacita' parte davvero.
    void toast.offsetWidth;
    toast.classList.add("is-visibile");

    // Si nasconde da solo dopo ~1.8 secondi.
    clearTimeout(timerNascondi);
    timerNascondi = setTimeout(nascondiToast, 1800);
  }

  function nascondiToast() {
    toast.classList.remove("is-visibile");
    // Aspetta la fine della transizione prima di rimetterlo hidden.
    setTimeout(function () {
      toast.hidden = true;
    }, 250);
  }

  function copiaEmail() {
    var email = pillolaEmail.textContent.trim();

    // API moderna, con fallback per browser più vecchi.
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(email).then(mostraToast).catch(copiaConFallback);
    } else {
      copiaConFallback();
    }

    function copiaConFallback() {
      var campoTemporaneo = document.createElement("textarea");
      campoTemporaneo.value = email;
      campoTemporaneo.style.position = "fixed";
      campoTemporaneo.style.opacity = "0";
      document.body.appendChild(campoTemporaneo);
      campoTemporaneo.select();
      try {
        document.execCommand("copy");
        mostraToast();
      } catch (errore) {
        /* se anche il fallback fallisce non mostriamo nulla */
      }
      document.body.removeChild(campoTemporaneo);
    }
  }

  bottoneCopia.addEventListener("click", copiaEmail);

  // Click fuori dal toast: lo nasconde subito.
  document.addEventListener("click", function (evento) {
    if (toast.classList.contains("is-visibile") &&
        evento.target !== bottoneCopia &&
        !toast.contains(evento.target)) {
      nascondiToast();
    }
  });
})();
