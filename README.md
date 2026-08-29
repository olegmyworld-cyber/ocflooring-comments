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

## Changes on branch `claude/nwocflooring-blog-sections-470kqm`

### Blog listing page — removed three trailing sections (2026-08-29)

**Request:** remove the "See Available Appointments" CTA, the Google Reviews
carousel, and the "More services" carousel from `/blog`.

**Change:** removed three component instances from the Blog page
(`65f32565e111adbbb806ceaa`) via the Webflow Data API. No component definitions
were touched, so every other page that uses these sections is unaffected.

| Removed instance | Component | Rendered as |
| --- | --- | --- |
| `fb218189-298c-5985-be04-6be23ffba878` | `Section // CTA 2` | "See Available Appointments" + image grid + *Schedule Free In-Home Estimate* button |
| `e8f86afb-d7cf-889a-5692-3a73ef388a65` | `Section // Reviews` | Elfsight Google Reviews widget (`elfsight-app-48ef4cd4-…`) |
| `8f988b5e-0fe5-5afa-8f20-343cc2093e03` | `Section // Services` | "More services" carousel + *Book Appointment* button |

Page body order is now: Global Styles, Navbar, `section_hero-services`,
`Line RED`, `Section // Partners`, `section_blog`, `Section // Areas`, `Footer`.

No script change was needed: neither `octrustreviewsinjector9d` nor
`ocreviewsmover` runs on `/blog` (both guard on home / city / about-us /
our-work / why-were-different paths), so nothing re-injects a review section
there.

Published live to `nwocflooring.com`, `www.nwocflooring.com`, and the Webflow
subdomain.
