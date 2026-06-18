// OC Flooring — Webflow registered inline script: "OC Mobile BeforeAfter Fix" (id: oc_mobile_beforeafter_fix)
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
// Applied at: site footer.
//
// Part 1 (original): injects a <style> block — on phones it lets the benefit/before-after
// images fill the column, and it caps the h2 / hero heading font sizes site-wide.
//
// Part 2 (2026-06-17): the before/after section caption "Love your home. Love your floors.
// Love the life lived on them." is restyled to match the hero subtitle ("Crafted Just for Your
// Home — Built to Last") and moved to sit as a clean heading directly ABOVE the two photos, on
// the hardwood floor installation pages (slug contains "hardwood-floor-installation").
//
// This lives here (rather than as its own footer script) because the site's script block is at
// its 15-per-block limit, and this script already owns the before/after section. An earlier
// attempt overlaid the caption *on top of* the photos; with the photos stacked on mobile it
// crossed the seam and looked bad, so it was changed to the heading-above layout.
//
// Implementation notes (Part 2):
//   - Scoped to installation pages via the path guard, and to the exact caption text.
//   - The before/after photo pair is located as the lowest common ancestor of the visible
//     "Before" and "After" badges; the caption is inserted just before that container.
//   - Font family / weight / color are copied at runtime from the hero subtitle so it matches
//     the site's serif heading; we only set size, line-height, centering and margin. The
//     original italic "Text Block 67" styling is overridden.
//   - Idempotent (re-running re-applies the same styles and leaves the caption in place).
//
// NOTE: readable source of record. The deployed copy is minified to fit Webflow's 2000-char
// inline-script limit.

// Part 1 — mobile image + heading-size CSS.
(function () {
  var s = document.createElement('style');
  s.setAttribute('data-oc', 'mobile-beforeafter');
  s.textContent = '@media screen and (max-width:767px){.benefit-item_image{max-width:100%!important}.benefit-family-image{width:100%!important;max-width:100%!important;height:auto!important}}html body .h2-heading{font-size:clamp(26px,5.4vw,47px)!important}html body .heading-hero,html body .h1-hero.is-services.is-flex,html body .heading-hero-custom.is-thanks,html body .blog-name{font-size:clamp(30px,6.2vw,57px)!important}';
  document.head.appendChild(s);
})();

// Part 2 — before/after caption → serif heading above the photos (installation pages).
(function () {
  if (!/hardwood-floor-installation/.test(location.pathname)) return;
  var Q = 'div,span,p,h1,h2,h3';
  var T = 'love your home. love your floors. love the life lived on them.';

  function nm(s) { return (s || '').replace(/\s+/g, ' ').trim().toLowerCase(); }

  // Deepest element whose text equals `w` (or, when x is set, starts with `w`).
  function ex(w, x) {
    var a = document.querySelectorAll(Q), r = null;
    for (var i = 0; i < a.length; i++) {
      var v = nm(a[i].textContent);
      if ((x ? v.indexOf(w) === 0 : v === w) && (!r || r.contains(a[i]))) r = a[i];
    }
    return r;
  }

  function go() {
    var c = ex(T), b = ex('before'), f = ex('after');
    if (!c || !b || !f) return;

    // Lowest common ancestor of the Before/After badges = the photo-pair container.
    var st = [], n = b;
    while (n) { st.push(n); n = n.parentElement; }
    n = f;
    var anc = null;
    while (n) { if (st.indexOf(n) >= 0) { anc = n; break; } n = n.parentElement; }
    if (!anc) return;

    // Match the hero subtitle's serif look.
    var sub = ex('crafted just for your home', 1);
    if (sub) {
      var cs = getComputedStyle(sub);
      c.style.fontFamily = cs.fontFamily;
      c.style.color = cs.color;
      c.style.fontWeight = cs.fontWeight;
    }
    c.style.removeProperty('display');
    c.style.setProperty('font-style', 'normal', 'important');
    c.style.setProperty('font-size', 'clamp(20px,3vw,34px)', 'important');
    c.style.setProperty('line-height', '1.3', 'important');
    c.style.setProperty('text-align', 'center', 'important');
    c.style.setProperty('margin', '0 0 18px', 'important');

    // Place the caption directly above the photo pair.
    if (anc.parentNode && c.nextElementSibling !== anc) anc.parentNode.insertBefore(c, anc);
  }

  [500, 1500, 3000].forEach(function (t) { setTimeout(go, t); });
})();
