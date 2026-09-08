/* OCMouseflowLoader 1.1.0 — bot-filtered Mouseflow loader (site head custom code).
 * Website ID 0c356f71-0798-49b6-95e1-59d767833639. Guards, in order:
 * 1. navigator.webdriver → skip (automated browsers)
 * 2. known crawler/tool user agents → skip
 * 3. timezone must be America/* or Pacific/Honolulu (customers are Puget Sound local;
 *    overseas data-center bots are excluded)
 * 4. loads only on first real interaction (mousemove/touch/scroll/key) — crawlers
 *    that never interact consume zero Mouseflow session quota
 */
(function(){try{if(navigator.webdriver)return;var ua=navigator.userAgent||'';if(/bot|crawl|spider|headless|lighthouse|slurp|preview|python|curl|wget|gptbot|oai-|claudebot|bingbot|petalbot|ahrefs|semrush|scrapy|phantom|selenium/i.test(ua))return;var tz='';try{tz=Intl.DateTimeFormat().resolvedOptions().timeZone||''}catch(e){}if(tz.indexOf('America/')!==0&&tz!=='Pacific/Honolulu')return;var loaded=false;function load(){if(loaded)return;loaded=true;window._mfq=window._mfq||[];var mf=document.createElement('script');mf.type='text/javascript';mf.defer=true;mf.src='//cdn.mouseflow.com/projects/0c356f71-0798-49b6-95e1-59d767833639.js';document.head.appendChild(mf)}['mousemove','touchstart','scroll','keydown'].forEach(function(ev){addEventListener(ev,load,{once:true,passive:true})})}catch(e){}})();
