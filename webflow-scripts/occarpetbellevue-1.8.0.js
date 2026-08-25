// OC Flooring — Webflow registered inline script: "ocCarpetBellevue" v1.8.0
// (id: occarpetbellevue)
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
// Applied at: page footer of /city-of-bellevue/carpet-installation-in-bellevue-wa
// (page id 6a8ccb1ebf28596111eed9f2) via the page-level scripts list.
//
// Purpose: loads bundle oc-carpet-bellevue-1.8.0.js (Webflow asset
// 6a8cfffb3f0cf95fa3d37dc4). v1.8.0 makes the bundle city-agnostic for the
// carpet city-page rollout: the estimator's ballpark label derives its city
// from the URL slug, and the shared areas slider's Carpet Installation slide
// is promoted to the front on carpet pages. Applied to every
// carpet-installation-in-<city>-wa page.
(function () {
  if (document.getElementById('oc-carpet-loader')) return;
  var s = document.createElement('script');
  s.id = 'oc-carpet-loader';
  s.src = 'https://cdn.prod.website-files.com/6377e8e6a53936b48ef1cad0/6a8cfffb3f0cf95fa3d37dc4_oc-carpet-bellevue-1.8.0.js';
  s.defer = true;
  (document.body || document.head).appendChild(s);
})();
