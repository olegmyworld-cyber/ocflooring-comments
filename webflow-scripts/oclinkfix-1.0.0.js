/* ocLinkFix 1.0.0 — repoint internal links that target paths which no longer exist.
 *
 * Semrush "internal broken links", 29 Aug 2026, found 20 links to three dead patterns:
 *   /services-near-me/<slug>                              -> the folder is flooring-services-near-me
 *   /services/floor-refinishing                           -> same folder
 *   /city-of-<c>/laminate-flooring-installation-in-<c>-wa -> no city laminate pages exist
 *
 * These hrefs are NOT in the Designer content, the page or site custom code, any HTML
 * embed, the shared Navbar/Footer/Services/Areas components (the nav dropdown uses page
 * IDs and resolves correctly), or any CMS field — all checked via the Webflow API. They
 * are injected at runtime by one of the CDN-hosted registered scripts, whose sources
 * could not be read from the session that wrote this.
 *
 * So this rewrites them in the DOM after the injector runs. It only touches hrefs that
 * match the three dead patterns, every one of which 404s today, so a rewrite can only
 * improve them. Once the offending injector is found and corrected, delete this script.
 */
(function () {
  function map(p) {
    if (p.indexOf('/services-near-me/') === 0) return '/flooring-services-near-me/' + p.slice(18);
    if (p === '/services/floor-refinishing') return '/flooring-services-near-me/floor-refinishing';
    var m = p.match(/^\/(city-of-[a-z-]+)\/laminate-flooring-installation-in-([a-z-]+)-wa\/?$/);
    if (m) return '/' + m[1] + '/vinyl-plank-flooring-installation-in-' + m[2] + '-wa';
    return null;
  }
  function run() {
    var as = document.getElementsByTagName('a'), n = 0;
    for (var i = 0; i < as.length; i++) {
      var a = as[i];
      if (a.host && a.host !== location.host) continue;
      var r = map(a.pathname || '');
      if (r) { a.setAttribute('href', r + (a.search || '') + (a.hash || '')); n++; }
    }
    return n;
  }
  if (document.readyState !== 'loading') run();
  else document.addEventListener('DOMContentLoaded', run);
  window.addEventListener('load', run);
  [300, 900, 2000, 4000].forEach(function (t) { setTimeout(run, t); });
  try {
    var mo = new MutationObserver(function () {
      clearTimeout(window.__oclf);
      window.__oclf = setTimeout(run, 120);
    });
    mo.observe(document.documentElement, { childList: true, subtree: true });
    setTimeout(function () { mo.disconnect(); }, 15000);
  } catch (e) {}
})();
