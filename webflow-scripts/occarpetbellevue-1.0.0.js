// OC Flooring — Webflow registered inline script: "ocCarpetBellevue" (id: occarpetbellevue)
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
// Applied at: page footer of /city-of-bellevue/carpet-installation-in-bellevue-wa
// (page id 6a8ccb1ebf28596111eed9f2) via the page-level scripts list.
//
// Purpose: loads the carpet page bundle (oc-carpet-bellevue-1.0.0.js, hosted as a
// Webflow asset) that renders the interactive cost estimator into #ci-estimator
// and drives the FAQ accordion. Page-scoped, so no path guard is needed.
(function () {
  if (document.getElementById('oc-carpet-loader')) return;
  var s = document.createElement('script');
  s.id = 'oc-carpet-loader';
  s.src = 'https://cdn.prod.website-files.com/6377e8e6a53936b48ef1cad0/6a8ccfeff4c78f7f2b0b6018_oc-carpet-bellevue-1.0.0.js';
  s.defer = true;
  (document.body || document.head).appendChild(s);
})();
