# OC Flooring — Webflow fix scripts

Source records for custom code applied to the OC Flooring Webflow site
(`nwocflooring.com`, site id `6377e8e6a53936b48ef1cad0`). These are registered as
inline scripts via the Webflow Scripts API and applied at the site footer.

## Changes on branch `claude/oc-flooring-webflow-fixes-amosur`

### Bona sealer widget — "CUSTOMER FAVORITE" badge overlap (2026-06-14)

**Problem:** On mobile, the red `★ CUSTOMER FAVORITE` badge overlaid on the room
image overlapped the `LIVING / KITCHEN` room toggle pills in the Bona tone/sealer
widget (`#oc-tone-steps` / `#bona-tone-widget`).

**Fix:** Merged a badge-overlap guard into the existing `BonaMobileFix`
(`bonamobilefix`) script rather than adding a new one (the site footer was at its
15-script-per-block limit). The guard finds the badge and toggle by their visible
text (robust to the minified widget bundle's class names), measures their live
bounding boxes, and only repositions the badge (nudges it just below the toggle row)
when they actually overlap. Also keeps the badge on one line / slightly smaller on
phones. See [`webflow-scripts/bonamobilefix-1.0.0.js`](webflow-scripts/bonamobilefix-1.0.0.js).

Published live to `nwocflooring.com`, `www.nwocflooring.com`, and the Webflow
subdomain.

## Blog posts (branch `claude/clever-noether-l41bks`)

### Hardwood Floor Refinishing in Everett, WA (2026-09-15)

Webflow rich-text embed for a new Blogs CMS item targeting "hardwood floor
refinishing Everett WA" and the Snohomish County long tail.

- [`blog/hardwood-floor-refinishing-everett-wa.html`](blog/hardwood-floor-refinishing-everett-wa.html)
  — Post Body. Same `.ocb` design system as the King & Snohomish cost guide
  (Mulish, `#8B0000` brand). Sixteen `data-rt-embed-type` blocks, each under
  Webflow's 10,000-char embed limit. Hooks: an Everett calculator (era selector,
  stair treads at $55–$75, add-ons, 500 sq ft minimum) and a five-question
  "recoat or refinish?" quiz. FAQ accordion with 13 questions. Structured data
  is a single `@graph` (BlogPosting, Service with Everett `areaServed` and priced
  Offers, FAQPage).
- [`blog/hardwood-floor-refinishing-everett-wa.meta.md`](blog/hardwood-floor-refinishing-everett-wa.meta.md)
  — Name, slug, title tag, meta description, summary, category, City Links
  field HTML, and the keyword map.

Verified in headless Chromium: calculator math (min billing, stair range,
add-ons), quiz verdicts, FAQ toggles, no horizontal overflow at 320–1200 px.

### Wills Flooring blog program (2026-09-16)

200 question-led posts for willsflooring.com (Webflow site `66cc1f4542ee0c42e43d0303`,
Blog Posts collection `66cecfc7e7f88d2528ab474e`), one per day from 2026-09-17, across
hardwood refinishing, hardwood installation, vinyl plank and carpet in Seattle, Everett,
Lynnwood, Kirkland, Edmonds, Sammamish and Snohomish. Everything lives in
[`blog/wills-program/`](blog/wills-program/):

- `plan.py` / `plan.json` — the 200 titles, slugs, categories, cities and publish dates.
- `SPEC_GUIDE.md` — writing rules, brand facts, published prices, block types.
- `specs/NNN-<slug>.json` — one spec per post; `legacy/` holds rewrites of the five old posts.
- `render.py` — spec → Apple-style Webflow rich-text body (`out/`, git-ignored) plus CMS fieldData.
- `validate.py`, `qa.mjs` — plan/style checks and headless-Chromium checks (calculator, FAQ, mobile overflow).
- `UPLOAD.md`, `uploaded/` — how posts are pushed to Webflow as drafts, and the item ids created.
- `PUBLISH_LOG.md` — written by the daily Routine "Wills Flooring daily blog publish"
  (15:30 UTC), which flips due drafts to live if they have an Image Main.

Carpet labor is priced from King/Snohomish market research (stretch-in $0.99, glue-down $1.29,
stairs $30, removal +$0.45, furniture +$0.25 per sq ft, 500 sq ft minimum), so carpet posts use the
same calculator as the other categories. All 206 posts carry the warm palette added 2026-09-17.
Hero images are the owner's to add in the Webflow Editor; `HERO_IMAGES_NEEDED.md` lists what is
still missing. Publishing is paused until Oleg says go.
