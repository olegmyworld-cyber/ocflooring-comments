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

**Actual root cause (found after Designer edits had no visible effect):** a
*different* registered script, **`OCHeadingFix`** (`ocheadingfix`), injects this
into `<head>`:

```css
html body .heading-hero, … { font-size: clamp(30px, 6.2vw, 57px) !important }
```

That `!important` rule pins the hero title to **~57px on desktop** (too big) and
**~30px on phones** (too small) — matching the complaint exactly — and it
overrides any `font-size` set on `.heading-hero` / `.heading-hero-custom` in the
Webflow Designer. That is why several rounds of Designer class edits (and the
`Global Styles` fluid root font-size, `html { font-size: calc(... + vw) }`) made
no visible difference. NOTE: the earlier Designer breakpoint edits to
`heading-hero` / `heading-hero-custom` are still in place but are now moot —
they're outranked by the `!important` rule below.

**Fix:** Beat the `!important` clamp with a competing rule of **higher
specificity** — `html body .heading-hero.heading-hero` (repeated class →
specificity `(0,2,2)` vs the old `(0,1,2)`) — plus `!important`, so it wins
regardless of stylesheet order. Because both Webflow script blocks are at the
15-script-per-block limit, the rule is **merged into the already-applied header
script `OCHeaderInit`** (the same merge tactic used for `BonaMobileFix`), rather
than adding a new script. Header placement means the CSS lands before first
paint (no flash). Sizes are in **px** (independent of the fluid root) and form a
deliberate *reverse ramp* — smaller on desktop, larger on mobile:

| Breakpoint   | `font-size` | vs old clamp |
|--------------|-------------|--------------|
| desktop      | `46px`      | down from ~57px |
| `≤991px`     | `44px`      |              |
| `≤767px`     | `41px`      |              |
| `≤479px`     | `38px`      | up from ~30px |

**Follow-up — hero subheading (same day):** the hero subheading
(`.subheading-hero`, e.g. "Love Your Floors Again — Without the Mess") was
shrinking out of proportion with the title on phones. Added mobile-only rules to
the same `OCHeaderInit` block (desktop left at its Designer `2.3rem`) so the
title:subheading ratio matches desktop: `≤991px 34px / ≤767px 32px / ≤479px 30px`.

See [`webflow-scripts/ocheaderinit-1.0.0.js`](webflow-scripts/ocheaderinit-1.0.0.js).
Applies site-wide to every page using the Hero component (home, service, and
city landing pages). Published live to `nwocflooring.com`,
`www.nwocflooring.com`, and the Webflow subdomain.

> Lesson: before changing hero/heading sizes in the Designer, check the
> registered Scripts (`OCHeadingFix`, `SiteFontStyle*`, etc.) for `!important`
> CSS that may already be pinning them.
