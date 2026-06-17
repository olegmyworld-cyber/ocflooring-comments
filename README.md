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

## Changes on branch `claude/mobile-tile-h1-sizing-fj08xy`

### Hero `h1` title — too small on mobile (2026-06-17)

**Problem:** On phones the hero `<h1>` page title (e.g. "Hardwood Floor
Installation in Monroe, WA") looked too small. The title lives in the shared
`Section // Hero` component and is styled by the `heading-hero` class (with a
sibling `heading-hero-custom` variant used on other hero layouts). Both classes
capped the mobile-portrait (`tiny`, ≤478px) font size at a fixed `2.3rem`, which
is the size phones in portrait actually rendered.

**Fix:** Updated the `tiny` breakpoint of both `heading-hero` and
`heading-hero-custom` directly in the Webflow Designer (no script — a native
style change so the above-the-fold title doesn't flash/resize on load):

- `font-size: clamp(2.4rem, 10vw, 3.2rem)` — fluid, so the title scales with the
  viewport (~38px on a 320px screen up to ~48px near the 478px breakpoint)
  instead of a flat 2.3rem.
- `line-height: 1.08` — tighter, more impactful multi-line wrapping.
- `letter-spacing: -0.015em` — subtle tracking for a more premium headline.

Desktop/tablet sizing is untouched (only the `tiny` breakpoint changed). Applies
site-wide to every page using the Hero component (home, service, and city
landing pages). Published live to `nwocflooring.com`, `www.nwocflooring.com`,
and the Webflow subdomain.
