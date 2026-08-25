// OC Flooring — Webflow registered inline script: "ocCarpetBellevue" v1.6.0
// (id: occarpetbellevue)
// Site: OC Flooring Hardwood Refinishing (6377e8e6a53936b48ef1cad0) — nwocflooring.com
// Applied at: page footer of /city-of-bellevue/carpet-installation-in-bellevue-wa
// (page id 6a8ccb1ebf28596111eed9f2) via the page-level scripts list.
//
// Purpose: loads bundle oc-carpet-bellevue-1.6.0.js (Webflow asset
// 6a8cf1e83f0cf95fa3cfec1c). v1.6.0 replaces the native-Webflow-form uploader
// (whose submits failed on the live site) with the same #ocpq photo-quote
// widget the hardwood floor-repair pages use: identical design and identical
// submission — multipart POST to formsubmit.co → info.ocflooring@gmail.com,
// _template=table, subject "Photo quote - Bellevue, WA - <Name> - <N> photos".
// Widget source of record: webflow-scripts/carpet-ocpq-embed-1.0.0.html.
(function () {
  if (document.getElementById('oc-carpet-loader')) return;
  var s = document.createElement('script');
  s.id = 'oc-carpet-loader';
  s.src = 'https://cdn.prod.website-files.com/6377e8e6a53936b48ef1cad0/6a8cf1e83f0cf95fa3cfec1c_oc-carpet-bellevue-1.6.0.js';
  s.defer = true;
  (document.body || document.head).appendChild(s);
})();
