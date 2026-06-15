// OC Flooring — Webflow registered inline script: "OCReviewsMover" (id: ocreviewsmover)
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
// Applied at: PAGE-level footer on /about-us, /our-work, /why-were-different.
//
// Purpose: on those pages the new trust-reviews section (loaded by octrustreviewsinjector9d)
// is present, but the OLD review widget — injected via classic page/site custom code, not a
// Webflow canvas element — also showed. This script:
//   1. Removes the old widget independently (covering Elfsight and other common review-widget
//      vendors), and
//   2. Drops a marker where the old widget was, then moves the new section into that spot.
//
// Decoupled design: removal does NOT depend on first finding the new section (the previous
// version gated removal on detection, so when detection failed the old widget was never
// removed). The vendor selector list is intentionally Elfsight-first since the site already
// had an Elfsight-removal script, indicating Elfsight is the widget in use.
(function () {
  var P = ['/about-us', '/our-work', '/why-were-different'];
  if (P.indexOf(location.pathname.replace(/\/+$/, '')) < 0) return;

  // Known review-widget vendor containers (old widget).
  var V = '[class*="elfsight-app"],.eapps-widget,[data-elfsight-app-lazy],[class*="trustindex"],.ti-widget,[class*="embedsocial"],[id*="EmbedSocial"],[class*="sk-ww"],[class*="tagembed"],[class*="trustmary"],[class*="shapo"],[id*="featurable"],[class*="featurable"],[class*="sociablekit"],iframe[src*="elfsight"],iframe[src*="trustindex"],iframe[src*="embedsocial"],iframe[src*="sociablekit"]';

  // The new trust-reviews section injected by the v9c bundle.
  function newSec() {
    var e = document.querySelector('[id="oc-trust-reviews"],[class*="oc-trust"],[id*="oc-trust"],[class*="trust-reviews"],[class*="oc-review"]');
    return e ? (e.closest('section') || e) : null;
  }

  function go() {
    var vs = document.querySelectorAll(V);
    if (vs.length) {
      var first = vs[0];
      var host = first.closest('.w-embed') || first;
      // Leave a marker at the old widget's position so the new section can take its place.
      if (!document.getElementById('oc-rev-slot') && host.parentNode) {
        var m = document.createElement('div'); m.id = 'oc-rev-slot';
        host.parentNode.insertBefore(m, host);
      }
      [].forEach.call(vs, function (a) { var t = a.closest('.w-embed') || a; if (t && t.parentNode) t.parentNode.removeChild(t); });
    }
    var slot = document.getElementById('oc-rev-slot');
    var ns = newSec();
    if (slot && ns && !ns.contains(slot) && slot.previousElementSibling !== ns && slot.parentNode) {
      slot.parentNode.insertBefore(ns, slot);
    }
  }

  function init() {
    go();
    window.addEventListener('load', go);
    [300, 800, 1500, 2500, 4000, 6000, 9000].forEach(function (t) { setTimeout(go, t); });
    try {
      var mo = new MutationObserver(function () { clearTimeout(window.__rm); window.__rm = setTimeout(go, 200); });
      mo.observe(document.documentElement, { childList: true, subtree: true });
      setTimeout(function () { mo.disconnect(); }, 12000);
    } catch (e) {}
  }
  if (document.readyState != 'loading') init(); else document.addEventListener('DOMContentLoaded', init);
})();
