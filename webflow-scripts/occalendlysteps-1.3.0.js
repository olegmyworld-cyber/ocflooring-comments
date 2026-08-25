// OC Flooring — Webflow registered inline script: "OCCalendlySteps" (id: occalendlysteps)
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
// Applied at: page footers of "Home" (/), "Floor Refinishing"
// (/services/floor-refinishing) and all 29 hardwood-floor-refinishing-in-*-wa
// city pages (published under city folders, e.g.
// /seattle/hardwood-floor-refinishing-in-seattle-wa).
//
// What it does:
//   Fills the empty space under step 5 ("Final Walkthrough") of the "Our 5-Step
//   Hardwood Refinishing Process in {City}" column with an accented booking card
//   (red top bar + "★ FREE — BOOK ONLINE" badge + navy serif heading) holding the
//   Calendly inline calendar used on the Contact Us page
//   (calendly.com/nwwillsflooring/free-in-home-estimate-online-today-clone-1).
//
// v1.3.0 — ROOT-CAUSE FIX for "nothing appears on any page" after v1.2.0:
//   v1.2.0 built the card via innerHTML with literal HTML tags ('<span …>',
//   '<h3 …>' …) inside the inline script source. Every other registered inline
//   script on this site — all proven to render — builds DOM exclusively with
//   createElement and loads bigger markup from external hosted files; none
//   contains a literal HTML tag, and v1.1.0 (createElement-only) worked while
//   v1.2.0 (innerHTML) showed nothing anywhere. Conclusion: Webflow's inline
//   custom-code pipeline does not tolerate tag-like sequences inside registered
//   inline scripts. v1.3.0 therefore builds the identical accent card with
//   createElement only — the deployed minified source contains not a single
//   '<' character (comparisons are written as `len>i`). Also new:
//     - visibility-aware anchoring: among multiple `.ots-steps-col` matches or
//       "FINAL WALKTHROUGH" text nodes, only elements with live client rects
//       are considered, so a hidden template copy can't swallow the card.
//     - Calendly widget.js is loaded once on insert (dynamic script tags are
//       async by default).
//   Placement logic otherwise as v1.1.0: `.ots-steps-col` fast path, else find
//   the rendered "FINAL WALKTHROUGH" text (skipping SCRIPT/STYLE) and insert
//   after the last step of the column whose text matches
//   /5-STEP|REFINISHING PROCESS/. Polls every 500ms for up to 60s.
//
// Verified in headless Chromium against six mock structures (exact class,
// nested list, flat rows, late-injected, hidden template + visible section,
// and true inline-<script> embedding): one insert each, correct visible
// position, zero page errors.
//
// NOTE: This file is the readable source of record. The deployed copy is
// minified to fit Webflow's 2000-char inline-script limit (1,983 chars).
(function () {
  var CAL_URL = 'https://calendly.com/nwwillsflooring/free-in-home-estimate-online-today-clone-1?hide_gdpr_banner=1';

  function T(e) { return (e.textContent || '').replace(/\s+/g, ' ').toUpperCase(); }
  function visible(e) { return e.getClientRects().length > 0; }

  // createElement helper: tag, cssText, textContent. No innerHTML anywhere —
  // see the v1.3.0 note above.
  function E(t, css, text) {
    var e = document.createElement(t);
    if (css) e.style.cssText = css;
    if (text) e.textContent = text;
    return e;
  }

  // Build the accent card and insert it into parent `p` before node `a`
  // (null = append at the end).
  function insert(p, a) {
    var box = E('div',
      'margin-top:32px;width:100%;background:#fff;border-top:4px solid #b3202c;' +
      'border-radius:12px;box-shadow:0 12px 32px #16294c29;padding:22px 20px 6px;' +
      'box-sizing:border-box');
    box.className = 'oc-cal-embed';

    var hd = E('h3', 'margin:10px 0 4px;color:#16294c;font-size:1.6rem',
      'Book Your Free In-Home Estimate');
    // Match the serif face of the section's own headings.
    var f = p.querySelector('h2,h3,h4');
    if (f) hd.style.fontFamily = getComputedStyle(f).fontFamily;

    var cal = E('div', 'height:700px;width:100%');
    cal.className = 'calendly-inline-widget';
    cal.dataset.url = CAL_URL;

    box.appendChild(E('span',
      'display:inline-block;background:#b3202c;color:#fff;font-weight:700;' +
      'font-size:12px;padding:5px 12px;border-radius:99px',
      '★ FREE — BOOK ONLINE'));
    box.appendChild(hd);
    box.appendChild(E('p', 'margin:0;color:#3f4c63', 'Pick a day and time that works for you.'));
    box.appendChild(cal);
    p.insertBefore(box, a);

    var s = E('script');
    s.src = 'https://assets.calendly.com/assets/external/widget.js';
    document.body.appendChild(s);
    return true;
  }

  function inject() {
    if (document.querySelector('.oc-cal-embed')) return true; // already installed

    // Fast path: a VISIBLE steps column with the known class.
    var cols = document.querySelectorAll('.ots-steps-col'), i;
    for (i = 0; cols.length > i; i++) if (visible(cols[i])) return insert(cols[i], null);

    // Fallback: smallest VISIBLE rendered element containing "FINAL WALKTHROUGH"
    // (skipping script/style so injector template strings don't match).
    var all = document.body.querySelectorAll('*'), leaf = null, e;
    for (i = 0; all.length > i; i++) {
      e = all[i];
      if (/^(SCRIPT|STYLE)$/.test(e.tagName)) continue;
      if (T(e).indexOf('FINAL WALKTHROUGH') >= 0 && visible(e) && (!leaf || leaf.contains(e))) leaf = e;
    }
    if (!leaf) return false; // section not on the page (yet) — keep polling

    // Climb until the PARENT also holds the section heading; the node we stop
    // on is then the last-step child of the steps column — insert after it.
    var n = leaf;
    while (n.parentElement && n.parentElement != document.body &&
           !/5-STEP|REFINISHING PROCESS/.test(T(n.parentElement))) n = n.parentElement;
    return n.parentElement && n.parentElement != document.body
      ? insert(n.parentElement, n.nextSibling) : false;
  }

  // The section is injected async by other footer scripts; poll for up to
  // 60s (120 × 500ms) until it shows up.
  var tries = 0;
  var t = setInterval(function () {
    if (inject() || ++tries > 120) clearInterval(t);
  }, 500);
})();
