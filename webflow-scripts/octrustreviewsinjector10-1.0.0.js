// Webflow registered inline script: OCTrustReviewsInjector10 (id octrustreviewsinjector10, v1.0.0)
// Applied site-wide in the footer on 2026-09-08. Replaces octrustreviewsinjector9d, which the
// Data API could no longer update (404) — the old script was removed from the site scripts list.
//
// Loads the Google-reviews trust section (oc-trust-reviews-v9d-min.js) on:
//   - every /hardwood-floor-refinishing-in-* city page (non-blog)
//   - /about-us, /our-work, /why-were-different
//   - NEW: /flooring-services-near-me/floor-refinishing (main refinishing service page)
//   - NEW: /arlington/hardwood-floor-refinishing (city page whose slug does not match the pattern)
// The two new paths were added so that every page carrying aggregateRating schema (4.7 / 99)
// also shows the reviews visibly, as Google's review-snippet guidelines require.
// The trailing fix() keeps the "Why Choose OC Flooring" block spaced below the injected section.
(function(){var p=location.pathname.replace(/\/+$/,''),city=/hardwood-floor-refinishing-in-/.test(p)&&!/\/blog\//.test(p),extra=['/about-us','/our-work','/why-were-different','/flooring-services-near-me/floor-refinishing','/arlington/hardwood-floor-refinishing'].indexOf(p)>=0;if(!city&&!extra)return;if(!document.getElementById('oc-trust-loader')){var s=document.createElement('script');s.id='oc-trust-loader';s.src='https://cdn.prod.website-files.com/6377e8e6a53936b48ef1cad0/6a34b7508360e1ed0c735ebf_oc-trust-reviews-v9d-min.js';s.defer=true;document.body.appendChild(s)}function fix(){var hs=document.querySelectorAll('h1,h2,h3,h4,h5,h6'),h=null;for(var i=0;i<hs.length;i++){var t=(hs[i].textContent||'').replace(/\s+/g,' ').trim().toUpperCase();if(t.indexOf('WHY CHOOSE OC FLOORING')===0){h=hs[i];break}}if(!h)return;var b=h;while(b.parentElement&&b.parentElement!==document.body&&((b.parentElement.textContent||'').toUpperCase().indexOf('WHY CHOOSE OC FLOORING')===0))b=b.parentElement;b.style.setProperty('margin-top',innerWidth<=600?'48px':'80px','important')}document.readyState==='loading'?document.addEventListener('DOMContentLoaded',fix,{once:true}):fix();addEventListener('resize',fix,{passive:true})})();
