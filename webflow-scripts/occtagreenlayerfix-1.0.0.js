// OC Flooring — Webflow registered inline script: "OCCtaGreenLayerFix" (id: occtagreenlayerfix)
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
// Applied at: site footer.
//
// Problem (2026-09-01): the site-footer "green contact CTA" tweak adds the class oc-cta-green
// (background + color:#fff !important) to every a[href="/contact"] whose class matches
// /button|btn|cta/i. That also catches Webflow's layered .button-wrapper buttons, which paint
// their own .button-background pill on top of the anchor: the green never shows, but the forced
// white color is inherited by .button-text, leaving a white label on a white pill. On
// /flooring-services-near-me/floor-refinishing that is the "Free 30-Minute In-Home Flooring Visit"
// CTA — the button rendered as an empty white blob.
//
// Fix: keep the green treatment for flat custom CTAs, take the class back off the layered Webflow
// buttons so they return to their designed colors. The injected guard rule keeps the label legible
// even in the window before the class is removed.
(function () {
  var C = 'oc-cta-green';
  try {
    var s = document.createElement('style');
    s.id = 'oc-cta-green-layer-guard';
    s.textContent = 'a.button-wrapper.' + C + ' .button-background{background-color:#1e7a3c!important}';
    (document.head || document.documentElement).appendChild(s);
  } catch (e) {}
  function strip() {
    var l = document.querySelectorAll('a.button-wrapper.' + C);
    for (var i = 0; i < l.length; i++) l[i].classList.remove(C);
  }
  function run() { strip(); setTimeout(strip, 0); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', run);
  else run();
  window.addEventListener('load', run);
  setTimeout(strip, 800);
  setTimeout(strip, 2500);
})();
