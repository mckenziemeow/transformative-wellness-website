/**
 * Seasonal / urgency copy — toggle `active` or edit `text` without touching HTML.
 * `TW_PROMO` is derived for existing site-enhancements.js hooks.
 */
window.PROMO_CONFIG = {
  packagePromo: { text: "Spring Special — Book by April 15", active: true },
  membershipPromo: {
    text: "Join this month: 20% off first treatment (select services)",
    active: true,
  },
  newPatientOffer: {
    text: "Complimentary B12 with first consultation",
    active: true,
  },
};

(function () {
  var P = window.PROMO_CONFIG || {};
  window.TW_PROMO = {
    packagesDeadline: "April 15, 2026",
    packagesHeadline:
      P.packagePromo && P.packagePromo.active ? P.packagePromo.text : "",
    membershipHeadline:
      P.membershipPromo && P.membershipPromo.active ? P.membershipPromo.text : "",
    scrollBarMessage:
      P.newPatientOffer && P.newPatientOffer.active
        ? "New Patient Special: Complimentary B12 shot with your first consultation"
        : "",
    scrollBarCta: "Book Now",
  };
})();
