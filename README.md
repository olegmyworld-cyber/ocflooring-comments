# OC Flooring — Webflow fix scripts

Source records for custom code applied to the OC Flooring Webflow site
(`nwocflooring.com`, site id `6377e8e6a53936b48ef1cad0`). These are registered as
inline scripts via the Webflow Scripts API and applied at the site footer.

## Changes on branch `claude/oc-flooring-carpet-page-ig4q1w`

### New page: Carpet Installation in Bellevue, WA (2026-08-24)

Built the "Carpet Mobile Showroom v2" Claude Design
([`design/Carpet Mobile Showroom v2.dc.html`](design/Carpet%20Mobile%20Showroom%20v2.dc.html))
as a native Webflow page in the **City of Bellevue** folder:

- **Page:** `/city-of-bellevue/carpet-installation-in-bellevue-wa`
  (page id `6a8ccb1ebf28596111eed9f2`, folder id `65f32565e111adbbb806cece`).
  Created via the Pages API with the design's SEO title/description and Open
  Graph metadata; JSON-LD (`FlooringContractor` + `Service` + `BreadcrumbList` +
  `FAQPage`) written through the schema-markup API with URLs updated to the
  real published path.
- **Content:** all eleven sections (hero + nav, trust bar, cost answer,
  how-it-works, services & prices, sample gallery, cost estimator, stretch vs
  replace, reviews, FAQ, service areas, CTA, footer) built as native Webflow
  elements with `ci-*` prefixed classes via the WHTML builder. 13 images
  (hero, 8 carpet swatches, 3 job photos, logo) uploaded as site assets with
  SEO file names and bound to the image elements.
- **Interactive code:** the cost estimator + FAQ accordion live in
  [`webflow-scripts/oc-carpet-bellevue-1.0.0.js`](webflow-scripts/oc-carpet-bellevue-1.0.0.js),
  uploaded as a Webflow asset and loaded by the registered inline script
  [`webflow-scripts/occarpetbellevue-1.0.0.js`](webflow-scripts/occarpetbellevue-1.0.0.js)
  (page footer). Google Fonts (Newsreader + Hanken Grotesk) and the canonical
  link are injected by
  [`webflow-scripts/carpetbellevuefontscanonical-1.0.0.js`](webflow-scripts/carpetbellevuefontscanonical-1.0.0.js)
  (page header) because the custom-code API rejects markup containing external
  URLs. Estimator styles + font fallbacks are in the page's head custom code.
- **Not published:** the page is staged in the Designer only — publish the site
  to take it live.

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
