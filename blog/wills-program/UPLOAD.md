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

1. **Hero images.** Every scheduled post has an empty Image Main. The daily Routine holds a
   post rather than publishing it when the image is missing, and names the slug.
2. **Site publish.** The template hero change (image right, text left) and the five updated
   legacy bodies only reach the live site after a Webflow publish. Close Designer tabs first:
   an open tab once overwrote a post body on publish.
3. **Dead CSS.** `blog/wills-hardwood-floor-refinishing-everett-wa.html` (CMS item
   `6aa9c8c879f234ee20d70b90`) still carries a per-post hero override targeting
   `.section_hero.is-default`. The template elements now carry `blog-hero*` classes only, so
   after the site publish that override matches nothing. Harmless, but it can be stripped
   once the publish has happened. Do not strip it before, or the live post loses its hero.
4. **Pricing gaps.** Carpet posts use the price-free estimator because Wills publishes no
   carpet rate. Confirm carpet pricing, that install rates are labor-only, and the $100 LVP
   stair price the calculator assumes.
