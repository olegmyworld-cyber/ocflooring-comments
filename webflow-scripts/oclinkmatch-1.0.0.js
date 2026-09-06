// OC Flooring — "ocLinkMatch" 1.0.0 — site-wide freeform footer code.
// Makes every city + service link go where its text says. If an anchor reads
// "Tile Installation in Seattle, WA" it must point at /seattle/tile-installation-in-seattle-wa,
// whatever a Designer element, a CMS field or a runtime script put in its href.
// Only touches anchors whose CURRENT target is already a city/service page or a
// service hub (so deliberate links to blog posts, /contact, galleries etc. are never changed),
// and only when the text names BOTH a service and a city. Runs at load, then re-checks
// on DOM mutations for 15 s so links injected by other scripts are covered too.
(function () {
  var SVC = [
    [/\btile/i, 'tile-installation'],
    [/\bcarpet/i, 'carpet-installation'],
    [/refinish|screen (and|&) recoat|buff (and|&) (re)?coat|recoat|sand(ing)? (and|&) (re)?finish/i, 'hardwood-floor-refinishing'],
    [/\brepair/i, 'hardwood-floor-repair'],
    [/vinyl|\blvp\b|laminate|waterproof floor/i, 'vinyl-plank-flooring-installation'],
    [/hardwood (floor(ing)? )?install|floor installation|install(ation)? (of )?(new )?(solid|engineered|hardwood|wood)|new hardwood|hardwood floors? in\b|hardwood flooring (services )?in\b/i, 'hardwood-floor-installation']
  ];
  var CITY = /\b(bellevue|seattle|kirkland|newcastle|new castle|everett|marysville|shoreline|sammamish|arlington|snohomish|issaquah|whidbey island|monroe|snoqualmie|lake stevens|mukilteo|kenmore|north bend|edmonds|mill creek|medina|bothell|woodinville|mercer island|oak harbor|duvall|redmond|renton|lynnwood|cottage lake)\b/i;
  var FOLDER = { seattle: ['seattle', 'seattle'], arlington: ['arlington', ''], bothell: ['hardwood-floor-refinishing', 'bothell'], newcastle: ['city-of-new-castle', 'newcastle'] };
  var PAGE = /^\/(city-of-[a-z-]+|seattle|arlington|hardwood-floor-refinishing)\/(tile-installation|carpet-installation|hardwood-floor-refinishing|hardwood-floor-repair|vinyl-plank-flooring-installation|hardwood-floor-installation)(-in-[a-z-]+-wa)?\/?$|^\/flooring-services-near-me\/[a-z-]+\/?$|^\/$/;
  function svcOf(t) { for (var i = 0; i < SVC.length; i++) if (SVC[i][0].test(t)) return SVC[i][1]; return null; }
  function expected(t) {
    var m = CITY.exec(t); if (!m) return null;
    var s = svcOf(t); if (!s) return null;
    var c = m[1].toLowerCase().replace('new castle', 'newcastle').replace(/ /g, '-');
    if (c === 'bellevue' && s === 'hardwood-floor-refinishing') return '/';
    var f = FOLDER[c] || ['city-of-' + c, c];
    return f[1] ? '/' + f[0] + '/' + s + '-in-' + f[1] + '-wa' : '/' + f[0] + '/' + s;
  }
  function run() {
    var as = document.querySelectorAll('a[href]'), n = 0;
    for (var i = 0; i < as.length; i++) {
      var a = as[i];
      if (a.host && a.host !== location.host) continue;
      var p = (a.pathname || '').replace(/\/+$/, '') || '/';
      if (!PAGE.test(p)) continue;
      var t = (a.textContent || a.getAttribute('aria-label') || a.title || '').replace(/\s+/g, ' ').trim();
      if (!t) continue;
      var e = expected(t);
      if (e && e !== p) { a.setAttribute('href', e + (a.search || '') + (a.hash || '')); a.setAttribute('data-oclm', p); n++; }
    }
    return n;
  }
  if (document.readyState !== 'loading') run(); else document.addEventListener('DOMContentLoaded', run);
  window.addEventListener('load', run);
  [500, 1500, 3000, 6000].forEach(function (t) { setTimeout(run, t); });
  try {
    var mo = new MutationObserver(function () { clearTimeout(window.__oclm); window.__oclm = setTimeout(run, 150); });
    mo.observe(document.documentElement, { childList: true, subtree: true });
    setTimeout(function () { mo.disconnect(); }, 15000);
  } catch (e) {}
})();
