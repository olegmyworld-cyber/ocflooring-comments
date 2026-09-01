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

### Floor Refinishing page — home-page review section replaces Trustindex widget (2026-09-01)

**Page:** `/flooring-services-near-me/floor-refinishing` (Webflow page id
`65f32565e111adbbb806cf36`).

**Problem:** the page showed the old Trustindex "What Our Customers Say" Google
Reviews widget (the `Section // Reviews` component instance, `section.section_reviews`),
not the `#ocf-trust` reviews section used on the home page and the city
`hardwood-floor-refinishing-in-*` pages.

**Change:** added an HTML Embed element in that exact slot (between `Section // CTA 2`
and `Section // Services`) containing the same `#ocf-trust` markup as the home page —
licensing bar, "Loved by Bellevue & the Eastside" heading, 4.7 / 119 Google rating,
the four review cards and the "Read all reviews on Google" button — then removed the
`Section // Reviews` instance from this page only (the component itself is untouched,
so other pages keep it). The home page's trailing map iframe is omitted; the home page
hides it at runtime anyway via `OCRemoveHomeMap`. Mobile keeps the same horizontal
card slider the home page has (`#ocf-trust .rev-grid` under 767px).

Source of record: [`webflow-embeds/floor-refinishing-ocf-trust-reviews.html`](webflow-embeds/floor-refinishing-ocf-trust-reviews.html).
