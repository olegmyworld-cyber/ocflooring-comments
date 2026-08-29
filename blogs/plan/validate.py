import json, re, sys, os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
slug = sys.argv[1]
plan = {p['slug']: p for p in json.load(open('blogs/plan/PLAN.json'))}
me = plan[slug]
body = open(f'blogs/{slug}.body.html').read()
meta = json.load(open(f'blogs/{slug}.meta.json'))
existing = set(open('blogs/plan/EXISTING-SLUGS.txt').read().split())
pages = {p['slug'] for p in json.load(open('blogs/plan/pages_index.json')) if p['slug']}
errs = []
# links
for L in set(re.findall(r'href="([^"]+)"', body)):
    if L.startswith(('tel:', 'https://g.page')): continue
    elif L.startswith('/blog/'):
        s = L[6:]
        if s in existing: continue
        if s in plan and plan[s]['publish_date'] < me['publish_date']: continue
        errs.append(f'bad blog link (missing or scheduled later): {L}')
    elif L.startswith('/'):
        if L[1:] not in pages: errs.append(f'bad page link: {L}')
    else: errs.append(f'unexpected link: {L}')
blog_links = {L[6:] for L in set(re.findall(r'href="(/blog/[^"]+)"', body))}
if len(blog_links) < 4: errs.append(f'only {len(blog_links)} blog-to-blog links; need >= 4')
city = me.get('city')
NO_PAGE = {'Bellevue'}
if city and city not in NO_PAGE:
    cslug = 'hardwood-floor-refinishing-in-' + city.lower().replace(' ', '-') + '-wa'
    if f'href="/{cslug}"' not in body: errs.append(f'must link own city service page /{cslug}')
if not re.search(r'href="/hardwood-floor-refinishing', body): errs.append('no city refinishing page link')
if '/contact' not in body: errs.append('no /contact link')
# structure
from datetime import date
y,m,d = map(int, me['publish_date'].split('-'))
D = date(y,m,d).strftime('%B ') + str(d) + f', {y}'
if f'>{D}</span>' not in body: errs.append(f'date badge must show "{D}"')
if '16a34a' not in body: errs.append('green date badge missing')
for frag,label in [('Quick answer','quick answer card'),('ocb-facts','facts grid'),('faq-wrap','FAQ'),
                   ('application/ld+json','JSON-LD'),('ocb-cta','CTA'),('Related reading','related links'),
                   ('IntersectionObserver','anim footer')]:
    if frag not in body: errs.append(f'missing {label}')
if not (4 <= body.count('<h2>') <= 8): errs.append(f'h2 count {body.count("<h2>")} outside 4-8')
if ('ocb-table' not in body) and ('ocb-2col' not in body): errs.append('needs a table or 2-col block')
faqn = body.count('faq-item" role="listitem"')
if not (7 <= faqn <= 9): errs.append(f'FAQ count {faqn} outside 7-9')
# meta
if not meta['post-summary'].startswith(D + ' · '): errs.append(f'summary must start "{D} · "')
if len(meta['title-tag']) > 60: errs.append(f'title-tag {len(meta["title-tag"])} > 60')
if len(meta['meta-description']) > 160: errs.append(f'meta-description {len(meta["meta-description"])} > 160')
if meta['blog-category'] != me['category']: errs.append('wrong category id')
if meta['slug'] != slug or meta['name'] != me['name']: errs.append('meta name/slug mismatch with PLAN')
wc = len(re.sub(r'<[^>]+>',' ',body).split())
if wc < 1500: errs.append(f'too short: ~{wc} words incl. components')
if errs:
    print(f'FAIL {slug}'); [print('  -', e) for e in errs]; sys.exit(1)
print(f'OK {slug}')
