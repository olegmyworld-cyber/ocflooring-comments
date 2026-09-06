#!/usr/bin/env python3
"""Rules: does a link's text agree with its destination? Shared by CMS + page audits."""
import json,re,html
BASE='/tmp/claude-0/-home-user-ocflooring-comments/da842897-cf86-5777-b3b9-c35c0668eca3/scratchpad/'
LIVE=set(open(BASE+'live_paths.txt').read().split('\n'))|{'/'}
SLUGS=json.load(open(BASE+'cms_slugs.json'))
PAGES=json.load(open(BASE+'pages.json'))
ID2PATH={p['id']:(p['publishedPath'] or '/') for p in PAGES}
FOLDER={}  # city key -> (folder, suffix)
for p in LIVE:
    m=re.match(r'^/(city-of-[a-z-]+|seattle|arlington|hardwood-floor-refinishing)/([a-z-]+?)(?:-in-([a-z-]+)-wa)?$',p)
    if not m: continue
    f=m.group(1)
    if f=='arlington': FOLDER['arlington']=('arlington','')
    elif f=='seattle': FOLDER['seattle']=('seattle','seattle')
    elif f=='hardwood-floor-refinishing': FOLDER['bothell']=('hardwood-floor-refinishing','bothell')
    elif f=='city-of-new-castle': FOLDER['newcastle']=('city-of-new-castle','newcastle')
    else: FOLDER[f[8:]]=(f,f[8:])
CITY_NAMES={k:k.replace('-',' ') for k in FOLDER}
CITY_NAMES['newcastle']='newcastle'
SVC_ORDER=['tile-installation','carpet-installation','hardwood-floor-refinishing','hardwood-floor-repair','vinyl-plank-flooring-installation','hardwood-floor-installation']
HUB={'tile-installation':'/flooring-services-near-me/tile-installation','carpet-installation':'/flooring-services-near-me/carpet-installation',
     'hardwood-floor-refinishing':'/flooring-services-near-me/floor-refinishing','hardwood-floor-repair':'/flooring-services-near-me/flooring-repair',
     'vinyl-plank-flooring-installation':'/flooring-services-near-me/vinyl-plank-flooring-and-laminate-flooring','hardwood-floor-installation':'/flooring-services-near-me/hardwood-floor-installation'}
def norm_path(p):
    if not p: return p
    p=p.strip()
    p=re.sub(r'^https?://(www\.)?nwocflooring\.com','',p)
    p=p.split('#')[0].split('?')[0]
    if p=='' : return '/'
    if not p.startswith('/'): return p
    p=re.sub(r'/+$','',p) or '/'
    return p.lower()
def is_internal(p): return isinstance(p,str) and p.startswith('/')
def is_live(p):
    p=norm_path(p)
    if p in LIVE: return True
    parts=p.strip('/').split('/')
    if len(parts)==2 and parts[0] in SLUGS and parts[1] in SLUGS[parts[0]]: return True
    if len(parts)==1 and parts[0] in ('blog','gallery','vinyl-gallery','product','category','sku','blog-category'): return True
    return False
def svc_of_path(p):
    p=norm_path(p)
    m=re.match(r'^/(city-of-[a-z-]+|seattle|arlington|hardwood-floor-refinishing)/([a-z-]+?)(?:-in-[a-z-]+-wa)?$',p)
    if m:
        s=m.group(2)
        return s if s in SVC_ORDER else None
    for k,v in HUB.items():
        if p==v: return k
    if p=='/flooring-services-near-me/laminate-flooring-installation': return 'vinyl-plank-flooring-installation'
    return None
def city_of_path(p):
    p=norm_path(p)
    m=re.match(r'^/(city-of-[a-z-]+|seattle|arlington|hardwood-floor-refinishing)/([a-z-]+?)(?:-in-([a-z-]+)-wa)?$',p)
    if not m: return None
    f=m.group(1)
    if f=='arlington': return 'arlington'
    if f=='seattle': return 'seattle'
    if f=='hardwood-floor-refinishing': return 'bothell' if svc_of_path(p) else None
    if f=='city-of-new-castle': return 'newcastle'
    return f[8:]
def svc_of_text(t):
    t=t.lower()
    if re.search(r'\btile',t): return 'tile-installation'
    if re.search(r'\bcarpet',t): return 'carpet-installation'
    if re.search(r'refinish|sand(ing)? (and|&) (re)?finish|screen (and|&) recoat|buff (and|&) (re)?coat|recoat',t): return 'hardwood-floor-refinishing'
    if re.search(r'\brepair',t): return 'hardwood-floor-repair'
    if re.search(r'vinyl|\blvp\b|laminate|waterproof floor',t): return 'vinyl-plank-flooring-installation'
    if re.search(r'hardwood (floor(ing)? )?install|floor installation|install(ation)? (of )?(new )?(solid|engineered|hardwood|wood)|new hardwood|hardwood floors? in\b|hardwood flooring (services )?in\b',t): return 'hardwood-floor-installation'
    return None
CITY_RE=re.compile(r'\b(bellevue|seattle|kirkland|newcastle|new castle|everett|marysville|shoreline|sammamish|arlington|snohomish|issaquah|whidbey island|monroe|snoqualmie|lake stevens|mukilteo|kenmore|north bend|edmonds|mill creek|medina|bothell|woodinville|mercer island|oak harbor|duvall|redmond|renton|lynnwood|cottage lake)\b',re.I)
def city_of_text(t):
    m=CITY_RE.search(t or '')
    if not m: return None
    return m.group(1).lower().replace('new castle','newcastle').replace(' ','-')
def expected(city,svc):
    if city not in FOLDER: return None
    f,suf=FOLDER[city]
    return '/%s/%s'%(f,svc) if suf=='' else '/%s/%s-in-%s-wa'%(f,svc,suf)
def check(text,target):
    """Return (status, expected, reason). status in ok|dead|mismatch|unknown"""
    t=norm_path(target) if isinstance(target,str) else target
    if not is_internal(t or ''): return ('external' if t else 'none',None,'')
    if not is_live(t): return ('dead',None,'target is not a live page')
    if re.match(r'^/(blog|gallery|vinyl-gallery|product|category|sku|blog-category)(/|$)',t): return ('ok',None,'content link')
    if t=='/': t='/city-of-bellevue/hardwood-floor-refinishing-in-bellevue-wa'  # home page is the Bellevue refinishing landing page
    tc,ts=city_of_text(text),svc_of_text(text)
    pc,ps=city_of_path(t),svc_of_path(t)
    if ts and tc:
        exp=expected(tc,ts)
        if exp=='/city-of-bellevue/hardwood-floor-refinishing-in-bellevue-wa': exp='/'
        if exp and exp!=t and not (exp=='/' and t=='/city-of-bellevue/hardwood-floor-refinishing-in-bellevue-wa'): return ('mismatch',exp,'text says %s in %s'%(ts,tc))
    elif ts and not tc:
        if ps and ps!=ts: return ('mismatch',HUB[ts],'text says %s but target is %s'%(ts,ps))
    elif tc and not ts:
        # text is a city name only: target should be that city's page (any service) 
        if pc and pc!=tc: return ('mismatch',None,'text says %s but target city is %s'%(tc,pc))
    return ('ok',None,'')
if __name__=='__main__':
    import sys
    for a in sys.argv[1:]:
        t,u=a.split('=>'); print(a,check(t,u))
