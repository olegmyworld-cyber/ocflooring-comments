# Shared assembly helpers for OC Flooring blog bodies (house style)
import json

CSS = open('shared_css.html').read()
ANIM = open('shared_anim.html').read()

PHONE_SVG = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-2px;flex:0 0 auto"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
PIN_SVG = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-2px;flex:0 0 auto"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>'
HOME_SVG = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-2px;flex:0 0 auto"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>'

def date_badge(date_str):
    return f'<div data-rt-embed-type=\'true\'><div class="ocb" style="margin:22px 0 -6px"><span style="display:inline-block;background:#16a34a;color:#fff;border-radius:999px;padding:7px 16px;font-size:14px;font-weight:800;letter-spacing:.01em;box-shadow:0 4px 12px rgba(22,163,74,.35)">{date_str}</span></div></div>'

def quick_answer(answer_html, chip2_label):
    return f'''<div data-rt-embed-type='true'><section class="ocb ocb-card" style="background:linear-gradient(180deg,#fff,#f8fafc)">
  <span class="ocb-eyebrow">Quick answer</span>
  <p style="margin:0;font-size:17.9px;line-height:1.65">{answer_html}</p>
  <div class="ocb-chips">
    <span class="ocb-chip">{PIN_SVG} King &amp; Snohomish County</span>
    <span class="ocb-chip">{HOME_SVG} {chip2_label}</span>
    <span class="ocb-chip">{PHONE_SVG} <a href="tel:+14255951079" style="color:inherit;text-decoration:none">(425) 595-1079</a></span>
  </div>
</section></div>'''

def facts(f):
    cells = ''.join(f'\n  <div class="ocb-fact"><span class="n">{n}</span><p>{p}</p></div>' for n, p in f)
    return f'''<div data-rt-embed-type='true'><section class="ocb"><div class="ocb-facts">{cells}
</div></section></div>'''

def table(caption, headers, rows):
    th = ''.join(f'<th>{h}</th>' for h in headers)
    trs = ''
    for r in rows:
        tds = ''.join(f'<td>{c}</td>' for c in r)
        trs += f'\n    <tr>{tds}</tr>'
    cap = f'\n  <h3 style="margin:0 0 10px;font-size:18.5px;font-weight:900;color:#5c0000">{caption}</h3>' if caption else ''
    return f'''<div data-rt-embed-type='true'><section class="ocb ocb-card">{cap}
  <div style="overflow-x:auto"><table class="ocb-table">
    <tr>{th}</tr>{trs}
  </table></div>
</section></div>'''

def two_col(title_a, items_a, title_b, items_b):
    lis_a = ''.join(f'\n      <li>{i}</li>' for i in items_a)
    lis_b = ''.join(f'\n      <li>{i}</li>' for i in items_b)
    return f'''<div data-rt-embed-type='true'><section class="ocb"><div class="ocb-2col">
  <div class="ocb-card" style="margin:0">
    <h3 style="margin:0;font-size:18.5px;font-weight:900;color:#5c0000">{title_a}</h3>
    <ul class="ocb-check">{lis_a}
    </ul>
  </div>
  <div class="ocb-card" style="margin:0">
    <h3 style="margin:0;font-size:18.5px;font-weight:900;color:#334155">{title_b}</h3>
    <ul class="ocb-check ocb-x">{lis_b}
    </ul>
  </div>
</div></section></div>'''

def faq(title, qas):
    items = ''
    for q, a in qas:
        items += f'\n    <details class="faq-item" role="listitem"><summary class="faq-q">{q}</summary><div class="faq-a">{a}</div></details>'
    ld = {"@context": "https://schema.org", "@type": "FAQPage",
          "mainEntity": [{"@type": "Question", "name": q,
                          "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qas]}
    ld_json = json.dumps(ld, ensure_ascii=False)
    return f'''<div data-rt-embed-type='true'><!-- FAQ accordion + JSON-LD -->
<section class="faq-wrap ocb" aria-labelledby="faq-title">
  <h2 id="faq-title" class="faq-title">{title}</h2>
  <div class="faq-items" role="list">{items}
  </div>
</section>

<style>
  .faq-wrap{{--line:#e5e7eb;margin:28px auto;padding:20px;border:1px solid var(--line);border-radius:16px;background:#fff;box-shadow:0 8px 30px rgba(2,6,23,.06)}}
  .faq-title{{margin:0 0 14px;font-size:24px;font-weight:900;text-align:center;color:#5c0000}}
  .faq-items{{display:grid;gap:10px}}
  .faq-item{{border:1px solid var(--line);border-radius:14px;background:#f9fafb;overflow:hidden}}
  .faq-q{{cursor:pointer;display:block;padding:14px 16px;font-weight:800;color:#0f172a}}
  .faq-q::-webkit-details-marker{{display:none}}
  .faq-item[open] .faq-q{{background:linear-gradient(180deg, rgba(139,0,0,.08), rgba(139,0,0,.02))}}
  .faq-a{{padding:0 16px 14px;color:#1f2937;line-height:1.6}}
</style>

<script type="application/ld+json">
{ld_json}
</script></div>'''

def cta(h2, sub):
    return f'''<div data-rt-embed-type='true'><section class="ocb ocb-cta" style="margin:30px 0">
  <style>
    html body .post-body .ocb-cta h2, .ocb-cta h2{{color:#fff!important}}
    html body .post-body .ocb-cta .ocb-cta-sub, .ocb-cta .ocb-cta-sub{{color:rgba(255,255,255,.88)!important}}
    html body .post-body .ocb-cta .ocb-cta-chips span, .ocb-cta .ocb-cta-chips span{{color:rgba(255,255,255,.94)!important}}
    html body .post-body .ocb-cta a.ocb-cta-ghost, .ocb-cta a.ocb-cta-ghost{{color:#fff!important;text-decoration:none!important}}
    html body .post-body .ocb-cta a.ocb-cta-gold, .ocb-cta a.ocb-cta-gold{{color:#fbbc04!important}}
    html body .post-body .ocb-cta a.ocb-cta-phone, .ocb-cta a.ocb-cta-phone{{color:#5c0000!important;text-decoration:none!important}}
  </style>
  <div style="background:linear-gradient(135deg,#8B0000,#5c0000);border-radius:20px;padding:28px 24px;color:#fff;text-align:center;box-shadow:0 14px 34px rgba(92,0,0,.3)">
    <h2 style="margin:0 0 6px;color:#fff;font-size:24px;font-weight:900">{h2}</h2>
    <p class="ocb-cta-sub" style="margin:0 0 16px;color:rgba(255,255,255,.85);font-size:16.3px">{sub}</p>
    <div style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap">
      <a class="ocb-cta-phone" href="tel:+14255951079" style="background:#fff;color:#5c0000;border-radius:12px;padding:13px 22px;font-weight:900;text-decoration:none">{PHONE_SVG} (425) 595-1079</a>
      <a class="ocb-cta-ghost" href="/contact" style="background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.4);color:#fff;border-radius:12px;padding:13px 22px;font-weight:800;text-decoration:none">Book My Free Consultation</a>
    </div>
    <div class="ocb-cta-chips" style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-top:16px;font-size:14.1px;color:rgba(255,255,255,.9)">
      <span>✓ Since 2013</span><span>✓ 1,000+ floors</span><span>✓ 1-yr workmanship warranty</span><span>✓ Licensed &amp; insured</span><span>✓ Financing available</span>
    </div>
    <p style="margin:14px 0 0;font-size:14.4px"><a class="ocb-cta-gold" href="https://g.page/r/CR-6MJtUZVexEBM/review" target="_blank" rel="noopener" style="color:#fbbc04;text-decoration:underline">★★★★★ See why 120+ neighbors review us on Google</a></p>
  </div>
</section></div>'''

def related(links):
    parts = ' · '.join(f'<a href="{u}">{t}</a>' for u, t in links)
    return f'<p><strong>Related reading:</strong> {parts}</p>'

def assemble(slug, parts):
    body = CSS + '\n\n' + '\n\n'.join(parts) + '\n\n' + ANIM
    open(slug + '.body.html', 'w').write(body)
    print(slug, 'body chars:', len(body))
    return body
