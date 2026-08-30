#!/usr/bin/env python3
"""Hard gate for tile/carpet posts. Usage: python3 blogs/plan/tc_validate.py <slug>
Exits non-zero with reasons on any failure. Run from anywhere."""
import json, re, sys, os, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
os.chdir(ROOT)

slug = sys.argv[1]
plan = json.load(open('blogs/plan/TILE-CARPET-PLAN.json'))
rows = {r['slug']: r for s in ('tile', 'carpet') for r in plan[s]}
me = rows[slug]
body = open(f'blogs/{slug}.body.html').read()
meta = json.load(open(f'blogs/{slug}.meta.json'))
CSS = open('blogs/src/shared_css.html').read()
core = body[len(CSS):] if body.startswith(CSS) else None

refin = {p['slug']: p['publish_date'] for p in json.load(open('blogs/plan/PLAN.json'))}
tc = {r['slug']: r['publish_date'] for s in ('tile', 'carpet') for r in plan[s]}
existing = set(open('blogs/plan/EXISTING-SLUGS.txt').read().split())
svc_pages = set(plan['service_pages'].values())
pages_ok = svc_pages | set(open('blogs/plan/VALID-PAGE-PATHS.txt').read().split()) | {'/contact'}

errs = []
if core is None:
    errs.append('body does not start with the exact shared CSS block (regenerate via builder)')
    core = body

for L in set(re.findall(r'href="([^"]+)"', body)):
    if L.startswith(('tel:', 'https://g.page')):
        continue
    if L.startswith('/blog/'):
        s = L[6:]
        if s in existing:
            continue
        d = refin.get(s) or tc.get(s)
        if d and d < me['publish_date']:
            continue
        errs.append(f'bad blog link (missing, or publishes on/after this post): {L}')
    elif L.startswith('/'):
        if L not in pages_ok:
            errs.append(f'bad page link (not a verified path): {L}')
    else:
        errs.append(f'unexpected link: {L}')

blog_links = {m for m in re.findall(r'href="(/blog/[^"]+)"', body)}
if len(blog_links) < 4:
    errs.append(f'only {len(blog_links)} blog-to-blog links; need >= 4')
if 'href="/contact"' not in body:
    errs.append('missing /contact link')

own = me.get('own_service_page')
if own and f'href="{own}"' not in body:
    errs.append(f'must link own city service page {own}')
if not own:
    svc = me['service']
    if not re.search(rf'href="/[^"]*/{svc}-installation-in-[a-z-]+-wa"', body):
        errs.append(f'general post must link at least one {svc} service page')

cl = meta.get('city-links', '')
cl_links = re.findall(r'href="([^"]+)"', cl)
if len(cl_links) < 4 or any(h not in svc_pages for h in cl_links):
    errs.append('city-links must hold 4+ links, all verified service pages of this service')
if own and own not in cl_links:
    errs.append('city-links must include the own-city service page')

d = datetime.date.fromisoformat(me['publish_date'])
badge = d.strftime('%B %-d, %Y')
if badge not in body: errs.append(f'date badge text "{badge}" not in body')
if '#16a34a' not in body: errs.append('green date pill missing')
if not meta.get('post-summary', '').startswith(badge + ' ·'):
    errs.append(f'post-summary must start with "{badge} ·"')
if meta.get('publish_date') != me['publish_date']: errs.append('meta publish_date mismatch')
if meta.get('blog-category') != me['blog-category']: errs.append('meta blog-category mismatch')
if meta.get('slug') != slug or meta.get('name') != me['title']:
    errs.append('meta name/slug must match the plan exactly')
if len(meta.get('title-tag', '')) > 60: errs.append('title-tag > 60 chars')
if not 40 <= len(meta.get('meta-description', '')) <= 160: errs.append('meta-description not 40-160 chars')

h2s = len(re.findall(r'<h2', core))
if not 5 <= h2s <= 10: errs.append(f'{h2s} h2s; want 5-10')
faqs = len(re.findall(r'<details', core))
if not 7 <= faqs <= 9: errs.append(f'{faqs} FAQ items; want 7-9')
words = len(re.sub(r'<[^>]+>', ' ', core).split())
if words < 1500: errs.append(f'only ~{words} words; need >= 1500')
if '<section' in body: errs.append('<section> present - Webflow Editor strips it')
if re.search(r'<svg\b', core): errs.append('raw <svg> in body - Webflow Editor strips it')
for token, why in [('ocb-eyebrow', 'quick-answer card'), ('ocb-facts', 'facts grid'),
                   ('faq-items', 'FAQ block'), ('"@type": "FAQPage"', 'FAQPage JSON-LD'),
                   ('ocb-cta', 'CTA block'), ('Related reading', 'related links'),
                   ('ocb-anim-ready', 'reveal animation')]:
    if token not in body: errs.append(f'missing {why}')
if not ('ocb-table' in body or 'ocb-2col' in body): errs.append('need a table or 2-col block')

if errs:
    print(f'FAIL {slug}'); [print('  -', e) for e in errs]; sys.exit(1)
print(f'OK {slug} ({words} words, {h2s} h2s, {faqs} FAQs, {len(blog_links)} blog links)')
