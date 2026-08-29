import json,re,collections,random
rows=json.load(open('classified.json'))
city_pages=json.load(open('citypages.json'))

# manual corrections where keyword scoring picked the wrong service
OVERRIDE={
 'carpet-installation-cost-bothell-wa':'carpet-installation',
 'laminate-flooring-installation-cost-seattle-wa':'vinyl-plank-flooring-installation',
 'squeaky-hardwood-floors-refinishing-wont-fix':'hardwood-floor-repair',
 'why-does-my-hardwood-floor-have-gaps':'hardwood-floor-repair',
 'can-you-add-hardwood-to-existing-hardwood-floors':'hardwood-floor-installation',
 'red-oak-vs-white-oak-flooring':'hardwood-floor-installation',
 'american-cherry-hardwood-vs-brazilian-cherry-hardwood':'hardwood-floor-installation',
 'maple-hardwood-flooring-a-durable-and-attractive-option-for-your-home':'hardwood-floor-installation',
 'upkeep-for-carpet-vs-hardwood-flooring':'carpet-installation',
 'hardwood-vs-tile-in-the-kitchen':'tile-installation',
 'what-to-do-when-you-experience-water-damage-in-your-seattle-home-or-business':'hardwood-floor-repair',
 'sun-damaged-hardwood-floors':'hardwood-floor-repair',
 'refinishing-hardwood-floors-with-urine-stains-a-comprehensive-guide':'hardwood-floor-repair',
 'can-you-replace-just-one-piece-of-vinyl-plank-flooring':'vinyl-plank-flooring-installation',
 'our-stair-installation-services':'hardwood-floor-installation',
 'all-about-subfloors-what-you-need-to-know':'hardwood-floor-installation',
 'what-you-need-to-know-about-baseboards':'hardwood-floor-installation',
 'where-to-buy-hardwood-flooring-near-me':'hardwood-floor-installation',
}
for r in rows:
    if r['slug'] in OVERRIDE: r['service']=OVERRIDE[r['slug']]

ADJ={
 'hardwood-floor-refinishing':['hardwood-floor-repair','hardwood-floor-installation'],
 'hardwood-floor-installation':['hardwood-floor-refinishing','vinyl-plank-flooring-installation','tile-installation'],
 'hardwood-floor-repair':['hardwood-floor-refinishing','hardwood-floor-installation'],
 'carpet-installation':['vinyl-plank-flooring-installation','tile-installation','hardwood-floor-installation'],
 'vinyl-plank-flooring-installation':['tile-installation','carpet-installation','hardwood-floor-installation'],
 'tile-installation':['vinyl-plank-flooring-installation','hardwood-floor-installation','carpet-installation'],
}
BIG=['bellevue','seattle','everett','lynnwood','kirkland','redmond','bothell','sammamish','edmonds','mill-creek']

idx={(c['service'],c['city']):c for c in city_pages}
by_service=collections.defaultdict(list)
for c in city_pages: by_service[c['service']].append(c['city'])

use=collections.Counter()          # (service,city) -> how many blog posts link to it
CAP=10                             # stop honouring a topical preference past this many inbound links
MAX_PER_CITY=2                     # at most 2 of a post's 4 links may share one city

idx={(c['service'],c['city']):c for c in city_pages}
by_service=collections.defaultdict(list)
for c in city_pages: by_service[c['service']].append(c['city'])

# posts that actually name a city go first, so their relevant city pages are still
# under CAP when they get picked; generic posts then fill in the spread.
rows.sort(key=lambda r:(0 if r['title_cities'] else (1 if r['body_cities'] else 2), r['service'], r['slug']))

for r in rows:
    svc=r['service']
    prefer=r['title_cities']+[c for c in r['body_cities'] if c not in r['title_cities']]
    links=[]; taken=set(); per_city=collections.Counter()

    def take(service,city):
        links.append((service,city)); use[(service,city)]+=1
        taken.add((service,city)); per_city[city]+=1

    def best(service, prefer_cities):
        """least-linked city for `service`, honouring preferences that aren't capped out"""
        pool=[c for c in by_service[service]
              if (service,c) not in taken and per_city[c]<MAX_PER_CITY]
        if not pool: return None
        for c in prefer_cities:
            if c in pool and use[(service,c)]<CAP: return c
        return min(pool,key=lambda c:(use[(service,c)], BIG.index(c) if c in BIG else 99, c))

    home=[c for c in prefer[:1]]           # the city this post is actually about, if any
    adj=ADJ[svc]
    # 1) the post's own service, in its own city when it names one
    for c in [best(svc, home)]:
        if c: take(svc,c)
    # 2) a neighbouring service in that same city -> the block reads locally for that reader
    c=best(adj[0], home) or best(adj[1] if len(adj)>1 else adj[0], home)
    if c: take(adj[0] if (adj[0],c) not in taken and c in by_service[adj[0]] else adj[1], c)
    # 3) the post's own service again, spread to a different, less-linked city
    c=best(svc, [])
    if c: take(svc,c)
    # 4) one more neighbouring service, spread
    for a in adj[1:]+adj[:1]:
        if len(links)>=4: break
        c=best(a, [])
        if c: take(a,c)
    # top up if any slot could not be filled
    i=0
    while len(links)<4 and i<40:
        for a in [svc]+adj:
            if len(links)>=4: break
            c=best(a, [])
            if c: take(a,c)
        i+=1
    r['links']=[{'service':s,'city':c,'path':idx[(s,c)]['path'],'slug':idx[(s,c)]['slug']} for s,c in links]

# --- coverage repair: every city page must earn at least one inbound blog link ---
# Swap an uncovered page into a post that can legitimately host it, displacing a link
# to an already well-covered page (never one that would drop back to zero).
def linkable(r, service):
    return service==r['service'] or service in ADJ[r['service']]

for _ in range(6):
    zeros=[k for k in idx if use[k]==0]
    if not zeros: break
    for (zs,zc) in zeros:
        done=False
        for r in rows:
            if done or not linkable(r, zs): continue
            cities=collections.Counter(l['city'] for l in r['links'])
            if (zs,zc) in {(l['service'],l['city']) for l in r['links']}: continue
            if cities[zc]>=MAX_PER_CITY: continue
            for i,l in enumerate(r['links']):
                if use[(l['service'],l['city'])]<=2: continue   # don't strip a scarce page
                if l['city']==zc: continue
                use[(l['service'],l['city'])]-=1
                use[(zs,zc)]+=1
                r['links'][i]={'service':zs,'city':zc,'path':idx[(zs,zc)]['path'],'slug':idx[(zs,zc)]['slug']}
                done=True; break

zero=[k for k in idx if use[k]==0]
print('total links:',sum(use.values()))
print('city pages with 0 inbound blog links:',len(zero))
dist=collections.Counter(use[k] for k in idx)
print('inbound-link distribution (links -> #pages):',dict(sorted(dist.items())))
for svc in sorted(by_service):
    tot=sum(use[(svc,c)] for c in by_service[svc])
    mn=min(use[(svc,c)] for c in by_service[svc])
    print(f'  {svc:36s} total={tot:4d} min-per-city={mn}')
json.dump(rows,open('assigned.json','w'),indent=1)
