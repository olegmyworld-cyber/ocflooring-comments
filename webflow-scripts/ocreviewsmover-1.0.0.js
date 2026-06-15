// OC Flooring — Webflow registered inline script: "OCReviewsMover" (id: ocreviewsmover)
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
// Applied at: PAGE-level footer on /about-us, /our-work, /why-were-different
// (the site footer block was already at the 15-script limit).
//
// Purpose: on those three pages the new trust-reviews section (loaded by
// octrustreviewsinjector9d) appeared, but the OLD review widget (Elfsight) was still present
// and the new section landed in a default spot. This script removes the old widget and moves
// the new section into the exact position the old widget occupied.
//
// Detection is class-name-agnostic where possible: the old widget is found via Elfsight
// markers; the new section via a prioritized selector list plus a "looks like reviews"
// content check, excluding the "why trust" section and anything containing Elfsight.
(function () {
  var P = ['/about-us', '/our-work', '/why-were-different'];
  if (P.indexOf(location.pathname.replace(/\/+$/, '')) < 0) return;

  function rev(e) { return /google|verified|★|review/i.test(e.textContent || ''); }
  function cls(e) { return typeof e.className == 'string' ? e.className : ''; }

  // The new review section injected by the trust-reviews bundle.
  function newSec() {
    var sel = ['#oc-trust-reviews', '[class*="oc-trust-reviews"]', '[id*="trust-reviews"]', '[class*="trust-reviews"]', '[id*="oc-reviews"]', '[class*="oc-reviews"]', '[class*="oc-trust"]'];
    for (var i = 0; i < sel.length; i++) {
      var ls = document.querySelectorAll(sel[i]);
      for (var j = 0; j < ls.length; j++) {
        var e = ls[j];
        if (e.querySelector('[class*="elfsight-app"],.eapps-widget')) continue; // not the old one
        if (/why/i.test(cls(e))) continue;                                       // not the "why trust" block
        if (rev(e)) return e;
      }
    }
    return null;
  }

  // The old Elfsight widget's containing section.
  function oldW() {
    var e = document.querySelector('[class*="elfsight-app"],.eapps-widget');
    if (e) return e.closest('.section_reviews') || e.closest('.w-embed') || e;
    return null;
  }

  function go() {
    var ns = newSec(); if (!ns) return;
    var ow = oldW(); if (!ow || ow === ns || ow.contains(ns) || ns.contains(ow)) return;
    ow.parentNode.insertBefore(ns, ow); // drop the new section where the old one was
    ow.parentNode.removeChild(ow);      // remove the old widget
  }

  function init() {
    go();
    window.addEventListener('load', go);
    [300, 800, 1500, 2500, 4000, 6000, 8000].forEach(function (t) { setTimeout(go, t); });
    try {
      var mo = new MutationObserver(function () { clearTimeout(window.__rm); window.__rm = setTimeout(go, 200); });
      mo.observe(document.documentElement, { childList: true, subtree: true });
      setTimeout(function () { mo.disconnect(); }, 11000);
    } catch (e) {}
  }
  if (document.readyState != 'loading') init(); else document.addEventListener('DOMContentLoaded', init);
})();
