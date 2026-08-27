import json, sys
m = json.load(open('rewrite-map.json'))
ids = json.load(open('tile-pageids.json'))
slug = sys.argv[1]; part = sys.argv[2]
p = json.load(open(f'packs/{slug}.json'))
pid = ids[slug]['pageId']
roles = [k for k in m if not k.startswith('chip') and k != 'carpetLink']
def st(i, el, text):
    return {"label": f"r{i}", "set_text": {"id": {"component": pid, "element": el}, "text": text}}
if part == '1':
    acts = [st(i, m[r]['el'], p['roles'][r]) for i, r in enumerate(roles[:29])]
elif part == '2':
    acts = [st(i+29, m[r]['el'], p['roles'][r]) for i, r in enumerate(roles[29:])]
elif part == '3':
    chips = p['chips']
    acts = [st(i, m[f'chip{i+1}']['el'], c) for i, c in enumerate(chips)]
    acts.append(st(99, m['carpetLink']['el'], p['carpetLinkText']))
    acts.append({"label": "clink", "set_link": {"id": {"component": pid, "element": m['carpetLink']['el']},
                 "linkType": "url", "link": ids[slug]['carpetPath']}})
    if len(chips) < 16:
        for i in range(len(chips), 16):
            acts.append({"label": f"rmchip{i+1}", "remove_element": {"id": {"component": pid, "element": m[f'chip{i+1}']['el']}}})
print(json.dumps(acts, ensure_ascii=False))
