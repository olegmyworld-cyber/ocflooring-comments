/* ocBlogDates 1.0.0 — turns the "Month D, YYYY · " prefix on blog-card
   summaries into a green date pill (matches the in-article date badge).
   Idempotent; re-runs via MutationObserver for injected cards. */
(function(){
  var M='January|February|March|April|May|June|July|August|September|October|November|December';
  var re=new RegExp('^('+M+')\\s\\d{1,2},\\s\\d{4}\\s*·\\s*');
  function go(){try{
    var els=document.querySelectorAll('p,div');
    for(var i=0;i<els.length;i++){
      var el=els[i];
      if(el.children.length>0||el.getAttribute('data-ocdate'))continue;
      var t=el.textContent||'';
      var m=t.match(re);
      if(!m)continue;
      el.setAttribute('data-ocdate','1');
      var date=m[0].replace(/\s*·\s*$/,'');
      el.textContent=t.slice(m[0].length);
      var b=document.createElement('div');
      b.setAttribute('data-ocdate','1');
      b.style.cssText='margin:0 0 10px';
      var s=document.createElement('span');
      s.textContent=date;
      s.style.cssText='display:inline-block;background:#16a34a;color:#fff;border-radius:999px;padding:4px 13px;font-size:12.5px;font-weight:800;letter-spacing:.01em;line-height:1.5';
      b.appendChild(s);
      el.parentNode.insertBefore(b,el);
    }
  }catch(e){}}
  var w;
  function arm(){go();
    try{
      var mo=new MutationObserver(function(){clearTimeout(w);w=setTimeout(go,150)});
      mo.observe(document.body,{childList:true,subtree:true});
    }catch(e){}
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',arm);else arm();
})();
