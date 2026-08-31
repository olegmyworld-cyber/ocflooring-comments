/* OCMaxTracking 1.0.0 — comprehensive GA4 event tracking for nwocflooring.com
 * Applied via site footer freeform custom code. Sends events through gtag()
 * (GA4 G-P7TMG0E0JK) and dataLayer (GTM-PR94PQZW).
 * Events: oc_phone_click, oc_sms_click, oc_email_click, oc_calendly_click,
 * oc_cta_click, oc_form_submit, oc_outbound_click, oc_scroll (25/50/75/90),
 * oc_engaged (15s/60s/180s active time).
 */
(function(){
  function ev(n,p){
    p=p||{};p.page_path=location.pathname;
    try{if(typeof gtag==='function')gtag('event',n,p)}catch(e){}
    try{if(window.dataLayer){p.event=n;dataLayer.push(p)}}catch(e){}
  }
  // Clicks: phone / sms / email / calendly / CTA / outbound
  document.addEventListener('click',function(e){
    var a=e.target&&e.target.closest?e.target.closest('a'):null;if(!a||!a.href)return;
    var h=a.href,t=(a.textContent||'').trim().slice(0,80);
    if(h.indexOf('tel:')===0)ev('oc_phone_click',{link_text:t,number:h.slice(4)});
    else if(h.indexOf('sms:')===0)ev('oc_sms_click',{link_text:t});
    else if(h.indexOf('mailto:')===0)ev('oc_email_click',{link_text:t});
    else if(h.indexOf('calendly.com')>-1)ev('oc_calendly_click',{link_text:t});
    else if(a.hostname&&a.hostname!==location.hostname&&h.indexOf('http')===0)ev('oc_outbound_click',{link_url:h.slice(0,100)});
    else if(/button|btn|cta/i.test(a.className||''))ev('oc_cta_click',{link_text:t,link_url:a.pathname});
  },true);
  // Webflow form submissions
  document.addEventListener('submit',function(e){
    var f=e.target;if(!f||f.tagName!=='FORM')return;
    ev('oc_form_submit',{form_name:f.getAttribute('data-name')||f.getAttribute('name')||f.id||'form'});
    ev('generate_lead',{method:'website_form'});
  },true);
  // Scroll depth 25/50/75/90
  var marks={25:0,50:0,75:0,90:0};
  addEventListener('scroll',function(){
    var d=document.documentElement,m=d.scrollHeight-innerHeight;if(m<200)return;
    var p=Math.round((scrollY||d.scrollTop)/m*100);
    [25,50,75,90].forEach(function(k){if(p>=k&&!marks[k]){marks[k]=1;ev('oc_scroll',{percent:k})}});
  },{passive:true});
  // Active time on page: 15s / 60s / 180s (counts only while tab is visible)
  var act=0,sent={};
  setInterval(function(){
    if(document.hidden)return;act+=5;
    [15,60,180].forEach(function(k){if(act>=k&&!sent[k]){sent[k]=1;ev('oc_engaged',{seconds:k})}});
  },5000);
})();
