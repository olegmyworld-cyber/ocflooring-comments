#!/usr/bin/env python3
"""Analyze workflow extraction output (pages + components) -> issues.json"""
import json,sys,re
sys.path.insert(0,'/tmp/claude-0/-home-user-ocflooring-comments/da842897-cf86-5777-b3b9-c35c0668eca3/scratchpad')
from linkcheck import check,norm_path,ID2PATH,is_live
data=json.load(open(sys.argv[1]))
entries=(data.get('pages') or [])+(data.get('components') or [])
issues=[];stats={'links':0,'pages':len(entries)}
for pg in entries:
    for l in pg.get('links',[]):
        stats['links']+=1
        mode=(l.get('mode') or '').lower(); to=l.get('to') or ''; text=l.get('text') or ''
        target=None
        if mode=='page':
            target=ID2PATH.get(to)
            if target is None:
                issues.append(dict(page=pg['path'],page_id=pg['page_id'],kind='dead-pageid',text=text,target=to,expected=None,why='pageId not found in site pages',**{k:l.get(k) for k in ('where','eid','ecomp','prop_id','prop_name','attr_href')})); continue
        elif mode in ('url','collectionpage','pagesection'):
            target=to
        else:
            continue  # phone/email/file/none
        if mode=='pagesection': continue
        st,exp,why=check(text,target)
        if st in ('dead','mismatch'):
            issues.append(dict(page=pg['path'],page_id=pg['page_id'],kind=st,text=text,target=target,expected=exp,why=why,mode=mode,**{k:l.get(k) for k in ('where','eid','ecomp','prop_id','prop_name','attr_href')}))
        # stale custom href attribute that disagrees with the real link
        ah=l.get('attr_href')
        if ah and target and norm_path(ah)!=norm_path(target):
            issues.append(dict(page=pg['path'],page_id=pg['page_id'],kind='attr-mismatch',text=text,target=target,expected=norm_path(target),why='custom href attribute %s differs from link %s'%(ah,target),mode=mode,**{k:l.get(k) for k in ('where','eid','ecomp','prop_id','prop_name','attr_href')}))
json.dump(issues,open('issues.json','w'),indent=1)
from collections import Counter
print(stats, Counter(i['kind'] for i in issues))
for i in issues: print(i['kind'],'|',i['page'],'|',i.get('where'),'|',i['text'][:50],'|',i['target'],'->',i['expected'],'|',i['why'])
