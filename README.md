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

## Changes on branch `claude/hero-responsive-design-4y25xa`

### Laminate hero — too small on desktop (2026-06-25)

**Problem:** On the laminate floor installation pages the desktop hero
(`.section_hero`) is a two-column layout — heading/description/button on the left,
the floor cover photo (`.hero-cover-img`) on the right. The photo rendered small
and top-aligned, leaving a large empty area beside the text, so the hero looked
undersized on desktop. The mobile (stacked) layout already looked correct.

**Fix:** Injected a small desktop-only (`min-width: 992px`) CSS rule that enlarges
`.hero-cover-img` inside the hero (~48vw wide, capped at 760px, 560px tall) so the
photo fills the right column and the hero reads as a proper, full-size hero. The
dimensions were verified live in the Webflow Designer against the Arlington hero.

Shipped as **page-level footer freeform custom code** on all 30 laminate pages
(the `laminate-flooring-installation` hub page + every
`laminate-flooring-installation-in-<city>-wa` page). It is applied per page rather
than site-wide because the site footer's registered-script block was at its
15-script limit; per-page scoping also guarantees the home page, hardwood, vinyl,
and other page types are unaffected, and the desktop media query leaves mobile
untouched. See [`webflow-scripts/laminate-hero-fix.css`](webflow-scripts/laminate-hero-fix.css).

### Unified hero across all laminate city pages (2026-06-25)

**Problem:** Only the Arlington laminate page had the new photo-hero design
(`.section_hero` with a `.hero-cover-img` floor photo on the right). Every other
laminate city page still used the older shared **"Section // Hero"** component,
which has a different layout and a different background image — so the laminate
city pages were inconsistent.

**Fix (done in the Webflow Designer, not in this repo):** Converted Arlington's
hero into a reusable component **"Laminate City Hero"** and added two
`textContent` props (`Heading`, `Description`) bound to the H1 and paragraph. Then
on all 29 laminate city pages, replaced the old `Section // Hero` instance with a
`Laminate City Hero` instance positioned at the top of the body, setting each
page's Heading/Description props to that page's own existing (verbatim) SEO copy.
Result: every laminate city page now shares Arlington's hero design and the same
floor photo, while keeping its own city-specific text. The desktop-enlarge CSS
above applies automatically since the new hero uses `.section_hero .hero-cover-img`.

Known follow-up: the Seattle page
(`laminate-flooring-installation-in-seattle-wa`) had pre-existing copy that names
"Seattle" (not "West Seattle") and describes hardwood (not laminate); preserved
verbatim during the migration and left for content review.
