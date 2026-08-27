(function(){
  function apply(){
    var w=document.querySelector('.steps-content-wrapper.is-services');
    if(!w)return;
    var mobile=window.innerWidth<=767;
    var kids=w.querySelectorAll('.steps-inner-wrap');
    if(mobile){
      w.style.setProperty('display','flex','important');
      w.style.setProperty('flex-direction','row','important');
      w.style.setProperty('flex-wrap','nowrap','important');
      w.style.setProperty('overflow-x','auto','important');
      w.style.setProperty('gap','16px','important');
      for(var i=0;i<kids.length;i++){
        kids[i].style.setProperty('flex','0 0 86%','important');
        kids[i].style.setProperty('width','86%','important');
        kids[i].style.setProperty('max-width','86%','important');
        kids[i].style.setProperty('min-width','0','important');
      }
    }else{
      w.style.removeProperty('display');
      w.style.removeProperty('flex-direction');
      w.style.removeProperty('flex-wrap');
      w.style.removeProperty('overflow-x');
      w.style.removeProperty('gap');
      for(var j=0;j<kids.length;j++){
        kids[j].style.removeProperty('flex');
        kids[j].style.removeProperty('width');
        kids[j].style.removeProperty('max-width');
        kids[j].style.removeProperty('min-width');
      }
    }
  }
  apply();
  window.addEventListener('resize',apply);
  new MutationObserver(apply).observe(document.body,{childList:true,subtree:true});
  setInterval(apply,1000);
})();
