// OC Flooring — Webflow registered inline script: "OCCalendlySteps" (id: occalendlysteps)
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
// Applied at: page footers of "Home" (page 65f32565e111adbbb806ce6e, published at /)
// and "Floor Refinishing" (page 65f32565e111adbbb806cf36, /services/floor-refinishing).
//
// What it does:
//   Fills the empty space under step 5 ("Final Walkthrough") of the "Our 5-Step
//   Hardwood Refinishing Process in Bellevue" column with the same Calendly
//   inline booking calendar used on the Contact Us page
//   (calendly.com/nwwillsflooring/free-in-home-estimate-online-today-clone-1).
//
// v1.1.0 — markup-agnostic placement. v1.0.0 anchored on the injected section's
//   `#oc-tone-steps .ots-steps-col` markup, which no longer matches on the Home
//   page (the section bundles have been rewritten several times, and the live
//   DOM can't be inspected through the Data API). This version:
//     1. Still tries `.ots-steps-col` first (cheap, exact).
//     2. Otherwise finds the smallest visible element containing the text
//        "FINAL WALKTHROUGH" (skipping SCRIPT/STYLE/NOSCRIPT so the injector
//        bundles' own template strings don't match), then climbs to the child
//        of the container whose text includes "5-STEP" / "REFINISHING PROCESS"
//        (the steps column with its heading) and inserts the calendar right
//        after that child — i.e. directly under step 5, whatever the classes.
//   Also polls for 60s (was 15s) in case the section is built late.
//
// Idempotent (bails if .oc-cal-embed exists); loads Calendly widget.js once and
// re-scans via Calendly.initInlineWidgets() if it is already present. Embed URL,
// sizing (min-width:320px;height:700px) and hide_gdpr_banner flag are copied
// verbatim from the Contact page HTML embed.
//
// NOTE: This file is the readable source of record. The deployed copy is minified
// to fit Webflow's 2000-char inline-script limit (see the registered script on
// the site).
(function () {
  var CAL_URL = 'https://calendly.com/nwwillsflooring/free-in-home-estimate-online-today-clone-1?hide_gdpr_banner=1';

  function T(e) { return (e.textContent || '').replace(/\s+/g, ' ').toUpperCase(); }

  // Build the heading + calendar block and insert it into parent `p` before
  // node `a` (null = append at the end). Loads Calendly's bootstrap once.
  function insert(p, a) {
    var box = document.createElement('div');
    box.className = 'oc-cal-embed';
    box.style.cssText = 'margin-top:28px;width:100%';

    var hd = document.createElement('h3');
    hd.textContent = 'Book Your Free In-Home Estimate';
    hd.style.cssText = 'margin:0 0 4px;color:#16294c;font-size:1.5rem;line-height:1.2';
    // Match the serif face of the section's own headings.
    var f = p.querySelector('h2,h3,h4');
    if (f) try { hd.style.fontFamily = getComputedStyle(f).fontFamily; } catch (e) {}

    var w = document.createElement('div');
    w.className = 'calendly-inline-widget';
    w.setAttribute('data-url', CAL_URL);
    w.style.cssText = 'min-width:320px;height:700px;width:100%';

    box.appendChild(hd);
    box.appendChild(w);
    p.insertBefore(box, a);

    if (!document.querySelector('script[src*="assets.calendly.com"]')) {
      var s = document.createElement('script');
      s.src = 'https://assets.calendly.com/assets/external/widget.js';
      s.async = true;
      document.body.appendChild(s);
    } else if (window.Calendly && Calendly.initInlineWidgets) {
      Calendly.initInlineWidgets();
    }
    return true;
  }

  function inject() {
    if (document.querySelector('.oc-cal-embed')) return true; // already installed

    // Exact match on the known steps-column class, when present.
    var col = document.querySelector('.ots-steps-col');
    if (col) return insert(col, null);

    // Fallback: smallest rendered element containing "FINAL WALKTHROUGH".
    var all = document.body.querySelectorAll('*'), leaf = null, i, e;
    for (i = 0; i < all.length; i++) {
      e = all[i];
      if (e.tagName == 'SCRIPT' || e.tagName == 'STYLE' || e.tagName == 'NOSCRIPT') continue;
      if (T(e).indexOf('FINAL WALKTHROUGH') >= 0 && (!leaf || leaf.contains(e))) leaf = e;
    }
    if (!leaf) return false; // section not on the page (yet) — keep polling

    // Climb until the PARENT also holds the section heading; the node we stop
    // on is then the last-step child of the steps column — insert after it.
    var n = leaf, P;
    while (n.parentElement && n.parentElement != document.body) {
      P = T(n.parentElement);
      if (P.indexOf('5-STEP') >= 0 || P.indexOf('REFINISHING PROCESS') >= 0) break;
      n = n.parentElement;
    }
    if (!n.parentElement || n.parentElement == document.body) return false;
    return insert(n.parentElement, n.nextSibling);
  }

  function init() {
    if (inject()) return;
    // The section is injected async by other footer scripts; poll for up to
    // 60s (120 × 500ms) until it shows up.
    var tries = 0;
    var t = setInterval(function () {
      if (inject() || ++tries > 120) clearInterval(t);
    }, 500);
  }
  if (document.readyState != 'loading') init(); else addEventListener('DOMContentLoaded', init);
})();
