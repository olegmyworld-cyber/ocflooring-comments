// OC Flooring — Webflow registered inline script: "ocCarpetBellevue" (id: occarpetbellevue) v1.1.0
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
// Applied at: page footer of /city-of-bellevue/carpet-installation-in-bellevue-wa
// (page id 6a8ccb1ebf28596111eed9f2) via the page-level scripts list.
//
// v1.1.0 (2026-08-24): points at bundle 1.1.0, which now injects the estimator
// styles itself — the page-level head custom code set via the API did not
// survive to the published page, leaving the estimator unstyled.
(function () {
  if (document.getElementById('oc-carpet-loader')) return;
  var s = document.createElement('script');
  s.id = 'oc-carpet-loader';
  s.src = 'https://cdn.prod.website-files.com/6377e8e6a53936b48ef1cad0/6a8cd69f388cff38c7cb90a3_oc-carpet-bellevue-1.1.0.js';
  s.defer = true;
  (document.body || document.head).appendChild(s);
})();
