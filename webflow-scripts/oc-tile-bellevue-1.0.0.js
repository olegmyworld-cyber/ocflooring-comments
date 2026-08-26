// OC Flooring — tile installation city pages bundle: "ocTileBellevue" v1.0.0
// Pages: /city-of-*/tile-installation-in-<city>-wa (all tile city pages;
// built for Bellevue, page id 6a8f63898db417f9f6632e49, from the
// "Tile Installation Bellevue" Claude Design).
// What it does, in order:
//   1. gives .ti-page exact top clearance under the fixed site navbar;
//   2. injects the tile page styles the Designer API can't express
//      (Google-font families, hover states, media queries), the tile
//      estimator styles (te-*), and the #ocpq photo-quote widget styles;
//   3. renders the interactive tile cost estimator into #ti-estimator
//      (rates from the design: labor $11/sf, demo $3.50/sf, heated $13/sf,
//      waterproofing $9/sf, setting materials $1.90/sf, 12% waste, format
//      multipliers x1.00/x1.28/x1.55, tile tiers $3/$7/$14 per sf, job
//      minimums $3,200 shower / $900 bath floor / $1,100 backsplash,
//      high = low x1.22, rounded to $50); city name derives from the URL
//      slug tile-installation-in-<city>-wa;
//   4. drives the .ti-faq-item accordion (first item open);
//   5. injects the Calendly inline booking widget into #ti-cal-mount;
//   6. runs the #ocpq photo-quote widget (markup is server-rendered by the
//      page's HTML embed; submission is the same formsubmit.co multipart
//      POST as the carpet and repair pages, subject
//      "Photo quote - <City> - <Name> - <N> photos");
//   7. promotes the "Tile Installation Service Areas" slide to the front of
//      the shared Proudly Serving areas slider (parity with OCAreasStart).
// Uploaded as a Webflow asset; loaded by registered inline script
// "ocTileBellevue". Source of record: webflow-scripts/oc-tile-bellevue-1.0.0.js

(function(){
function fit(){var n=document.querySelector('.navbar'),w=document.querySelector('.ti-page');
if(!n||!w)return;var b=n.getBoundingClientRect().bottom;
if(b>40&&b<400)w.style.paddingTop=b+'px';}
fit();window.addEventListener('load',fit);window.addEventListener('resize',fit);setTimeout(fit,600);
})();
(function(){
if(document.getElementById('oc-tile-css'))return;
var st=document.createElement('style');st.id='oc-tile-css';
st.textContent=".ti-page{font-family:Archivo,Arial,sans-serif}\n.ti-h1,.ti-h2,.ti-h2-sm,.ti-band-p,.ti-stat-n,.ti-trust-score,.ti-card-h,.ti-card-price,.ti-mat-name,.ti-day-n,.ti-quote-p,.ti-faq-qt,.tg-title,.ti-cta-h,.ti-footer-name,.ti-layer-n{font-family:'Instrument Serif',Georgia,serif;font-weight:400}\n.ti-card-unit{font-family:Archivo,Arial,sans-serif}\n.ti-btn:hover{background-color:#1B3E3A;color:#FBFAF7}\n.ti-btn-ghost:hover{background-color:#16201E;color:#FBFAF7}\n.ti-btn-darkghost:hover{border-color:#FBFAF7;color:#FBFAF7}\n.ti-crumb:hover,.ti-outlink:hover,.ti-footer-a:hover{color:#1B3E3A}\n.ti-footer-a:hover{color:#FBFAF7}\n.tg-card:hover .tg-more{color:#1B3E3A}\n.ti-faq-q:hover .ti-faq-sign{border-color:#2E5D57}\n@media (min-width:600px){.ti-shot-wide{grid-column:span 2}}\n.ti-faq-item .ti-faq-a{display:none}\n.ti-faq-item[data-open=\"1\"] .ti-faq-a{display:block}\n#ti-cal-mount .calendly-inline-widget{min-width:320px;height:700px}\n#ti-estimator input[type=number]::-webkit-outer-spin-button,#ti-estimator input[type=number]::-webkit-inner-spin-button{-webkit-appearance:none;margin:0}\n#ti-estimator input[type=number]{appearance:textfield;-moz-appearance:textfield}\n.te-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr));gap:1px;background:#3A453F;border:1px solid #3A453F}\n.te-panel{background:#16201E;padding:clamp(20px,3vw,34px);min-width:0}\n.te-lab{font:600 10.5px/1 Archivo,Arial,sans-serif;letter-spacing:.16em;text-transform:uppercase;color:#8A9691}\n.te-picks{margin-top:16px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,150px),1fr));gap:10px}\n.te-picks3{margin-top:14px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,140px),1fr));gap:10px}\n.te-pick{position:relative;background:#0F1614;border:1px solid #3A453F;padding:16px 14px;cursor:pointer;text-align:left;font-family:inherit}\n.te-pick:hover{border-color:#C08B5C}\n.te-pick.on{background:#1B2724;border-color:#C08B5C}\n.te-pick-n{font:600 13.5px/1.25 Archivo,Arial,sans-serif;color:#FBFAF7}\n.te-pick-m{margin-top:7px;font:400 13px/1 'Instrument Serif',Georgia,serif;color:#C08B5C}\n.te-pick-s{margin-top:7px;font:400 11.5px/1.4 Archivo,Arial,sans-serif;color:#8A9691}\n.te-div{margin-top:30px;padding-top:26px;border-top:1px solid #3A453F}\n.te-2col{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,190px),1fr));gap:24px}\n.te-arearow{margin-top:14px;display:flex;align-items:center;gap:12px}\n.te-in{width:104px;background:#0F1614;border:1px solid #3A453F;color:#FBFAF7;padding:14px;font:500 15px/1 Archivo,Arial,sans-serif;text-align:center}\n.te-insuf{font:500 12px/1.4 Archivo,Arial,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#A8B3AD}\n.te-hint{margin-top:10px;font:400 12px/1.5 Archivo,Arial,sans-serif;color:#8A9691}\n.te-addons{margin-top:14px;display:flex;flex-direction:column;gap:12px}\n.te-chk{display:flex;align-items:flex-start;gap:11px;background:transparent;border:0;padding:0;cursor:pointer;text-align:left;font-family:inherit}\n.te-box{position:relative;width:19px;height:19px;flex-shrink:0;border:1px solid #4A554F;background:#0F1614;display:inline-block}\n.te-box i{position:absolute;top:3px;left:3px;right:3px;bottom:3px;background:#C08B5C;display:none}\n.te-chk.on .te-box i{display:block}\n.te-chktxt{font:500 13.5px/1.35 Archivo,Arial,sans-serif;color:#FBFAF7}\n.te-chktxt small{display:block;margin-top:3px;font-weight:400;font-size:11.5px;color:#8A9691}\n.te-sum{background:#FBFAF7;color:#16201E;padding:clamp(20px,3vw,34px);min-width:0}\n.te-sumlab{font:600 10.5px/1 Archivo,Arial,sans-serif;letter-spacing:.16em;text-transform:uppercase;color:#8F5230}\n.te-range{margin-top:18px;font:400 clamp(30px,3.8vw,44px)/1 'Instrument Serif',Georgia,serif;letter-spacing:-.01em;color:#16201E}\n.te-sumtxt{margin-top:12px;font:400 14.5px/1.55 Archivo,Arial,sans-serif;color:#5A655F}\n.te-lines{margin-top:26px;border-top:1px solid #16201E}\n.te-line{display:flex;justify-content:space-between;gap:16px;padding:13px 0;border-bottom:1px solid #E2DFD6;font:400 14px/1.4 Archivo,Arial,sans-serif;color:#5A655F}\n.te-line b{font-weight:600;color:#16201E;white-space:nowrap}\n.te-tip{margin-top:20px;background:#EDEBE4;border-left:2px solid #2E5D57;padding:16px 18px;font:400 13.5px/1.6 Archivo,Arial,sans-serif;color:#3A453F}\n.te-cta{margin-top:22px;display:block;text-align:center;background:#2E5D57;color:#FBFAF7;padding:18px 24px;font:600 13px/1 Archivo,Arial,sans-serif;letter-spacing:.12em;text-transform:uppercase;text-decoration:none}\n.te-cta:hover{background:#1B3E3A;color:#FBFAF7}\n.te-fine{margin:14px 0 0;font:400 12px/1.6 Archivo,Arial,sans-serif;color:#5A655F}\n#ocpq{background:#EDEBE4;padding:clamp(36px,6vw,84px) clamp(16px,4vw,48px);color:#16201E}\n#ocpq *{box-sizing:border-box}\n#ocpq [hidden]{display:none!important}\n#ocpq .ocpq-wrap{max-width:1060px;margin:0 auto;display:flex;flex-direction:column;gap:clamp(26px,4vw,40px)}\n#ocpq .ocpq-head{display:flex;flex-direction:column;gap:14px;max-width:740px}\n#ocpq .ocpq-eyebrow{display:flex;align-items:center;gap:10px;font-size:13px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#2E5D57}\n#ocpq .ocpq-eyebrow span{width:28px;height:2px;background:#2E5D57;display:block}\n#ocpq h2{font-family:'Instrument Serif',Georgia,serif;font-size:clamp(29px,5vw,50px);font-weight:400;line-height:1.06;letter-spacing:-.02em;margin:0;color:#16201E}\n#ocpq .ocpq-lead{font-size:clamp(16px,1.6vw,19px);line-height:1.6;color:#4A554F;margin:0;max-width:62ch}\n#ocpq .ocpq-card{background:#fff;border:1px solid #D5D2C8;border-radius:0;box-shadow:0 24px 48px -32px rgba(22,32,30,.35);padding:clamp(22px,3.4vw,40px);display:flex;flex-direction:column;gap:clamp(22px,3vw,30px)}\n#ocpq #ocpq-form{display:flex;flex-direction:column;gap:16px}\n#ocpq .ocpq-drop{border:2px dashed #D5D2C8;background:#FBFAF7;border-radius:0;padding:clamp(26px,5vw,52px) 20px;text-align:center;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:13px;transition:background .15s,border-color .15s}\n#ocpq .ocpq-drop.is-over{border-color:#2E5D57;background:#EEF2EF}\n#ocpq .ocpq-dropicon{width:58px;height:58px;border-radius:0;background:#E7E4DB;color:#2E5D57;display:grid;place-items:center}\n#ocpq .ocpq-dropicon svg{width:28px;height:28px}\n#ocpq .ocpq-droptitle{font-family:'Instrument Serif',Georgia,serif;font-size:clamp(18px,2.2vw,22px);font-weight:400}\n#ocpq .ocpq-dropsub{font-size:15px;color:#5A655F;line-height:1.5;max-width:46ch}\n#ocpq .ocpq-btnrow{display:flex;flex-wrap:wrap;gap:12px}\n#ocpq .ocpq-ghost{flex:1 1 210px;min-height:54px;border-radius:0;border:1.5px solid #D5D2C8;background:#fff;color:#16201E;font-weight:700;font-size:15px;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:9px;font-family:inherit;transition:background .15s,border-color .15s}\n#ocpq .ocpq-ghost:hover{background:#fbf6ee;border-color:#2E5D57}\n#ocpq .ocpq-ghost svg{width:18px;height:18px}\n#ocpq .ocpq-hint{display:flex;align-items:center;gap:9px;font-size:14.5px;color:#5A655F;line-height:1.5}\n#ocpq .ocpq-hint svg{width:16px;height:16px;color:#2E5D57;flex:0 0 auto}\n#ocpq .ocpq-galhead{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:12px}\n#ocpq .ocpq-count{font-weight:800;font-size:15px}\n#ocpq .ocpq-need{font-size:14px}\n#ocpq .ocpq-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(128px,1fr));gap:12px}\n#ocpq .ocpq-thumb{position:relative;border-radius:0;overflow:hidden;border:1px solid #D5D2C8;background:#EDEBE4;aspect-ratio:4/3}\n#ocpq .ocpq-thumb .img{width:100%;height:100%;background-size:cover;background-position:center}\n#ocpq .ocpq-thumb .rm{position:absolute;top:6px;right:6px;width:30px;height:30px;border-radius:50%;border:none;background:rgba(22,32,30,.72);color:#fff;cursor:pointer;display:grid;place-items:center}\n#ocpq .ocpq-thumb .rm:hover{background:#2E5D57}\n#ocpq .ocpq-thumb .rm svg{width:14px;height:14px}\n#ocpq .ocpq-thumb .nm{position:absolute;left:0;right:0;bottom:0;padding:14px 8px 6px;font-size:11px;color:#fff;background:linear-gradient(transparent,rgba(22,32,30,.8));white-space:nowrap;overflow:hidden;text-overflow:ellipsis}\n#ocpq .ocpq-working{font-size:14.5px;color:#5A655F;font-weight:600}\n#ocpq .ocpq-textarea{width:100%;min-height:120px;padding:14px 15px;border-radius:0;border:1.5px solid #D5D2C8;background:#FBFAF7;font-size:16px;line-height:1.55;color:#16201E;font-family:inherit;resize:vertical}\n#ocpq .ocpq-textarea:focus{outline:none;border-color:#2E5D57;background:#fff}\n#ocpq .ocpq-textarea::placeholder{color:#8A9691}\n#ocpq .ocpq-thumb.is-nopreview{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:7px;padding:10px;text-align:center;background:#EDEBE4}\n#ocpq .ocpq-thumb.is-nopreview svg{width:22px;height:22px;color:#8A9691}\n#ocpq .ocpq-thumb.is-nopreview .lbl{font-size:11px;color:#5A655F;line-height:1.3;word-break:break-word}\n#ocpq .ocpq-nopreview{font-size:13.5px;color:#5A655F;margin-top:10px;line-height:1.5}\n#ocpq .ocpq-err{color:#a32e19;font-size:14.5px;font-weight:600}\n#ocpq #ocpq-reveal{display:flex;flex-direction:column;gap:clamp(22px,3vw,28px);border-top:1px solid #efe6d7;padding-top:clamp(22px,3vw,28px);animation:ocpqReveal .32s ease both}\n@keyframes ocpqReveal{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}\n#ocpq .ocpq-block{display:flex;flex-direction:column;gap:12px}\n#ocpq .ocpq-blocktitle{font-family:'Instrument Serif',Georgia,serif;font-weight:400;font-size:clamp(17px,2vw,20px)}\n#ocpq .ocpq-blocksub{font-size:14.5px;color:#5A655F}\n#ocpq .ocpq-chips{display:flex;flex-wrap:wrap;gap:9px}\n#ocpq .ocpq-chip{min-height:48px;padding:0 18px;border-radius:0;cursor:pointer;font-weight:600;font-size:15px;background:#FBFAF7;border:1.5px solid #D5D2C8;color:#3A453F;font-family:inherit;transition:background .15s,border-color .15s}\n#ocpq .ocpq-chip[aria-pressed=\"true\"]{background:#DCE7E3;border-color:#2E5D57;color:#16201E}\n#ocpq .ocpq-fields{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px}\n#ocpq .ocpq-field{display:flex;flex-direction:column;gap:7px}\n#ocpq .ocpq-field span{font-weight:800;font-size:14px}\n#ocpq .ocpq-field input{width:100%;min-height:54px;padding:0 15px;border-radius:0;border:1.5px solid #D5D2C8;background:#FBFAF7;font-size:16px;color:#16201E;font-family:inherit}\n#ocpq .ocpq-field input:focus{outline:none;border-color:#2E5D57;background:#fff}\n#ocpq .ocpq-submitrow{display:flex;flex-wrap:wrap;align-items:center;gap:16px}\n#ocpq .ocpq-submit{min-height:58px;padding:0 32px;border-radius:0;border:none;background:#2E5D57;color:#fff;font-weight:800;font-size:17px;cursor:pointer;font-family:inherit;transition:background .15s}\n#ocpq .ocpq-submit:hover{background:#1B3E3A}\n#ocpq .ocpq-submit[disabled]{opacity:.65;cursor:default}\n#ocpq .ocpq-note{font-size:14px;color:#5A655F;line-height:1.5;max-width:40ch}\n#ocpq #ocpq-done{display:flex;flex-direction:column;gap:clamp(22px,3vw,30px)}\n#ocpq .ocpq-donetop{display:flex;align-items:flex-start;gap:15px}\n#ocpq .ocpq-check{width:46px;height:46px;border-radius:50%;background:#e7f0e3;color:#1f8a4c;display:grid;place-items:center;flex:0 0 auto}\n#ocpq .ocpq-check svg{width:23px;height:23px}\n#ocpq #ocpq-donehead{font-family:'Instrument Serif',Georgia,serif;font-size:clamp(21px,2.6vw,28px);font-weight:400;margin:0 0 6px}\n#ocpq #ocpq-donebody{margin:0;color:#4A554F;font-size:16px;line-height:1.55;max-width:58ch}\n#ocpq .ocpq-next{background:#16201E;border-radius:0;padding:clamp(22px,3vw,30px);color:#DDE3DF;display:flex;flex-direction:column;gap:16px}\n#ocpq .ocpq-nexttag{font-size:12px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#C08B5C}\n#ocpq .ocpq-step{display:flex;gap:14px;align-items:flex-start}\n#ocpq .ocpq-step>span{width:24px;height:24px;border-radius:50%;border:1.5px solid rgba(192,139,92,.55);display:grid;place-items:center;font-size:12px;font-weight:800;color:#C08B5C;flex:0 0 auto;margin-top:2px}\n#ocpq .ocpq-step b{display:block;font-weight:800;font-size:16px}\n#ocpq .ocpq-step i{display:block;font-style:normal;font-size:14.5px;color:#A8B3AD;line-height:1.55;max-width:56ch;margin-top:3px}\n#ocpq .ocpq-donebtns{display:flex;flex-wrap:wrap;gap:12px;align-items:center}\n#ocpq .ocpq-call{min-height:54px;padding:0 24px;border-radius:0;background:#16201E;color:#FBFAF7;font-weight:800;font-size:15px;text-decoration:none;display:inline-flex;align-items:center}\n#ocpq .ocpq-promise{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:clamp(16px,2.5vw,28px);border-top:1px solid #D5D2C8;padding-top:clamp(22px,3vw,32px)}\n#ocpq .ocpq-promise div{display:flex;flex-direction:column;gap:5px}\n#ocpq .ocpq-promise b{font-family:'Instrument Serif',Georgia,serif;font-weight:400;font-size:22px}\n#ocpq .ocpq-promise span{font-size:14.5px;color:#5A655F;line-height:1.5}";
document.head.appendChild(st);
})();
(function(){
var root=document.getElementById('ti-estimator');if(!root)return;
var CITYN=(function(){var seg=location.pathname.split('/').filter(Boolean).pop()||'';
var i=seg.indexOf('-in-');if(i>-1){var c=seg.slice(i+4);if(c.slice(-3)==='-wa')c=c.slice(0,-3);
if(c)return c.split('-').map(function(w){return w?w.charAt(0).toUpperCase()+w.slice(1):w}).join(' ')}
return 'local'})();
var LAB=11,DEMO=3.5,HEAT=13,WP=9,SET=1.9;
var SCOPES=[
{name:'Shower / tub surround',note:'Walls, floor, niche',area:110,hint:'Walls + shower floor. A standard alcove is ~110 sq ft.',prep:1.25,wp:true},
{name:'Bathroom floor',note:'Powder or full bath',area:45,hint:'Just the floor. A full bath is 40–60 sq ft.',prep:1,wp:false},
{name:'Kitchen / living floor',note:'Open runs, fewer cuts',area:320,hint:'Large open floor. Fewer cuts per sq ft than a bath.',prep:0.92,wp:false},
{name:'Backsplash',note:'Counter to cabinet',area:30,hint:'A typical kitchen run is 25–35 sq ft.',prep:1.35,wp:false}];
var FORMATS=[
{name:'12×12 to 12×24',mult:'×1.00',note:'The baseline. Fast, forgiving.',m:1},
{name:'Large format',mult:'×1.28',note:'24″+ or slab-look. Needs a flatter substrate.',m:1.28},
{name:'Mosaic / pattern',mult:'×1.55',note:'Sheets, herringbone, penny. Labor lives here.',m:1.55}];
var TIERS=[
{name:'Value',rate:'$3/sf',note:'Ceramic, builder porcelain',r:3},
{name:'Mid',rate:'$7/sf',note:'Good porcelain, glass mosaic',r:7},
{name:'High',rate:'$14/sf',note:'Stone, zellige, designer porcelain',r:14}];
var MINS=[3200,900,0,1100];
var TIPS=[
'Waterproofing is ~10% of a shower and prevents the one failure that costs five figures. It is never the line to cut.',
'Heated floor is only worth doing while this floor is open — retrofitting later means demoing what you just paid for.',
'On big open floors, ask about large format: fewer grout lines, less cleaning, and labor barely moves per sq ft.',
'Backsplash labor is all cuts and outlets. A simpler layout here buys you a better tile.'];
var S={scope:0,area:110,format:0,tier:1,demo:true,heated:false,wp:true};
function num(v){var x=parseFloat(v);return isFinite(x)&&x>0?x:0}
function money(v){return '$'+(Math.round(v/50)*50).toLocaleString('en-US')}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function render(){
var sc=SCOPES[S.scope],fmt=FORMATS[S.format],tier=TIERS[S.tier];
var area=num(S.area),order=Math.round(area*1.12);
var labor=area*LAB*fmt.m*sc.prep,mat=order*tier.r,setting=area*SET;
var demoCost=S.demo?area*DEMO:0;
var heatCost=S.heated&&S.scope!==0&&S.scope!==3?area*HEAT:0;
var wpCost=S.wp&&sc.wp?area*WP:0;
var minJob=MINS[S.scope],raw=labor+mat+setting+demoCost+heatCost+wpCost;
var low=Math.max(minJob,raw),high=low*1.22;
var lines=[
['Tile · '+order+' sq ft with waste',money(mat)],
['Setting labor · '+Math.round(area)+' sq ft '+fmt.mult,money(labor)],
['Thinset, grout, trim, membrane',money(setting)]];
if(wpCost>0)lines.push(['Bonded waterproofing + flood test',money(wpCost)]);
if(demoCost>0)lines.push(['Demo old tile + haul-away',money(demoCost)]);
if(heatCost>0)lines.push(['Electric heated floor + thermostat',money(heatCost)]);
if(minJob>raw)lines.push(['Job minimum · crew day, setup & trim',money(minJob-raw)]);
var h='<div class="te-grid"><div class="te-panel"><div class="te-lab">Scope</div><div class="te-picks">';
SCOPES.forEach(function(s,i){
h+='<button type="button" class="te-pick'+(S.scope===i?' on':'')+'" data-t="scope" data-i="'+i+'"><div class="te-pick-n">'+s.name+'</div><div class="te-pick-s">'+s.note+'</div></button>'});
h+='</div><div class="te-div te-2col"><div><div class="te-lab">Tiled area</div><div class="te-arearow">'
+'<input type="number" class="te-in" id="te-area" value="'+esc(S.area)+'" aria-label="Tiled area in square feet">'
+'<div class="te-insuf">sq ft</div></div><div class="te-hint">'+sc.hint+'</div></div>'
+'<div><div class="te-lab">Prep &amp; extras</div><div class="te-addons">'
+'<button type="button" class="te-chk'+(S.demo?' on':'')+'" data-t="demo"><span class="te-box"><i></i></span><span class="te-chktxt">Demo the old tile<small>$'+DEMO.toFixed(2)+'/sf incl. haul-away</small></span></button>'
+'<button type="button" class="te-chk'+(S.wp?' on':'')+'" data-t="wp"><span class="te-box"><i></i></span><span class="te-chktxt">Bonded waterproofing<small>'+(sc.wp?'Required on showers — we won’t skip it':'Not needed for this scope')+'</small></span></button>'
+'<button type="button" class="te-chk'+(S.heated?' on':'')+'" data-t="heated"><span class="te-box"><i></i></span><span class="te-chktxt">Heated floor<small>'+(S.scope===0||S.scope===3?'Floors only':'$'+HEAT+'/sf incl. thermostat')+'</small></span></button>'
+'</div></div></div>'
+'<div class="te-div"><div class="te-lab">Tile format — this is the labor lever</div><div class="te-picks3">';
FORMATS.forEach(function(f,i){
h+='<button type="button" class="te-pick'+(S.format===i?' on':'')+'" data-t="format" data-i="'+i+'"><div class="te-pick-n">'+f.name+'</div><div class="te-pick-m">'+f.mult+'</div><div class="te-pick-s">'+f.note+'</div></button>'});
h+='</div></div><div class="te-div"><div class="te-lab">Tile budget</div><div class="te-picks3">';
TIERS.forEach(function(t,i){
h+='<button type="button" class="te-pick'+(S.tier===i?' on':'')+'" data-t="tier" data-i="'+i+'"><div class="te-pick-n">'+t.name+'</div><div class="te-pick-m">'+t.rate+'</div><div class="te-pick-s">'+t.note+'</div></button>'});
h+='</div></div></div><div class="te-sum"><div class="te-sumlab">Your '+CITYN+' ballpark</div>'
+'<div class="te-range">'+(area>0?money(low)+' – '+money(high):'Enter an area')+'</div>'
+'<div class="te-sumtxt">'+Math.round(area)+' sq ft · '+order+' ordered with waste · '+tier.name.toLowerCase()+' tile · '+fmt.name.toLowerCase()+'</div>'
+'<div class="te-lines">';
lines.forEach(function(l){h+='<div class="te-line"><span>'+l[0]+'</span><b>'+l[1]+'</b></div>'});
h+='</div><div class="te-tip">'+TIPS[S.scope]+'</div>'
+'<a href="#book" class="te-cta">Book the free estimate</a>'
+'<p class="te-fine">Estimate only. Substrate repair, plumbing changes, curbless pans and stone fabrication change the real price — we measure and put it in writing at no charge.</p></div></div>';
root.innerHTML=h;
root.querySelectorAll('.te-pick').forEach(function(el){el.addEventListener('click',function(){
var t=el.dataset.t,i=+el.dataset.i;
if(t==='scope'){S.scope=i;S.area=SCOPES[i].area}else if(t==='format'){S.format=i}else{S.tier=i}
render()})});
var ai=root.querySelector('#te-area');if(ai)ai.addEventListener('change',function(){S.area=ai.value;render()});
root.querySelectorAll('.te-chk').forEach(function(el){el.addEventListener('click',function(){
var t=el.dataset.t;if(t==='demo')S.demo=!S.demo;else if(t==='wp')S.wp=!S.wp;else S.heated=!S.heated;
render()})});
}
render();
})();
(function(){
var items=document.querySelectorAll('.ti-faq-item');
function set(it,open){var s=it.querySelector('.ti-faq-sign');
if(s)s.textContent=open?'–':'+';it.setAttribute('data-open',open?'1':'0')}
items.forEach(function(it,i){set(it,i===0);
var q=it.querySelector('.ti-faq-q');if(!q)return;
q.addEventListener('click',function(){var was=it.getAttribute('data-open')==='1';
items.forEach(function(o){set(o,false)});if(!was)set(it,true)})});
})();
(function(){
var m=document.getElementById('ti-cal-mount');if(!m||m.dataset.init)return;m.dataset.init='1';
var URL='https://calendly.com/nwwillsflooring/free-in-home-estimate-online-today-clone-1?hide_gdpr_banner=1';
var el=document.createElement('div');el.className='calendly-inline-widget';el.setAttribute('data-url',URL);
m.appendChild(el);
if(!document.querySelector('script[src*="assets.calendly.com"]')){
var s=document.createElement('script');s.src='https://assets.calendly.com/assets/external/widget.js';s.async=true;
document.head.appendChild(s);}
var iv=setInterval(function(){
if(!window.Calendly||!window.Calendly.initInlineWidget)return;
if(el.querySelector('iframe')){clearInterval(iv);return}
window.Calendly.initInlineWidget({url:URL,parentElement:el});
clearInterval(iv);
},300);
setTimeout(function(){clearInterval(iv)},15000);
})();
// #ocpq photo-quote widget logic (markup server-rendered by the page's HTML embed)
(function(){
var D=document,root=D.getElementById('ocpq');if(!root||root.dataset.init)return;root.dataset.init='1';
var TOKEN='23b2e17e0ea51fa0ff449f9fc736414e';
var ACTION='https://formsubmit.co/'+TOKEN;
var INBOX='info.ocflooring@gmail.com';
var MAX=8,MIN=1,TIMEOUT=120000;
var HARD_TOTAL=9*1024*1024;
var photos=[],damage=[],busy=false;
function titleCase(s){return s.split('-').map(function(w){return w?w.charAt(0).toUpperCase()+w.slice(1):w}).join(' ')}
function cityName(){
var seg=location.pathname.split('/').filter(Boolean).pop()||'';
var i=seg.indexOf('-in-');
if(i>-1){var c=seg.slice(i+4);if(c.slice(-3)==='-wa')c=c.slice(0,-3);if(c)return titleCase(c)+', WA';}
var h=D.querySelector('h1');
if(h&&h.textContent){var t=h.textContent,j=t.toLowerCase().lastIndexOf(' in ');if(j>-1)return t.slice(j+4).trim();}
return seg?titleCase(seg):'Unknown page';
}
var CITY=cityName();
function $(id){return D.getElementById(id)}
var drop=$('ocpq-drop'),fileIn=$('ocpq-file'),camIn=$('ocpq-cam');
function encode(cv,q){return new Promise(function(res){try{cv.toBlob(res,'image/jpeg',q)}catch(e){res(null)}})}
function decodeOriented(file){
var first=Promise.reject();first.catch(function(){});
if(typeof createImageBitmap==='function'){
first=createImageBitmap(file,{imageOrientation:'from-image'})
.catch(function(e){if(e&&e.name==='TypeError'){return createImageBitmap(file)}throw e})
.then(function(b){return {d:b,free:function(){if(b.close)b.close()}}});
}
return first.catch(function(){
var url=URL.createObjectURL(file),free=function(){URL.revokeObjectURL(url)};
var img=new Image();img.decoding='async';img.src=url;
var ready=img.decode?img.decode():new Promise(function(ok,no){img.onload=ok;img.onerror=function(){no(new Error('load'))}});
return ready.then(function(){if(!img.naturalWidth){free();throw new Error('no pixels')}return {d:img,free:free}},function(e){free();throw e});
});
}
function canPreview(url){return new Promise(function(res){var im=new Image();im.onload=function(){res(true)};im.onerror=function(){res(false)};im.src=url})}
function isJpeg(t){t=String(t||'').toLowerCase();return t.indexOf('jpeg')>-1||t.indexOf('jpg')>-1}
function baseName(n){var i=String(n).lastIndexOf('.');return i>0?String(n).slice(0,i):String(n)}
function shrink(file,maxEdge,cap,retried){
maxEdge=maxEdge||2048;cap=cap||700*1024;var src=null;
if(!(file instanceof File)||String(file.type||'').toLowerCase().indexOf('image/')!==0)return Promise.resolve(file);
return decodeOriented(file).then(function(s){
src=s;var d=s.d,sw=d.width||d.naturalWidth,sh=d.height||d.naturalHeight;
if(!sw||!sh)throw new Error('no dims');
if(Math.max(sw,sh)<=maxEdge&&isJpeg(file.type)&&file.size<=cap)throw {keep:1};
var scale=Math.min(1,maxEdge/Math.max(sw,sh));
var tw=Math.max(1,Math.round(sw*scale)),th=Math.max(1,Math.round(sh*scale));
var AREA=16777216;
if(tw*th>AREA){var k=Math.sqrt(AREA/(tw*th));tw=Math.max(1,Math.floor(tw*k));th=Math.max(1,Math.floor(th*k))}
var cv=D.createElement('canvas');cv.width=tw;cv.height=th;
var ctx=cv.getContext('2d',{alpha:false});
if(!ctx)throw {keep:1};
ctx.fillStyle='#fff';ctx.fillRect(0,0,tw,th);
ctx.imageSmoothingEnabled=true;ctx.imageSmoothingQuality='high';
ctx.drawImage(d,0,0,tw,th);s.free();src=null;
var q=0.80;
return encode(cv,q).then(function step(b){
if(b&&b.size>cap&&q>0.55){q=Math.round((q-0.10)*100)/100;return encode(cv,q).then(step)}
return b;
}).then(function(b){
cv.width=cv.height=1;
if(!b||!b.size||b.type!=='image/jpeg')return file;
if(b.size>cap&&!retried&&maxEdge>1400)return shrink(file,1400,cap,true);
if(b.size>=file.size)return file;
return new File([b],baseName(file.name)+'.jpg',{type:'image/jpeg',lastModified:file.lastModified||Date.now()});
});
}).catch(function(){if(src&&src.free)src.free();return file});
}
function show(el,t){if(t!==undefined)el.textContent=t;el.hidden=false}
function hide(el){el.hidden=true}
function bytes(n){return n>=1048576?(n/1048576).toFixed(1)+' MB':Math.round(n/1024)+' KB'}
function totalBytes(){var t=0;photos.forEach(function(p){t+=p.file.size});return t}
function render(){
var n=photos.length;
$('ocpq-gallery').hidden=n===0;$('ocpq-reveal').hidden=n===0;$('ocpq-emptyhint').hidden=n>0;
$('ocpq-count').textContent=(n===1?'1 photo added':n+' photos added')+(n?' · '+bytes(totalBytes()):'');
var need=$('ocpq-need');
if(n>=3){need.textContent='Great — that is plenty to work from.';need.style.color='#1f8a4c'}
else{need.textContent='One or two more angles helps us price it faster.';need.style.color='#5A655F'}
var g=$('ocpq-thumbs');g.innerHTML='';
photos.forEach(function(p){
var d=D.createElement('div');d.className='ocpq-thumb';
var im=D.createElement('div');
if(p.ok===false){
d.className='ocpq-thumb is-nopreview';im.className='lbl';
im.innerHTML='<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3v5h5"/><path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h9l5 5v11a2 2 0 0 1-2 2Z"/></svg>';
var tl=D.createElement('div');tl.className='lbl';tl.textContent=p.name;im.appendChild(tl);
im.setAttribute('aria-label','Photo '+p.name+', no preview available in this browser. It will still be sent.');
}else{
im.className='img';im.setAttribute('role','img');
im.setAttribute('aria-label','Photo of your space: '+p.name);
im.style.backgroundImage='url("'+p.url+'")';
}
var rm=D.createElement('button');rm.type='button';rm.className='rm';
rm.setAttribute('aria-label','Remove photo '+p.name);
rm.innerHTML='<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg>';
rm.addEventListener('click',function(e){e.stopPropagation();if(busy)return;
URL.revokeObjectURL(p.url);photos=photos.filter(function(x){return x.id!==p.id});
hide($('ocpq-photoerr'));render()});
var nm=D.createElement('div');nm.className='nm';nm.textContent=p.name;
d.appendChild(im);d.appendChild(rm);
if(p.ok!==false)d.appendChild(nm);
g.appendChild(d);
});
var np=$('ocpq-nopreview'),blind=photos.filter(function(x){return x.ok===false}).length;
if(blind){np.textContent=blind===1?'One photo cannot be previewed in this browser (iPhone HEIC files often cannot). It will still be sent with your request.':blind+' photos cannot be previewed in this browser (iPhone HEIC files often cannot). They will still be sent with your request.';np.hidden=false}
else np.hidden=true;
}
function addFiles(list){
var files=Array.prototype.slice.call(list||[]);
if(!files.length||busy)return;
var room=MAX-photos.length,err='',ok=[];
files.forEach(function(f){
if(String(f.type||'').toLowerCase().indexOf('image/')!==0){err='Photos only, please — '+f.name+' is not an image.';return}
ok.push(f);
});
if(ok.length>room)err='Eight photos is the limit — we kept the first '+Math.max(room,0)+'.';
ok=ok.slice(0,Math.max(room,0));
if(!ok.length){if(err)show($('ocpq-photoerr'),err);drop.classList.remove('is-over');return}
busy=true;var st=$('ocpq-working');
show(st,'Preparing '+(ok.length===1?'your photo':ok.length+' photos')+'…');
var i=0;
(function next(){
if(i>=ok.length){
busy=false;hide(st);drop.classList.remove('is-over');
if(totalBytes()>HARD_TOTAL){
var over=[];
while(totalBytes()>HARD_TOTAL&&photos.length>MIN){var g=photos.pop();URL.revokeObjectURL(g.url);over.push(g.name)}
if(over.length)err='These were very large, so we kept the first '+photos.length+' photos.';
}
if(err)show($('ocpq-photoerr'),err);else hide($('ocpq-photoerr'));
render();return;
}
var f=ok[i++];st.textContent='Preparing photo '+i+' of '+ok.length+'…';
shrink(f).then(function(out){
var u=URL.createObjectURL(out);
canPreview(u).then(function(okPrev){
photos.push({id:String(Date.now())+'-'+String(i)+'-'+out.size,name:out.name,url:u,file:out,ok:okPrev});
render();next();
});
});
})();
}
drop.addEventListener('click',function(){if(!busy)fileIn.click()});
drop.addEventListener('keydown',function(e){if((e.key==='Enter'||e.key===' ')&&!busy){e.preventDefault();fileIn.click()}});
drop.addEventListener('dragover',function(e){e.preventDefault();drop.classList.add('is-over')});
drop.addEventListener('dragleave',function(){drop.classList.remove('is-over')});
drop.addEventListener('drop',function(e){e.preventDefault();addFiles(e.dataTransfer.files)});
$('ocpq-browse').addEventListener('click',function(){if(!busy)fileIn.click()});
$('ocpq-camera').addEventListener('click',function(){if(!busy)camIn.click()});
fileIn.addEventListener('change',function(e){addFiles(e.target.files);e.target.value=''});
camIn.addEventListener('change',function(e){addFiles(e.target.files);e.target.value=''});
Array.prototype.forEach.call(D.querySelectorAll('#ocpq .ocpq-chip'),function(b){
var label=b.textContent.trim();
b.addEventListener('click',function(){
var i=damage.indexOf(label);
if(i>-1){damage.splice(i,1);b.setAttribute('aria-pressed','false')}
else{damage.push(label);b.setAttribute('aria-pressed','true')}
hide($('ocpq-formerr'));
});
});
function digits(v){return String(v).replace(/[^0-9]/g,'')}
function fmtPhone(v){var d=digits(v);if(d.length===11&&d.charAt(0)==='1')d=d.slice(1);
return d.length===10?'('+d.slice(0,3)+') '+d.slice(3,6)+'-'+d.slice(6):String(v).trim()}
function emailOk(v){var at=v.indexOf('@');if(at<1)return false;var dom=v.slice(at+1);
if(dom.indexOf('@')>-1)return false;var dot=dom.lastIndexOf('.');
return dot>0&&dom.length-dot>2&&v.indexOf(' ')===-1}
function fail(el,msg,focusId){show(el,msg);
if(focusId){var f=$(focusId);if(f){try{f.focus({preventScroll:true})}catch(e){f.focus()}}}
el.scrollIntoView({block:'center',behavior:'smooth'})}
function hiddenIn(form,name,value){var i=D.createElement('input');i.type='hidden';i.name=name;i.value=value;form.appendChild(i)}
$('ocpq-submit').addEventListener('click',function(){
if(busy)return;
var name=$('ocpq-name').value.trim(),email=$('ocpq-email').value.trim(),phone=$('ocpq-phone').value.trim();
var fe=$('ocpq-formerr'),pe=$('ocpq-photoerr');
if(photos.length<MIN)return fail(pe,'Add at least one photo of the space so we can price it.');
if(!damage.length)return fail(fe,'Tell us what we are tiling — one tap.');
if(!name)return fail(fe,'We need a name to put on the quote.','ocpq-name');
if(!emailOk(email))return fail(fe,'That email address does not look right — the quote goes there.','ocpq-email');
if(digits(phone).length<10)return fail(fe,'A phone number lets us reach you if a photo is unclear.','ocpq-phone');
hide(fe);hide(pe);busy=true;
var btn=$('ocpq-submit');btn.disabled=true;btn.textContent='Sending your photos…';
var done=false;
var sink=D.createElement('iframe');
sink.name='ocpq-sink-'+Date.now();sink.style.display='none';
D.body.appendChild(sink);
var form=D.createElement('form');
form.method='POST';form.action=ACTION;form.enctype='multipart/form-data';
form.target=sink.name;form.style.display='none';
hiddenIn(form,'_next',location.origin+'/robots.txt');
hiddenIn(form,'_captcha','false');
hiddenIn(form,'_template','table');
hiddenIn(form,'_subject','Photo quote - '+CITY+' - '+name+' - '+photos.length+(photos.length===1?' photo':' photos'));
hiddenIn(form,'_replyto',email);
hiddenIn(form,'Name',name);
hiddenIn(form,'Email',email);
hiddenIn(form,'Phone',fmtPhone(phone));
hiddenIn(form,'Damage',damage.join(', '));
hiddenIn(form,'Details',($('ocpq-notes').value||'').trim()||'(none given)');
hiddenIn(form,'Photos',String(photos.length));
hiddenIn(form,'City',CITY);
hiddenIn(form,'Page',(D.title||'').split('|')[0].trim()||CITY);
hiddenIn(form,'Page URL',location.href.split('?')[0]);
photos.forEach(function(p,i){
var inp=D.createElement('input');inp.type='file';
inp.name=(i===0)?'attachment':('attachment'+(i+1));
var dt=new DataTransfer();dt.items.add(p.file);inp.files=dt.files;
form.appendChild(inp);
});
D.body.appendChild(form);
function cleanup(){try{form.remove()}catch(e){}setTimeout(function(){try{sink.remove()}catch(e){}},1000)}
function succeed(){
if(done)return;done=true;clearTimeout(timer);busy=false;cleanup();
photos.forEach(function(p){URL.revokeObjectURL(p.url)});
$('ocpq-form').hidden=true;$('ocpq-done').hidden=false;
$('ocpq-donehead').textContent='Got it, '+(name.split(' ')[0]||'thanks')+' — your photos are with our estimator.';
$('ocpq-donebody').textContent='Your written quote follows the same business day. If the photos leave anything unclear, we will call you at '+fmtPhone(phone)+' rather than guess.';
try{$('ocpq-donehead').setAttribute('tabindex','-1');$('ocpq-donehead').focus({preventScroll:true})}catch(e){}
$('ocpq-done').scrollIntoView({block:'start',behavior:'smooth'});
try{if(typeof window.gtag==='function')window.gtag('event','generate_lead',{method:'photo_quote',city:CITY})}catch(e){}
}
function stumble(msg){
if(done)return;done=true;clearTimeout(timer);busy=false;cleanup();
btn.disabled=false;btn.textContent='Send photos & get my quote';
fail(fe,msg);
try{if(typeof window.gtag==='function')window.gtag('event','form_error',{method:'photo_quote',city:CITY})}catch(e2){}
}
sink.addEventListener('load',function(){
var href=null;
try{href=sink.contentWindow.location.href}catch(e){href=null}
if(href&&href.indexOf(location.origin)===0)return succeed();
stumble('That did not go through, and we would rather tell you than lose it. Your photos are still here — press Send again, or email them to '+INBOX+'.');
});
var timer=setTimeout(function(){
stumble('That took too long to upload — usually a weak signal. Your photos are still here, so try Send again, ideally on Wi-Fi.');
},TIMEOUT);
form.submit();
});
$('ocpq-reset').addEventListener('click',function(){
photos.forEach(function(p){URL.revokeObjectURL(p.url)});
photos=[];damage=[];busy=false;
Array.prototype.forEach.call(D.querySelectorAll('#ocpq .ocpq-chip'),function(c){c.setAttribute('aria-pressed','false')});
$('ocpq-name').value='';$('ocpq-email').value='';$('ocpq-phone').value='';$('ocpq-notes').value='';
hide($('ocpq-photoerr'));hide($('ocpq-formerr'));hide($('ocpq-working'));
var btn=$('ocpq-submit');btn.disabled=false;btn.textContent='Send photos & get my quote';
$('ocpq-done').hidden=true;$('ocpq-form').hidden=false;render();
});
render();
})();
// Promote the Tile Installation slide in the shared areas slider (parity
// with the site's OCAreasStart, which handles the other service categories).
(function(){
function pick(){
var boxes=document.querySelectorAll('.areas-content-wrapper .content-box-area');
for(var i=0;i<boxes.length;i++){
var h=boxes[i].querySelector('.heading-area,h3');
if(h&&h.textContent.replace(/\s+/g,' ').trim().toLowerCase()==='tile installation service areas'){
var par=boxes[i].parentNode;
if(par&&par.firstElementChild!==boxes[i])par.insertBefore(boxes[i],par.firstElementChild);
return true}}
return false}
try{if(!pick()&&document.readyState==='loading')document.addEventListener('DOMContentLoaded',pick)}catch(e){}
})();
