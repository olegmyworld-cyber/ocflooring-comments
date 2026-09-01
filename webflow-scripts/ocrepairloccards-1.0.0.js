// OC Flooring — Webflow registered inline script: "ocRepairLocCards" (id: ocrepairloccards)
// Applied at: PAGE-level footer on all 30 hardwood-floor-repair pages (city pages +
// the Arlington-folder hardwood-floor-repair page).
//
// Purpose: on every city floor-repair page, the neighborhoods/history section
// (section[aria-labelledby="ocrp-loc"]) is 3+ long paragraphs of city-specific prose —
// a wall of text. This script restyles it in place, generically, whatever the city:
// each paragraph becomes a white card with a red icon tile (home / layers / map pin /
// droplet, cycling), stacked with soft shadows on the section's cream background —
// matching the card language used elsewhere on those pages and on the county hub's
// redesigned sections. Text is untouched; only presentation changes.
// The county hub page (/flooring-services-near-me/flooring-repair) is excluded by the
// path guard — its sections were rebuilt by hand in an embed.
(function(){
  if(location.pathname.indexOf('hardwood-floor-repair')<0)return;
  function f(){
    var w=document.querySelector('section[aria-labelledby="ocrp-loc"] .ocrp-prose');
    if(!w||w.getAttribute('data-ocx'))return;w.setAttribute('data-ocx','1');
    if(!document.getElementById('ocx-css')){
      var st=document.createElement('style');st.id='ocx-css';
      st.textContent='.ocrp-prose.ocx{display:grid;gap:18px}.ocx .ocxc{display:flex;gap:20px;align-items:flex-start;background:#fff;border:1px solid #e7e0d6;border-radius:18px;padding:24px 26px;box-shadow:0 10px 30px -20px rgba(12,31,63,.35)}.ocx .ocxi{width:46px;height:46px;flex:none;border-radius:14px;background:rgba(190,30,45,.09);color:#be1e2d;display:grid;place-items:center}.ocx .ocxi svg{width:24px;height:24px}.ocx .ocxc p{margin:0!important;max-width:none!important}@media(max-width:640px){.ocx .ocxc{flex-direction:column;gap:14px;padding:20px}}';
      document.head.appendChild(st);
    }
    var I=['<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/>',
           '<path d="M12 3l9 5-9 5-9-5 9-5z"/><path d="M3 13l9 5 9-5"/><path d="M3 17l9 5 9-5"/>',
           '<path d="M12 21s-7-5.6-7-11a7 7 0 0 1 14 0c0 5.4-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
           '<path d="M12 3s6 6.3 6 10.2a6 6 0 0 1-12 0C6 9.3 12 3 12 3z"/>'];
    w.classList.add('ocx');
    var ps=[].slice.call(w.children).filter(function(e){return e.tagName==='P'});
    ps.forEach(function(p,i){
      var c=document.createElement('div');c.className='ocxc';
      var ic=document.createElement('span');ic.className='ocxi';
      ic.innerHTML='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+I[i%I.length]+'</svg>';
      w.insertBefore(c,p);c.appendChild(ic);c.appendChild(p);
    });
  }
  f();document.addEventListener('DOMContentLoaded',f);window.addEventListener('load',f);setTimeout(f,600);
})();
