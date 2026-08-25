// OC Flooring — hardwood floor repair page (Bellevue) icon layer v1.0.0
// Page: /city-of-bellevue/hardwood-floor-repair-in-bellevue-wa
// (page id 65fa27ec5d0c6abb2205947e). Uploaded as a Webflow asset; loaded by
// the registered inline script "ocRepairIcons" applied at the page footer.
//
// Adds the same decorative stroke-icon treatment as the carpet page's v1.7.0
// icon layer, in the repair page's own palette (tan chips, #be1e2d strokes):
// - camera inside every green "Upload Your Photos" pill (.ocbp-btn)
// - wrench / swap chips in the top-right of the "Repair it if / Refinish it
//   if" decision cards (.ocrf-card), tinted to each card's accent
// - the two quick-test text glyphs (water-drop and rug test) upgraded from
//   plain characters to matching stroke SVGs (.ocrf-ti)
// - a book icon on the "Flooring Guides & Answers" heading (.ocgd-h)
// The page's other icons (What-We-Repair cards, checklist bullets, FAQ +/-)
// already exist in the embeds. Purely decorative (aria-hidden), idempotent,
// try/catch-guarded: a failure leaves the page exactly as before.
(function(){
var P={"camera": "<rect x=\"2.5\" y=\"7\" width=\"19\" height=\"13.5\" rx=\"2\"/><path d=\"M8.3 7 9.7 4.2h4.6L15.7 7\"/><circle cx=\"12\" cy=\"13.6\" r=\"3.3\"/>", "wrench": "<path d=\"M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z\"/>", "swap": "<path d=\"M7 8.5h11\"/><path d=\"m14.8 5.3 3.2 3.2-3.2 3.2\"/><path d=\"M17 15.5H6\"/><path d=\"m9.2 12.3-3.2 3.2 3.2 3.2\"/>", "droplet": "<path d=\"M12 3.5c3.2 4.2 5.8 6.7 5.8 10a5.8 5.8 0 0 1-11.6 0c0-3.3 2.6-5.8 5.8-10Z\"/>", "sun": "<circle cx=\"12\" cy=\"12\" r=\"4\"/><path d=\"M12 2.8v2.4M12 18.8v2.4M2.8 12h2.4M18.8 12h2.4M5.5 5.5l1.7 1.7M16.8 16.8l1.7 1.7M18.5 5.5l-1.7 1.7M7.2 16.8l-1.7 1.7\"/>", "book": "<path d=\"M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5v14Z\"/><path d=\"M4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5\"/>"};
function svg(n){return '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'+P[n]+'</svg>'}
function chip(host,name,cls){
if(!host||!P[name])return;
for(var i=0;i<host.children.length;i++)if((' '+host.children[i].className+' ').indexOf(' ocxi ')>-1)return;
var s=document.createElement('span');s.className='ocxi'+(cls?' '+cls:'');
s.setAttribute('aria-hidden','true');s.innerHTML=svg(name);
host.insertBefore(s,host.firstChild)}
function all(sel){return Array.prototype.slice.call(document.querySelectorAll(sel))}
function deco(){
if(!document.getElementById('oc-repair-icons-css')){
var st=document.createElement('style');st.id='oc-repair-icons-css';
st.textContent=".ocxi{display:inline-grid;place-items:center;background:#f1e7d6;color:#be1e2d;border-radius:12px;width:40px;height:40px}\n.ocxi svg{width:20px;height:20px;display:block}\n.ocrf-card{position:relative}\n.ocxi-rf{position:absolute;top:20px;right:22px}\n.ocrf-card.is-green .ocxi-rf{background:#e7f0e3;color:#1f7a3c}\n.ocrf-card.is-red .ocxi-rf{background:#fbe7e9;color:#be1e2d}\n.ocxi-btn{width:auto;height:auto;background:transparent;color:inherit;border-radius:0;margin-right:9px;vertical-align:-4px}\n.ocxi-btn svg{width:18px;height:18px}\n.ocxi-inl{width:30px;height:30px;border-radius:9px;margin-right:10px;vertical-align:-7px}\n.ocxi-inl svg{width:17px;height:17px}\n.ocrf-ti{display:inline-block}\n.ocrf-ti svg{width:20px;height:20px;display:block;margin-top:2px}";
document.head.appendChild(st)}
all('.ocbp-btn').forEach(function(a){chip(a,'camera','ocxi-btn')});
all('.ocrf-card').forEach(function(c){
var red=(' '+c.className+' ').indexOf(' is-red ')>-1;
chip(c,red?'swap':'wrench','ocxi-rf')});
all('.ocrf-ti').forEach(function(s){
if(s.querySelector('svg'))return;
var t=((s.parentNode&&s.parentNode.textContent)||'').toLowerCase();
s.innerHTML=svg(/water/.test(t)?'droplet':'sun')});
chip(document.querySelector('.ocgd-h'),'book','ocxi-inl');
}
function run(){try{deco()}catch(e){}}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',run);else run();
window.addEventListener('load',run);setTimeout(run,600);
})();
