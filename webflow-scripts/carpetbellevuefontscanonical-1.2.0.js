// OC Flooring — Webflow registered inline script: "CarpetBellevueFontsCanonical"
// v1.2.0 (id: carpetbellevuefontscanonical)
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
// Applied at: page header of every carpet-installation-in-<city>-wa page
// via the page-level scripts lists.
//
// v1.2.0: adds Playfair Display 700/800 to the Google Fonts request — the
// photo-quote widget (same design as the repair pages' #ocpq) sets its
// headings in Playfair Display, which the carpet page's own Webflow styles
// don't otherwise load. Also still loads Newsreader + Hanken Grotesk and adds
// the canonical link when absent.
(function () {
  var d = document, h = d.head;
  function L(rel, href, cross) {
    var l = d.createElement('link');
    l.rel = rel;
    l.href = href;
    if (cross !== undefined) l.crossOrigin = cross;
    h.appendChild(l);
    return l;
  }
  if (!d.querySelector('link[href*="fonts.googleapis"][href*="Hanken"]')) {
    L('preconnect', 'https://fonts.googleapis.com');
    L('preconnect', 'https://fonts.gstatic.com', '');
    L('stylesheet', 'https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;1,6..72,300;1,6..72,400&family=Hanken+Grotesk:wght@400;500;600;700&family=Playfair+Display:wght@700;800&display=swap');
  }
  if (!d.querySelector('link[rel="canonical"]') && location.pathname.indexOf('carpet-installation-in-') > -1) {
    L('canonical', 'https://www.nwocflooring.com' + location.pathname.replace(/\/+$/, ''));
  }
})();
