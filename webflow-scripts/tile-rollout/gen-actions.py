import json, sys
m = json.load(open('rewrite-map.json'))
ids = json.load(open('tile-pageids.json'))
slug = sys.argv[1]; part = sys.argv[2]
# Webflow rate-limits per ACTION, not per call: batches larger than ~15 actions
# can partially fail with 429 inside an HTTP-200 response. Parts 1a/1b/2a/2b
# keep each call at or under 15 actions.
p = json.load(open(f'packs/{slug}.json'))
pid = ids[slug]['pageId']
roles = [k for k in m if not k.startswith('chip') and k != 'carpetLink']
def st(i, el, text):
    return {"label": f"r{i}", "set_text": {"id": {"component": pid, "element": el}, "text": text}}
CHUNKS = {'1a': (0, 15), '1b': (15, 29), '2a': (29, 43), '2b': (43, 57),
          '1': (0, 29), '2': (29, 57)}  # 1/2 kept for back-compat; prefer 1a/1b/2a/2b
if part in CHUNKS:
    lo, hi = CHUNKS[part]
    acts = [st(i + lo, m[r]['el'], p['roles'][r]) for i, r in enumerate(roles[lo:hi])]
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
