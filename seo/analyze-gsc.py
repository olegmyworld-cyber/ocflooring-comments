import json,re
d=json.load(open('gsc12m.json'))['result']
def branded(q): return 'oc flooring' in q or 'nwoc' in q or 'ocflooring' in q
nb=[r for r in d if not branded(r['query'])]

CATS=[
 ('Hardwood refinishing', r'refinish|sand.*(floor|wood)|resurfac'),
 ('Carpet', r'carpet'),
 ('Laminate', r'laminate'),
 ('LVP / vinyl plank', r'vinyl|lvp|lvt'),
 ('Hardwood install', r'hardwood|wood floor|engineered'),
 ('Stain colors', r'stain|duraseal|bona|color'),
 ('Repair', r'repair|fix|replace board|patch'),
 ('Tile', r'tile|porcelain|ceramic'),
 ('Floating floor', r'floating'),
 ('Stairs', r'stair|tread|riser'),
 ('Cost / pricing', r'cost|price|pricing|per square|estimate|how much|cheap|afford'),
]
def cat(q):
    out=[]
    for n,p in CATS:
        if re.search(p,q): out.append(n)
    return out or ['Other']

agg={}
for r in nb:
    for c in cat(r['query']):
        a=agg.setdefault(c,{'i':0,'c':0,'n':0,'ex':[]})
        a['i']+=r['impressions']; a['c']+=r['clicks']; a['n']+=1
        a['ex'].append(r)
print('=== CATEGORY DEMAND (12 mo, non-branded) ===')
for c,a in sorted(agg.items(),key=lambda x:-x[1]['i']):
    a['ex'].sort(key=lambda r:-r['impressions'])
    avgpos=sum(r['position']*r['impressions'] for r in a['ex'])/a['i']
    print(f"{c:22s} impr={a['i']:7d} clicks={a['c']:4d} queries={a['n']:4d} avgpos={avgpos:5.1f}")
    print('     top:', ' | '.join(r['query'] for r in a['ex'][:5]))

CITIES=['seattle','bellevue','everett','lynnwood','redmond','monroe','marysville','kirkland','bothell','edmonds','snohomish','mill creek','shoreline','renton','issaquah','sammamish','mukilteo','arlington','woodinville','tacoma','kent','lake stevens','stanwood','granite falls','duvall','carnation','north bend','burlington','mount vernon','bellingham','anacortes','camano','oak harbor','puyallup','federal way','auburn','bremerton']
print()
print('=== CITY DEMAND ===')
cg={}
for r in nb:
    for c in CITIES:
        if c in r['query']:
            a=cg.setdefault(c,{'i':0,'c':0,'n':0,'ex':[]})
            a['i']+=r['impressions']; a['c']+=r['clicks']; a['n']+=1; a['ex'].append(r)
for c,a in sorted(cg.items(),key=lambda x:-x[1]['i'])[:25]:
    a['ex'].sort(key=lambda r:-r['impressions'])
    print(f"{c:16s} impr={a['i']:7d} clicks={a['c']:4d} q={a['n']:4d}  top: {a['ex'][0]['query']}")
