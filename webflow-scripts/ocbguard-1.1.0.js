/* Blog post style guard.

   Webflow's Editor re-sanitizes post-body whenever a post is saved there -- which
   is how images get added -- and drops every <section>. That takes the .ocb,
   .ocb-cta and .faq-wrap wrapper classes with it, so the post loses its cards and
   the site's own !important rules on .post-body h2/p/a win: the CTA goes
   dark-on-dark and the FAQ loses its card.

   Two layers. The stylesheet keys off markup the sanitizer keeps, so the CTA is
   readable from first paint. The JS then puts the wrapper classes back on the
   surviving parent element. Both are no-ops on a post whose wrappers are intact. */
(function () {
  var C = '[style*="135deg,#8B0000"]', h = 'html body .post-body ';
  var css = ':root{--ink:#0f172a;--muted:#64748b;--line:#e5e7eb;--soft:#f8fafc;'
    + '--brand:#8B0000;--brand2:#5c0000;--gold:#fbbc04}'
    + h + C + ' h2{color:#fff!important}'
    + h + C + ' p{color:rgba(255,255,255,.92)!important}'
    + h + C + ' span{color:rgba(255,255,255,.95)!important}'
    + h + C + ' a{text-decoration:none!important}'
    + h + C + ' a[href^="tel"]{background:#fff!important;color:#5c0000!important}'
    + h + C + ' a[href="/contact"]{background:rgba(255,255,255,.16)!important;'
    + 'color:#fff!important;border:1px solid rgba(255,255,255,.55)!important}'
    + h + C + ' a[href*="g.page"]{color:#fbbc04!important;text-decoration:underline!important}'
    + h + '[style*="0 -6px"]{margin-bottom:8px!important}';
  var s = document.createElement('style');
  s.id = 'ocb-guard'; s.textContent = css; document.head.appendChild(s);

  // Re-apply a wrapper class `up` levels above each match, unless it is already there.
  function wrap(sel, cls, up) {
    document.querySelectorAll('.post-body ' + sel).forEach(function (el) {
      var p = el;
      for (var i = 0; i < (up || 1) && p; i++) p = p.parentElement;
      if (p && !/\bocb\b|\bfaq-wrap\b/.test(p.className)) p.className = (p.className + ' ' + cls).trim();
    });
  }
  function run() {
    try {
      wrap('.ocb-eyebrow', 'ocb ocb-card');
      wrap('.ocb-facts', 'ocb');
      wrap('.ocb-table', 'ocb ocb-card', 2);
      wrap('.ocb-2col', 'ocb');
      wrap('.faq-items', 'faq-wrap ocb');
      wrap(C, 'ocb ocb-cta');
    } catch (e) {}
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', run); else run();
})();
