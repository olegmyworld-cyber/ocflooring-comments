// OC Flooring — 404 page fallback redirects (page-level footer code on the /404 page).
// Site: nwocflooring.com (Webflow site 6377e8e6a53936b48ef1cad0)
// Runs only on the 404 page. Maps legacy URLs (old /services/*, old city-page slugs,
// /city-of-arlington/*, deleted laminate city pages, renamed blog posts, dead products)
// to the closest live page, then location.replace()s there. Real 301s live in Webflow
// Site settings > Publishing > 301 redirects (see redirects.csv); this script is the
// safety net for anything not yet imported there.
(function () {
  var p = (location.pathname || '/').replace(/\/+$/, '').toLowerCase() || '/';
  try { if (sessionStorage.getItem('oc404') === p) return; sessionStorage.setItem('oc404', p); } catch (e) {}
  var SVC = '/flooring-services-near-me/';
  // Old /services/<slug> that were renamed rather than moved 1:1.
  var SA = {
    'seattle-wa-wood-wall-paneling-acoustic-panels': 'wood-wall-panels',
    'commercial-flooring-services-in-seattle-wa-by-oc-flooring': 'commercial-flooring-installation',
    'quality-flooring-solutions-for-northwest-homebuilders': 'commercial-flooring-installation',
    'stair-installation-in-lynnwood-wa': 'stair-installation-and-remodeling',
    'flooring-material': 'our-products',
    'dustless-floor-sanding-copy': 'dustless-floor-sanding',
    'eco-friendly-floor-refinishing-sustainable-health': 'eco-friendly-floor-refinishing',
    'premium-solid-hardwood-flooring-installation-services': 'solid-hardwood-flooring'
  };
  // Deleted / renamed blog posts -> closest live post.
  var BA = {
    'how-much-does-carpet-installation-cost-in-bothell-wa-with-oc-flooring-company': 'carpet-installation-cost-bothell-wa',
    'engineered-hardwood-vs-luxury-vinyl-plank-which-is-better-in-lynnwood-wa': 'what-is-better-laminate-or-engineered-hardwood',
    'prefinished-hardwood-vs-unfinished-hardwood-in-kirkland-wa-which-is-right-for-your-home': 'pre-finished-vs-site-finished-hardwood-floors',
    'your-go-to-flooring-carpet-installation-service-in-mill-creek-wa': 'flooring-guide-mill-creek-wa',
    'top-5-affordable-flooring-options-in-lynnwood-you-cant-miss': '5-carpet-options-for-carpet-installation-in-lynnwood-wa',
    'what-is-the-best-flooring-to-put-in-a-new-house-oc-floorings-showroom-in-lynnwood-wa-has-you-covered-2': 'what-to-know-about-home-flooring-installation',
    'wood-floor-stain-colors-how-to-choose-the-right-stain-for-hardwood-floors': 'what-color-should-i-stain-my-wood-floors'
  };
  // City folder -> slug suffix used by the live city pages ("" = no suffix, e.g. /arlington/tile-installation).
  var CITY = {
    'seattle': 'seattle', 'hardwood-floor-refinishing': 'bothell', 'arlington': '',
    'city-of-new-castle': 'newcastle'
  };
  function cls(s) {
    if (/laminate|vinyl/.test(s)) return 'vinyl-plank-flooring-installation';
    if (/refinishing|restoration/.test(s)) return 'hardwood-floor-refinishing';
    if (/repair/.test(s)) return 'hardwood-floor-repair';
    if (/tile/.test(s)) return 'tile-installation';
    if (/carpet/.test(s)) return 'carpet-installation';
    if (/install|flooring-services|floor-services/.test(s)) return 'hardwood-floor-installation';
    return null;
  }
  function target(p) {
    var m = p.match(/^\/([a-z0-9-]+)\/([a-z0-9-]+)$/);
    if (!m) return p === '/thank-you' ? '/contact' : null;
    var f = m[1], s = m[2];
    if (f === 'services') {
      if (SA[s]) return SVC + SA[s];
      var c = cls(s);
      if (c && !/^(hardwood-floor|floor-refinishing|flooring-repair|tile-installation|carpet-installation|laminate|vinyl|dustless|eco|engineered|solid|unfinished|buff|stair|commercial|insurance|our-products|flooring-store|wood-wall)/.test(s)) {
        return SVC + ({ 'vinyl-plank-flooring-installation': 'vinyl-plank-flooring-and-laminate-flooring', 'hardwood-floor-refinishing': 'floor-refinishing', 'hardwood-floor-repair': 'flooring-repair', 'hardwood-floor-installation': 'hardwood-floor-installation' }[c] || c);
      }
      return SVC + s; // 1:1 move of the old /services folder
    }
    if (f === 'blog') return BA[s] ? '/blog/' + BA[s] : '/blog';
    if (f === 'product') return SVC + 'our-products';
    if (f === 'gallery' || f === 'vinyl-gallery') return '/our-work';
    if (f === 'city-of-arlington') f = 'arlington';
    if (f === 'city-of-bellevue' && /refinishing/.test(s)) return '/';
    var city = CITY[f] !== undefined ? CITY[f] : (f.indexOf('city-of-') === 0 ? f.slice(8) : null);
    if (city === null) return null;
    var c2 = cls(s);
    if (!c2) return null;
    return '/' + f + '/' + c2 + (city ? '-in-' + city + '-wa' : '');
  }
  var t = target(p);
  if (t && t !== p) location.replace(t + location.search + location.hash);
})();
