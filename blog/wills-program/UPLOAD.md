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
6. **Pricing still unconfirmed by Oleg.** Carpet has published labor rates as of 2026-09-16, so
   no post uses the price-free estimator any more. Open: whether $0.99/sq ft stretch-in clears
   the carpet sub's cost, whether stair pricing should split (straight vs winder/open-sided),
   that install rates are labor-only, and the $100 LVP stair price the calculator assumes.

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

## Schedule rebase (2026-09-22)

The Routine sat disabled from 2026-09-16, so 2026-09-17 through 2026-09-22 passed unpublished.
Rather than let the first fire dump six due drafts at once, every scheduled date moved forward
six days: the queue now runs **2026-09-23 to 2027-04-10**, one post per day. `plan.py` start
date changed, all 200 specs re-dated, `uploaded/*.json` refreshed, `SCHEDULE.md` written.

Both CMS date batches were pushed with `scheduled-publish-date` only and no `isDraft`, so draft
status was preserved (100 + 99 items returned, all still drafts).

### Known gap: schema dates inside the bodies

`render.py` writes the spec date into the JSON-LD as `datePublished` / `dateModified`, so the
199 drafts now carry dates six days behind their new slot, and the already-live stairs post
(`6aaafc2d8f4d1f2643a0869a`) still advertises `datePublished: 2027-02-15`, a future date on a
live page. Bodies are ~45 KB each, too large to re-push from the main session in bulk.

The Routine now closes this on its own: on each publish day it re-renders the post and pushes
the fresh `description-big` alongside flipping the item live, so every post goes live with
correct schema dates. The stairs post is fixed on the first run.

### The already-live post

`best-carpet-for-stairs-with-dogs-everett` is post #152, slot 2027-02-21, but Oleg published it
on 2026-09-17. `plan.py` carries an `ALREADY_LIVE` override so its schema dates read the real
publish date and its slot is kept in a `slot` field. Add to that map any other post published
out of order.
