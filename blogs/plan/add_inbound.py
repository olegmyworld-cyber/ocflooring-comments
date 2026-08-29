#!/usr/bin/env python3
"""Give a freshly published post 4 inbound links from already-indexed live posts.

A brand-new post has nothing pointing at it, so Google has little reason to crawl it.
blogs/plan/INBOUND-PLAN.json assigns every one of the 100 new posts 4 donor posts that
are already live and indexed. The links may only be added AFTER the target is live --
linking to a draft serves a 404.

Two steps, run from the repo root:

  1) python3 blogs/plan/add_inbound.py donors <target-slug>
     -> prints the 4 donor slugs, one per line, for the Webflow filter.

  2) Fetch those 4 donors from Webflow (list_collection_items, filter.slug.in = the
     4 slugs). The response is large and gets saved to a file; pass that file here:

     python3 blogs/plan/add_inbound.py merge <target-slug> <webflow-response-file>

     -> writes one small JSON file per donor into .inbound-out/ containing
        {"id", "slug", "city-links"} ready to paste into update_collection_items,
        and prints a one-line summary per donor.

Idempotent: a donor that already links the target is reported as "already linked" and
no payload is written for it.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PLAN = os.path.join(HERE, 'INBOUND-PLAN.json')
OUT = '.inbound-out'
MARK = 'data-oc-guides="1"'
HEAD = '<h3>More floor-care guides</h3>'


def target(slug):
    plan = json.load(open(PLAN))
    t = next((x for x in plan['targets'] if x['slug'] == slug), None)
    if not t:
        sys.exit(f'no inbound-plan entry for {slug}')
    return t


def build(existing, slug, anchor):
    """Append a link to the target inside the guides list, creating it if absent."""
    cl = (existing or '').rstrip()
    href = f'/blog/{slug}'
    if f'href="{href}"' in cl:
        return None                                   # already linked
    li = f'<li><a href="{href}">{anchor}</a></li>'
    m = re.search(r'(<ul[^>]*' + re.escape(MARK) + r'[^>]*>)(.*?)(</ul>)', cl, re.S)
    if m:
        return cl[:m.end(2)] + li + cl[m.end(2):]
    return cl + HEAD + f'<ul role="list" {MARK}>' + li + '</ul>'


def load_items(path):
    """Pull collection items out of a Webflow tool response, whatever shape it came in."""
    raw = open(path).read()
    try:                                              # [{type,text}, ...] envelope
        outer = json.loads(raw)
        if isinstance(outer, list):
            raw = ''.join(e.get('text', '') for e in outer)
    except json.JSONDecodeError:
        pass
    i = raw.find('{"label"')
    d = json.loads(raw[i if i >= 0 else 0:])
    r = d['result'] if 'result' in d else d
    return r['items'] if isinstance(r, dict) else r


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    mode, slug = sys.argv[1], sys.argv[2]
    t = target(slug)

    if mode == 'donors':
        print(','.join(d['slug'] for d in t['donors']))
        return

    if mode != 'merge' or len(sys.argv) < 4:
        sys.exit(__doc__)

    items = {x['fieldData']['slug']: x for x in load_items(sys.argv[3])}
    os.makedirs(OUT, exist_ok=True)
    for old in os.listdir(OUT):
        os.remove(os.path.join(OUT, old))

    ready = []
    for d in t['donors']:
        it = items.get(d['slug'])
        if not it:
            print(f'MISSING  {d["slug"]} -- not in the response'); continue
        new = build(it['fieldData'].get('city-links'), slug, t['name'])
        if new is None:
            print(f'already  {d["slug"]}'); continue
        p = os.path.join(OUT, d['slug'] + '.json')
        json.dump({'id': it['id'], 'slug': d['slug'], 'city-links': new}, open(p, 'w'), indent=1)
        ready.append(it['id'])
        print(f'ready    {d["slug"]} -> {p}')
    print('\nitem ids to publish after updating: ' + json.dumps(ready))


if __name__ == '__main__':
    main()
