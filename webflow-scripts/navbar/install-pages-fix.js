(function(){
  var P=location.pathname;
  if(P.indexOf('hardwood-floor-installation')===-1)return;
  function T(e){return (e.textContent||'').replace(/\s+/g,' ').trim();}
  function imp(el,p,v){el.style.setProperty(p,v,'important');}
  function clr(el,l){for(var i=0;l.length>i;i++)el.style.removeProperty(l[i]);}
  function smallestWith(rx,cap){
    var els=document.body.getElementsByTagName('*'),best=null,i,t;
    for(i=0;els.length>i;i++){
      t=T(els[i]);
      if(t.length>cap||!rx.test(t))continue;
      if(!best||T(best).length>t.length)best=els[i];
    }
    return best;
  }
  function ctaOne(bt){
    var anc=bt.parentElement,lvl=0,ph=null,a2,j;
    while(anc&&6>lvl){
      a2=anc.getElementsByTagName('a');
      for(j=0;a2.length>j;j++){if(T(a2[j]).indexOf('595-1079')!==-1){ph=a2[j];break;}}
      if(ph)break;
      anc=anc.parentElement;lvl++;
    }
    if(!ph||!anc||T(anc).length>600)return;
    var all=anc.getElementsByTagName('*'),k;
    if(767>=window.innerWidth){
      imp(anc,'display','block');imp(anc,'height','auto');imp(anc,'min-height','0');
      for(k=0;all.length>k;k++){imp(all[k],'position','static');imp(all[k],'float','none');imp(all[k],'transform','none');}
      imp(ph,'display','block');imp(ph,'width','auto');imp(ph,'max-width','92%');imp(ph,'margin','10px auto');imp(ph,'white-space','normal');
      imp(bt,'display','block');imp(bt,'width','auto');imp(bt,'max-width','92%');imp(bt,'margin','10px auto');imp(bt,'white-space','normal');
    }else{
      clr(anc,['display','height','min-height']);
      for(k=0;all.length>k;k++)clr(all[k],['position','float','transform']);
      clr(ph,['display','width','max-width','margin','white-space']);
      clr(bt,['display','width','max-width','margin','white-space']);
    }
  }
  function ctaFix(){
    var as=document.body.getElementsByTagName('a'),i,t,list=[];
    for(i=0;as.length>i;i++){t=T(as[i]);if(40>t.length&&t.indexOf('Free Estimate')!==-1)list.push(as[i]);}
    for(i=0;list.length>i;i++)ctaOne(list[i]);
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
    try{ctaFix();}catch(e){}
    try{killAreas();}catch(e){}
  }
  run();
  window.addEventListener('resize',run);
  new MutationObserver(run).observe(document.documentElement,{childList:true,subtree:true});
  var c=0,iv=setInterval(function(){run();if(++c>600)clearInterval(iv);},500);
})();
