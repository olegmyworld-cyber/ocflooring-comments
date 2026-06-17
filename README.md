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

**Root cause (important):** Two things were missed on the first attempt:

1. The hero `<h1>` inherited its size from the base `h1` tag style
   (`default-h1`: `font-size: 3rem` on `main`, `2.5rem` on `tiny`). The
   `heading-hero` class had **no** `main` `font-size`, so desktop rendered at
   `3rem`. The first pass set `main` to `3.25rem` — i.e. it made desktop
   *bigger*, the wrong direction.
2. The site uses a **fluid root font-size** (in the `Global Styles` embed:
   `html { font-size: calc(... + vw) }`), so every `rem` scales with viewport
   width. That's why the original `clamp(...vw...)` barely moved on phones.

**Fix:** A deliberate *reverse ramp* on both `heading-hero` and
`heading-hero-custom` — smallest on desktop, growing toward mobile — set
directly in the Webflow Designer (native style change, no script). The `.heading-hero`
class legitimately overrides the `h1` tag (there is no `!important` anywhere):

| Breakpoint        | `font-size` | `line-height` | notes                    |
|-------------------|-------------|---------------|--------------------------|
| `main` (desktop)  | `2.6rem`    | `1.16`        | down from inherited 3rem |
| `medium` (≤991px) | `2.65rem`   | `1.16`        |                          |
| `small` (≤767px)  | `2.75rem`   | `1.14`        |                          |
| `tiny` (≤478px)   | `2.85rem`   | `1.1`         | `letter-spacing -0.01em` |

The hero paragraph (`paragraph-hero`) under the title was also bumped on mobile
for readability: `font-size 1rem → 1.0625rem`, `line-height 1.6` at `tiny`
(it already had `font-style: italic` there).

Applies site-wide to every page using the Hero component (home, service, and
city landing pages). Published live to `nwocflooring.com`,
`www.nwocflooring.com`, and the Webflow subdomain.

> If a published change ever appears to "not show", it is almost always browser
> /CDN caching — load the page in a private window or with a `?v=2` query string
> to bypass the cache.
