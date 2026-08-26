// OC Flooring — Webflow registered inline script: "TileBellevueFontsCanonical"
// v1.0.0 (id: tilebellevuefontscanonical)
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
// Applied at: page header of every tile-installation-in-<city>-wa page.
// Loads the tile design's Google Fonts (Instrument Serif + Archivo) and adds
// the canonical link when absent (Webflow page settings can't set one).
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
  if (!d.querySelector('link[href*="fonts.googleapis"][href*="Instrument"]')) {
    L('preconnect', 'https://fonts.googleapis.com');
    L('preconnect', 'https://fonts.gstatic.com', '');
    L('stylesheet', 'https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Archivo:wght@400;500;600;700&display=swap');
  }
  if (!d.querySelector('link[rel="canonical"]') && location.pathname.indexOf('tile-installation-in-') > -1) {
    L('canonical', 'https://www.nwocflooring.com' + location.pathname.replace(/\/+$/, ''));
  }
})();
