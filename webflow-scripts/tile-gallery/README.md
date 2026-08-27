# Tile gallery page — source of record

Live page: `/tile-gallery` (page id `6a8fb630bf19a48fafa6a9e5`, site
`6377e8e6a53936b48ef1cad0`). Built 2026-08-27 from the Claude Design file
`Tile Gallery.dc.html` in Oleg's `Carpet_mobile_showroom_service_design.zip`.

## Files
- `gallery-projects.json` — the 21 project entries as extracted from the design
  (id, category, materials line, title, body, alt text), in display order.
- `gallery-asset-ids.json` — slug → Webflow asset id for the 21 uploaded photos.
  Hosted at
  `https://s3.amazonaws.com/webflow-prod-assets/6377e8e6a53936b48ef1cad0/<id>_tile-gallery-<slug>.webp`.
- `ocpqboost-target-pages.json` — the 91 pages the `ocpqBoost` script is applied
  to (30 tile, 30 carpet, 31 hardwood-repair incl. `/services/flooring-repair`).

## Page structure (classes prefixed `tg-`)
breadcrumb → hero + 3 stat cards → sticky category filter bar → 21-figure grid
→ dark CTA → footer. The design's dev-only "Adding your photos" bar was
deliberately omitted (the design itself says "Turn this bar off before
publishing").

Category counts, which the filter chips display: All 21 · Showers & Tubs 6 ·
Bath Walls 9 · Backsplash 3 · Floors 2 · Features 1.

## Script
`webflow-scripts/tilegalleryfontsfilter-1.0.1.js` — registered inline as
`tilegalleryfontsfilter` 1.0.1, applied at the page footer. Loads Instrument
Serif + Archivo, adds the canonical `https://www.nwocflooring.com/tile-gallery`,
gives `.tg-page` clearance under the fixed navbar, and drives the category
filter (click + Enter/Space, `aria-pressed`, `role="button"`).

The filter chips were authored as `<button>` but Webflow's WHTML builder turns
them into Link elements, so the script supplies the button semantics and calls
`preventDefault()` on click.

## Canonical / breadcrumb note
The design's canonical was `/our-work/tile-gallery`, but **`/our-work` does not
exist on this site** — it is neither a page nor a folder (checked all 221 page
entries), which is why the tile pages' "Full gallery →" and footer "Gallery"
links were dead. The page therefore lives at the root as `/tile-gallery`, and
the JSON-LD breadcrumb is Home → Tile Installation (Bellevue) → Tile Gallery.
Root also keeps it clear of the per-city folder wildcard 301s that were catching
the city URLs.
