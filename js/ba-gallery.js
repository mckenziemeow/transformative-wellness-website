/**
 * Category filter for before-after gallery (Phase 2).
 */
(function () {
  function init() {
    var tabs = document.querySelectorAll(".ba-tab");
    var items = document.querySelectorAll(".gallery-ba-item");
    if (!tabs.length || !items.length) return;

    function setFilter(filter) {
      items.forEach(function (el) {
        var cat = el.getAttribute("data-category") || "all";
        var show = filter === "all" || cat === filter;
        el.hidden = !show;
      });
      tabs.forEach(function (t) {
        t.classList.toggle("is-active", t.getAttribute("data-filter") === filter);
        t.setAttribute("aria-selected", t.getAttribute("data-filter") === filter ? "true" : "false");
      });
    }

    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        setFilter(tab.getAttribute("data-filter") || "all");
      });
    });

    setFilter("all");
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
