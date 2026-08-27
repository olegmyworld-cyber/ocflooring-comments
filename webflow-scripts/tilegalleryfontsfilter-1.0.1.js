(function(){var p=document.createElement('link');p.rel='preconnect';p.href='https://fonts.gstatic.com';p.crossOrigin='';document.head.appendChild(p);
var s=document.createElement('link');s.rel='stylesheet';s.href='https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Archivo:wght@400;500;600;700&display=swap';document.head.appendChild(s);
var c=document.createElement('link');c.rel='canonical';c.href='https://www.nwocflooring.com/tile-gallery';document.head.appendChild(c);
function fit(){var n=document.querySelector('.navbar'),w=document.querySelector('.tg-page');if(!n||!w)return;var y=n.getBoundingClientRect().bottom;if(y>40&&y<400)w.style.paddingTop=y+'px';}
function init(){fit();addEventListener('resize',fit);setTimeout(fit,400);setTimeout(fit,1200);
var t=document.createElement('style');t.textContent=".tg-fbtn:hover{border-color:#16201E}.tg-fbtn.on{background:#16201E;color:#FBFAF7;border-color:#16201E}.tg-fbtn:focus-visible{outline:2px solid #2E5D57;outline-offset:2px}.tg-btn:hover{background:#C08B5C}.tg-btn2:hover,.tg-foota:hover{color:#FBFAF7}.tg-fig.tg-off{display:none}.tg-figimg{transition:transform .5s ease}.tg-fig:hover .tg-figimg{transform:scale(1.04)}";document.head.appendChild(t);
var b=[].slice.call(document.querySelectorAll('.tg-fbtn')),f=[].slice.call(document.querySelectorAll('.tg-fig'));
function go(x){var k=x.getAttribute('data-cat');b.forEach(function(y){y.classList.toggle('on',y===x);y.setAttribute('aria-pressed',y===x?'true':'false')});f.forEach(function(g){g.classList.toggle('tg-off',k!=='all'&&g.getAttribute('data-cat')!==k)});}
b.forEach(function(x){x.setAttribute('role','button');x.setAttribute('tabindex','0');x.addEventListener('click',function(e){e.preventDefault();go(x)});x.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();go(x)}})});
if(b[0])go(b[0]);}
if(document.readyState!=='loading')init();else addEventListener('DOMContentLoaded',init);})();
