import json
rows=json.load(open('assigned.json'))
SVC={'hardwood-floor-refinishing':'Hardwood Floor Refinishing','hardwood-floor-installation':'Hardwood Floor Installation',
     'hardwood-floor-repair':'Hardwood Floor Repair','carpet-installation':'Carpet Installation',
     'vinyl-plank-flooring-installation':'Vinyl Plank Flooring Installation','tile-installation':'Tile Installation'}
cn=lambda c:' '.join(w.capitalize() for w in c.split('-'))
out={}
for r in rows:
    li=''.join(f'<li><a href="{l["path"]}">{SVC[l["service"]]} in {cn(l["city"])}, WA</a></li>' for l in r['links'])
    out[r['id']]=(f'<h3>{SVC[r["service"]]} near you</h3>'
                  f'<p>OC Flooring serves King and Snohomish County. Jump straight to your city:</p>'
                  f'<ul role="list">{li}</ul>')
json.dump(out,open('citylinks.json','w'))
tot=sum(len(v) for v in out.values())
print('items:',len(out),'total chars:',tot,'avg:',tot//len(out),'max:',max(len(v) for v in out.values()))
k=rows[0]['id']; print('\nSAMPLE:\n',out[k])
