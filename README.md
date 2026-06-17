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

### Hero typography — too big on desktop, too small on mobile (2026-06-17)

**Problem:** The hero `<h1>` page title (e.g. "Hardwood Floor Installation in
Snohomish, WA") had **no explicit desktop size**, so it inherited a very large
base size and dominated the screen on desktop, while on phones it still felt
small. The title lives in the shared `Section // Hero` component, styled by the
`heading-hero` class (with a sibling `heading-hero-custom` used on other hero
layouts). Original sizing: no `main` (desktop) `font-size` at all, and a flat
`2.3rem` cap at the mobile-portrait (`tiny`, ≤478px) breakpoint.

**Fix:** Set an explicit, balanced responsive scale on both `heading-hero` and
`heading-hero-custom` directly in the Webflow Designer (native style change, no
script — so the above-the-fold title doesn't flash/resize on load). This brings
desktop *down* and mobile *up*, with smooth steps in between:

| Breakpoint        | `font-size` | `line-height` |
|-------------------|-------------|---------------|
| `main` (desktop)  | `3.25rem`   | `1.12`        |
| `medium` (≤991px) | `3rem`      | `1.12`        |
| `small` (≤767px)  | `2.95rem`   | `1.1`         |
| `tiny` (≤478px)   | `2.9rem`    | `1.08`        |

The `tiny` breakpoint also keeps `letter-spacing: -0.015em` for a tighter,
more premium headline. (A first pass had set `tiny` to
`clamp(2.4rem, 10vw, 3.2rem)`, but on phone-width screens that landed only
~2px above the original 2.3rem, so it was replaced with the flat `2.9rem`
above.)

The hero paragraph (`paragraph-hero`) under the title was also bumped on mobile
for readability: `font-size 1rem → 1.0625rem`, `line-height 1.6` at `tiny`
(it already had `font-style: italic` there).

Applies site-wide to every page using the Hero component (home, service, and
city landing pages). Published live to `nwocflooring.com`,
`www.nwocflooring.com`, and the Webflow subdomain.
