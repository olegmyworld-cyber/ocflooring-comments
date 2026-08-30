#!/usr/bin/env python3
"""Report which Blogs CMS items have a post-body that differs from the repo.

The repo is the source of truth for post bodies. Two things knock the CMS copy out
of step: saving a post in the Webflow Editor (the sanitizer strips <section> and
<svg>), and items created without a body because a ~29 KB field does not fit in a
single tool call from a context-limited session.

Usage:
  1) Fetch the collection (3 pages of 100) and save each tool response to a file.
  2) python3 blogs/plan/body_sync.py <response-file> [<response-file> ...]

Prints one line per item needing a push, worst first, and writes .body-sync/<slug>.txt
containing the exact body to send. Push each with update_collection_items using only
`post-body` in fieldData -- one item per call, the body is far too large to batch.
"""
import json, os, sys, glob

OUT = '.body-sync'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_items(path):
    raw = open(path).read()
    try:
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
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    live = {}
    for p in sys.argv[1:]:
        for x in load_items(p):
            live[x['fieldData']['slug']] = x

    os.makedirs(OUT, exist_ok=True)
    for old in glob.glob(os.path.join(OUT, '*')):
        os.remove(old)

    rows = []
    for path in sorted(glob.glob(os.path.join(ROOT, 'blogs', '*.body.html'))):
        slug = os.path.basename(path)[:-len('.body.html')]
        item = live.get(slug)
        if not item:
            continue
        want = open(path).read()
        have = item['fieldData'].get('post-body') or ''
        if have == want:
            continue
        why = 'empty' if not have else ('sanitised' if '<section' not in have else 'stale')
        open(os.path.join(OUT, slug + '.txt'), 'w').write(want)
        rows.append((0 if why == 'empty' else 1, slug, item['id'], why, len(want)))

    rows.sort()
    for _, slug, iid, why, n in rows:
        print(f'{why:10s} {n:6d}  {iid}  {slug}')
    print(f'\n{len(rows)} item(s) need a body push; bodies written to {OUT}/')
    print('in sync:', len(live) - len(rows))


if __name__ == '__main__':
    main()
