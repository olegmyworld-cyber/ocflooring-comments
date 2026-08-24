// OC Flooring — Webflow registered inline script: "CarpetBellevueFontsCanonical"
// (id: carpetbellevuefontscanonical)
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
// Applied at: page header of /city-of-bellevue/carpet-installation-in-bellevue-wa
// (page id 6a8ccb1ebf28596111eed9f2) via the page-level scripts list.
//
// Purpose: loads the Google Fonts the carpet page design uses (Newsreader +
// Hanken Grotesk) and adds the page's canonical link when no canonical is
// already present. Injected as a script because the Webflow custom-code API
// rejects <link> tags (and any markup containing external URLs) in freeform
// head/footer blocks.
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
    L('stylesheet', 'https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;1,6..72,300;1,6..72,400&family=Hanken+Grotesk:wght@400;500;600;700&display=swap');
  }
  if (!d.querySelector('link[rel="canonical"]') && location.pathname.indexOf('/city-of-bellevue/carpet-installation-in-bellevue-wa') === 0) {
    L('canonical', 'https://www.nwocflooring.com/city-of-bellevue/carpet-installation-in-bellevue-wa');
  }
})();
