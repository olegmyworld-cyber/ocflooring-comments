// OC Flooring — carpet installation page bundle: "ocCarpetBellevue" v1.0.0
// Page: /city-of-bellevue/carpet-installation-in-bellevue-wa (page id 6a8ccb1ebf28596111eed9f2)
// Renders the interactive cost estimator into #ci-estimator and drives the FAQ accordion.
// Uploaded as a Webflow asset; loaded by the registered inline script "occarpetbellevue".
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
