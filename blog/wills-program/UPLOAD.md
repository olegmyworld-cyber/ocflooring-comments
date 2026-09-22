# Uploading rendered posts to Webflow (Wills Flooring)

`render.py` writes `out/<slug>.json`, a ready `fieldData` object for the Blog Posts collection
(`66cecfc7e7f88d2528ab474e`, site `66cc1f4542ee0c42e43d0303`).

Create (new scheduled posts), always as drafts:

```
data_cms_tool → create_collection_items
  collection_id: 66cecfc7e7f88d2528ab474e
  request: { isDraft: true, fieldData: [ <contents of out/<slug>.json> ] }
```

Update (legacy posts; manifest contains "id"):

```
data_cms_tool → update_collection_items
  collection_id: 66cecfc7e7f88d2528ab474e
  request: { items: [ { id: <id>, fieldData: { description-small, description-big, time-to-read } } ] }   # omit isDraft to keep live status
```

Rules
- One item per call is safest (bodies are 40–60 KB). Never set isDraft false on new posts; the daily Routine does that.
- After each create, list the item by slug and confirm `description-big` length equals the local file length.
- Slugs must be unique; if a create fails with a slug conflict, check whether the item already exists before retrying.
- Image Main is left empty on purpose: the owner adds hero photos in the Webflow Editor.

## Status (2026-09-16)

All 200 scheduled posts are in the Blog Posts collection as drafts, verified byte-for-byte
against `out/<slug>.json`, with correct `scheduled-publish-date` and no Image Main. Item ids
are in `uploaded/<slug>.json`. The five legacy posts were updated in place: still live, hero
images and slugs untouched, bodies replaced with the new design (`uploaded/legacy-*.json`).

Open items for the owner:

1. **Hero images.** As of 2026-09-22 every scheduled post through **2026-11-14** has an Image
   Main (59 in a row, no gaps), so the queue has about eight weeks of runway. Later dates are
   still patchy. The daily Routine holds a post rather than publishing it when the image is
   missing, and names the slug. `HERO_IMAGES_NEEDED.md` is the 2026-09-17 snapshot and is stale.

2. **Six dates already passed unused.** The plan started 2026-09-17; the Routine has been
   disabled since 2026-09-16, so 2026-09-17 through 2026-09-22 came and went as drafts. On its
   first fire the Routine publishes every *due* draft, which would push all six live in one day.
   Either accept the batch or shift `scheduled-publish-date` forward before enabling it.
4. **Site publish.** The template hero change (image right, text left) and the five updated
   legacy bodies only reach the live site after a Webflow publish. Close Designer tabs first:
   an open tab once overwrote a post body on publish.
5. **Dead CSS.** `blog/wills-hardwood-floor-refinishing-everett-wa.html` (CMS item
   `6aa9c8c879f234ee20d70b90`) still carries a per-post hero override targeting
   `.section_hero.is-default`. The template elements now carry `blog-hero*` classes only, so
   after the site publish that override matches nothing. Harmless, but it can be stripped
   once the publish has happened. Do not strip it before, or the live post loses its hero.
4. **Pricing gaps.** Carpet posts use the price-free estimator because Wills publishes no
   carpet rate. Confirm carpet pricing, that install rates are labor-only, and the $100 LVP
   stair price the calculator assumes.

## Carpet repricing (2026-09-16)

Carpet labor was published for the first time after market research across King and Snohomish
County, deliberately set at the low end: $0.99/sq ft stretch-in, $1.29 glue-down, $30 per step,
$0.45/sq ft removal and haul-away, $0.25/sq ft furniture, 500 sq ft minimum. All 50 carpet posts
moved off the price-free estimator onto the carpet calculator and were re-pushed to Webflow in
place, still as drafts. All 200 stored bodies were then re-verified byte-for-byte against a fresh
local render.

The rate lives in one place, `CALC["carpet"]` in render.py. To change it: edit that entry, re-render,
and re-push the 50 carpet items. The posts quote the numbers in prose too, so a change of more than a
few cents also needs the carpet specs revised.

**Publishing is PAUSED.** Routine `trig_01W2ziMwdhrCCpEf7xKPJShg` is disabled at the owner's request.
Re-enable it only when the owner says go.
