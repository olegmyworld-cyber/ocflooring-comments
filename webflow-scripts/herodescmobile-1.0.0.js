// OC Flooring — Webflow registered inline script: "HeroDescMobile" (id: herodescmobile)
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
// Applied at: page footer of /city-of-bellevue/hardwood-floor-installation-in-bellevue-wa
// (page id 65f32565e111adbbb806d03e).
//
// What it does:
//   The hero of the Bellevue hardwood-installation page uses the shared hero component
//   (componentId 859df468-...). Its "Description" paragraph on this page is long
//   ("OC Flooring provides professional hardwood floor installation in Bellevue, WA...")
//   and rendered too large on phones. This script shrinks ONLY that paragraph on mobile.
//
// Implementation notes:
//   - The paragraph lives inside a Webflow component instance, so its class name is not
//     reliably knowable from the Data API. The element is instead located by a distinctive
//     substring of its visible text (same robust by-text approach as bonamobilefix), then
//     tagged with the `oc-hero-desc-sm` class.
//   - A single injected <style> with mobile media queries does the actual resizing, so the
//     responsive behavior is handled by CSS (no resize listener needed). 14px <=767px,
//     13px <=479px, with tightened line-height.
//   - init() re-runs on a few timers as a safety net in case the hero mounts late.
//   - Scoped to this one page via add_page_script, so other pages using the same hero
//     component are unaffected.
(function () {
  var KEY = 'provides professional hardwood floor installation';
  function T(e) { return (e.textContent || '').replace(/\s+/g, ' ').trim(); }

  // Smallest (innermost) element whose text contains KEY — the actual paragraph element.
  function leaf() {
    var a = document.body.querySelectorAll('p,div,span'), h = null, i;
    for (i = 0; i < a.length; i++) { if (T(a[i]).indexOf(KEY) >= 0) { if (!h || h.contains(a[i])) h = a[i]; } }
    return h;
  }

  function init() {
    var el = leaf();
    if (el) el.classList.add('oc-hero-desc-sm');
    if (!document.getElementById('oc-hero-desc-sm-css')) {
      var s = document.createElement('style');
      s.id = 'oc-hero-desc-sm-css';
      s.textContent = '@media screen and (max-width:767px){.oc-hero-desc-sm{font-size:14px!important;line-height:1.5!important}}@media screen and (max-width:479px){.oc-hero-desc-sm{font-size:13px!important}}';
      document.head.appendChild(s);
    }
  }

  if (document.readyState != 'loading') init(); else addEventListener('DOMContentLoaded', init);
  [400, 1200, 2500].forEach(function (t) { setTimeout(init, t); });
})();
