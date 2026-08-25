// OC Flooring — Webflow registered inline script: "OCCalendlySteps" (id: occalendlysteps)
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
// Applied at: page footers of "Home" (/), "Floor Refinishing"
// (/services/floor-refinishing) and all 29 hardwood-floor-refinishing-in-*-wa
// city pages (published under city folders, e.g.
// /seattle/hardwood-floor-refinishing-in-seattle-wa).
//
// What it does:
//   Places an accented booking card (red top bar + "★ FREE — BOOK ONLINE" badge
//   + navy serif heading + the Contact Us page's Calendly inline calendar)
//   directly under step 5 ("Final Walkthrough") of the "Our 5-Step Hardwood
//   Refinishing Process in {City}" column.
//
// v1.4.0 — PLACEMENT FIX. v1.3.0 rendered (root cause of the earlier blank
//   pages was v1.2.0's literal-HTML-in-strings, which Webflow's inline
//   custom-code pipeline rejects — v1.3.0+ is createElement-only with zero '<'
//   characters in the deployed source), but the card landed BELOW the whole
//   two-column section: on the live pages the section heading is a sibling of
//   the two-column wrap, so climbing from "Final Walkthrough" to the first
//   ancestor whose parent holds the heading overshot to section level.
//   v1.4.0 anchors to the steps list itself instead: climb from the visible
//   "FINAL WALKTHROUGH" leaf until the PARENT also contains another step's
//   title ("DUSTLESS SANDING", step 2) — that parent is the innermost
//   container holding all five steps, and the node we stop on is the step-5
//   row. The card is inserted immediately after it, i.e. exactly under
//   "5 · Final Walkthrough" inside the right column. If no ancestor matches
//   (unexpected variant), it falls back to the previous heading climb
//   (/5-STEP|REFINISHING PROCESS/) so the card still appears near the section.
//   The `.ots-steps-col` fast path was removed — the live markup no longer
//   exposes it in a usefully-scoped way.
//
// Verified in headless Chromium against six mock structures, including one
// replicating the live layout (heading outside the column wrap; left column
// containing a "Dustless SANDING SYSTEM" stat tile — harmless, since only
// ANCESTORS of step 5 are considered): one insert each, correct position
// (inside the steps list, right after step 5), zero page errors.
//
// NOTE: This file is the readable source of record. The deployed copy is
// minified to fit Webflow's 2000-char inline-script limit (1,950 chars).
(function () {
  var CAL_URL = 'https://calendly.com/nwwillsflooring/free-in-home-estimate-online-today-clone-1?hide_gdpr_banner=1';

  function T(e) { return (e.textContent || '').replace(/\s+/g, ' ').toUpperCase(); }
  function visible(e) { return e.getClientRects().length > 0; }

  // createElement helper: tag, cssText, textContent. No innerHTML anywhere.
  function E(t, css, text) {
    var e = document.createElement(t);
    if (css) e.style.cssText = css;
    if (text) e.textContent = text;
    return e;
  }

  // Build the accent card and insert it into parent `p` before node `a`.
  function insert(p, a) {
    var box = E('div',
      'margin-top:28px;width:100%;background:#fff;border-top:4px solid #b3202c;' +
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

  // Climb from `l` until the PARENT's text matches `rx`; returns the node whose
  // parent matched (i.e. the direct child of the matching container), or null.
  function up(l, rx) {
    var n = l;
    while (n.parentElement && n.parentElement != document.body && !rx.test(T(n.parentElement)))
      n = n.parentElement;
    return n.parentElement && n.parentElement != document.body ? n : null;
  }

  function inject() {
    if (document.querySelector('.oc-cal-embed')) return true; // already installed

    // Smallest VISIBLE rendered element containing "FINAL WALKTHROUGH"
    // (skipping script/style so injector template strings don't match).
    var all = document.body.querySelectorAll('*'), leaf = null, i, e;
    for (i = 0; all.length > i; i++) {
      e = all[i];
      if (/^(SCRIPT|STYLE)$/.test(e.tagName)) continue;
      if (T(e).indexOf('FINAL WALKTHROUGH') >= 0 && visible(e) && (!leaf || leaf.contains(e))) leaf = e;
    }
    if (!leaf) return false; // section not on the page (yet) — keep polling

    // Primary: stop at the steps list (the innermost ancestor that also holds
    // step 2's title) → n is the step-5 row; insert right after it.
    // Fallback: the old heading climb, so the card still shows on variants.
    var n = up(leaf, /DUSTLESS SANDING/) || up(leaf, /5-STEP|REFINISHING PROCESS/);
    return n ? insert(n.parentElement, n.nextSibling) : false;
  }

  // The section is injected async by other footer scripts; poll for up to
  // 60s (120 × 500ms) until it shows up.
  var tries = 0;
  var t = setInterval(function () {
    if (inject() || ++tries > 120) clearInterval(t);
  }, 500);
})();
