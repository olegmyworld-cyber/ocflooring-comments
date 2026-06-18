// OC Flooring — Webflow registered inline script: "OCReviewsSlider" (id: ocreviewsslider)
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
// Applied at: site header, guarded to hardwood floor INSTALLATION and REFINISHING pages.
//
// Purpose: turn the customer-reviews section into a horizontal swipe slider on phones
// (<=767px). Two different review sections exist on the site:
//
//   1. Installation pages — a self-contained html-embed <section class="ocf-reviews"> whose
//      cards live in a `.ocf-grid` of `.ocf-card`s. Known structure, so the carousel is pure
//      CSS scroll-snap applied to `.ocf-reviews .ocf-grid`.
//
//   2. Refinishing pages — the review section is rendered at runtime by an external bundle
//      (oc-trust-reviews-v9c-min.js via OCTrustReviewsInjector9d). Its internal class names
//      aren't knowable here, so we detect the card "track" generically: inside the trust
//      section (#oc-trust-reviews / [class*="oc-trust"] / [class*="trust-reviews"]) we pick
//      the element with the most direct children that carry substantial text (>=3 cards),
//      tag it `.ocrs-track`, and apply the same scroll-snap CSS.
//
// Notes:
//   - Desktop/tablet layout is untouched; the slider only activates at <=767px.
//   - CSS is injected with !important and appended to <body> so it overrides the embed's own
//     in-body <style> regardless of source order.
//   - Re-runs on timers + a short-lived MutationObserver to catch the async-rendered trust
//     section. Idempotent: CSS injected once, track tagged once (re-tagged if re-rendered).
//   - This is a best-effort generic carousel for the refinishing/trust section (its DOM can't
//     be inspected from this environment); verify on a live refinishing page.
//
// NOTE: deployed copy is minified to fit Webflow's 2000-char inline-script limit.
(function () {
  var p = location.pathname;
  if (!/hardwood-floor-(installation|refinishing)/.test(p)) return;

  var CSS =
    '@media screen and (max-width:767px){' +
    '.ocf-reviews .ocf-grid,.ocrs-track{display:flex!important;grid-template-columns:none!important;flex-wrap:nowrap!important;overflow-x:auto!important;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;gap:14px;scrollbar-width:none;scroll-padding-left:0}' +
    '.ocf-reviews .ocf-grid::-webkit-scrollbar,.ocrs-track::-webkit-scrollbar{display:none}' +
    '.ocf-reviews .ocf-grid>*,.ocrs-track>*{flex:0 0 86%!important;scroll-snap-align:start;min-width:0}' +
    '}';

  function css() {
    if (document.getElementById('ocrs-css')) return;
    var s = document.createElement('style');
    s.id = 'ocrs-css';
    s.textContent = CSS;
    document.body.appendChild(s);
  }

  // Generic: tag the review-card track inside the (runtime-rendered) trust-reviews section.
  function trust() {
    if (document.querySelector('.ocrs-track')) return;
    var sec = document.querySelector('#oc-trust-reviews,[class*="oc-trust"],[class*="trust-reviews"]');
    if (!sec) return;
    var els = sec.getElementsByTagName('*'), best = null, bn = 0, i, j;
    for (i = 0; i < els.length; i++) {
      var e = els[i], k = e.children, c = 0;
      if (k.length < 3) continue;
      for (j = 0; j < k.length; j++) { if ((k[j].textContent || '').trim().length > 60) c++; }
      if (c >= 3 && c > bn) { bn = c; best = e; }
    }
    if (best) best.classList.add('ocrs-track');
  }

  function run() { css(); try { trust(); } catch (e) {} }

  if (document.readyState != 'loading') run(); else addEventListener('DOMContentLoaded', run);
  [500, 1500, 3000, 5000].forEach(function (t) { setTimeout(run, t); });
  try {
    var mo = new MutationObserver(function () { clearTimeout(window.__ocrs); window.__ocrs = setTimeout(run, 200); });
    mo.observe(document.documentElement, { childList: true, subtree: true });
    setTimeout(function () { mo.disconnect(); }, 12000);
  } catch (e) {}
})();
