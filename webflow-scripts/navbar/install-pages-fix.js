(function(){
  var P=location.pathname;
  if(P.indexOf('hardwood-floor-installation')===-1)return;
  function T(e){return (e.textContent||'').replace(/\s+/g,' ').trim();}
  function imp(el,p,v){el.style.setProperty(p,v,'important');}
  function clr(el,l){for(var i=0;l.length>i;i++)el.style.removeProperty(l[i]);}
  var TRACK=['display','flex-direction','flex-wrap','justify-content','overflow-x','overflow-y','gap','scroll-snap-type','max-width'];
  var CARD=['flex','width','max-width','min-width','scroll-snap-align','box-sizing'];
  function cardRow(scope){
    var els=scope.getElementsByTagName('*'),best=null,bn=0,i,j;
    for(i=0;els.length>i;i++){
      var e=els[i],k=e.children,c=0;
      if(3>k.length)continue;
      for(j=0;k.length>j;j++){if((k[j].textContent||'').trim().length>15||k[j].querySelector('img'))c++;}
      if(c>=3&&c>bn){bn=c;best=e;}
    }
    return best;
  }
  function smallestWith(rx,cap){
    var els=document.body.getElementsByTagName('*'),best=null,i,t;
    for(i=0;els.length>i;i++){
      t=T(els[i]);
      if(t.length>cap||!rx.test(t))continue;
      if(!best||T(best).length>t.length)best=els[i];
    }
    return best;
  }
  function sectionRow(rx){
    var h=smallestWith(rx,140);
    if(!h)return null;
    var n=h,lvl=0;
    while(n&&6>lvl){
      var r=cardRow(n);
      if(r&&r!==h&&!h.contains(r))return r;
      n=n.parentElement;lvl++;
    }
    return null;
  }
  function applySlider(row){
    if(!row)return;
    var cards=row.children,i;
    if(767>=window.innerWidth){
      imp(row,'display','flex');imp(row,'flex-direction','row');imp(row,'flex-wrap','nowrap');
      imp(row,'justify-content','flex-start');imp(row,'overflow-x','auto');imp(row,'overflow-y','hidden');
      imp(row,'gap','14px');imp(row,'scroll-snap-type','x mandatory');imp(row,'max-width','100%');
      for(i=0;cards.length>i;i++){
        imp(cards[i],'flex','0 0 86%');imp(cards[i],'width','86%');imp(cards[i],'max-width','86%');
        imp(cards[i],'min-width','0');imp(cards[i],'box-sizing','border-box');imp(cards[i],'scroll-snap-align','center');
      }
    }else{
      clr(row,TRACK);
      for(i=0;cards.length>i;i++)clr(cards[i],CARD);
    }
  }
  function ctaFix(){
    var b=null,els=document.body.getElementsByTagName('*'),i,t;
    for(i=0;els.length>i;i++){
      t=T(els[i]);
      if(t.indexOf('595-1079')===-1||t.indexOf('Free Estimate')===-1||t.length>200)continue;
      if(!b||T(b).length>t.length)b=els[i];
    }
    if(!b)return;
    var k=b.children,j;
    if(767>=window.innerWidth){
      imp(b,'display','flex');imp(b,'flex-wrap','wrap');imp(b,'gap','10px');
      imp(b,'align-items','center');imp(b,'justify-content','center');
      for(j=0;k.length>j;j++){imp(k[j],'position','static');imp(k[j],'margin','0');imp(k[j],'max-width','100%');imp(k[j],'float','none');}
    }else{
      clr(b,['display','flex-wrap','gap','align-items','justify-content']);
      for(j=0;k.length>j;j++)clr(k[j],['position','margin','max-width','float']);
    }
  }
  function killAreas(){
    if(document.getElementById('oc-hia-gone'))return;
    var h=smallestWith(/Installation Across/i,200);
    if(!h)return;
    var n=h,lvl=0;
    while(n.parentElement&&n.parentElement!==document.body&&8>lvl&&8>n.getElementsByTagName('a').length){n=n.parentElement;lvl++;}
    if(8>n.getElementsByTagName('a').length)return;
    if(!n.contains(h)||T(n).length>4000)return;
    var m=document.createElement('span');m.id='oc-hia-gone';m.style.display='none';
    document.body.appendChild(m);
    n.parentNode.removeChild(n);
  }
  function run(){
    try{applySlider(sectionRow(/Flooring Types We Install/i));}catch(e){}
    try{applySlider(sectionRow(/Installation Methods/i));}catch(e){}
    try{applySlider(sectionRow(/Book a Free Estimate/i));}catch(e){}
    try{ctaFix();}catch(e){}
    try{killAreas();}catch(e){}
  }
  run();
  window.addEventListener('resize',run);
  new MutationObserver(run).observe(document.documentElement,{childList:true,subtree:true});
  var c=0,iv=setInterval(function(){run();if(++c>600)clearInterval(iv);},500);
})();
