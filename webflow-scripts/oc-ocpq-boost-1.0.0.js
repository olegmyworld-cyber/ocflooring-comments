// OC Flooring — photo-quote confirmation + attention layer v1.0.0
//
// Applies to every page that carries the #ocpq photo-upload widget
// (hardwood floor repair pages, where the widget lives in the shared Footer
// component's HTML embed; carpet installation pages, rendered by the carpet
// bundle; tile installation pages, rendered by the tile bundle) and to the
// scheduling cards on the carpet (.ci-book-cal) and tile (.ti-cal-card) pages.
//
// Two jobs, both purely additive — nothing here changes how a submission is
// built or sent, and every hook is try/catch-guarded and idempotent:
//
//   1. CONFIRMATION. When the widget's success panel (#ocpq-done) appears,
//      the visitor gets an unmissable acknowledgement that the pictures went
//      out: a fixed toast at the top of the viewport with a green tick, plus
//      a green "sent" bar pinned above the success copy inside the card, plus
//      an aria-live announcement for screen readers. The toast self-dismisses
//      after 10s and can be dismissed by click or Escape.
//
//   2. ATTENTION. Gentle motion that draws the eye to the two actions that
//      matter — uploading a photo and booking a visit. The drop zone breathes
//      and its icon floats until the visitor adds the first photo; the send
//      button gets a slow sheen once the form is revealed; the scheduling
//      card pulses a ring three times the first time it scrolls into view.
//      All of it is disabled under prefers-reduced-motion.
//
// The widget is rendered by JavaScript on the carpet and tile pages, so the
// script waits for #ocpq to exist (MutationObserver plus a bounded poll) and
// binds again if the widget is re-rendered.
(function () {
  if (window.__ocpqBoost) return;
  window.__ocpqBoost = 1;

  var D = document;
  var REDUCED = false;
  try {
    REDUCED = !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  } catch (e) {}

  var CSS =
    '@keyframes ocbBreathe{0%,100%{box-shadow:0 0 0 0 rgba(46,93,87,0)}50%{box-shadow:0 0 0 12px rgba(46,93,87,.13)}}' +
    '@keyframes ocbFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-7px)}}' +
    '@keyframes ocbRing{0%{box-shadow:0 0 0 0 rgba(46,93,87,.42)}70%{box-shadow:0 0 0 20px rgba(46,93,87,0)}100%{box-shadow:0 0 0 0 rgba(46,93,87,0)}}' +
    '@keyframes ocbSheen{0%{transform:translateX(-130%)}55%,100%{transform:translateX(240%)}}' +
    '@keyframes ocbToastIn{from{opacity:0;transform:translate(-50%,-16px)}to{opacity:1;transform:translate(-50%,0)}}' +
    '@keyframes ocbToastOut{to{opacity:0;transform:translate(-50%,-16px)}}' +
    '@keyframes ocbPop{0%{transform:scale(.55);opacity:0}62%{transform:scale(1.14);opacity:1}100%{transform:scale(1);opacity:1}}' +
    '.ocb-breathe{animation:ocbBreathe 2.8s ease-in-out infinite}' +
    '.ocb-breathe .ocpq-dropicon{animation:ocbFloat 2.4s ease-in-out infinite}' +
    '.ocb-ring{animation:ocbRing 2s ease-out 3}' +
    '.ocb-sheen{position:relative;overflow:hidden}' +
    '.ocb-sheen::after{content:"";position:absolute;top:0;bottom:0;left:0;width:36%;background:linear-gradient(100deg,transparent,rgba(255,255,255,.4),transparent);transform:translateX(-130%);animation:ocbSheen 3.8s ease-in-out infinite;pointer-events:none}' +
    '#ocb-toast{position:fixed;left:50%;top:16px;transform:translateX(-50%);z-index:2147483000;width:min(92vw,520px);display:flex;gap:13px;align-items:flex-start;background:#16201E;color:#FBFAF7;padding:16px 18px;border-left:4px solid #1f8a4c;box-shadow:0 20px 46px -18px rgba(0,0,0,.6);font:400 15px/1.5 Archivo,Arial,Helvetica,sans-serif;animation:ocbToastIn .3s ease both;cursor:pointer}' +
    '#ocb-toast b{display:block;font-weight:700;font-size:16.5px;margin:0 0 3px}' +
    '#ocb-toast small{display:block;margin-top:6px;font-size:13px;line-height:1.5;color:#A8B3AD}' +
    '#ocb-toast .ocb-tick{width:32px;height:32px;flex:0 0 auto;border-radius:50%;background:#1f8a4c;color:#fff;display:grid;place-items:center;animation:ocbPop .45s ease both}' +
    '#ocb-toast .ocb-tick svg{width:18px;height:18px;display:block}' +
    '#ocb-toast .ocb-x{margin-left:auto;flex:0 0 auto;opacity:.55;font-size:19px;line-height:1}' +
    '.ocb-sentbar{margin:0 0 20px;background:#e7f0e3;border-left:3px solid #1f8a4c;color:#14361f;padding:14px 16px;font:600 15px/1.5 Archivo,Arial,Helvetica,sans-serif;display:flex;gap:11px;align-items:center;animation:ocbPop .4s ease both}' +
    '.ocb-sentbar svg{width:19px;height:19px;flex:0 0 auto;display:block}' +
    '.ocb-sr{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}' +
    '@media (max-width:640px){#ocb-toast{top:auto;bottom:16px;animation:none}}' +
    '@media (prefers-reduced-motion:reduce){.ocb-breathe,.ocb-breathe .ocpq-dropicon,.ocb-ring,.ocb-sheen::after,#ocb-toast,#ocb-toast .ocb-tick,.ocb-sentbar{animation:none!important}}';

  function styles() {
    if (D.getElementById('ocb-css')) return;
    var s = D.createElement('style');
    s.id = 'ocb-css';
    s.textContent = CSS;
    (D.head || D.documentElement).appendChild(s);
  }

  var TICK = '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="m4 12.5 5 5L20 6.5"/></svg>';
  var live = null;

  function announce(msg) {
    try {
      if (!live) {
        live = D.createElement('div');
        live.className = 'ocb-sr';
        live.setAttribute('role', 'status');
        live.setAttribute('aria-live', 'polite');
        D.body.appendChild(live);
      }
      live.textContent = msg;
    } catch (e) {}
  }

  var toastTimer = null;

  function closeToast() {
    var t = D.getElementById('ocb-toast');
    if (!t) return;
    clearTimeout(toastTimer);
    if (REDUCED) { try { t.remove(); } catch (e) {} return; }
    t.style.animation = 'ocbToastOut .25s ease both';
    setTimeout(function () { try { t.remove(); } catch (e) {} }, 260);
  }

  function toast(head, body) {
    try {
      closeToast();
      var t = D.createElement('div');
      t.id = 'ocb-toast';
      t.setAttribute('role', 'status');
      t.innerHTML = '<span class="ocb-tick">' + TICK + '</span><span><b></b><span class="ocb-msg"></span><small></small></span><span class="ocb-x" aria-hidden="true">&times;</span>';
      t.querySelector('b').textContent = head;
      t.querySelector('.ocb-msg').textContent = body;
      t.querySelector('small').textContent = 'Tap to dismiss';
      t.addEventListener('click', closeToast);
      D.body.appendChild(t);
      toastTimer = setTimeout(closeToast, 10000);
    } catch (e) {}
  }

  D.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeToast();
  });

  // ---- 1. confirmation -----------------------------------------------------
  function onSent(done) {
    if (!done || done.getAttribute('data-ocb-sent') === '1') return;
    done.setAttribute('data-ocb-sent', '1');

    var name = '';
    try {
      var h = D.getElementById('ocpq-donehead');
      var m = h && h.textContent ? h.textContent.match(/Got it,\s*([^—-]+)/) : null;
      if (m) name = m[1].trim().replace(/[,\s]+$/, '');
    } catch (e) {}

    var count = 0;
    try {
      count = D.querySelectorAll('#ocpq-thumbs .ocpq-thumb').length;
    } catch (e) {}
    var photos = count === 1 ? 'Your photo is' : count > 1 ? 'All ' + count + ' photos are' : 'Your photos are';

    try {
      if (!D.querySelector('.ocb-sentbar')) {
        var bar = D.createElement('div');
        bar.className = 'ocb-sentbar';
        bar.innerHTML = TICK + '<span></span>';
        bar.querySelector('span').textContent = photos + ' on their way to our estimator.';
        done.insertBefore(bar, done.firstChild);
      }
    } catch (e) {}

    toast(
      name ? 'Photos sent, ' + name + '.' : 'Photos sent.',
      photos + ' with our estimator — nothing else for you to do.'
    );
    announce('Your photos were sent successfully. A written quote follows by email the same business day.');
  }

  function watchDone(root) {
    var done = (root || D).querySelector('#ocpq-done');
    if (!done || done.getAttribute('data-ocb-watch') === '1') return;
    done.setAttribute('data-ocb-watch', '1');
    if (!done.hidden) onSent(done);
    try {
      new MutationObserver(function () {
        if (!done.hidden) onSent(done);
        else done.removeAttribute('data-ocb-sent');
      }).observe(done, { attributes: true, attributeFilter: ['hidden', 'style'] });
    } catch (e) {}
  }

  // ---- 2. attention --------------------------------------------------------
  function inView(el, fn) {
    try {
      if (!('IntersectionObserver' in window)) { fn(); return; }
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (en) {
          if (en.isIntersecting) { io.disconnect(); fn(); }
        });
      }, { threshold: 0.35 });
      io.observe(el);
    } catch (e) { fn(); }
  }

  function dropAttention() {
    var drop = D.getElementById('ocpq-drop');
    if (!drop || drop.getAttribute('data-ocb-attn') === '1') return;
    drop.setAttribute('data-ocb-attn', '1');

    function stop() { drop.classList.remove('ocb-breathe'); }

    inView(drop, function () {
      var gal = D.getElementById('ocpq-gallery');
      if (gal && !gal.hidden) return;
      drop.classList.add('ocb-breathe');
    });

    drop.addEventListener('click', stop);
    ['ocpq-browse', 'ocpq-camera'].forEach(function (id) {
      var b = D.getElementById(id);
      if (b) b.addEventListener('click', stop);
    });
    try {
      var gal2 = D.getElementById('ocpq-gallery');
      if (gal2) {
        new MutationObserver(function () { if (!gal2.hidden) stop(); })
          .observe(gal2, { attributes: true, attributeFilter: ['hidden'] });
      }
    } catch (e) {}
  }

  function submitAttention() {
    var reveal = D.getElementById('ocpq-reveal');
    var btn = D.getElementById('ocpq-submit');
    if (!reveal || !btn || reveal.getAttribute('data-ocb-attn') === '1') return;
    reveal.setAttribute('data-ocb-attn', '1');

    function sync() {
      if (!reveal.hidden && !btn.disabled) btn.classList.add('ocb-sheen');
      else btn.classList.remove('ocb-sheen');
    }
    sync();
    try {
      new MutationObserver(sync).observe(reveal, { attributes: true, attributeFilter: ['hidden'] });
      new MutationObserver(sync).observe(btn, { attributes: true, attributeFilter: ['disabled'] });
    } catch (e) {}
  }

  function bookAttention() {
    var card = D.querySelector('.ti-cal-card, .ci-book-cal');
    if (!card) {
      var cal = D.querySelector('.calendly-inline-widget');
      card = cal && cal.parentElement;
    }
    if (!card || card.getAttribute('data-ocb-attn') === '1') return;
    card.setAttribute('data-ocb-attn', '1');
    inView(card, function () {
      card.classList.add('ocb-ring');
      setTimeout(function () { card.classList.remove('ocb-ring'); }, 6500);
    });
  }

  // ---- wiring --------------------------------------------------------------
  function bind() {
    styles();
    try { watchDone(); } catch (e) {}
    try { dropAttention(); } catch (e) {}
    try { submitAttention(); } catch (e) {}
    try { bookAttention(); } catch (e) {}
  }

  function start() {
    bind();
    // The carpet and tile widgets render after load; the booking cards can be
    // injected later still. Watch for a bounded window, then stop.
    var tries = 0;
    var poll = setInterval(function () {
      bind();
      if (++tries > 40) clearInterval(poll);
    }, 500);
    try {
      var mo = new MutationObserver(function () { bind(); });
      mo.observe(D.body, { childList: true, subtree: true });
      setTimeout(function () { mo.disconnect(); }, 25000);
    } catch (e) {}
  }

  if (D.readyState === 'loading') D.addEventListener('DOMContentLoaded', start);
  else start();
})();
