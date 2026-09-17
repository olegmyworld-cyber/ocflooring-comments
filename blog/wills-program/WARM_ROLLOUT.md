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
