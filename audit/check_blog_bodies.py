#!/usr/bin/env python3
"""Check links in blog bodies (repo queue or CMS export). Usage: check_bodies.py repo|cms"""
import json,re,sys,os,glob
sys.path.insert(0,'/tmp/claude-0/-home-user-ocflooring-comments/da842897-cf86-5777-b3b9-c35c0668eca3/scratchpad')
from linkcheck import check,is_live,norm_path
S='/tmp/claude-0/-home-user-ocflooring-comments/da842897-cf86-5777-b3b9-c35c0668eca3/scratchpad'
cms=json.load(open(S+'/cms_slugs.json'))
live_blog=set(cms['blog'])
plan={p['slug']:p for p in json.load(open(S+'/futureblogs/PLAN.json'))}
redir={}
for line in open('/home/user/ocflooring-comments/redirects/redirects.csv'):
    a,b=line.strip().split(',',1); redir[a]=b
mode=sys.argv[1]
posts=[]
if mode=='repo':
    for m in sorted(glob.glob(S+'/futureblogs/repo/*.meta.json')):
        meta=json.load(open(m)); slug=meta['slug']
        bf=m.replace('.meta.json','.body.html')
        body=open(bf).read() if os.path.exists(bf) else ''
        posts.append(dict(slug=slug,date=meta.get('publish_date') or plan.get(slug,{}).get('publish_date'),body=body,city=meta.get('city-links',''),draft=slug not in live_blog))
else:
    for line in open(S+'/futureblogs/items.jsonl'):
        it=json.loads(line)
        posts.append(dict(slug=it['slug'],date=(it.get('publish_date') or plan.get(it['slug'],{}).get('publish_date') or (it.get('lastPublished') or '')[:10]),body=it.get('post_body') or '',city=it.get('city_links') or '',draft=bool(it.get('isDraft')),archived=bool(it.get('isArchived'))))
all_slugs=live_blog|set(plan)|{p['slug'] for p in posts}
pdate={p['slug']:p['date'] for p in posts}; pdate.update({s:plan[s]['publish_date'] for s in plan})
A=re.compile(r'<a\b[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>',re.S|re.I)
issues=[];n=0;nl=0
for p in posts:
    n+=1
    for field,html in (('body',p['body']),('city-links',p['city'])):
        for href,inner in A.findall(html or ''):
            nl+=1
            text=re.sub(r'<[^>]+>','',inner); text=re.sub(r'\s+',' ',text).strip()
            h=href.strip()
            if h.startswith(('tel:','mailto:','#','javascript:')): continue
            if re.match(r'https?://',h):
                m=re.match(r'https?://(www\.)?nwocflooring\.com(/[^?#]*)?',h)
                if not m: continue
                h=m.group(2) or '/'
            path=norm_path(h.split('?')[0].split('#')[0]) or '/'
            def add(kind,why,exp=None): issues.append(dict(post=p['slug'],date=p['date'],draft=p['draft'],field=field,text=text[:70],href=href,kind=kind,why=why,expected=exp))
            if path.startswith('/blog/'):
                s=path[len('/blog/'):].strip('/')
                if s in live_blog: pass
                elif s in all_slugs:
                    d=pdate.get(s)
                    if p['date'] and d and d>p['date']: add('blog-future','target post scheduled %s, after this post (%s)'%(d,p['date']))
                    elif not p['draft']: add('blog-draft','target post is still a draft; live post links to it')
                else: add('dead','no blog post with this slug'+(' (redirected to %s)'%redir[path] if path in redir else ''))
                continue
            if not is_live(path):
                add('dead','not a live page'+(' (redirect covers it -> %s)'%redir[path] if path in redir else ''))
                continue
            st,exp,why=check(text,path)
            if st in ('mismatch','dead'): add(st,why,exp)
from collections import Counter
print('posts',n,'links',nl,Counter(i['kind'] for i in issues))
json.dump(issues,open(S+'/futureblogs/issues_%s.json'%mode,'w'),indent=1)
for i in issues: print(i['kind'],'|',i['post'],i['date'],'draft' if i['draft'] else 'LIVE','|',i['field'],'|',i['text'][:45],'|',i['href'],'|',i['why'])
