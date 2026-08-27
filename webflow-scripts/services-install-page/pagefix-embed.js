(function(){
  /* ---------- 1. mobile slider enforcement (structure-aware) ---------- */
  var TRACK=['display','flex-direction','flex-wrap','justify-content','overflow-x','overflow-y','gap','scroll-snap-type','width','max-width'];
  var CARD=['flex','width','max-width','min-width','scroll-snap-align','box-sizing'];
  function imp(el,p,v){el.style.setProperty(p,v,'important');}
  function clr(el,list){for(var i=0;list.length>i;i++)el.style.removeProperty(list[i]);}
  function slide(wrapper,cards){
    if(!cards||!cards.length)return;
    var track=cards[0].parentElement;
    if(!track)return;
    var nested=wrapper&&track!==wrapper;
    if(767>=window.innerWidth){
      /* if the page's own script nested the cards in an inner track, neutralise the
         outer wrapper so the track itself spans the full width and card % math is right */
      if(nested){imp(wrapper,'display','block');imp(track,'width','100%');imp(track,'max-width','100%');}
      imp(track,'display','flex');imp(track,'flex-direction','row');imp(track,'flex-wrap','nowrap');
      imp(track,'justify-content','flex-start');imp(track,'overflow-x','auto');imp(track,'overflow-y','hidden');
      imp(track,'gap','14px');imp(track,'scroll-snap-type','x mandatory');
      for(var i=0;cards.length>i;i++){
        imp(cards[i],'flex','0 0 86%');imp(cards[i],'width','86%');
        imp(cards[i],'max-width','86%');imp(cards[i],'min-width','0');
        imp(cards[i],'scroll-snap-align','center');imp(cards[i],'box-sizing','border-box');
      }
    }else{
      clr(track,TRACK);
      if(nested)clr(wrapper,['display']);
      for(var j=0;cards.length>j;j++)clr(cards[j],CARD);
    }
  }
  function slidersRun(){
    var st=document.querySelector('.steps-content-wrapper.is-services');
    if(st)slide(st,st.querySelectorAll('.steps-inner-wrap'));
    var secs=document.querySelectorAll('.section_features');
    for(var k=0;secs.length>k;k++){
      var w=secs[k].querySelector('.services-wrap');
      if(w)slide(w,w.querySelectorAll('.services-item-wpapper'));
    }
  }

  /* ---------- 2. remove duplicate "Installation Across ... County" section ---------- */
  function T(e){return (e.textContent||'').replace(/\s+/g,' ');}
  function killAreas(){
    if(document.getElementById('oc-hia-gone'))return true;
    var all=document.body.querySelectorAll('h1,h2,h3,h4,div,p,span,strong,b'),hit=null,i,t;
    for(i=0;all.length>i;i++){
      t=T(all[i]);
      if(t.indexOf('Installation Across')===-1)continue;
      if(t.length>200)continue;
      if(!hit||T(hit).length>t.length)hit=all[i];
    }
    if(!hit)return false;
    var n=hit;
    while(n.parentElement&&n.parentElement!==document.body&&T(n).indexOf('Snohomish')===-1)n=n.parentElement;
    if(T(n).indexOf('Snohomish')===-1)return false;
    if(T(n).length>3000)return false;
    var m=document.createElement('span');m.id='oc-hia-gone';m.style.display='none';
    document.body.appendChild(m);
    n.parentNode.removeChild(n);
    return true;
  }

  function run(){slidersRun();killAreas();}
  run();
  window.addEventListener('resize',run);
  new MutationObserver(run).observe(document.body,{childList:true,subtree:true});
  var c=0,iv=setInterval(function(){run();if(++c>600)clearInterval(iv);},500);
})();
