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

## Changes on branch `claude/oc-flooring-404-redirects-12ef4v`

### Dead URLs returning "Page not found" (2026-09-06)

**Problem:** `nwocflooring.com/services/flooring-repair` and 174 other URLs that Google
still indexes (16 months of Search Console data) land on the 404 page. Four
families: the old `/services/*` folder (now `/flooring-services-near-me/*`), the
old long city-page slugs (`…-in-everett-wa-waterproof-flooring` etc.), the
`/city-of-arlington/*` folder (now `/arlington/*`), and the deleted laminate city
pages, plus a few renamed blog posts and two retired products. Semrush's latest
crawl shows no broken internal links, so these come from Google / old backlinks only.

**Fix, two layers:**

1. [`redirects/redirects.csv`](redirects/redirects.csv) — the 14 redirects already in Webflow (exported 2026-09-06) plus 173 new exact rows, no header row (Webflow rejected the header as an invalid path),
   to import in Webflow: *Site settings → Publishing → 301 redirects → Import*.
   This is the real fix (HTTP 301, passes SEO value). The Webflow API has no
   redirects endpoint, so the import is a one-time manual step.
   [`redirects/redirects-review.md`](redirects/redirects-review.md) lists every
   row with its clicks/impressions so the mapping can be sanity-checked.
2. [`webflow-scripts/oc404redirects-1.0.0.js`](webflow-scripts/oc404redirects-1.0.0.js)
   — page-level footer code on the `/404` page (page id `65f32565e111adbbb806cea8`).
   Rule-based, so it also catches old URLs not in the CSV: it classifies the old
   slug (laminate/vinyl, refinishing, repair, tile, carpet, install) and sends the
   visitor to the same city's current page. A `sessionStorage` guard prevents loops.
   Tested against all 175 known dead URLs.

**Judgment calls:** deleted laminate city pages go to the same city's vinyl-plank
page (site groups vinyl + laminate); the two Bellevue refinishing URLs go to the
home page (no Bellevue refinishing city page exists); dead products go to
`/flooring-services-near-me/our-products`.
