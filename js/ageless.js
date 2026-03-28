(function () {
  var popup = document.getElementById("ageless-popup");
  if (!popup) return;
  if (sessionStorage.getItem("ageless_popup_shown")) return;

  var closeBtn = popup.querySelector(".ageless-popup-close");
  function hide() {
    popup.classList.remove("ageless-popup--visible");
    popup.setAttribute("hidden", "");
  }
  if (closeBtn) closeBtn.addEventListener("click", hide);

  setTimeout(function () {
    if (sessionStorage.getItem("ageless_popup_shown")) return;
    sessionStorage.setItem("ageless_popup_shown", "1");
    popup.removeAttribute("hidden");
    popup.classList.add("ageless-popup--visible");
  }, 5000);
})();
