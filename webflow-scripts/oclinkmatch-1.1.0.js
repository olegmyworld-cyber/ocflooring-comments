/* OCLinkMatch 1.1.0 — site footer custom code, nwocflooring.com
 * Keeps every "<service> in <city>" link pointed at that city's page for that service.
 * 1.0.0 rewrote hrefs after load. 1.1.0 additionally intercepts the click itself
 * (capture phase on window), so a late href rewrite or a competing click handler
 * can no longer send the visitor elsewhere. Only touches internal anchors whose
 * current target is already a city page or a service hub, whose text names exactly
 * one city, and whose text is a short label (<=90 chars).
 */
(function () {
  var S = [
    [/\btile/i, 'tile-installation'],
    [/\bcarpet/i, 'carpet-installation'],
    [/refinish|recoat|\bsand/i, 'hardwood-floor-refinishing'],
    [/\brepair/i, 'hardwood-floor-repair'],
    [/vinyl|\blvp\b|laminate|waterproof/i, 'vinyl-plank-flooring-installation'],
    [/install|new hardwood|hardwood floor/i, 'hardwood-floor-installation']
  ];
  var C = /\b(bellevue|seattle|kirkland|newcastle|new castle|everett|marysville|shoreline|sammamish|arlington|snohomish|issaquah|whidbey island|monroe|snoqualmie|lake stevens|mukilteo|kenmore|north bend|edmonds|mill creek|medina|bothell|woodinville|mercer island|oak harbor|duvall|redmond|renton|lynnwood|cottage lake)\b/ig;
  var F = { seattle: ['seattle', 'seattle'], arlington: ['arlington', ''], bothell: ['hardwood-floor-refinishing', 'bothell'], newcastle: ['city-of-new-castle', 'newcastle'] };
  var P = /^\/(city-of-[a-z-]+|seattle|arlington|hardwood-floor-refinishing|flooring-services-near-me)\/[a-z-]+\/?$|^\/$/;

  function nh(h) { return (h || '').toLowerCase().replace(/^www\./, ''); }

  // text -> expected path, or null when the text does not name exactly one service + one city
  function x(t) {
    if (t.length > 90) return null;
    var m = t.match(C);
    if (!m || m.length !== 1) return null;
    var s = null, i;
    for (i = 0; i < S.length; i++) if (S[i][0].test(t)) { s = S[i][1]; break; }
    if (!s) return null;
    var c = m[0].toLowerCase().replace('new castle', 'newcastle').replace(/ /g, '-');
    if (c === 'bellevue' && s === 'hardwood-floor-refinishing') return '/';
    var f = F[c] || ['city-of-' + c, c];
    return f[1] ? '/' + f[0] + '/' + s + '-in-' + f[1] + '-wa' : '/' + f[0] + '/' + s;
  }

  // anchor -> expected path when it differs from the anchor's current path, else null
  function ex(a) {
    if (a.host && nh(a.host) !== nh(location.host)) return null;
    var p = (a.pathname || '').replace(/\/+$/, '') || '/';
    if (!P.test(p)) return null;
    var t = (a.textContent || '').replace(/\s+/g, ' ').trim();
    if (!t) return null;
    var e = x(t);
    return e && e !== p ? e : null;
  }

  function r() {
    var A = document.querySelectorAll('a[href]'), i, e;
    for (i = 0; i < A.length; i++) { e = ex(A[i]); if (e) A[i].setAttribute('href', e); }
  }

  // Click guard: runs before any page script's click handler.
  addEventListener('click', function (ev) {
    try {
      if (ev.button || ev.metaKey || ev.ctrlKey || ev.shiftKey || ev.altKey) return;
      var a = ev.target && ev.target.closest ? ev.target.closest('a[href]') : null;
      if (!a) return;
      var e = ex(a);
      if (!e) return;
      ev.preventDefault();
      ev.stopImmediatePropagation();
      location.assign(e);
    } catch (err) {}
  }, true);

  if (document.readyState !== 'loading') r(); else document.addEventListener('DOMContentLoaded', r);
  addEventListener('load', r);
  [800, 2500, 6000].forEach(function (t) { setTimeout(r, t); });
  try {
    var o = new MutationObserver(function () { clearTimeout(window.__oclm); window.__oclm = setTimeout(r, 150); });
    o.observe(document.documentElement, { childList: true, subtree: true });
    setTimeout(function () { o.disconnect(); }, 15000);
  } catch (e) {}
})();
