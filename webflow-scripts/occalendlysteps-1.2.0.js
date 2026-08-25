// OC Flooring — Webflow registered inline script: "OCCalendlySteps" (id: occalendlysteps)
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
// Applied at: page footers of "Home" (page 65f32565e111adbbb806ce6e, published at /)
// and "Floor Refinishing" (page 65f32565e111adbbb806cf36, /services/floor-refinishing).
//
// What it does:
//   Fills the empty space under step 5 ("Final Walkthrough") of the "Our 5-Step
//   Hardwood Refinishing Process in Bellevue" column with the Calendly inline
//   booking calendar used on the Contact Us page
//   (calendly.com/nwwillsflooring/free-in-home-estimate-online-today-clone-1).
//
// v1.2.0 — accented booking card (user: "make more accent on it"). The calendar
//   now sits in a white card with a red top bar, a red "★ FREE — BOOK ONLINE"
//   pill badge, a larger navy serif heading and a short sub-line, matching the
//   site's navy/red/cream palette. To stay under the 2000-char inline limit the
//   card is built via innerHTML, and the "Calendly already loaded" re-scan
//   branch was dropped: the widget bootstrap is simply appended on insert
//   (safe — ins() runs exactly once per page, guarded by .oc-cal-embed, and
//   neither page loads Calendly otherwise).
// v1.1.0 — markup-agnostic placement (`.ots-steps-col` fast path, else find the
//   rendered "FINAL WALKTHROUGH" text and insert after the last step of the
//   column holding the "5-STEP"/"REFINISHING PROCESS" heading); 60s polling.
//
// Verified in headless Chromium against four mock section structures (exact
// class, nested list, flat rows, late-injected): one insert each, correct
// position, one widget.js tag.
//
// NOTE: This file is the readable source of record. The deployed copy is minified
// to fit Webflow's 2000-char inline-script limit (see the registered script on
// the site).
(function () {
  var CAL_URL = 'https://calendly.com/nwwillsflooring/free-in-home-estimate-online-today-clone-1?hide_gdpr_banner=1';

  function T(e) { return (e.textContent || '').replace(/\s+/g, ' ').toUpperCase(); }

  // Build the accent card (badge + heading + sub-line + calendar) and insert it
  // into parent `p` before node `a` (null = append at the end).
  function insert(p, a) {
    var box = document.createElement('div');
    box.className = 'oc-cal-embed';
    box.style.cssText =
      'margin-top:32px;width:100%;background:#fff;border-top:4px solid #b3202c;' +
      'border-radius:12px;box-shadow:0 12px 32px #16294c29;padding:22px 20px 6px;' +
      'box-sizing:border-box';
    box.innerHTML =
      '<span style="display:inline-block;background:#b3202c;color:#fff;font-weight:700;' +
      'font-size:12px;padding:5px 12px;border-radius:99px">★ FREE — BOOK ONLINE</span>' +
      '<h3 style="margin:10px 0 4px;color:#16294c;font-size:1.6rem">Book Your Free In-Home Estimate</h3>' +
      '<p style="margin:0;color:#3f4c63;font-size:15px">Pick a day and time that works for you.</p>' +
      '<div class="calendly-inline-widget" data-url="' + CAL_URL + '" style="height:700px;width:100%"></div>';

    // Match the serif face of the section's own headings.
    var f = p.querySelector('h2,h3,h4');
    if (f) try { box.querySelector('h3').style.fontFamily = getComputedStyle(f).fontFamily; } catch (e) {}

    p.insertBefore(box, a);

    var s = document.createElement('script');
    s.src = 'https://assets.calendly.com/assets/external/widget.js';
    s.async = true;
    document.body.appendChild(s);
    return true;
  }

  function inject() {
    if (document.querySelector('.oc-cal-embed')) return true; // already installed

    // Exact match on the known steps-column class, when present.
    var col = document.querySelector('.ots-steps-col');
    if (col) return insert(col, null);

    // Fallback: smallest rendered element containing "FINAL WALKTHROUGH"
    // (skipping script/style so injector template strings don't match).
    var all = document.body.querySelectorAll('*'), leaf = null, i, e;
    for (i = 0; i < all.length; i++) {
      e = all[i];
      if (/^(SCRIPT|STYLE|NOSCRIPT)$/.test(e.tagName)) continue;
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

  // The section is injected async by other footer scripts; poll for up to
  // 60s (120 × 500ms) until it shows up.
  var tries = 0;
  var t = setInterval(function () {
    if (inject() || ++tries > 120) clearInterval(t);
  }, 500);
})();
