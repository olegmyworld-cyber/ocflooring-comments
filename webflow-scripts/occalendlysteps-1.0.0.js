// OC Flooring — Webflow registered inline script: "OCCalendlySteps" (id: occalendlysteps)
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
// Applied at: page footer of "Floor Refinishing" (page 65f32565e111adbbb806cf36,
// published at /services/floor-refinishing).
//
// What it does:
//   Fills the empty space under step 5 ("Final Walkthrough") of the "Our 5-Step
//   Hardwood Refinishing Process in Bellevue" column with the same Calendly
//   inline booking calendar used on the Contact Us page
//   (calendly.com/nwwillsflooring/free-in-home-estimate-online-today-clone-1).
//
// Implementation notes:
//   - The 5-step process lives in the right column (.ots-steps-col) of the
//     runtime-injected Bona tone/steps section (#oc-tone-steps), so this script
//     polls until that column exists, then appends a heading + the Calendly
//     inline widget div and loads Calendly's widget.js once.
//   - Idempotent: bails if .oc-cal-embed is already present; reuses an already
//     loaded Calendly widget.js via Calendly.initInlineWidgets().
//   - The embed URL, sizing (min-width:320px;height:700px) and hide_gdpr_banner
//     flag are copied verbatim from the Contact page HTML embed.
//
// NOTE: This file is the readable source of record. The deployed copy is minified
// to fit Webflow's 2000-char inline-script limit (see the registered script on
// the site).
(function () {
  var CAL_URL = 'https://calendly.com/nwwillsflooring/free-in-home-estimate-online-today-clone-1?hide_gdpr_banner=1';

  function inject() {
    var root = document.getElementById('oc-tone-steps');
    var col = root && root.querySelector('.ots-steps-col');
    if (!col) return false;              // section not injected yet — keep polling
    if (col.querySelector('.oc-cal-embed')) return true; // already installed

    var box = document.createElement('div');
    box.className = 'oc-cal-embed';
    box.style.cssText = 'margin-top:28px;width:100%';

    var hd = document.createElement('h3');
    hd.textContent = 'Book Your Free In-Home Estimate';
    hd.style.cssText = 'margin:0 0 4px;color:#16294c;font-size:1.5rem;line-height:1.2';
    // Match the serif face of the section's own headings (minified bundle, so
    // the font is read off a live heading instead of hardcoding a family).
    var src = col.querySelector('h2,h3,h4');
    if (src) try { hd.style.fontFamily = getComputedStyle(src).fontFamily; } catch (e) {}

    var w = document.createElement('div');
    w.className = 'calendly-inline-widget';
    w.setAttribute('data-url', CAL_URL);
    w.style.cssText = 'min-width:320px;height:700px;width:100%';

    box.appendChild(hd);
    box.appendChild(w);
    col.appendChild(box);

    // Load Calendly's embed bootstrap exactly once; if it is already on the
    // page, ask it to (re)scan for the widget div we just added.
    if (!document.querySelector('script[src*="assets.calendly.com/assets/external/widget.js"]')) {
      var s = document.createElement('script');
      s.src = 'https://assets.calendly.com/assets/external/widget.js';
      s.async = true;
      document.body.appendChild(s);
    } else if (window.Calendly && Calendly.initInlineWidgets) {
      Calendly.initInlineWidgets();
    }
    return true;
  }

  function init() {
    if (inject()) return;
    // The #oc-tone-steps section is injected async by another footer script;
    // poll for up to 15s (60 × 250ms) until it shows up.
    var tries = 0;
    var t = setInterval(function () {
      if (inject() || ++tries > 60) clearInterval(t);
    }, 250);
  }
  if (document.readyState != 'loading') init(); else addEventListener('DOMContentLoaded', init);
})();
