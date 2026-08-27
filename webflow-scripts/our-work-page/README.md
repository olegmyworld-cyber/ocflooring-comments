# Our Work page — mobile-only slider for gallery categories (2026-08-27)

Request: "for only mobile version only do as slider hardwood floor
refinishing and flooring installation categories" — a screenshot of the
`/our-work` page's "Hardwood Floor Refinishing" section (14 projects, 3-up
grid) with the request to make it (and the "Flooring Installation"
category) a slider on mobile only.

## Where this lives

The `/our-work` page (page id `65f32565e111adbbb806d079`) renders its
entire gallery — both category sections — from a single native `HtmlEmbed`
element (id `7a1aafb3-cc09-566b-0b88-6c2fa30911c0`) containing self-contained
HTML/CSS/JS: a `DATA` array with two entries, `"Hardwood Floor
Refinishing"` (14 photos) and `"Flooring Installation"` (15 photos), each
rendered into its own `<section class="ocw-sec">` with a `.ocw-grid` photo
grid and a fullscreen lightbox viewer. Both categories share the same
`.ocw-grid`/`.ocw-card` classes, so one CSS change covers both — exactly
the two categories the request named.

## Fix

Added a new `@media(max-width:767px)` block (site's established mobile
breakpoint, used throughout this session) that converts `.ocw-grid` from
CSS grid to a horizontal scroll-snap slider — `display:flex`,
`overflow-x:auto`, `scroll-snap-type:x mandatory`, cards at `flex:0 0 82%`
with `scroll-snap-align:center` — leaving the existing `@media(max-width:
900px)` 2-column tablet rule and the default 3-column desktop grid
completely untouched (the new rule comes after it in source order and only
applies at ≤767px, so it cleanly overrides without needing to edit the
900px block).

**Verified in headless Chromium** against a byte-for-byte copy of the live
embed (`ourwork-gallery-embed.html` in this folder) at three viewports:
- 1280px (desktop): `.ocw-grid` still `display:grid`, 3 tracks, no change.
- 800px (tablet): `.ocw-grid` still `display:grid`, 2 tracks, no change.
- 390px (mobile): `.ocw-grid` becomes `display:flex` with
  `overflow-x:auto`; cards sized `flex:0 0 82%`; the grid's own
  `scrollWidth` (4062px) far exceeds the viewport (a real horizontal
  scroller), while `document.body.scrollWidth` stays exactly 390 — the
  slider scrolls internally, the page itself never overflows.
- All 29 cards (14 + 15) rendered correctly in every run, confirming the
  large inline photo-data array carried through the edit intact.

Updated directly via the Data API's element-settings tool (`set_settings`
on the embed's `code` value) — no new registered script needed, since this
is native custom code already on the page. Re-read after the write to
confirm the stored value matches exactly (no truncation).

Published live to `nwocflooring.com`, `www.nwocflooring.com`, and the
Webflow subdomain.
