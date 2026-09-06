#!/usr/bin/env python3
"""Extract link-like nodes from a saved Webflow get_all_elements tool result (file or stdin).
Usage: extract_links.py <tool-result-file>
Prints JSON: {"trees":[{"label", "links":[...], "todo_links":[...], "embeds":[...], "error"}]}
 links      : Link/Button elements whose target is already known (url/phone/email) + component-instance link props
 todo_links : Link elements with linkType none/missing that have visible text -> need get_settings (all_resolved_settings) to read {mode,to}
 embeds     : HtmlEmbed element ids -> need get_settings to read key "code" and extract <a href> + anchor text
"""
import json,sys,re
def load(path):
    raw=open(path).read()
    try: arr=json.loads(raw)
    except Exception:
        arr=[]; dec=json.JSONDecoder(); i=0
        while i<len(raw):
            j=raw.find('{',i)
            if j<0: break
            try: obj,k=dec.raw_decode(raw,j); arr.append({'text':json.dumps(obj)}); i=k
            except Exception: i=j+1
    out=[]
    for it in arr:
        t=it['text'] if isinstance(it,dict) else it
        s=t.find('{')
        try: d=json.loads(t[s:])
        except Exception: continue
        out.append(d)
    return out
def text_of(n):
    parts=[]
    def w(x):
        if isinstance(x,dict):
            tc=x.get('textContent')
            if isinstance(tc,str): parts.append(tc)
            for c in x.get('children',[]) or []: w(c)
    w(n)
    return re.sub(r'\s+',' ',' '.join(p for p in parts if p)).strip()
def walk(n,acc,todo,embeds):
    if not isinstance(n,dict): return
    t=n.get('type'); st=n.get('settings') or {}; attrs=n.get('attributes') or {}
    link=st.get('link') if isinstance(st,dict) else None
    eid=(n.get('id') or {}).get('element'); ecomp=(n.get('id') or {}).get('component')
    if t=='HtmlEmbed':
        embeds.append({'eid':eid,'ecomp':ecomp})
    if t in ('Link','Button','LinkBlock','NavbarLink') or link is not None or 'href' in attrs:
        lt=(link or {}).get('linkType')
        rec={'eid':eid,'ecomp':ecomp,'type':t,'styles':n.get('styleNames'),'link_type':lt,'href':(link or {}).get('href'),
             'attr_href':attrs.get('href'),'text':text_of(n)[:160]}
        if lt in (None,'none') and not attrs.get('href'):
            todo.append(rec)
        else:
            acc.append(rec)
    if t=='ComponentInstance':
        inst=n.get('instanceDetails') or {}
        for p in inst.get('props',[]) or []:
            pv=p.get('value')
            if isinstance(pv,dict) and ('mode' in pv or 'href' in pv or 'pageId' in pv):
                to=pv.get('to')
                acc.append({'eid':eid,'ecomp':ecomp,'type':'ComponentInstanceProp','component':inst.get('name'),'component_id':inst.get('id'),
                            'prop':p.get('name'),'prop_id':p.get('propId'),'link_type':pv.get('mode') or pv.get('linkType'),
                            'href':pv.get('href') or (to if isinstance(to,str) else None),
                            'page_id':pv.get('pageId') or (to.get('pageId') if isinstance(to,dict) else None),'attr_href':None,
                            'text':' | '.join(str(q.get('value'))[:80] for q in inst.get('props',[]) if isinstance(q.get('value'),str) and 'Text' in str(q.get('name')) or (isinstance(q.get('value'),str) and str(q.get('name')) in ('H1 Heading','Heading')))[:200]})
    for c in n.get('children',[]) or []: walk(c,acc,todo,embeds)
def main():
    path=sys.argv[1]
    res=[]
    for d in load(path):
        label=d.get('label'); r=d.get('result')
        datas=[]
        if isinstance(r,list):
            for x in r:
                if isinstance(x,dict) and 'data' in x: datas.append(x['data'])
        elif isinstance(r,dict) and 'data' in r: datas.append(r['data'])
        acc=[];todo=[];embeds=[]
        for dd in datas: walk(dd,acc,todo,embeds)
        res.append({'label':label,'links':acc,'todo_links':todo,'embeds':embeds,'error':d.get('error')})
    print(json.dumps({'trees':res}))
main()
