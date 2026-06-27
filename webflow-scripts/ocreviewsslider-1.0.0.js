// OC Flooring — "OCReviewsSlider"
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
//
// Deployed in: the site-wide FOOTER custom-code block (Webflow Site Settings → Custom Code,
// managed via the Scripts API's site freeform footer). It is NOT applied as a registered
// script because the site is at the hard 15-applied-registered-scripts-per-site cap; freeform
// custom code is a separate block that does not count against that cap. (A registered script
// "ocreviewsslider" with the same logic also exists but is intentionally left UNAPPLIED.)
//
// Purpose: on phones, turn the new trust-reviews section (injected by octrustreviewsinjector9d /
// the oc-trust-reviews bundle) from a tall vertical stack of review cards into a single-row,
// horizontally swipeable slider. Desktop/tablet layout is untouched.
//
// Scope (matches the request "Home page and all hardwood floor refinishing cities pages"):
//   - the home page ('', '/index', '/home'), and
//   - every hardwood-floor-refinishing(/-in-<city>) page (the regex also covers the existing
//     hardwood-floor-installation pages, which carry the same review section).
//
// How it works:
//   1. css(): injects a mobile-only (<=767px) stylesheet that flips the review-card container
//      to a horizontal flex track with CSS scroll-snap, hidden scrollbar, and ~86%-width cards
//      (so the next card peeks in to signal swipeability). It targets two things: the bundle's
//      own grid (.ocf-reviews .ocf-grid) when present, and the .ocrs-track class we add below.
//   2. trust(): locates the review section (#oc-trust-reviews / [class*="oc-trust"] /
//      [class*="trust-reviews"]) and, because the bundle is minified and its inner class names
//      are not stable, finds the card container structurally — the descendant with the most
//      direct children that each hold a substantial (>60 char) block of text (i.e. the row of
//      quote cards) — and tags it .ocrs-track. The CSS does the rest.
//   3. Re-runs on DOMContentLoaded, on a few timers, and via a short-lived MutationObserver to
//      catch the bundle's async injection. Idempotent: bails once .ocrs-track exists.
//
// Blast radius is limited: the stylesheet only applies at <=767px and only to the grid/track
// inside the review section, so a mis-detection can at worst restyle that one container on
// phones — it cannot affect desktop or the rest of the page.
//
// NOTE: This file is the readable source of record. The deployed copy is minified to fit
// Webflow's 2000-char inline-script limit (see the registered script on the site).
(function () {
  var p = location.pathname.replace(/\/+$/, '');
  var home = p === '' || p === '/index' || p === '/home';
  if (!home && !/hardwood-floor-(installation|refinishing)/.test(p)) return;

  var CSS = '@media screen and (max-width:767px){' +
    '.ocf-reviews .ocf-grid,.ocrs-track{display:flex!important;grid-template-columns:none!important;' +
    'flex-wrap:nowrap!important;overflow-x:auto!important;scroll-snap-type:x mandatory;' +
    '-webkit-overflow-scrolling:touch;gap:14px;scrollbar-width:none;scroll-padding-left:16px;padding-bottom:6px}' +
    '.ocf-reviews .ocf-grid::-webkit-scrollbar,.ocrs-track::-webkit-scrollbar{display:none}' +
    '.ocf-reviews .ocf-grid>*,.ocrs-track>*{flex:0 0 86%!important;scroll-snap-align:start;min-width:0}}';

  function css() {
    if (document.getElementById('ocrs-css')) return;
    var s = document.createElement('style');
    s.id = 'ocrs-css';
    s.textContent = CSS;
    (document.body || document.head).appendChild(s);
  }

  // Tag the row of review cards inside the trust-reviews section so the CSS can turn it into a track.
  function trust() {
    if (document.querySelector('.ocrs-track')) return;
    var sec = document.querySelector('#oc-trust-reviews,[class*="oc-trust"],[class*="trust-reviews"]');
    if (!sec) return;
    var els = sec.getElementsByTagName('*'), best = null, bn = 0, i, j;
    for (i = 0; i < els.length; i++) {
      var e = els[i], k = e.children, c = 0;
      if (k.length < 3) continue;
      for (j = 0; j < k.length; j++) {
        if ((k[j].textContent || '').trim().length > 60) c++;
      }
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
