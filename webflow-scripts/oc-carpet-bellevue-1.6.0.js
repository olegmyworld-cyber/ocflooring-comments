// OC Flooring — carpet installation page bundle: "ocCarpetBellevue" v1.6.0
// Page: /city-of-bellevue/carpet-installation-in-bellevue-wa (page id 6a8ccb1ebf28596111eed9f2)
// Renders the interactive cost estimator into #ci-estimator, drives the FAQ accordion,
// and injects the estimator styles (see v1.1.0 note below).
// Uploaded as a Webflow asset; loaded by the registered inline script "occarpetbellevue".
// The estimator styles ride inside the bundle (page-level head custom
// code proved unreliable through the API), injected once at load.
// v1.2.0: the site navbar is position:fixed, so give the page wrapper exact
// top clearance by measuring the navbar (incl. its announcement sub-line).
// v1.5.0: the photo-quote form is rebuilt at runtime into the same design as
// the repair page's photo uploader (photo drop-tiles, chips, labeled field
// grid, promise row) while keeping the native Webflow form underneath, and
// the hook band moved to the page's natural cream palette (styles updated in
// the Designer; no red background).
// v1.5.1: 'New carpet installation' removed from the project-type chips.
// v1.6.0: the native-Webflow-form uploader is replaced by the SAME photo-quote
// widget the hardwood floor-repair pages use (#ocpq): identical design (CSS
// from the shared Footer component embed), identical submission — multipart
// POST to formsubmit.co -> info.ocflooring@gmail.com, _template=table,
// subject "Photo quote - <City> - <Name> - <N> photos" — with carpet wording.
// The bundle injects the styles, renders the section before the final CTA,
// and runs the widget logic. Source of record for the widget:
// webflow-scripts/carpet-ocpq-embed-1.0.0.html in the repo.
(function(){
function fit(){var n=document.querySelector('.navbar'),w=document.querySelector('.ci-page');
if(!n||!w)return;var b=n.getBoundingClientRect().bottom;
if(b>40&&b<400)w.style.paddingTop=b+'px';}
fit();window.addEventListener('load',fit);window.addEventListener('resize',fit);setTimeout(fit,600);
})();
(function(){
if(document.getElementById('oc-carpet-css'))return;
var st=document.createElement('style');st.id='oc-carpet-css';
st.textContent="#ci-estimator{margin-top:42px}\n.es-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr));gap:26px;align-items:start}\n.es-panel{background:#3A322D;border-radius:22px;padding:clamp(18px,4vw,32px);min-width:0}\n.es-lab{font:600 12.5px/1 'Hanken Grotesk',Arial,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:#B0A29A}\n.es-rows{margin-top:18px;display:flex;flex-direction:column;gap:14px}\n.es-row{display:flex;flex-wrap:wrap;align-items:center;gap:8px 14px;min-width:0}\n.es-rowname{flex:1 1 100%;min-width:0;font:500 15.5px/1.3 'Hanken Grotesk',Arial,sans-serif;color:#fff}\n.es-flex{flex:1 1 auto;display:flex;flex-wrap:nowrap;align-items:center;gap:8px;min-width:0}\n.es-in{flex:1 1 60px;min-width:0;background:#2E2724;border:1px solid #554942;color:#fff;border-radius:12px;padding:13px 6px;font:500 15px/1 'Hanken Grotesk',Arial,sans-serif;text-align:center}\n.es-x{flex:0 0 auto;font:400 13px/1 'Hanken Grotesk',Arial,sans-serif;color:#B0A29A}\n.es-sf{flex:1 1 auto;min-width:0;font:500 14px/1 'Hanken Grotesk',Arial,sans-serif;color:#CFC3B8;text-align:right;white-space:nowrap;overflow:hidden}\n.es-rm{flex:0 0 34px;background:transparent;border:1px solid #554942;color:#CFC3B8;border-radius:999px;padding:9px 0;cursor:pointer;font:500 15px/1 'Hanken Grotesk',Arial,sans-serif}\n.es-rm:hover{border-color:#D8A99A;color:#D8A99A}\n.es-note{margin-top:12px;font:400 12.5px/1.5 'Hanken Grotesk',Arial,sans-serif;color:#B0A29A}\n.es-add{margin-top:16px;background:transparent;border:1px dashed #554942;color:#fff;border-radius:999px;padding:13px 22px;cursor:pointer;font:600 14.5px/1 'Hanken Grotesk',Arial,sans-serif}\n.es-add:hover{border-color:#D8A99A;color:#D8A99A}\n.es-div{margin-top:30px;padding-top:26px;border-top:1px solid #4A403A}\n.es-2col{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,210px),1fr));gap:26px}\n.es-strow{margin-top:14px;display:flex;align-items:center;gap:12px}\n.es-stin{width:92px;background:#2E2724;border:1px solid #554942;color:#fff;border-radius:12px;padding:13px;font:500 15px/1 'Hanken Grotesk',Arial,sans-serif;text-align:center}\n.es-sttxt{font:500 14.5px/1.4 'Hanken Grotesk',Arial,sans-serif;color:#CFC3B8}\n.es-sttxt small{color:#B0A29A;font-weight:400;font-size:12.5px}\n.es-addons{margin-top:14px;display:flex;flex-direction:column;gap:11px}\n.es-chk{display:flex;align-items:center;gap:11px;background:transparent;border:0;padding:0;cursor:pointer;text-align:left}\n.es-box{position:relative;width:21px;height:21px;flex-shrink:0;border:1px solid #554942;border-radius:7px;background:#2E2724;display:inline-block}\n.es-box i{position:absolute;top:3px;left:3px;right:3px;bottom:3px;background:#D8A99A;border-radius:4px;display:none}\n.es-chk.on .es-box i{display:block}\n.es-chktxt{font:500 14.5px/1.35 'Hanken Grotesk',Arial,sans-serif;color:#fff}\n.es-tiers{margin-top:14px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,145px),1fr));gap:12px}\n.es-tier{background:#2E2724;border:1px solid #554942;border-radius:16px;padding:18px 16px;cursor:pointer;text-align:left}\n.es-tier:hover{border-color:#B0A29A}\n.es-tier.on{border-color:#D8A99A;box-shadow:inset 0 0 0 1px #D8A99A}\n.es-tname{font:600 15.5px/1 'Hanken Grotesk',Arial,sans-serif;color:#fff}\n.es-trate{margin-top:8px;font:400 15px/1 Newsreader,Georgia,serif;color:#D8A99A}\n.es-tnote{margin-top:8px;font:400 12.5px/1.45 'Hanken Grotesk',Arial,sans-serif;color:#B0A29A}\n.es-sum{background:#FFFDFA;color:#332D28;border-radius:22px;padding:clamp(20px,4vw,34px);min-width:0;position:sticky;top:96px;box-shadow:0 20px 50px rgba(0,0,0,.18)}\n.es-sumlab{font:600 12.5px/1 'Hanken Grotesk',Arial,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:#8F4F3C}\n.es-range{margin-top:16px;font:400 clamp(32px,4vw,46px)/1.05 Newsreader,Georgia,serif;letter-spacing:-.01em;color:#2E2724}\n.es-sumtxt{margin-top:12px;font:400 15px/1.55 'Hanken Grotesk',Arial,sans-serif;color:#6E635B}\n.es-lines{margin-top:24px;padding-top:22px;border-top:1px solid #EDE4DA;display:flex;flex-direction:column;gap:11px}\n.es-line{display:flex;justify-content:space-between;gap:16px;font:400 14.5px/1.5 'Hanken Grotesk',Arial,sans-serif;color:#6E635B}\n.es-line b{font-weight:600;color:#332D28;white-space:nowrap}\n.es-cta{margin-top:26px;display:block;text-align:center;background:#C0392F;color:#fff;padding:18px 24px;border-radius:999px;font:600 16.5px/1 'Hanken Grotesk',Arial,sans-serif;box-shadow:0 10px 24px rgba(192,57,47,.22);text-decoration:none}\n.es-cta:hover{background:#A32F26;color:#fff}\n#ci-estimator input[type=number]::-webkit-outer-spin-button,#ci-estimator input[type=number]::-webkit-inner-spin-button{-webkit-appearance:none;margin:0}\n#ci-estimator input[type=number]{appearance:textfield;-moz-appearance:textfield}\n.es-fine{margin:16px 0 0;font:400 12.5px/1.6 'Hanken Grotesk',Arial,sans-serif;color:#6E635B}\n.ci-ring::before,.ci-ring::after{content:\"\";position:absolute;top:0;left:0;right:0;bottom:0;border-radius:999px;border:3px solid #1e7a3c;opacity:0;pointer-events:none}\n.ci-ring::before{animation:ciring 2.2s ease-out infinite}\n.ci-ring::after{animation:ciring 2.2s ease-out 1.1s infinite}\n@keyframes ciring{0%{opacity:.7;transform:scale(1)}100%{opacity:0;transform:scale(1.45)}}\n@media (prefers-reduced-motion:reduce){.ci-ring::before,.ci-ring::after{animation:none}}\n.ci-pq-mount form{max-width:860px;background:#fff;border:1px solid #EDE4DA;border-radius:22px;padding:clamp(22px,3vw,36px);box-shadow:0 2px 4px rgba(46,39,36,.03)}\n.ci-pq-mount label{display:block;margin:18px 0 7px;font:600 12.5px/1.3 'Hanken Grotesk',Arial,sans-serif;letter-spacing:.06em;text-transform:uppercase;color:#8F4F3C}\n.ci-pq-mount label:first-child{margin-top:0}\n.ci-pq-mount input[type=text],.ci-pq-mount input[type=email],.ci-pq-mount input[type=tel],.ci-pq-mount select,.ci-pq-mount textarea{width:100%;border:1px solid #DCCFC2;border-radius:12px;padding:13px 14px;font:400 15px/1.4 'Hanken Grotesk',Arial,sans-serif;color:#332D28;background:#FFFDFA;height:auto;margin-bottom:0}\n.ci-pq-mount textarea{min-height:110px;resize:vertical}\n.ci-pq-mount input:focus,.ci-pq-mount select:focus,.ci-pq-mount textarea:focus{outline:2px solid #C0392F;outline-offset:-1px;border-color:#C0392F}\n.ci-pq-mount input[type=file]:not(.w-file-upload-input){width:100%;border:2px dashed #DCCFC2;border-radius:12px;padding:16px 14px;background:#FFFDFA;font:400 14px/1.4 'Hanken Grotesk',Arial,sans-serif;color:#6E635B;cursor:pointer}\n.ci-pq-mount .w-file-upload-input{width:.1px;height:.1px;padding:0;border:0;opacity:0;overflow:hidden;position:absolute;z-index:-100}\n.ci-pq-mount input[type=submit]{margin-top:26px;background:#C0392F;border:0;color:#fff;padding:18px 32px;border-radius:999px;cursor:pointer;font:600 16.5px/1 'Hanken Grotesk',Arial,sans-serif;box-shadow:0 10px 24px rgba(192,57,47,.22);width:auto;height:auto}\n.ci-pq-mount input[type=submit]:hover{background:#A32F26}\n.ci-pq-mount .w-form-done{background:#E8F3EA;border:1px solid #BFDCC6;border-radius:16px;padding:22px 26px;font:500 16px/1.6 'Hanken Grotesk',Arial,sans-serif;color:#1e5a30;text-align:left}\n.ci-pq-mount .w-form-fail{background:#FDECEA;border:1px solid #F2B8B0;border-radius:12px;padding:14px 18px;font:500 14.5px/1.5 'Hanken Grotesk',Arial,sans-serif;color:#A32F26}\n.pqx-block{margin-top:26px;padding-top:22px;border-top:1px solid #F2EBE3}\n.pqx-block:first-child{margin-top:0;padding-top:0;border-top:0}\n.pqx-bt{font:600 17px/1.3 'Hanken Grotesk',Arial,sans-serif;color:#332D28}\n.pqx-bs{margin-top:5px;font:400 13.5px/1.55 'Hanken Grotesk',Arial,sans-serif;color:#6E635B}\n.pqx-ph-grid{margin-top:16px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,170px),1fr));gap:12px}\n.pqx-on .w-file-upload{margin:0;min-width:0}\n.pqx-on .w-file-upload-default{display:block}\n.pqx-on .w-file-upload-label{display:block;width:100%;margin:0;border:2px dashed #DCCFC2;border-radius:16px;background:#FFFDFA;padding:24px 12px;text-align:center;cursor:pointer;transition:border-color .15s,background .15s;font:400 14px/1.4 'Hanken Grotesk',Arial,sans-serif;color:#6E635B;text-transform:none;letter-spacing:normal}\n.pqx-on .w-file-upload-label:hover{border-color:#C0392F;background:#FDF6F3}\n.pqx-on .w-icon-file-upload-icon{display:block;margin:0 auto 10px;color:#8F4F3C;font-size:22px;width:auto}\n.pqx-on .w-file-upload-text{display:block;font:600 14.5px/1.35 'Hanken Grotesk',Arial,sans-serif;color:#332D28}\n.pqx-cap{display:block;margin-top:5px;font:400 12.5px/1.4 'Hanken Grotesk',Arial,sans-serif;color:#6E635B}\n.pqx-on .w-file-upload-uploading,.pqx-on .w-file-upload-success{border:2px dashed #DCCFC2;border-radius:16px;background:#FFFDFA;padding:20px 14px;text-align:center;font:500 14px/1.4 'Hanken Grotesk',Arial,sans-serif;color:#6E635B}\n.pqx-on .w-file-upload-success{border:2px solid #BFDCC6;background:#E8F3EA;color:#1e5a30}\n.pqx-on .w-file-upload-error{margin-top:10px;border:1px solid #F2B8B0;border-radius:12px;background:#FDECEA;padding:10px 12px;font:500 13px/1.4 'Hanken Grotesk',Arial,sans-serif;color:#A32F26}\n.pqx-on .w-file-upload-file{background:transparent;border:0;padding:0;margin:0}\n.pqx-on .w-file-upload-file-name{font:500 13.5px/1.4 'Hanken Grotesk',Arial,sans-serif;color:#1e5a30;word-break:break-all}\n.pqx-chips{margin-top:14px;display:flex;flex-wrap:wrap;gap:9px}\n.pqx-chip{background:#F7F2EC;border:1px solid #EDE4DA;color:#5C534C;padding:11px 17px;border-radius:999px;cursor:pointer;font:500 14px/1 'Hanken Grotesk',Arial,sans-serif;transition:background .12s,color .12s,border-color .12s}\n.pqx-chip:hover{border-color:#C0392F;color:#A32F26}\n.pqx-chip.on,.pqx-chip.on:hover{background:#C0392F;border-color:#C0392F;color:#fff}\n.pqx-on select{display:none}\n.pqx-fields{margin-top:16px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,200px),1fr));gap:14px}\n.pqx-on .pqx-f{margin:0}\n.pqx-f span{display:block;font:600 12.5px/1 'Hanken Grotesk',Arial,sans-serif;letter-spacing:.06em;text-transform:uppercase;color:#8F4F3C;margin:0 0 7px}\n.pqx-subrow{margin-top:28px;display:flex;flex-wrap:wrap;align-items:center;gap:16px}\n.pqx-on input[type=submit]{margin-top:0}\n.pqx-note{flex:1;min-width:220px;font:400 13.5px/1.55 'Hanken Grotesk',Arial,sans-serif;color:#6E635B}\n.pqx-promise{margin-top:22px;max-width:860px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,200px),1fr));gap:14px}\n.pqx-promise>div{background:#fff;border:1px solid #EDE4DA;border-radius:14px;padding:16px 18px}\n.pqx-promise b{display:block;font:600 14.5px/1.3 'Hanken Grotesk',Arial,sans-serif;color:#332D28}\n.pqx-promise span{display:block;margin-top:4px;font:400 13px/1.5 'Hanken Grotesk',Arial,sans-serif;color:#6E635B}\n.ci-pq-note{margin-top:16px;font:400 13.5px/1.6 'Hanken Grotesk',Arial,sans-serif;color:#6E635B}";
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
// v1.5.0: rebuild the photo-quote form's presentation into the repair-page
// uploader design. The native Webflow form (and its file-upload widgets, which
// handle the actual uploads) stays intact underneath — nodes are only moved
// and wrapped, so Webflow's bound handlers keep working. If anything is
// missing the form is left in its plain stacked fallback layout.
(function(){
function build(){
var m=document.querySelector('.ci-pq-mount');
if(!m||(' '+m.className+' ').indexOf(' pqx-on ')>-1)return;
var f=m.querySelector('form');if(!f)return;
var name=f.querySelector('#name'),email=f.querySelector('#email'),
phone=f.querySelector('#pq-phone'),sel=f.querySelector('#pq-type'),
notes=f.querySelector('#pq-notes'),sub=f.querySelector('input[type=submit]'),
ups=f.querySelectorAll('.w-file-upload');
if(!name||!email||!phone||!sel||!notes||!sub||ups.length<3)return;
function d(cls,html){var e=document.createElement('div');e.className=cls;if(html)e.innerHTML=html;return e}
var caps=['The worst spot','A few feet back','The whole room'],i,j,k;
for(i=0;i<ups.length;i++){
var t=ups[i].querySelector('.w-file-upload-text');
if(t){t.textContent=caps[i]||'Add a photo';
var c=document.createElement('span');c.className='pqx-cap';c.textContent='Tap to add a photo';
t.parentNode.appendChild(c)}
var fi=ups[i].querySelector('input[type=file]');if(fi)fi.setAttribute('accept','image/*');
var inf=ups[i].querySelector('.w-file-upload-info');if(inf)inf.style.display='none'}
var rm=[],kids=f.children;
for(j=0;j<kids.length;j++)if(kids[j].tagName==='LABEL')rm.push(kids[j]);
for(j=0;j<rm.length;j++)f.removeChild(rm[j]);
var b1=d('pqx-block','<div class="pqx-bt">Add your photos</div><div class="pqx-bs">Even one helps. Three is ideal: a close-up of the worst spot, one from a few feet back, and one of the whole room. JPG, PNG or HEIC \u00b7 up to 10 MB each.</div><div class="pqx-ph-grid"></div>');
var g=b1.querySelector('.pqx-ph-grid');
for(k=0;k<ups.length;k++)g.appendChild(ups[k]);
var b2=d('pqx-block','<div class="pqx-bt">What\u2019s going on with the carpet?</div><div class="pqx-bs">Pick the closest one \u2014 it tells us what to look for in your photos.</div><div class="pqx-chips"></div>');
var TYPES=['Carpet stretching','Carpet repair','Stair carpet','Not sure \u2014 you tell me'];
try{sel.name='Project type'}catch(e){}
sel.innerHTML='';
var o0=document.createElement('option');o0.value='';o0.textContent='Choose one';sel.appendChild(o0);
for(k=0;k<TYPES.length;k++){var op=document.createElement('option');op.value=TYPES[k];op.textContent=TYPES[k];sel.appendChild(op)}
var chips=b2.querySelector('.pqx-chips');
TYPES.forEach(function(T){
var b=document.createElement('button');b.type='button';b.className='pqx-chip';b.textContent=T;b.setAttribute('aria-pressed','false');
b.addEventListener('click',function(){
var on=b.className.indexOf(' on')>-1;
chips.querySelectorAll('.pqx-chip').forEach(function(x){x.className='pqx-chip';x.setAttribute('aria-pressed','false')});
if(on){sel.value=''}else{sel.value=T;b.className='pqx-chip on';b.setAttribute('aria-pressed','true')}});
chips.appendChild(b)});
var b3=d('pqx-block','<div class="pqx-bt">Tell us about it in your own words</div><div class="pqx-bs">Optional \u2014 rooms, stairs, when it started, whether you already have carpet picked out.</div>');
b3.appendChild(notes);
var b4=d('pqx-block','<div class="pqx-bt">Where should the price go?</div><div class="pqx-fields"></div>');
var fg=b4.querySelector('.pqx-fields');
function wrap(inp,cap){var L=document.createElement('label');L.className='pqx-f';
var s=document.createElement('span');s.textContent=cap;L.appendChild(s);L.appendChild(inp);fg.appendChild(L)}
wrap(name,'Full name');wrap(email,'Email');wrap(phone,'Phone');
var row=d('pqx-subrow');row.appendChild(sub);
row.appendChild(d('pqx-note','Sent before 3pm on a weekday? Your price lands today. After that, first thing next morning.'));
f.appendChild(b1);f.appendChild(b2);b2.appendChild(sel);f.appendChild(b3);f.appendChild(b4);f.appendChild(row);
name.placeholder='Jordan Alvarez';email.placeholder='you@email.com';
phone.placeholder='(425) 555-0148';
notes.placeholder='Example: Ripples in two bedrooms and the hallway, about 600 sq ft, plus 13 stairs. Want a price for stretching vs replacing with mid-grade carpet.';
if(!document.getElementById('pqx-promise')){
var pr=d('pqx-promise');pr.id='pqx-promise';
pr.innerHTML='<div><b>Same day</b><span>A written price in your inbox, not a callback</span></div><div><b>A person, not a bot</b><span>Every photo reviewed by one of our estimators</span></div><div><b>No obligation</b><span>Licensed and insured \u00b7 1-year workmanship warranty</span></div>';
m.parentNode.insertBefore(pr,m.nextSibling)}
m.className+=' pqx-on';
}
function safe(){try{build()}catch(e){}}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',safe);else safe();
window.addEventListener('load',safe);
})();
// Anchor for the hook-band button (the settings API rejected writing the id).
(function(){var s=document.querySelector('.ci-book-sec');if(s&&!s.id)s.id='book'})();
// Photo-quote widget: same design + formsubmit.co pipeline as the repair pages' #ocpq.
(function(){
if(document.getElementById('ocpq'))return;
var st=document.createElement('style');st.id='ocpq-carpet-css';
st.textContent="#ocpq{background:#f6f2ec;padding:clamp(36px,6vw,84px) clamp(16px,4vw,48px);color:#0b1f3a}\n#ocpq *{box-sizing:border-box}\n#ocpq [hidden]{display:none!important}\n#ocpq .ocpq-wrap{max-width:1060px;margin:0 auto;display:flex;flex-direction:column;gap:clamp(26px,4vw,40px)}\n#ocpq .ocpq-head{display:flex;flex-direction:column;gap:14px;max-width:740px}\n#ocpq .ocpq-eyebrow{display:flex;align-items:center;gap:10px;font-size:13px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#be1e2d}\n#ocpq .ocpq-eyebrow span{width:28px;height:2px;background:#be1e2d;display:block}\n#ocpq h2{font-family:'Playfair Display',Georgia,serif;font-size:clamp(29px,5vw,50px);font-weight:800;line-height:1.06;letter-spacing:-.02em;margin:0;color:#0b1f3a}\n#ocpq .ocpq-lead{font-size:clamp(16px,1.6vw,19px);line-height:1.6;color:#4a5666;margin:0;max-width:62ch}\n#ocpq .ocpq-card{background:#fff;border:1px solid #e7e0d6;border-radius:20px;box-shadow:0 24px 48px -32px rgba(12,31,63,.4);padding:clamp(22px,3.4vw,40px);display:flex;flex-direction:column;gap:clamp(22px,3vw,30px)}\n#ocpq #ocpq-form{display:flex;flex-direction:column;gap:16px}\n#ocpq .ocpq-drop{border:2px dashed #dccfb9;background:#fcfaf6;border-radius:16px;padding:clamp(26px,5vw,52px) 20px;text-align:center;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:13px;transition:background .15s,border-color .15s}\n#ocpq .ocpq-drop.is-over{border-color:#be1e2d;background:#fbeeef}\n#ocpq .ocpq-dropicon{width:58px;height:58px;border-radius:15px;background:#f1e7d6;color:#be1e2d;display:grid;place-items:center}\n#ocpq .ocpq-dropicon svg{width:28px;height:28px}\n#ocpq .ocpq-droptitle{font-family:'Playfair Display',Georgia,serif;font-size:clamp(18px,2.2vw,22px);font-weight:800}\n#ocpq .ocpq-dropsub{font-size:15px;color:#6b5b4a;line-height:1.5;max-width:46ch}\n#ocpq .ocpq-btnrow{display:flex;flex-wrap:wrap;gap:12px}\n#ocpq .ocpq-ghost{flex:1 1 210px;min-height:54px;border-radius:12px;border:1.5px solid #dccfb9;background:#fff;color:#0b1f3a;font-weight:700;font-size:15px;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:9px;font-family:inherit;transition:background .15s,border-color .15s}\n#ocpq .ocpq-ghost:hover{background:#fbf6ee;border-color:#be1e2d}\n#ocpq .ocpq-ghost svg{width:18px;height:18px}\n#ocpq .ocpq-hint{display:flex;align-items:center;gap:9px;font-size:14.5px;color:#7a6a58;line-height:1.5}\n#ocpq .ocpq-hint svg{width:16px;height:16px;color:#be1e2d;flex:0 0 auto}\n#ocpq .ocpq-galhead{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:12px}\n#ocpq .ocpq-count{font-weight:800;font-size:15px}\n#ocpq .ocpq-need{font-size:14px}\n#ocpq .ocpq-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(128px,1fr));gap:12px}\n#ocpq .ocpq-thumb{position:relative;border-radius:12px;overflow:hidden;border:1px solid #e7e0d6;background:#f1eade;aspect-ratio:4/3}\n#ocpq .ocpq-thumb .img{width:100%;height:100%;background-size:cover;background-position:center}\n#ocpq .ocpq-thumb .rm{position:absolute;top:6px;right:6px;width:30px;height:30px;border-radius:50%;border:none;background:rgba(11,31,58,.72);color:#fff;cursor:pointer;display:grid;place-items:center}\n#ocpq .ocpq-thumb .rm:hover{background:#be1e2d}\n#ocpq .ocpq-thumb .rm svg{width:14px;height:14px}\n#ocpq .ocpq-thumb .nm{position:absolute;left:0;right:0;bottom:0;padding:14px 8px 6px;font-size:11px;color:#fff;background:linear-gradient(transparent,rgba(11,31,58,.8));white-space:nowrap;overflow:hidden;text-overflow:ellipsis}\n#ocpq .ocpq-working{font-size:14.5px;color:#6b5b4a;font-weight:600}\n#ocpq .ocpq-textarea{width:100%;min-height:120px;padding:14px 15px;border-radius:12px;border:1.5px solid #dccfb9;background:#fcfaf6;font-size:16px;line-height:1.55;color:#0b1f3a;font-family:inherit;resize:vertical}\n#ocpq .ocpq-textarea:focus{outline:none;border-color:#be1e2d;background:#fff}\n#ocpq .ocpq-textarea::placeholder{color:#a2937f}\n#ocpq .ocpq-thumb.is-nopreview{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:7px;padding:10px;text-align:center;background:#f6efe2}\n#ocpq .ocpq-thumb.is-nopreview svg{width:22px;height:22px;color:#b09873}\n#ocpq .ocpq-thumb.is-nopreview .lbl{font-size:11px;color:#6b5b4a;line-height:1.3;word-break:break-word}\n#ocpq .ocpq-nopreview{font-size:13.5px;color:#7a6a58;margin-top:10px;line-height:1.5}\n#ocpq .ocpq-err{color:#a32e19;font-size:14.5px;font-weight:600}\n#ocpq #ocpq-reveal{display:flex;flex-direction:column;gap:clamp(22px,3vw,28px);border-top:1px solid #efe6d7;padding-top:clamp(22px,3vw,28px);animation:ocpqReveal .32s ease both}\n@keyframes ocpqReveal{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}\n#ocpq .ocpq-block{display:flex;flex-direction:column;gap:12px}\n#ocpq .ocpq-blocktitle{font-family:'Playfair Display',Georgia,serif;font-weight:800;font-size:clamp(17px,2vw,20px)}\n#ocpq .ocpq-blocksub{font-size:14.5px;color:#7a6a58}\n#ocpq .ocpq-chips{display:flex;flex-wrap:wrap;gap:9px}\n#ocpq .ocpq-chip{min-height:48px;padding:0 18px;border-radius:999px;cursor:pointer;font-weight:600;font-size:15px;background:#fcfaf6;border:1.5px solid #dccfb9;color:#3a2e22;font-family:inherit;transition:background .15s,border-color .15s}\n#ocpq .ocpq-chip[aria-pressed=\"true\"]{background:#fbe7e9;border-color:#be1e2d;color:#0b1f3a}\n#ocpq .ocpq-fields{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px}\n#ocpq .ocpq-field{display:flex;flex-direction:column;gap:7px}\n#ocpq .ocpq-field span{font-weight:800;font-size:14px}\n#ocpq .ocpq-field input{width:100%;min-height:54px;padding:0 15px;border-radius:12px;border:1.5px solid #dccfb9;background:#fcfaf6;font-size:16px;color:#0b1f3a;font-family:inherit}\n#ocpq .ocpq-field input:focus{outline:none;border-color:#be1e2d;background:#fff}\n#ocpq .ocpq-submitrow{display:flex;flex-wrap:wrap;align-items:center;gap:16px}\n#ocpq .ocpq-submit{min-height:58px;padding:0 32px;border-radius:12px;border:none;background:#be1e2d;color:#fff;font-weight:800;font-size:17px;cursor:pointer;font-family:inherit;transition:background .15s}\n#ocpq .ocpq-submit:hover{background:#9c1623}\n#ocpq .ocpq-submit[disabled]{opacity:.65;cursor:default}\n#ocpq .ocpq-note{font-size:14px;color:#7a6a58;line-height:1.5;max-width:40ch}\n#ocpq #ocpq-done{display:flex;flex-direction:column;gap:clamp(22px,3vw,30px)}\n#ocpq .ocpq-donetop{display:flex;align-items:flex-start;gap:15px}\n#ocpq .ocpq-check{width:46px;height:46px;border-radius:50%;background:#e7f0e3;color:#1f8a4c;display:grid;place-items:center;flex:0 0 auto}\n#ocpq .ocpq-check svg{width:23px;height:23px}\n#ocpq #ocpq-donehead{font-family:'Playfair Display',Georgia,serif;font-size:clamp(21px,2.6vw,28px);font-weight:800;margin:0 0 6px}\n#ocpq #ocpq-donebody{margin:0;color:#4a5666;font-size:16px;line-height:1.55;max-width:58ch}\n#ocpq .ocpq-next{background:#0b1f3a;border-radius:16px;padding:clamp(22px,3vw,30px);color:#f6eee1;display:flex;flex-direction:column;gap:16px}\n#ocpq .ocpq-nexttag{font-size:12px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#e0a15c}\n#ocpq .ocpq-step{display:flex;gap:14px;align-items:flex-start}\n#ocpq .ocpq-step>span{width:24px;height:24px;border-radius:50%;border:1.5px solid rgba(224,161,92,.55);display:grid;place-items:center;font-size:12px;font-weight:800;color:#e0a15c;flex:0 0 auto;margin-top:2px}\n#ocpq .ocpq-step b{display:block;font-weight:800;font-size:16px}\n#ocpq .ocpq-step i{display:block;font-style:normal;font-size:14.5px;color:#c9bcaa;line-height:1.55;max-width:56ch;margin-top:3px}\n#ocpq .ocpq-donebtns{display:flex;flex-wrap:wrap;gap:12px;align-items:center}\n#ocpq .ocpq-call{min-height:54px;padding:0 24px;border-radius:12px;background:#0b1f3a;color:#fff7ea;font-weight:800;font-size:15px;text-decoration:none;display:inline-flex;align-items:center}\n#ocpq .ocpq-promise{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:clamp(16px,2.5vw,28px);border-top:1px solid #e7e0d6;padding-top:clamp(22px,3vw,32px)}\n#ocpq .ocpq-promise div{display:flex;flex-direction:column;gap:5px}\n#ocpq .ocpq-promise b{font-family:'Playfair Display',Georgia,serif;font-weight:800;font-size:22px}\n#ocpq .ocpq-promise span{font-size:14.5px;color:#6b5b4a;line-height:1.5}";
document.head.appendChild(st);
var holder=document.createElement('div');
holder.innerHTML="<section id=\"ocpq\" aria-labelledby=\"ocpq-title\"><div class=\"ocpq-wrap\"><header class=\"ocpq-head\"><div class=\"ocpq-eyebrow\"><span></span>No appointment needed</div><h2 id=\"ocpq-title\">Send photos of your carpet. Get a real quote by email today.</h2><p class=\"ocpq-lead\">Photograph the ripples \u2014 or the whole room \u2014 on your phone or upload from your computer. One of our estimators looks at every photo personally and emails you a written price the same business day \u2014 no visit, no sales call, no obligation.</p></header><div class=\"ocpq-card\"><div id=\"ocpq-form\"><div class=\"ocpq-drop\" id=\"ocpq-drop\" role=\"button\" tabindex=\"0\"><div class=\"ocpq-dropicon\"><svg aria-hidden=\"true\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M12 16V4\"/><path d=\"m7 9 5-5 5 5\"/><path d=\"M4 16v2a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-2\"/></svg></div><div class=\"ocpq-droptitle\">Drag your photos here, or tap to browse</div><div class=\"ocpq-dropsub\">Even one photo helps. Three is ideal: a close-up of the worst spot, one from a few feet back, and one of the whole room. Up to 8 &middot; JPG, PNG or HEIC.</div></div><div class=\"ocpq-btnrow\"><button type=\"button\" class=\"ocpq-ghost\" id=\"ocpq-browse\"><svg aria-hidden=\"true\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M4 20h16a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-4l-2-2h-4L8 6H4a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2Z\"/><circle cx=\"12\" cy=\"13\" r=\"3.2\"/></svg>Choose from device</button><button type=\"button\" class=\"ocpq-ghost\" id=\"ocpq-camera\"><svg aria-hidden=\"true\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><rect x=\"2\" y=\"7\" width=\"20\" height=\"14\" rx=\"2\"/><path d=\"M8 7 9.5 4h5L16 7\"/><circle cx=\"12\" cy=\"14\" r=\"3.4\"/></svg>Take a photo now</button></div><div class=\"ocpq-hint\" id=\"ocpq-emptyhint\"><svg aria-hidden=\"true\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M12 5v14\"/><path d=\"m6 13 6 6 6-6\"/></svg>Add a photo and we'll ask for your name, email and phone next \u2014 two more taps.</div><div class=\"ocpq-working\" id=\"ocpq-working\" role=\"status\" aria-live=\"polite\" hidden></div><input type=\"file\" id=\"ocpq-file\" accept=\"image/*\" multiple hidden><input type=\"file\" id=\"ocpq-cam\" accept=\"image/*\" capture=\"environment\" hidden><div id=\"ocpq-gallery\" hidden><div class=\"ocpq-galhead\"><div class=\"ocpq-count\" id=\"ocpq-count\"></div><div class=\"ocpq-need\" id=\"ocpq-need\"></div></div><div class=\"ocpq-grid\" id=\"ocpq-thumbs\"></div><div class=\"ocpq-nopreview\" id=\"ocpq-nopreview\" hidden></div></div><div class=\"ocpq-err\" id=\"ocpq-photoerr\" role=\"alert\" aria-live=\"assertive\" hidden></div><div id=\"ocpq-reveal\" hidden><div class=\"ocpq-block\"><div class=\"ocpq-blockhead\"><div class=\"ocpq-blocktitle\">What's going on with the carpet?</div><div class=\"ocpq-blocksub\">Pick everything that applies \u2014 it tells us what to look for in your photos.</div></div><div class=\"ocpq-chips\" id=\"ocpq-chips\"><button type=\"button\" class=\"ocpq-chip\" aria-pressed=\"false\">Ripples &amp; waves</button><button type=\"button\" class=\"ocpq-chip\" aria-pressed=\"false\">Matted traffic paths</button><button type=\"button\" class=\"ocpq-chip\" aria-pressed=\"false\">Pet damage or odor</button><button type=\"button\" class=\"ocpq-chip\" aria-pressed=\"false\">Seams splitting or fraying</button><button type=\"button\" class=\"ocpq-chip\" aria-pressed=\"false\">Stairs &amp; landings</button><button type=\"button\" class=\"ocpq-chip\" aria-pressed=\"false\">Water damage</button><button type=\"button\" class=\"ocpq-chip\" aria-pressed=\"false\">Not sure \u2014 you tell me</button></div></div><div class=\"ocpq-block\"><div class=\"ocpq-blockhead\"><div class=\"ocpq-blocktitle\">Tell us about it in your own words</div><div class=\"ocpq-blocksub\">Optional \u2014 how many rooms, when it started, whether you already have carpet picked out. Whatever you think we should know.</div></div><textarea id=\"ocpq-notes\" class=\"ocpq-textarea\" rows=\"4\" maxlength=\"2000\" placeholder=\"Example: The carpet in two bedrooms and the hallway is rippling near the doors. About 600 sq ft total. We also have 13 stairs. Would like a price for stretching vs replacing with mid-grade carpet.\"></textarea></div><div class=\"ocpq-block\"><div class=\"ocpq-blocktitle\">Where should the quote go?</div><div class=\"ocpq-fields\"><label class=\"ocpq-field\"><span>Full name</span><input type=\"text\" id=\"ocpq-name\" placeholder=\"Jordan Alvarez\" autocomplete=\"name\"></label><label class=\"ocpq-field\"><span>Email</span><input type=\"email\" id=\"ocpq-email\" placeholder=\"you@email.com\" autocomplete=\"email\" inputmode=\"email\"></label><label class=\"ocpq-field\"><span>Phone</span><input type=\"tel\" id=\"ocpq-phone\" placeholder=\"(425) 555-0148\" autocomplete=\"tel\" inputmode=\"tel\"></label></div></div><div class=\"ocpq-err\" id=\"ocpq-formerr\" role=\"alert\" aria-live=\"assertive\" hidden></div><div class=\"ocpq-submitrow\"><button type=\"button\" class=\"ocpq-submit\" id=\"ocpq-submit\">Send photos &amp; get my quote</button><div class=\"ocpq-note\">Sent before 3pm on a weekday? Your price lands today. After that, first thing next morning.</div></div></div><div id=\"ocpq-done\" hidden><div class=\"ocpq-donetop\"><div class=\"ocpq-check\"><svg aria-hidden=\"true\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"m4 12.5 5 5L20 6.5\"/></svg></div><div><h3 id=\"ocpq-donehead\"></h3><p id=\"ocpq-donebody\"></p></div></div><div class=\"ocpq-next\"><div class=\"ocpq-nexttag\">What happens next</div><div class=\"ocpq-step\"><span>1</span><div><b>An estimator opens your photos</b><i>Not an algorithm \u2014 the same person who would have walked your carpet in person.</i></div></div><div class=\"ocpq-step\"><span>2</span><div><b>You get a written price by email</b><i>Stretch or replace, itemized \u2014 what it costs and how long we need in your home.</i></div></div><div class=\"ocpq-step\"><span>3</span><div><b>Only then do you decide</b><i>Reply to book a date, ask a question, or ignore it entirely. No follow-up sales calls.</i></div></div></div><div class=\"ocpq-donebtns\"><a class=\"ocpq-call\" href=\"tel:+14255951079\">Call (425) 595-1079</a><button type=\"button\" class=\"ocpq-ghost\" id=\"ocpq-reset\">Send another room</button></div></div></div><div class=\"ocpq-promise\"><div><b>Same day</b><span>A written price in your inbox, not a callback</span></div><div><b>A person, not a bot</b><span>Every photo reviewed by one of our estimators</span></div><div><b>No obligation</b><span>Licensed and insured &middot; 1-year workmanship warranty</span></div></div></div></section>";
var sec=holder.firstChild;
var anchor=document.querySelector('.ci-cta')||document.querySelector('.ci-footer');
var page=document.querySelector('.ci-page');
if(anchor&&anchor.parentNode)anchor.parentNode.insertBefore(sec,anchor);
else if(page)page.appendChild(sec);
else document.body.appendChild(sec);
if(location.hash==='#ocpq'){try{sec.scrollIntoView()}catch(e){}}
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
else{need.textContent='One or two more angles helps us price it faster.';need.style.color='#7a6a58'}
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
im.setAttribute('aria-label','Photo of your carpet: '+p.name);
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
if(photos.length<MIN)return fail(pe,'Add at least one photo of the carpet so we can price it.');
if(!damage.length)return fail(fe,'Tell us what is going on with the carpet — one tap.');
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
})();
