// OC Flooring — Webflow registered inline script: "OCHeaderInit" (id: ocheaderinit) v1.1.0
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
// Applied at: site HEADER (runs synchronously in <head>, so injected CSS applies
// before first paint — no flash of unstyled/cropped content).
//
// What it does (v1.0.0 behavior, unchanged):
//   1. Mouseflow init (window._mfq) and loader.
//   2. Injects #oc-hide-fin: hides the /financing nav link.
//   3. Injects #oc-hero-title-size: responsive hero heading/subheading font sizes.
//
// Added in v1.1.0 — #oc-hero-ba (hero before/after composite, site-wide):
//   The 650x550 before/after composite (asset 69ec0333eda923fe81bd51c9, BEFORE/
//   AFTER pills and caption baked into the image) is the hero image on
//   /services/flooring-repair and the city floor-repair pages. The hero card box
//   (.hero-cover-img: width calc(100% - 48px), height calc(100% - 80px),
//   object-fit cover) is taller than the image's 1.18 aspect ratio on desktop, so
//   cover cropped the photos' sides and clipped the pills. The injected CSS is
//   keyed to that one asset id (matches the CDN filename in src), so no other
//   page's hero is affected:
//     - height:auto — the card follows the image's own aspect ratio at the same
//       width as before, vertically centered by the class's align-self:center;
//       the whole composite renders uncropped.
//     - @media (min-width:1930px) — where natural height would outgrow the
//       section (overflow:hidden would clip it), size by height instead and
//       center the card in its grid column.
//   Same treatment as the page-scoped rule in
//   ../page-embeds/flooring-repair-ocrep-tweaks.html, which stays in place
//   (identical values, no conflict).
//
// Merged into this script because the site is at its 15-applied-scripts limit
// (same convention as the BonaMobileFix merge). A standalone registration
// "ocheroba" 1.0.0 was created first and could not be applied or deleted
// (API 400) — it is unapplied and inert; ignore or reuse it.
//
// NOTE: This file is the readable source of record. The deployed copy is the
// minified registered script (1958 chars, limit 2000).
window._mfq = window._mfq || [];
(function () {
  // v1.0.0: hide the financing nav link.
  var s = document.createElement('style');
  s.id = 'oc-hide-fin';
  s.textContent = '.nav-link[href="/financing"],.nav-link[href="/financing/"]{display:none!important}';
  (document.head || document.documentElement).appendChild(s);

  // v1.0.0: responsive hero heading/subheading sizes.
  var h = document.createElement('style');
  h.id = 'oc-hero-title-size';
  h.textContent =
    'html body .heading-hero.heading-hero,html body .heading-hero-custom.heading-hero-custom{font-size:46px!important;line-height:1.12!important}' +
    '@media screen and (max-width:991px){html body .heading-hero.heading-hero,html body .heading-hero-custom.heading-hero-custom{font-size:44px!important}}' +
    '@media screen and (max-width:767px){html body .heading-hero.heading-hero,html body .heading-hero-custom.heading-hero-custom{font-size:41px!important;line-height:1.14!important}}' +
    '@media screen and (max-width:479px){html body .heading-hero.heading-hero,html body .heading-hero-custom.heading-hero-custom{font-size:38px!important;line-height:1.12!important;letter-spacing:-.01em!important}}' +
    '@media screen and (max-width:991px){html body .subheading-hero.subheading-hero{font-size:34px!important}}' +
    '@media screen and (max-width:767px){html body .subheading-hero.subheading-hero{font-size:32px!important}}' +
    '@media screen and (max-width:479px){html body .subheading-hero.subheading-hero{font-size:30px!important;line-height:1.2!important}}';
  (document.head || document.documentElement).appendChild(h);

  // v1.1.0: before/after composite hero — render uncropped at the image's own
  // aspect ratio, keyed to the one composite asset.
  var C = 'img.hero-cover-img[src*="69ec0333eda923fe81bd51c9"]',
      b = document.createElement('style');
  b.id = 'oc-hero-ba';
  b.textContent =
    C + '{height:auto!important}' +
    '@media (min-width:1930px){' + C + '{height:calc(100% - 48px)!important;width:auto!important;justify-self:center!important}}';
  (document.head || document.documentElement).appendChild(b);

  // v1.0.0: Mouseflow loader.
  var mf = document.createElement('script');
  mf.type = 'text/javascript';
  mf.defer = true;
  mf.src = '//cdn.mouseflow.com/projects/0c356f71-0798-49b6-95e1-59d767833639.js';
  document.getElementsByTagName('head')[0].appendChild(mf);
})();
