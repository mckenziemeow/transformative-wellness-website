/**
 * Scroll promo bar, hero video (reduced motion), tel click tracking hook.
 */
(function () {
  var cfg = window.TW_PROMO || {};
  var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function initHeroVideo() {
    var v = document.querySelector(".hero-bg-video");
    if (!v || reducedMotion) {
      if (v) {
        v.pause();
        v.removeAttribute("autoplay");
        v.style.display = "none";
      }
      var fb = document.querySelector(".hero-bg-fallback");
      if (fb) {
        fb.removeAttribute("hidden");
        fb.style.display = "block";
      }
      return;
    }
    v.addEventListener("error", function () {
      v.style.display = "none";
      var img = document.querySelector(".hero-bg-fallback");
      if (img) img.hidden = false;
    });
  }

  function initScrollPromo() {
    if (reducedMotion) return;
    var key = "tw_scroll_promo_dismissed";
    if (sessionStorage.getItem(key)) return;

    var bar = document.getElementById("scroll-promo-bar");
    if (!bar) return;

    var msg = bar.querySelector("[data-promo-message]");
    var cta = bar.querySelector("[data-promo-cta]");
    if (msg && cfg.scrollBarMessage) msg.textContent = cfg.scrollBarMessage;
    if (cta && cfg.scrollBarCta) cta.textContent = cfg.scrollBarCta;

    var shown = false;
    function onScroll() {
      if (shown) return;
      var doc = document.documentElement;
      var pct =
        ((doc.scrollTop + doc.clientHeight) / doc.scrollHeight) * 100;
      if (pct >= 50) {
        shown = true;
        bar.hidden = false;
        bar.classList.add("scroll-promo-bar--visible");
        window.removeEventListener("scroll", onScroll);
      }
    }

    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();

    var close = bar.querySelector(".scroll-promo-bar__close");
    if (close) {
      close.addEventListener("click", function () {
        sessionStorage.setItem(key, "1");
        bar.hidden = true;
        bar.classList.remove("scroll-promo-bar--visible");
      });
    }
  }

  function initTelTracking() {
    document.querySelectorAll('a[href^="tel:"]').forEach(function (a) {
      a.addEventListener("click", function () {
        if (typeof gtag === "function") {
          gtag("event", "phone_click", {
            event_category: "engagement",
            event_label: a.getAttribute("href"),
          });
        }
        if (typeof fbq === "function") {
          fbq("track", "Contact");
        }
      });
    });
  }

  function initPromoInject() {
    var cfg = window.TW_PROMO || {};
    document.querySelectorAll("[data-promo-package-urgency]").forEach(function (el) {
      if (cfg.packagesHeadline) el.textContent = cfg.packagesHeadline;
    });
    document.querySelectorAll("[data-promo-membership]").forEach(function (el) {
      if (cfg.membershipHeadline) el.textContent = cfg.membershipHeadline;
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      initHeroVideo();
      initScrollPromo();
      initTelTracking();
      initPromoInject();
    });
  } else {
    initHeroVideo();
    initScrollPromo();
    initTelTracking();
    initPromoInject();
  }
})();
