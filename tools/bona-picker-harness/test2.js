const {chromium}=require('playwright-core');
(async()=>{
  const browser=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
  const ctx=await browser.newContext({viewport:{width:1280,height:1000}});
  const reqs=[];
  await ctx.route(/^https?:\/\/(?!localhost)/,r=>{reqs.push(r.request().url());r.abort();});
  const results=[]; const t=(n,ok,x)=>results.push((ok?'PASS':'FAIL')+' '+n+(x?' — '+x:''));
  const p=await ctx.newPage();
  const errors=[]; p.on('pageerror',e=>errors.push(String(e).slice(0,300)));
  await p.goto('http://localhost:8471/flooring-services-near-me/floor-refinishing',{waitUntil:'load'});
  await p.waitForTimeout(400);
  const E=sel=>p.evaluate(s=>{const e=document.querySelector(s);return e?e.textContent.trim():null},sel);
  t('picker renders',await p.evaluate(()=>!!document.querySelector('#ocp .ocp')));
  t('left col visible',await p.evaluate(()=>getComputedStyle(document.querySelector('#ocrp .ocrp-left')).display!=='none'));
  t('seg buttons',(await E('#ocpSe'))==='Sealer Finish'&&(await E('#ocpSt'))==='Stain Color');
  t('default = IntenseSeal fav',(await E('#ocpName')).startsWith('Bona IntenseSeal')&&await p.evaluate(()=>!document.getElementById('ocpFav').hidden));
  t('tone line',(await E('#ocpTl'))==='Tone 2 of 5 · Rich',await E('#ocpTl'));
  t('best-for shown',(await E('#ocpBestT')).includes('Stained floors'));
  const img1=await p.evaluate(()=>document.getElementById('ocpImg').src);
  t('living img url',img1.endsWith('_bona-living-intense.jpg'),img1.split('/').pop());
  await p.click('#ocpRooms button[data-r=kit]');
  const img2=await p.evaluate(()=>document.getElementById('ocpImg').src);
  t('kitchen swap',img2.endsWith('_bona-kitchen-intense.jpg'),img2.split('/').pop());
  t('5 sealer swatches',await p.evaluate(()=>document.querySelectorAll('#ocpSw button').length)===5);
  // click nordic (last)
  await p.evaluate(()=>{const b=document.querySelectorAll('#ocpSw button');b[b.length-1].click()});
  t('nordic select',(await E('#ocpName')).startsWith('Bona NordicSeal')&&(await E('#ocpTl'))==='Tone 5 of 5 · Lightest',await E('#ocpTl'));
  // stain mode
  await p.click('#ocpSt');
  t('stain count 21',await p.evaluate(()=>document.querySelectorAll('#ocpSw button').length)===21);
  t('stain default Provincial',(await E('#ocpName'))==='Provincial',await E('#ocpName'));
  t('stain tl',(await E('#ocpTl'))==='Color 17 of 21',await E('#ocpTl'));
  const img3=await p.evaluate(()=>document.getElementById('ocpImg').src);
  t('stain room img',img3.endsWith('_bona-living-stain-provincial.jpg'),img3.split('/').pop());
  t('rooms hidden in stain mode',await p.evaluate(()=>document.getElementById('ocpRooms').style.display==='none'));
  t('best-for hidden in stain mode',await p.evaluate(()=>document.getElementById('ocpBest').style.display==='none'));
  await p.evaluate(()=>{document.querySelectorAll('#ocpSw button')[21-1].click()});
  t('true black select',(await E('#ocpName'))==='True Black');
  // back to sealer keeps state
  await p.click('#ocpSe');
  t('back to sealer',(await E('#ocpName')).startsWith('Bona NordicSeal'));
  // structure & other scripts
  t('#ocrp before gallery',await p.evaluate(()=>{const rp=document.getElementById('ocrp'),g=document.querySelector('.gallery-section');return !!(rp&&g&&(rp.compareDocumentPosition(g)&4));}));
  t('features hidden',await p.evaluate(()=>getComputedStyle(document.querySelector('.section_features')).display==='none'));
  t('gallery filtered',await p.evaluate(()=>document.querySelectorAll('#auto-height-swiper .swiper-slide').length===2));
  t('CTA filled',await p.evaluate(()=>{const a=document.querySelector('.section_appointments a');return a.textContent==='Book My Free Visit'&&a.getAttribute('href')==='/contact';}));
  // all image URLs point at the site CDN with expected names
  const bad=reqs.filter(u=>!/^https:\/\/cdn\.prod\.website-files\.com\/6377e8e6a53936b48ef1cad0\/[0-9a-f]{24}_bona-(living|kitchen|stain)/.test(u));
  t('all external requests are bona images',bad.length===0,bad.slice(0,3).join(','));
  t('no JS errors',errors.length===0,errors.join('|'));
  // mobile viewport
  await p.setViewportSize({width:390,height:800});
  await p.waitForTimeout(300);
  t('mobile: no horizontal overflow',await p.evaluate(()=>document.documentElement.scrollWidth<=395),String(await p.evaluate(()=>document.documentElement.scrollWidth)));
  await p.screenshot({path:'ocp-mobile.png',fullPage:true});
  await p.setViewportSize({width:1280,height:1000});
  await p.screenshot({path:'ocp-desktop.png',fullPage:true});
  console.log(results.join('\n'));
  await browser.close();
  process.exit(results.some(r=>r.startsWith('FAIL'))?1:0);
})().catch(e=>{console.error('HARNESS ERROR',e);process.exit(2)});
