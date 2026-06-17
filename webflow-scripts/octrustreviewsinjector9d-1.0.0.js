// OC Flooring — Webflow registered inline script: "OCTrustReviewsInjector9d" (id: octrustreviewsinjector9d)
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
// Applied at: site footer.
//
// Purpose: loads the trust-reviews bundle (oc-trust-reviews-v9c-min.js) that renders the new
// review section and replaces the old (Elfsight) review widget.
//
// Change (2026-06-15): extended the path guard so the loader also runs on /about-us,
// /our-work and /why-were-different (previously home + hardwood-floor-refinishing-in-* only),
// so those pages get the same new review section in place of the old widget.
//
// Change (2026-06-17): appended a second, independent IIFE ("area spacing") that adds
// breathing room above the "Why Choose OC Flooring in <City>" section. On the home + city
// pages that section (injected by OCWhyTrustV5Injector) sat flush against the service-area
// links block (the 📍 city pins injected by OCAreaLinksInjector) with no gap. The fix was
// merged here rather than added as a new footer script because the site's script block was
// already at its 15-script-per-block limit. The spacing IIFE has its own guard (it acts only
// when a "Why Choose OC Flooring" heading exists), so it runs site-wide regardless of the
// loader's path guard above.
//
// Change (2026-06-17b): appended a third, independent IIFE ("install caption → h3"). On the
// hardwood floor installation pages (slug contains "hardwood-floor-installation") the
// before/after section's caption "Love your home. Love your floors. Love the life lived on
// them." was a small italic Text Block (class "Text Block 67"). It's now upgraded to a real
// <h3> styled to look good (the bare <h3> inherits the site's global heading font/color; we
// only set a responsive size, centering and margin). Merged here (not a new script, and not a
// page-level script — the Pages custom-code API returned 404 for these pages) to respect the
// 15-script-per-block site limit. Scoped strictly to installation pages via the path guard and
// to the exact caption text, so it never touches the "Just 2 days…" quote or the refinishing
// pages (which share the same "Text Block 67" class). Idempotent via the data-oc-h3 marker.
(function () {
  var p = location.pathname.replace(/\/+$/, '');
  var home = p === '' || p === '/index' || p === '/home';
  var city = /hardwood-floor-refinishing-in-/.test(p) && !/\/blog\//.test(p);
  var extra = ['/about-us', '/our-work', '/why-were-different'].indexOf(p) >= 0;
  if (!home && !city && !extra) return;
  if (document.getElementById('oc-trust-loader')) return;
  var s = document.createElement('script');
  s.id = 'oc-trust-loader';
  s.src = 'https://cdn.prod.website-files.com/6377e8e6a53936b48ef1cad0/6a2c93d15f4fbb2b0c31f679_oc-trust-reviews-v9c-min.js';
  s.defer = true;
  (document.body || document.head).appendChild(s);
})();

// Area spacing: gap above the "Why Choose OC Flooring in <City>" section.
(function () {
  function N(e) { return (e.textContent || '').replace(/\s+/g, ' ').trim().toUpperCase(); }
  var K = 'WHY CHOOSE OC FLOORING';

  // Outermost wrapper whose text still STARTS with the heading — i.e. the dedicated
  // Why-Choose block, with nothing (no pins) preceding the heading inside it.
  function block() {
    var hs = document.querySelectorAll('h1,h2,h3,h4,h5,h6'), h = null;
    for (var i = 0; i < hs.length; i++) { if (N(hs[i]).indexOf(K) === 0) { h = hs[i]; break; } }
    if (!h) return null;
    var t = h;
    while (t.parentElement && t.parentElement !== document.body && N(t.parentElement).indexOf(K) === 0) {
      t = t.parentElement;
    }
    return t;
  }

  function fix() {
    var b = block();
    if (!b) return;
    b.style.setProperty('margin-top', window.innerWidth <= 600 ? '48px' : '80px', 'important');
  }

  function init() {
    fix();
    addEventListener('resize', fix);
    [300, 900, 1600, 2600, 4000, 6000].forEach(function (t) { setTimeout(fix, t); });
  }
  if (document.readyState != 'loading') init(); else addEventListener('DOMContentLoaded', init);
})();

// Install caption → h3: upgrade the before/after caption to a styled heading.
(function () {
  if (!/hardwood-floor-installation/.test(location.pathname)) return;
  var T = 'love your home. love your floors. love the life lived on them.';

  function go() {
    // Deepest element whose own text is exactly the caption.
    var a = document.querySelectorAll('div,p'), el = null;
    for (var i = 0; i < a.length; i++) {
      var t = (a[i].textContent || '').replace(/\s+/g, ' ').trim().toLowerCase();
      if (t === T && (!el || el.contains(a[i]))) el = a[i];
    }
    if (!el || el.getAttribute('data-oc-h3')) return;

    // Replace with a real <h3>. We intentionally drop the original class ("Text Block 67",
    // which forces italic Droid Sans 400) so the bare <h3> inherits the site's heading
    // font/color; we only set a responsive size, line-height, margin and centering.
    var h = document.createElement('h3');
    h.setAttribute('data-oc-h3', '1');
    h.textContent = el.textContent;
    h.style.cssText = 'font-size:clamp(22px,4.6vw,34px);line-height:1.25;margin:.3em 0 .5em;text-align:center';
    el.parentNode.replaceChild(h, el);
  }

  // Static section (not async-injected) — a few timers cover late style/layout passes.
  [400, 1200, 2500].forEach(function (t) { setTimeout(go, t); });
})();
