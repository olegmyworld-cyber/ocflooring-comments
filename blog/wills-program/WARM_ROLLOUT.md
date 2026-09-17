# Warm palette roll-out

`blog/wills-program/warm-rollout.json` is a JSON array of 204 objects:
`{"n": <plan number or 0 for legacy>, "slug": ..., "id": <Webflow item id>, "spec": "specs/NNN-x.json" or "legacy/x.json", "live": false|true}`.

Each agent takes a slice by array index and, for every entry:

1. `python3 blog/wills-program/render.py blog/wills-program/<spec>` → writes `blog/wills-program/out/<slug>.json`.
2. Read that out file with the **Read tool** (cat truncates these ~45 KB single-line files).
3. `update_collection_items` on collection `66cecfc7e7f88d2528ab474e`:
   `{"items":[{"id":"<id>","fieldData":{"description-big":"<body verbatim>"}}]}`.
   Only description-big. Never send isDraft, name, slug, image-main, category or scheduled-publish-date.
4. Verify the response body contains `--bg:#faf6f1` and `background:rgba(234,138,42,.13)`.
5. Rewrite `blog/wills-program/uploaded/<slug>.json` (or `uploaded/legacy-<slug>.json` when `live` is true),
   keeping every existing field, updating `bodyLen` and adding `"warm": true`.

**Nothing is published.** `live: true` entries are already-published posts whose new body waits for the
owner's next Webflow site publish. Post 152 is excluded; it was done first as the preview.


## Verification gotcha (learned 2026-09-17)

The collection holds **206** items: 200 scheduled posts, the 5 legacy rewrites, and the original
Everett refinishing post. A reconciliation that pages `limit:100` at offsets 0 and 100 silently
covers only 200 of them and will report "all clear" while missing six. Always page until
`offset >= pagination.total`, and cross-check the count against `pagination.total` rather than
against an expected number. The laminate post was found cold this way only because its local
record happened to lack the `warm` flag.

## Final reconciliation (2026-09-17)

Paged the whole collection (`limit:100` at offsets 0, 100, 200 — `pagination.total` 206, all 206 fetched)
and compared every stored `description-big` byte-for-byte, by SHA-1, against a fresh `render.py` run of
all 200 specs plus the 5 legacy rewrites, and the hand-maintained `wills-hardwood-floor-refinishing-everett-wa.html`
for the original Everett post.

```
fetched 206 of total 206
missing from CMS: []
body mismatches: 0
cold (missing --bg:#faf6f1 or rgba(234,138,42,.13)): 0
drafts: 199   live: 7
```

The warm palette is on every post. Draft/live status is unchanged: the only live items are the six that
were already live plus the stairs post Oleg published himself.
