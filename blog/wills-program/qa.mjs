// Renders every out/*.html in a bare page and checks JS errors, calculator/estimator/quiz behaviour and mobile overflow.
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import { readdirSync, readFileSync, writeFileSync } from 'node:fs';
const dir = new URL('./out/', import.meta.url).pathname;
const files = readdirSync(dir).filter(f => f.endsWith('.html')).sort();
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
let bad = 0;
for (const f of files) {
  const errs = [];
  const h1 = e => errs.push('PAGEERROR ' + e.message), h2 = m => { if (m.type() === 'error') errs.push('CONSOLE ' + m.text()); };
  page.on('pageerror', h1); page.on('console', h2);
  const body = readFileSync(dir + f, 'utf8');
  writeFileSync('/tmp/qa.html', "<!doctype html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width'></head><body style='margin:0'><div class='post-body w-richtext' style='max-width:820px;margin:0 auto;padding:16px'><style>.w-richtext a{display:block}</style>" + body + "</div></body></html>");
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto('file:///tmp/qa.html');
  const r = { f };
  try {
    if (await page.$('#rc-area')) { await page.fill('#rc-area', '1000'); await page.fill('#rc-stairs', '4'); await page.click('#rc-calc'); r.calc = await page.textContent('#rc-total'); }
    if (await page.$('#es-go')) { await page.click('#es-go'); r.est = await page.$$eval('#es-list li', a => a.length); }
    if (await page.$('.oq-q')) { for (const q of await page.$$('.oq-q')) { await (await q.$('button')).click(); } r.quiz = (await page.textContent('#oq-out h4')).slice(0, 40); }
    await page.click('.faq-item:nth-child(1) summary'); r.faq = await page.$eval('.faq-item:nth-child(1)', e => e.open);
    r.ld = await page.$$eval('script[type="application/ld+json"]', s => s.map(x => { try { JSON.parse(x.textContent); return 'ok'; } catch (e) { return 'BAD'; } }).join(','));
    r.h2 = await page.$$eval('.post-body > h2', a => a.length);
    await page.setViewportSize({ width: 360, height: 900 }); r.sw = await page.evaluate(() => document.documentElement.scrollWidth);
  } catch (e) { errs.push('STEP ' + e.message.split('\n')[0]); }
  page.off('pageerror', h1); page.off('console', h2);
  const ok = errs.length === 0 && r.sw <= 360 && r.faq && !/BAD/.test(r.ld);
  if (!ok) bad++;
  console.log((ok ? 'OK  ' : 'FAIL') + ' ' + JSON.stringify(r) + (errs.length ? ' ' + errs.join(' | ') : ''));
}
console.log(files.length + ' files, ' + bad + ' failing');
await browser.close();
