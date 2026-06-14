// OC Flooring — Webflow registered inline script: "BonaMobileFix" (id: bonamobilefix)
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
// Applied at: site footer. Runs wherever the Bona "tone/sealer" widget
// (#oc-tone-steps / #bona-tone-widget) appears (home + hardwood-floor-refinishing-in-* pages).
//
// What it does:
//   1. Mobile layout: collapses the widget to a single column and clears min/max-width
//      constraints on the inner columns so it fits narrow screens.
//   2. "CUSTOMER FAVORITE" badge (mobile): the full red text badge overlaid on the room
//      image collided with the "LIVING / KITCHEN" toggles and ran off the image edge on
//      phones. On screens <= 600px the badge is collapsed to a compact star (★) pinned in
//      the top-right corner of the image; the full text badge is restored on desktop.
//
// Implementation notes:
//   - The widget is a minified, runtime-injected bundle, so elements are located by visible
//     text ("CUSTOMER FAVORITE", "LIVING"/"KITCHEN") rather than class names.
//   - A stable handle to the badge element is cached on window.__fb, and its original HTML on
//     b.__h, so the star swap is reversible across viewport changes even after the text is
//     replaced. b.__m tracks the current (star vs full) state to avoid redundant DOM writes.
//   - Re-runs on resize and on a few timers to catch the widget's async injection.
//
// NOTE: This file is the readable source of record. The deployed copy is minified to fit
// Webflow's 2000-char inline-script limit (see the registered script on the site).
(function () {
  function T(e) { return (e.textContent || '').replace(/\s+/g, ' ').trim().toUpperCase(); }

  // Smallest element under `r` whose text contains `n`.
  function leaf(r, n) {
    var a = r.querySelectorAll('*'), h = null;
    for (var i = 0; i < a.length; i++) { if (T(a[i]).indexOf(n) >= 0) { if (!h || h.contains(a[i])) h = a[i]; } }
    return h;
  }

  // Nearest absolutely/fixed-positioned ancestor (the actual overlay box), else null.
  function pa(e, r) {
    while (e && e !== r) { var p = getComputedStyle(e).position; if (p == 'absolute' || p == 'fixed') return e; e = e.parentElement; }
    return null;
  }

  function fix() {
    var r = document.getElementById('oc-tone-steps') || document.getElementById('bona-tone-widget');
    if (!r) return;

    // 1) Mobile single-column layout.
    var m = window.innerWidth <= 900, w = r.querySelector('.ots-wrap');
    if (w) w.style.setProperty('grid-template-columns', m ? 'minmax(0,1fr)' : '', 'important');
    ['.ots-slider-col', '.ots-steps-col', '#bona-tone-widget', '.bt-shell', '.bt-slider', '.bt-stops'].forEach(function (s) {
      var e = r.querySelector(s);
      if (e) { e.style.setProperty('min-width', m ? '0' : '', 'important'); e.style.setProperty('max-width', m ? '100%' : '', 'important'); }
    });

    // 2) Badge: locate once and keep a stable, reversible handle.
    var b = window.__fb;
    if (!b || !document.body.contains(b)) {
      var bl = leaf(r, 'CUSTOMER FAVORITE');
      if (!bl) return;
      b = pa(bl, r) || bl;
      window.__fb = b;
      b.__h = b.innerHTML; // original badge markup (star + text)
      b.__m = 0;           // 0 = full, 1 = star-only
    }

    var sm = window.innerWidth <= 600;
    if (sm && !b.__m) { b.innerHTML = '★'; b.__m = 1; }  // collapse to a star on phones
    if (!sm && b.__m) { b.innerHTML = b.__h; b.__m = 0; }     // restore full badge on desktop

    var S = b.style;
    ['top', 'bottom', 'right', 'left', 'width', 'min-width', 'padding', 'font-size'].forEach(function (k) { S.removeProperty(k); });
    if (sm) {
      // Pin the compact star to the top-right corner, clear of the top-left toggles.
      S.setProperty('top', '8px', 'important');
      S.setProperty('right', '8px', 'important');
      S.setProperty('left', 'auto', 'important');
      S.setProperty('bottom', 'auto', 'important');
      S.setProperty('width', 'auto', 'important');
      S.setProperty('min-width', '0', 'important');
      S.setProperty('padding', '5px 8px', 'important');
      S.setProperty('font-size', '15px', 'important');
    }
  }

  function init() {
    fix();
    addEventListener('resize', fix);
    [300, 900, 1600, 2600, 4000, 6000].forEach(function (t) { setTimeout(fix, t); });
  }
  if (document.readyState != 'loading') init(); else addEventListener('DOMContentLoaded', init);
})();
