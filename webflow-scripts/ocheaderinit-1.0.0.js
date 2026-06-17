// OC Flooring — Webflow registered inline script: "OCHeaderInit" (id: ocheaderinit)
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
// Applied at: site HEADER (so its CSS lands before first paint — no flash on above-the-fold content).
//
// What it does:
//   1. Hides the "/financing" nav link site-wide (pre-existing behavior).
//   2. Loads the Mouseflow analytics bundle (pre-existing behavior).
//   3. Hero <h1> title sizing + hero subheading sizing (added 2026-06-17) — see note below.
//
// Why the hero sizing lives HERE (and not in the Designer):
//   Another registered script, "OCHeadingFix" (ocheadingfix), injects
//     html body .heading-hero { font-size: clamp(30px, 6.2vw, 57px) !important }
//   That !important rule pins the hero title to ~57px on desktop (too big) and ~30px on
//   phones (too small), and it overrides ANY font-size set on the `.heading-hero` /
//   `.heading-hero-custom` classes in the Webflow Designer. So Designer edits to those
//   classes had no visible effect. To win deterministically we inject a competing rule
//   with HIGHER specificity (repeated class: `.heading-hero.heading-hero` → (0,2,2) beats
//   the old (0,1,2)) plus !important, so it wins regardless of stylesheet order. It is
//   merged into this already-applied header script because both the header and footer
//   script blocks are at Webflow's 15-script-per-block limit (same constraint that forced
//   the BonaMobileFix merge).
//
// Hero title scale (px, so it is independent of the site's fluid root font-size):
//   desktop 46  /  ≤991px 44  /  ≤767px 41  /  ≤479px 38   (smaller on desktop, larger on
//   mobile than the old 57/30 clamp — i.e. a deliberate "reverse ramp" per the request).
//
// Hero subheading (.subheading-hero, e.g. "Love Your Floors Again — Without the Mess"):
//   on mobile it was shrinking out of proportion with the title. Bumped (mobile breakpoints
//   only; desktop left at its Designer 2.3rem) to keep the SAME title:subheading ratio as
//   desktop — ≤991px 34  /  ≤767px 32  /  ≤479px 30 (px). Higher-specificity + !important
//   for the same reason as the title.
//
// NOTE: deployed copy is minified to fit Webflow's 2000-char inline-script limit.
window._mfq = window._mfq || [];
(function () {
  // 1) Hide the financing nav link.
  var s = document.createElement('style');
  s.id = 'oc-hide-fin';
  s.textContent = '.nav-link[href="/financing"],.nav-link[href="/financing/"]{display:none!important}';
  (document.head || document.documentElement).appendChild(s);

  // 3) Hero <h1> title sizing — higher specificity + !important to beat OCHeadingFix's clamp.
  var h = document.createElement('style');
  h.id = 'oc-hero-title-size';
  h.textContent =
    'html body .heading-hero.heading-hero,html body .heading-hero-custom.heading-hero-custom{font-size:46px!important;line-height:1.12!important}' +
    '@media screen and (max-width:991px){html body .heading-hero.heading-hero,html body .heading-hero-custom.heading-hero-custom{font-size:44px!important}}' +
    '@media screen and (max-width:767px){html body .heading-hero.heading-hero,html body .heading-hero-custom.heading-hero-custom{font-size:41px!important;line-height:1.14!important}}' +
    '@media screen and (max-width:479px){html body .heading-hero.heading-hero,html body .heading-hero-custom.heading-hero-custom{font-size:38px!important;line-height:1.12!important;letter-spacing:-.01em!important}}' +
    // Hero subheading — keep it proportional to the title on mobile (desktop untouched).
    '@media screen and (max-width:991px){html body .subheading-hero.subheading-hero{font-size:34px!important}}' +
    '@media screen and (max-width:767px){html body .subheading-hero.subheading-hero{font-size:32px!important}}' +
    '@media screen and (max-width:479px){html body .subheading-hero.subheading-hero{font-size:30px!important;line-height:1.2!important}}';
  (document.head || document.documentElement).appendChild(h);

  // 2) Mouseflow analytics.
  var mf = document.createElement('script');
  mf.type = 'text/javascript';
  mf.defer = true;
  mf.src = '//cdn.mouseflow.com/projects/0c356f71-0798-49b6-95e1-59d767833639.js';
  document.getElementsByTagName('head')[0].appendChild(mf);
})();
