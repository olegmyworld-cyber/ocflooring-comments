import json,re,collections
items=json.load(open('blogs.json'))
city_pages=json.load(open('citypages.json'))

SERVICES={
 'carpet-installation':      dict(t=[('carpet',6),('restretch',5),('mohawk',4),('berber',4)], b=[('carpet',1)]),
 'tile-installation':        dict(t=[('tile',6),('shower',5),('backsplash',5),('grout',5),('porcelain',4)], b=[('tile',1),('grout',1)]),
 'vinyl-plank-flooring-installation': dict(t=[('vinyl',6),('lvp',6),('spc',6),('laminate',5),('floating floor',5),('waterproof',3)], b=[('vinyl',1),('laminate',1)]),
 'hardwood-floor-repair':    dict(t=[('repair',6),('gaps',5),('squeak',5),('scratch',4),('water damage',5),('water ring',4),('heat mark',4),('spot fix',5),('patch',4),('cupping',4),('white cloudy',4),('sticky',3),('worn traffic',4)], b=[('repair',1)]),
 'hardwood-floor-installation': dict(t=[('installation',5),('install',4),('engineered',5),('solid hardwood',5),('subfloor',5),('baseboard',3),('new floor',4),('prefinished',3),('pre-finished',3),('where to buy',4),('wood for your home',4),('stair',4)], b=[('installation',1)]),
 'hardwood-floor-refinishing': dict(t=[('refinish',7),('recoat',6),('sanding',6),('sand',4),('screen',5),('stain',5),('finish',4),('buff',5),('dustless',5),('polyurethane',5),('bona',5),('pallmann',5),('urine',4),('sun damage',4),('parquet',4),('fir floor',4),('pine floor',4),('hickory',4),('wide plank',4),('trio',4)], b=[('refinish',1),('sanding',1)]),
}
CITIES=sorted({c['city'] for c in city_pages})
CITY_ALIASES={c:c.replace('-',' ') for c in CITIES}

def norm(s): return re.sub(r'\s+',' ',(s or '').lower())

def strip_html(h): return re.sub(r'<[^>]+>',' ',h or '')

rows=[]
for it in items:
    fd=it['fieldData']
    title=norm(fd.get('name'))+' '+norm(fd.get('slug','').replace('-',' '))
    body=norm(strip_html(fd.get('post-body')))
    scores={}
    for svc,kw in SERVICES.items():
        s=0
        for k,w in kw['t']: s+=title.count(k)*w
        for k,w in kw['b']: s+=min(body.count(k),25)*w*0.35
        scores[svc]=s
    best=max(scores,key=scores.get)
    # city mentions, title first
    tc=[c for c in CITIES if CITY_ALIASES[c] in title]
    bc=collections.Counter()
    for c in CITIES:
        n=body.count(CITY_ALIASES[c])
        if n: bc[c]=n
    rows.append(dict(id=it['id'],slug=fd['slug'],name=fd.get('name'),draft=bool(it.get('isDraft')),
                     service=best,scores={k:round(v,1) for k,v in sorted(scores.items(),key=lambda x:-x[1])[:3]},
                     title_cities=tc,body_cities=[c for c,_ in bc.most_common(8)]))
json.dump(rows,open('classified.json','w'),indent=1)
cnt=collections.Counter(r['service'] for r in rows)
print(cnt)
print()
for r in sorted(rows,key=lambda r:r['service']):
    print(f"{r['service'][:26]:27s} {'DRAFT' if r['draft'] else '     '} {r['slug'][:62]:63s} {r['title_cities']}")
