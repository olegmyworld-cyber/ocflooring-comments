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

## Changes on branch `claude/mobile-slider-home-cities-ht0w4r`

### Mobile reviews slider — home + hardwood refinishing city pages (2026-06-27)

**Request:** On the mobile version of the home page and the hardwood-floor-refinishing
city pages, present the customer-reviews ("trust reviews") section as a swipeable slider
instead of a tall vertical stack of cards.

**Fix:** Added a small mobile-only enhancement that, on screens ≤ 767px, flips the review-card
container into a single-row horizontal CSS scroll-snap track (hidden scrollbar, ~86%-width
cards so the next one peeks in to signal swipeability). Desktop/tablet layout is untouched. The
script targets the reviews section (`#oc-trust-reviews` / `[class*="oc-trust"]` /
`[class*="trust-reviews"]`) and finds the card row structurally (the descendant with the most
direct children that each hold a substantial block of text), tagging it `.ocrs-track`. It runs
on the home page and `hardwood-floor-refinishing`/`-installation` pages. See
[`webflow-scripts/ocreviewsslider-1.0.0.js`](webflow-scripts/ocreviewsslider-1.0.0.js).

**Deployment note:** The site is at the hard 15-applied-registered-scripts-per-site cap, so this
could not be added as a new registered script. Instead it lives in the site-wide **footer
custom-code block** (a separate block that doesn't count against that cap), appended after the
existing footer scripts. The pre-existing registered `ocreviewsslider` script holds the same
logic but is intentionally left unapplied.
