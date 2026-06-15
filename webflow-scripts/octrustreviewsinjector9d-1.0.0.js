// OC Flooring — Webflow registered inline script: "OCTrustReviewsInjector9d" (id: octrustreviewsinjector9d)
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
// Applied at: site footer.
//
// Purpose: loads the trust-reviews bundle (oc-trust-reviews-v9c-min.js) that renders the new
// review section and replaces the old (Elfsight) review widget.
//
// Change (2026-06-15): extended the path guard so the loader also runs on /about-us,
// /our-work and /why-were-different (previously home + hardwood-floor-refinishing-in-* only),
// so those pages get the same new review section in place of the old widget.
(function () {
  var p = location.pathname.replace(/\/+$/, '');
  var home = p === '' || p === '/index' || p === '/home';
  var city = /hardwood-floor-refinishing-in-/.test(p) && !/\/blog\//.test(p);
  var extra = ['/about-us', '/our-work', '/why-were-different'].indexOf(p) >= 0;
  if (!home && !city && !extra) return;
  if (document.getElementById('oc-trust-loader')) return;
  var s = document.createElement('script');
  s.id = 'oc-trust-loader';
  s.src = 'https://cdn.prod.website-files.com/6377e8e6a53936b48ef1cad0/6a2c93d15f4fbb2b0c31f679_oc-trust-reviews-v9c-min.js';
  s.defer = true;
  (document.body || document.head).appendChild(s);
})();
