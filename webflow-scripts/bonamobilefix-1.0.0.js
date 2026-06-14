// OC Flooring — Webflow registered inline script: "BonaMobileFix" (id: bonamobilefix)
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
// Applied at: site footer. Runs wherever the Bona "tone/sealer" widget (#oc-tone-steps /
// #bona-tone-widget) is present (home page + hardwood-floor-refinishing-in-* city pages).
//
// What it does:
//   1. Mobile layout: collapses the widget to a single column and clears min/max-width
//      constraints on the inner columns so it fits narrow screens.
//   2. Badge overlap fix (added 2026-06-14): the red "★ CUSTOMER FAVORITE" badge was
//      overlapping the "LIVING / KITCHEN" room toggle pills on phones. The fix locates the
//      badge and the toggle by their text (class-name agnostic, robust to the minified
//      bundle), measures their live bounding boxes, and only if they actually overlap nudges
//      the badge down to just below the toggle row. It also keeps the badge on one line and
//      slightly smaller on phones. Re-runs on resize, on timers, and via a MutationObserver
//      to catch the widget's late/async injection.
(function () {
  function T(e) { return (e.textContent || '').replace(/\s+/g, ' ').trim().toUpperCase(); }
  function leaf(r, n) {
    var a = r.querySelectorAll('*'), h = null;
    for (var i = 0; i < a.length; i++) { if (T(a[i]).indexOf(n) >= 0) { if (!h || h.contains(a[i])) h = a[i]; } }
    return h;
  }
  function pa(e, r) {
    while (e && e !== r) { var ps = getComputedStyle(e).position; if (ps == 'absolute' || ps == 'fixed') return e; e = e.parentElement; }
    return null;
  }
  function ov(a, b) { return !(a.right <= b.left || a.left >= b.right || a.bottom <= b.top || a.top >= b.bottom); }
  function fix() {
    var root = document.getElementById('oc-tone-steps') || document.getElementById('bona-tone-widget');
    if (!root) return;
    var m = window.innerWidth <= 900;
    var w = root.querySelector('.ots-wrap');
    if (w) { if (m) { w.style.setProperty('grid-template-columns', 'minmax(0,1fr)', 'important'); } else { w.style.removeProperty('grid-template-columns'); } }
    ['.ots-slider-col', '.ots-steps-col', '#bona-tone-widget', '.bt-shell', '.bt-slider', '.bt-stops'].forEach(function (s) {
      var e = root.querySelector(s);
      if (e) { if (m) { e.style.setProperty('min-width', '0', 'important'); e.style.setProperty('max-width', '100%', 'important'); } else { e.style.removeProperty('min-width'); e.style.removeProperty('max-width'); } }
    });
    var bl = leaf(root, 'CUSTOMER FAVORITE');
    if (bl) {
      var b = pa(bl, root) || bl;
      var tl = leaf(root, 'LIVING') || leaf(root, 'KITCHEN');
      var t = tl ? (pa(tl, root) || tl) : null;
      ['top', 'bottom', 'right', 'left', 'max-width', 'font-size', 'white-space', 'box-sizing'].forEach(function (k) { b.style.removeProperty(k); });
      if (window.innerWidth <= 600) {
        b.style.setProperty('font-size', '10px', 'important');
        b.style.setProperty('white-space', 'nowrap', 'important');
        // Pin inside the image's right edge so the badge is never clipped on phones.
        b.style.setProperty('right', '8px', 'important');
        b.style.setProperty('left', 'auto', 'important');
        b.style.setProperty('max-width', 'calc(100% - 16px)', 'important');
        b.style.setProperty('box-sizing', 'border-box', 'important');
      }
      if (t) {
        var br = b.getBoundingClientRect(), tr = t.getBoundingClientRect();
        if (ov(br, tr)) {
          var op = b.offsetParent || root, pr = op.getBoundingClientRect();
          b.style.setProperty('top', ((tr.bottom - pr.top) + 8) + 'px', 'important');
          b.style.setProperty('bottom', 'auto', 'important');
        }
      }
    }
  }
  function init() {
    fix();
    window.addEventListener('resize', fix);
    [200, 800, 1600, 2600].forEach(function (t) { setTimeout(fix, t); });
    try {
      var mo = new MutationObserver(function () { clearTimeout(window.__bbf); window.__bbf = setTimeout(fix, 150); });
      mo.observe(document.documentElement, { childList: true, subtree: true });
      setTimeout(function () { mo.disconnect(); }, 9000);
    } catch (e) {}
  }
  if (document.readyState != 'loading') init(); else document.addEventListener('DOMContentLoaded', init);
})();
