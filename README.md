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

### Bellevue hardwood page — hero paragraph too large on mobile (2026-06-18)

**Problem:** On the Bellevue hardwood-installation page
(`/city-of-bellevue/hardwood-floor-installation-in-bellevue-wa`, page id
`65f32565e111adbbb806d03e`), the hero "Description" paragraph ("OC Flooring provides
professional hardwood floor installation in Bellevue, WA…") rendered too large on
phones.

**Fix:** Registered a new inline script `HeroDescMobile` (`herodescmobile`) and applied
it to that page's footer only. The paragraph lives inside the shared hero component
(`859df468-…`), so its class can't be read via the Data API; the script instead locates
the element by a distinctive substring of its text, tags it `oc-hero-desc-sm`, and
injects a mobile media query (14px ≤767px, 13px ≤479px, tighter line-height). Page-scoped
so the other ~40 pages using the same hero component are unaffected. See
[`webflow-scripts/herodescmobile-1.0.0.js`](webflow-scripts/herodescmobile-1.0.0.js).

### Reviews section as a mobile swipe slider — install + refinishing pages (2026-06-18)

**Goal:** make the customer-reviews section a horizontal swipe slider on phones across all
hardwood floor **installation** and **refinishing** pages.

**Two different review sections exist:**
- Installation pages use a self-contained html-embed `<section class="ocf-reviews">` with a
  `.ocf-grid` of `.ocf-card`s. Known structure -> pure CSS scroll-snap on `.ocf-reviews .ocf-grid`.
- Refinishing pages render reviews at runtime via the external bundle `oc-trust-reviews-v9c-min.js`
  (loaded by `OCTrustReviewsInjector9d`). Its DOM can't be inspected from this environment
  (network egress blocked, Designer offline), so the script detects the card "track" generically:
  inside `#oc-trust-reviews` / `[class*="oc-trust"]` / `[class*="trust-reviews"]` it tags the
  element with the most text-bearing direct children (>=3) as `.ocrs-track` and applies the same
  scroll-snap CSS. **Best-effort for the trust section — verify live.**

**Fix:** Registered inline script `OCReviewsSlider` (`ocreviewsslider`). The site-level script
budget was full (15/15), so it's applied as a **page-level** header script on 60 pages
(31 installation + 29 refinishing). Pages that already had a page custom-code block were updated
additively; pages without one were created via `set_page_scripts`. The slider activates only at
<=767px; desktop/tablet are unchanged. `/services/hardwood-floor-installation` was skipped (no
reviews section). See [`webflow-scripts/ocreviewsslider-1.0.0.js`](webflow-scripts/ocreviewsslider-1.0.0.js).
