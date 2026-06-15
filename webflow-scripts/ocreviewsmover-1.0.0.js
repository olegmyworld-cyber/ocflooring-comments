// OC Flooring — Webflow registered inline script: "OCReviewsMover" (id: ocreviewsmover)
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
// Applied at: PAGE-level footer on /about-us, /our-work, /why-were-different.
//
// Purpose: on those pages the new trust-reviews section (loaded by octrustreviewsinjector9d)
// is present, but a Google Map embed (and/or an old review widget) also showed. This script:
//   1. Removes the map (Webflow .w-widget-map and Google Maps iframes) and common review-widget
//      vendors — but never anything inside the footer/nav, and
//   2. Drops a marker where that element was, then moves the new section into that spot.
//
// Decoupled design: removal does NOT depend on first finding the new section (an earlier
// version gated removal on detection, so when detection failed nothing was removed). The map
// selectors (.w-widget-map, iframe[src*="/maps"|"maps.google"]) cover the Google Map; the
// vendor list (Elfsight-first, since the site already had an Elfsight remover) covers old
// review widgets.
//
// NOTE: deployed copy is minified to fit Webflow's 2000-char inline-script limit.
(function () {
  var P = ['/about-us', '/our-work', '/why-were-different'];
  if (P.indexOf(location.pathname.replace(/\/+$/, '')) < 0) return;

  // Old elements to remove: Google Map + common review-widget vendors.
  var V = '[class*="elfsight-app"],.eapps-widget,[class*="trustindex"],.ti-widget,[class*="embedsocial"],[class*="sk-ww"],[class*="tagembed"],.w-widget-map,[class*="w-widget-map"],iframe[src*="elfsight"],iframe[src*="/maps"],iframe[src*="maps.google"]';

  function inFoot(e) { return !!e.closest('footer,[class*="footer"],nav,[class*="navbar"]'); }
  function host(e) { return e.closest('.w-widget-map') || e.closest('.w-embed') || e; }
  function targets() { var o = []; [].forEach.call(document.querySelectorAll(V), function (e) { if (!inFoot(e)) o.push(e); }); return o; }

  // The new trust-reviews section injected by the v9c bundle.
  function newSec() {
    var ss = document.querySelectorAll('[id="oc-trust-reviews"],[class*="oc-trust"],[id*="oc-trust"],[class*="trust-reviews"],[class*="oc-review"],[class*="reviews"],[id*="reviews"]');
    for (var i = 0; i < ss.length; i++) {
      var e = ss[i];
      if (inFoot(e)) continue;
      if (e.id === 'oc-rev-slot') continue;
      if (e.matches(V)) continue; // not one of the things we're removing
      return e.closest('section') || e;
    }
    return null;
  }

  function go() {
    var ts = targets();
    if (ts.length) {
      var h0 = host(ts[0]);
      // Mark the old element's position so the new section can take its place.
      if (!document.getElementById('oc-rev-slot') && h0.parentNode) {
        var m = document.createElement('div'); m.id = 'oc-rev-slot';
        h0.parentNode.insertBefore(m, h0);
      }
      ts.forEach(function (e) { var t = host(e); if (t && t.parentNode) t.parentNode.removeChild(t); });
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
