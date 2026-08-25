// OC Flooring — Webflow registered inline script: "ocCarpetBellevue" v1.5.1
// (id: occarpetbellevue)
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
// Applied at: page footer of /city-of-bellevue/carpet-installation-in-bellevue-wa
// (page id 6a8ccb1ebf28596111eed9f2) via the page-level scripts list.
//
// Purpose: loads the carpet page bundle oc-carpet-bellevue-1.5.1.js (hosted as
// Webflow asset 6a8cef2a3f0cf95fa3ced042). v1.5.x restyles the photo-quote
// form into the repair-page uploader design (photo drop-tiles, chips, labeled
// field grid, promise row) on top of the native Webflow form; 1.5.1 removes
// "New carpet installation" from the project-type chips.
(function () {
  if (document.getElementById('oc-carpet-loader')) return;
  var s = document.createElement('script');
  s.id = 'oc-carpet-loader';
  s.src = 'https://cdn.prod.website-files.com/6377e8e6a53936b48ef1cad0/6a8cef2a3f0cf95fa3ced042_oc-carpet-bellevue-1.5.1.js';
  s.defer = true;
  (document.body || document.head).appendChild(s);
})();
