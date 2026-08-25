// OC Flooring — carpet installation page bundle: "ocCarpetBellevue" v1.2.0
// Page: /city-of-bellevue/carpet-installation-in-bellevue-wa (page id 6a8ccb1ebf28596111eed9f2)
// Renders the interactive cost estimator into #ci-estimator, drives the FAQ accordion,
// and injects the estimator styles (see v1.1.0 note below).
// Uploaded as a Webflow asset; loaded by the registered inline script "occarpetbellevue".
// The estimator styles ride inside the bundle (page-level head custom
// code proved unreliable through the API), injected once at load.
// v1.2.0: the site navbar is position:fixed, so give the page wrapper exact
// top clearance by measuring the navbar (incl. its announcement sub-line).
(function(){
function fit(){var n=document.querySelector('.navbar'),w=document.querySelector('.ci-page');
if(!n||!w)return;var b=n.getBoundingClientRect().bottom;
if(b>40&&b<400)w.style.paddingTop=b+'px';}
fit();window.addEventListener('load',fit);window.addEventListener('resize',fit);setTimeout(fit,600);
})();
(function(){
if(document.getElementById('oc-carpet-css'))return;
var st=document.createElement('style');st.id='oc-carpet-css';
st.textContent="#ci-estimator{margin-top:42px}\n.es-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr));gap:26px;align-items:start}\n.es-panel{background:#3A322D;border-radius:22px;padding:clamp(18px,4vw,32px);min-width:0}\n.es-lab{font:600 12.5px/1 'Hanken Grotesk',Arial,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:#B0A29A}\n.es-rows{margin-top:18px;display:flex;flex-direction:column;gap:14px}\n.es-row{display:flex;flex-wrap:wrap;align-items:center;gap:8px 14px;min-width:0}\n.es-rowname{flex:1 1 100%;min-width:0;font:500 15.5px/1.3 'Hanken Grotesk',Arial,sans-serif;color:#fff}\n.es-flex{flex:1 1 auto;display:flex;flex-wrap:nowrap;align-items:center;gap:8px;min-width:0}\n.es-in{flex:1 1 60px;min-width:0;background:#2E2724;border:1px solid #554942;color:#fff;border-radius:12px;padding:13px 6px;font:500 15px/1 'Hanken Grotesk',Arial,sans-serif;text-align:center}\n.es-x{flex:0 0 auto;font:400 13px/1 'Hanken Grotesk',Arial,sans-serif;color:#B0A29A}\n.es-sf{flex:1 1 auto;min-width:0;font:500 14px/1 'Hanken Grotesk',Arial,sans-serif;color:#CFC3B8;text-align:right;white-space:nowrap;overflow:hidden}\n.es-rm{flex:0 0 34px;background:transparent;border:1px solid #554942;color:#CFC3B8;border-radius:999px;padding:9px 0;cursor:pointer;font:500 15px/1 'Hanken Grotesk',Arial,sans-serif}\n.es-rm:hover{border-color:#D8A99A;color:#D8A99A}\n.es-note{margin-top:12px;font:400 12.5px/1.5 'Hanken Grotesk',Arial,sans-serif;color:#B0A29A}\n.es-add{margin-top:16px;background:transparent;border:1px dashed #554942;color:#fff;border-radius:999px;padding:13px 22px;cursor:pointer;font:600 14.5px/1 'Hanken Grotesk',Arial,sans-serif}\n.es-add:hover{border-color:#D8A99A;color:#D8A99A}\n.es-div{margin-top:30px;padding-top:26px;border-top:1px solid #4A403A}\n.es-2col{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,210px),1fr));gap:26px}\n.es-strow{margin-top:14px;display:flex;align-items:center;gap:12px}\n.es-stin{width:92px;background:#2E2724;border:1px solid #554942;color:#fff;border-radius:12px;padding:13px;font:500 15px/1 'Hanken Grotesk',Arial,sans-serif;text-align:center}\n.es-sttxt{font:500 14.5px/1.4 'Hanken Grotesk',Arial,sans-serif;color:#CFC3B8}\n.es-sttxt small{color:#B0A29A;font-weight:400;font-size:12.5px}\n.es-addons{margin-top:14px;display:flex;flex-direction:column;gap:11px}\n.es-chk{display:flex;align-items:center;gap:11px;background:transparent;border:0;padding:0;cursor:pointer;text-align:left}\n.es-box{position:relative;width:21px;height:21px;flex-shrink:0;border:1px solid #554942;border-radius:7px;background:#2E2724;display:inline-block}\n.es-box i{position:absolute;top:3px;left:3px;right:3px;bottom:3px;background:#D8A99A;border-radius:4px;display:none}\n.es-chk.on .es-box i{display:block}\n.es-chktxt{font:500 14.5px/1.35 'Hanken Grotesk',Arial,sans-serif;color:#fff}\n.es-tiers{margin-top:14px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,145px),1fr));gap:12px}\n.es-tier{background:#2E2724;border:1px solid #554942;border-radius:16px;padding:18px 16px;cursor:pointer;text-align:left}\n.es-tier:hover{border-color:#B0A29A}\n.es-tier.on{border-color:#D8A99A;box-shadow:inset 0 0 0 1px #D8A99A}\n.es-tname{font:600 15.5px/1 'Hanken Grotesk',Arial,sans-serif;color:#fff}\n.es-trate{margin-top:8px;font:400 15px/1 Newsreader,Georgia,serif;color:#D8A99A}\n.es-tnote{margin-top:8px;font:400 12.5px/1.45 'Hanken Grotesk',Arial,sans-serif;color:#B0A29A}\n.es-sum{background:#FFFDFA;color:#332D28;border-radius:22px;padding:clamp(20px,4vw,34px);min-width:0;position:sticky;top:96px;box-shadow:0 20px 50px rgba(0,0,0,.18)}\n.es-sumlab{font:600 12.5px/1 'Hanken Grotesk',Arial,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:#8F4F3C}\n.es-range{margin-top:16px;font:400 clamp(32px,4vw,46px)/1.05 Newsreader,Georgia,serif;letter-spacing:-.01em;color:#2E2724}\n.es-sumtxt{margin-top:12px;font:400 15px/1.55 'Hanken Grotesk',Arial,sans-serif;color:#6E635B}\n.es-lines{margin-top:24px;padding-top:22px;border-top:1px solid #EDE4DA;display:flex;flex-direction:column;gap:11px}\n.es-line{display:flex;justify-content:space-between;gap:16px;font:400 14.5px/1.5 'Hanken Grotesk',Arial,sans-serif;color:#6E635B}\n.es-line b{font-weight:600;color:#332D28;white-space:nowrap}\n.es-cta{margin-top:26px;display:block;text-align:center;background:#C0392F;color:#fff;padding:18px 24px;border-radius:999px;font:600 16.5px/1 'Hanken Grotesk',Arial,sans-serif;box-shadow:0 10px 24px rgba(192,57,47,.22);text-decoration:none}\n.es-cta:hover{background:#A32F26;color:#fff}\n#ci-estimator input[type=number]::-webkit-outer-spin-button,#ci-estimator input[type=number]::-webkit-inner-spin-button{-webkit-appearance:none;margin:0}\n#ci-estimator input[type=number]{appearance:textfield;-moz-appearance:textfield}\n.es-fine{margin:16px 0 0;font:400 12.5px/1.6 'Hanken Grotesk',Arial,sans-serif;color:#6E635B}";
document.head.appendChild(st);
})();
(function(){
var root=document.getElementById('ci-estimator');if(!root)return;
var MAT=[1.99,2.79,3.79],TN=['Good','Better','Best'],
TT=['Rentals, basements, level loop','Most homes — soft, warrantied','Wool, pet-proof, thick plush'],
LAB=1.49,STAIR=18,HAUL=0.5,PAD=0.65;
var S={rooms:[{l:13,w:12},{l:11,w:11},{l:10,w:10}],stairs:13,tier:1,haul:true,pet:false};
function num(v){var x=parseFloat(v);return isFinite(x)&&x>0?x:0}
function money(v){return '$'+(Math.round(v/25)*25).toLocaleString('en-US')}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function render(){
var floor=S.rooms.reduce(function(t,r){return t+num(r.l)*num(r.w)},0);
var order=Math.round(floor*1.1),steps=Math.max(0,Math.round(num(S.stairs)));
var mat=order*MAT[S.tier],lab=floor*LAB,st=steps*STAIR,haul=S.haul?floor*HAUL:0,pad=S.pet?order*PAD:0;
var low=mat+lab+st+haul+pad,high=low*1.18;
var lines=[['Carpet + pad · '+order+' sq ft ordered',money(mat)],['Installation labor · '+Math.round(floor)+' sq ft',money(lab)]];
if(steps>0)lines.push(['Stairs · '+steps+' steps',money(st)]);
if(S.haul)lines.push(['Old carpet removal & dump',money(haul)]);
if(S.pet)lines.push(['Pet moisture-barrier pad',money(pad)]);
var h='<div class="es-grid"><div class="es-panel"><div class="es-lab">Rooms</div><div class="es-rows">';
S.rooms.forEach(function(r,i){
h+='<div class="es-row"><div class="es-rowname">'+(i===0?'Living room':'Room '+(i+1))+'</div><div class="es-flex">'
+'<input type="number" class="es-in" data-k="l" data-i="'+i+'" value="'+esc(r.l)+'" aria-label="Room length in feet">'
+'<div class="es-x">ft ×</div>'
+'<input type="number" class="es-in" data-k="w" data-i="'+i+'" value="'+esc(r.w)+'" aria-label="Room width in feet">'
+'<div class="es-x">ft</div><div class="es-sf">'+Math.round(num(r.l)*num(r.w))+' sf</div>'
+'<button type="button" class="es-rm" data-i="'+i+'" aria-label="Remove room">×</button></div></div>'});
h+='</div><div class="es-note">Length × width in feet. Closets and hallways count — add them as their own row.</div>'
+'<button type="button" class="es-add">+ Add a room</button>'
+'<div class="es-div es-2col"><div><div class="es-lab">Stairs</div><div class="es-strow">'
+'<input type="number" class="es-stin" id="es-stairs" value="'+esc(S.stairs)+'" aria-label="Number of steps">'
+'<div class="es-sttxt">steps<br><small>count the landing as one</small></div></div></div>'
+'<div><div class="es-lab">Add-ons</div><div class="es-addons">'
+'<button type="button" class="es-chk'+(S.haul?' on':'')+'" data-t="haul"><span class="es-box"><i></i></span><span class="es-chktxt">Haul the old carpet away</span></button>'
+'<button type="button" class="es-chk'+(S.pet?' on':'')+'" data-t="pet"><span class="es-box"><i></i></span><span class="es-chktxt">Pet moisture-barrier pad</span></button>'
+'</div></div></div>'
+'<div class="es-div"><div class="es-lab">Carpet grade</div><div class="es-tiers">';
TN.forEach(function(t,i){
h+='<button type="button" class="es-tier'+(S.tier===i?' on':'')+'" data-i="'+i+'"><div class="es-tname">'+t+'</div><div class="es-trate">$'+MAT[i].toFixed(2)+'/sf</div><div class="es-tnote">'+TT[i]+'</div></button>'});
h+='</div></div></div><div class="es-sum"><div class="es-sumlab">Your Bellevue ballpark</div>'
+'<div class="es-range">'+(floor>0?money(low)+' – '+money(high):'Add a room')+'</div>'
+'<div class="es-sumtxt">'+Math.round(floor)+' sq ft of floor · '+order+' sq ft ordered with waste · '+steps+' steps</div>'
+'<div class="es-lines">';
lines.forEach(function(l){h+='<div class="es-line"><span>'+l[0]+'</span><b>'+l[1]+'</b></div>'});
h+='</div><a href="/contact" class="es-cta">Book the free measure</a>'
+'<p class="es-fine">Estimate only. Stairs, subfloor repairs, transitions and furniture change the real price — we measure and put it in writing at no charge.</p></div></div>';
root.innerHTML=h;
root.querySelectorAll('.es-in').forEach(function(el){el.addEventListener('change',function(){S.rooms[+el.dataset.i][el.dataset.k]=el.value;render()})});
root.querySelectorAll('.es-rm').forEach(function(el){el.addEventListener('click',function(){if(S.rooms.length>1){S.rooms.splice(+el.dataset.i,1);render()}})});
var add=root.querySelector('.es-add');if(add)add.addEventListener('click',function(){S.rooms.push({l:10,w:10});render()});
var si=root.querySelector('#es-stairs');if(si)si.addEventListener('change',function(){S.stairs=si.value;render()});
root.querySelectorAll('.es-chk').forEach(function(el){el.addEventListener('click',function(){if(el.dataset.t==='haul')S.haul=!S.haul;else S.pet=!S.pet;render()})});
root.querySelectorAll('.es-tier').forEach(function(el){el.addEventListener('click',function(){S.tier=+el.dataset.i;render()})});
}
render();
})();
(function(){
var items=document.querySelectorAll('.ci-faq-item');
function set(it,open){var a=it.querySelector('.ci-faq-a'),s=it.querySelector('.ci-faq-sign');
if(a)a.style.display=open?'block':'none';if(s)s.textContent=open?'–':'+';it.setAttribute('data-open',open?'1':'0')}
items.forEach(function(it,i){set(it,i===0);
var q=it.querySelector('.ci-faq-q');if(!q)return;
q.addEventListener('click',function(){var was=it.getAttribute('data-open')==='1';
items.forEach(function(o){set(o,false)});if(!was)set(it,true)})});
})();
