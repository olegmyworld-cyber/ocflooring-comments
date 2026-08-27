# Carpet installation pages — mobile slider + "Also serving" removal (2026-08-27)

Requests:
1. Make the carpet-swatches product grid ("After All II", "Clever Choice",
   "Frieze Twist", "Rustique Vibe", "Vintage Flair", "Game Changing II",
   "Cozy Harbor II", "Finely Detailed") a swipeable slider on mobile only,
   on **all carpet installation pages**.
2. Remove the "Also serving the Eastside & Seattle" pill-list section from
   **all carpet installation pages**.

## Site context discovered mid-task

The site grew from 161 to 220 pages since earlier work in this session — a
new batch of **30 carpet installation pages** now exists
(`carpet-installation-in-{city}-wa`, one per served city including Bellevue),
all built and published the same day. All 30 load the same two scripts:
`CarpetBellevueFontsCanonical` (header) and `ocCarpetBellevue` v1.8.0
(footer) — the latter is a loader that pulls a shared, hosted bundle
(`oc-carpet-bellevue-1.8.0.js`) rendering the swatches grid and the
"Also serving" section identically on every page. This meant one shared fix
applied once covers every page.

## Why text/structure-based targeting, not CSS class selectors

The shared bundle is hosted externally and this sandbox's network egress
blocks both `nwocflooring.com` and `cdn.prod.website-files.com`, so the
actual rendered DOM/class names could not be inspected directly (same
constraint hit earlier in this session for the refinishing-page 5-step
section). `occarpetpatch-1.0.0.js` therefore finds both targets at runtime
by content/structure, independent of unknown class names:

- **Swatches grid**: scans for a container with 6–14 direct children where
  ≥70% each contain an `<img>` (excluded if the image's *natural* — not
  viewport-rendered — width is a tiny icon, so the check survives a squished
  mobile layout) plus a short heading (<80 chars) and modest card text
  (<500 chars). Among candidates, prefers ones with large "real photo"
  images, then whichever child count is closest to 8. On mobile (≤767px)
  applies `display:flex` + `overflow-x:auto` + `scroll-snap` inline styles
  directly to the found element and 82%-width snap styles to its children;
  on desktop/tablet the inline styles are cleared, restoring the page's own
  native grid layout untouched. A `resize` listener keeps this correct across
  live viewport changes.
- **"Also serving" section**: finds the smallest visible element whose text
  contains "ALSO SERVING", then climbs to the nearest ancestor with an
  `aria-label` attribute (the convention every other custom section on this
  site already uses) as the primary section-boundary signal; if none is
  found within 8 levels, falls back to climbing while the parent's added
  text stays under an ~800-char budget (comfortably covers the ~30 city
  pills, well short of the next unrelated section's copy) and removes that
  element entirely via `.removeChild()`.

## Testing

Verified in headless Chromium against a reconstructed mock (swatch grid +
a decoy small-icon feature grid + a second borderline-sized decoy photo
grid + the also-serving section, both with and without `aria-label` + a
plain page with no matching content at all):
- Mobile (390px) → grid becomes a scroll-snap slider; desktop (1280px) →
  native grid preserved; verified both `aria-label` present and absent.
- Resize toggle mobile→desktop→mobile mid-session → correctly flips back
  and forth, no residual state issues.
- No-match page → safe no-op, zero page errors, footer/content untouched.
- Two decoy grids present simultaneously → correctly picks the real swatch
  grid over both decoys (natural-image-size + closest-to-8-children scoring).
- Also-serving section removed cleanly in every case; a nearby decoy
  feature grid was left completely untouched in every run.

## Deployment

`occarpetpatch-1.0.0.js` is 2,435 chars — over Webflow's 2,000-char inline
registered-script limit — so it's hosted as a site asset (uploaded via the
Data API's presigned-S3 flow, same as the site's own script bundles) and
loaded by a tiny inline loader script `ocCarpetPatchLoader`, applied at the
page footer of all 30 carpet installation pages (including Bellevue).

## Follow-up (2026-08-27, same session): mobile trust-bar alignment fix

Request: fix the "4.7★ 119 Google reviews / 12 years, family owned /
Licensed, bonded & insured in WA" trust bar's mobile layout on all carpet
installation pages, without touching desktop.

Unlike the swatches grid and Also-serving section, this trust bar is
**native Designer content** (`.ci-trust` / `.ci-trust-inner` and its
children — genuine global styles, confirmed shared across pages the same
way `.ti-work-grid` is on the tile pages), so it was fixed directly via
the Style API rather than a runtime script.

**Real bug (reproduced in a headless-Chromium mock of the exact live CSS
before touching anything):** `.ci-trust-inner` is a 3-column
`auto-fit, minmax(220px,1fr)` grid that correctly collapses to a single
stacked column on phones — no horizontal overflow. The actual problem was
alignment: item 1 (rating) is left-aligned, item 2 (years) is
`text-align:center`, item 3 (licensing) is `text-align:right` — by design,
for a 3-column desktop row. Stacked to one column on mobile, that produces
a jarring left → center → right zig-zag down the page.

**Fix**, added at the `small` (≤767px) breakpoint only — desktop's 3-column
row is untouched (verified: still 3 tracks at 1280px after the change):
- `.ci-trust-inner`: force `grid-template-columns:1fr`, tighter padding,
  smaller row gap.
- `.ci-trust-mid` / `.ci-trust-right`: `text-align:left` + `min-width:0`
  (belt-and-suspenders against grid-item min-content overflow).
- `.ci-trust-score`: `min-width:0` (same overflow guard).

Verified against the mock at 390px: all three items read left-aligned,
`document.body.scrollWidth` stayed 390 = viewport (no overflow) both before
and after.

## Follow-up (2026-08-27, same session): "Bring the showroom to me" CTA scroll fix

Request: "only for mobile version when i click on the bottom bring the
showroom to me, i need it scrolling righaway on schedule, not on the
description" — on all carpet installation pages.

**Investigation:** the CTA (`Link`, in the hero/hook section with the
"1 visit / $1.49/sq ft / 1 day" stat row) has `href="#book"`. The
semantically-matching target — the booking/schedule `Section`
(class `.ci-book-sec`) — had **no DOM id set anywhere on the page**, so the
in-page anchor had nothing to resolve to and the browser fell through to
whatever content happened to sit near the top of the fragment (reading as
"lands on the description"). This is a page-wide broken anchor, not a
genuine responsive bug — it was most visible on mobile because the longer
stacked layout makes a missed jump obvious, while on desktop's shorter
layout "landing nowhere" and "landing near schedule" look similar.

**Fix:** set the real Designer DOM id `book` on `.ci-book-sec` (via the
Style/Settings API's `set_dom_id`, not a runtime script — this is native
Designer content) on all 30 carpet installation pages, exploiting the same
cloned-page element-ID stability used for the trust-bar fix above: the
target section's `element` ID suffix is identical across all 30 pages, so
one `set_dom_id` call per page (same element-id literal) was enough,
without a per-page "find" round-trip. A working native `href="#book"` →
`id="book"` anchor is correct on every device, so no mobile-only JS shim
was needed.

## Follow-up (2026-08-27, same session): nav-menu category icons

Request: "add some nice icons to each categories, specially on mobile
version" — for the 13 category links in the site's "Services" dropdown nav
menu (Floor Installation, Floor Refinishing, Vinyl Plank Flooring, Floor
Repair, Carpet Installation, Tile Installation, Stairs Installation,
Laminate Installation, Floor Staining, Dustless Floor Sanding, Eco-Friendly
Finishing, Screen and Recoat, Our Floor Products).

This isn't carpet-page-specific — the nav menu is shared sitewide — so it's
documented in [`webflow-scripts/navbar/README.md`](../navbar/README.md).
