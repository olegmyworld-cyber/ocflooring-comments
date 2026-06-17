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

### Service-area pins / "Why Choose OC Flooring" spacing (2026-06-17)

**Problem:** On the home and city (`hardwood-floor-refinishing-in-*`) pages, the
service-area links block (the 📍 city pins injected by `OCAreaLinksInjector`) sat
flush against the `Why Choose OC Flooring in <City>` section (injected by
`OCWhyTrustV5Injector`) — there was no gap between the two.

**Fix:** Added a second, independent IIFE to the existing `OCTrustReviewsInjector9d`
script rather than registering a new footer script (the site's script block was
already at its 15-per-block limit). The added code locates the `Why Choose OC
Flooring` heading by its visible text (robust to the injected markup's class names),
climbs to the outermost wrapper whose text still *starts* with that heading (the
dedicated Why-Choose block, with no pins preceding it), and applies a responsive top
margin (`48px` on phones, `80px` on wider screens). Because it has its own
heading-present guard, it runs site-wide regardless of the loader's path guard. See
[`webflow-scripts/octrustreviewsinjector9d-1.0.0.js`](webflow-scripts/octrustreviewsinjector9d-1.0.0.js).

Published live to `nwocflooring.com`, `www.nwocflooring.com`, and the Webflow
subdomain.

### Hardwood installation before/after caption → H3 (2026-06-17)

**Problem:** On the ~30 hardwood floor installation pages (slug contains
`hardwood-floor-installation`), the before/after section's caption *"Love your home.
Love your floors. Love the life lived on them."* was a small italic text block
(class `Text Block 67`). The request was to present it as a proper, good-looking H3.

**Why a script (not a Designer/class edit):** these are individual static pages (no
shared component for this block), and `Text Block 67` is also used on the refinishing
pages — where it additionally wraps the *"Just 2 days between these photos."* quote —
so restyling the global class would bleed onto other pages and wrongly enlarge that
quote. The Pages custom-code API also returned 404 for these pages (no page-level
custom code), so the change was added as a **third independent IIFE inside
`OCTrustReviewsInjector9d`** (the site script block is at its 15-per-block limit).

**Fix:** scoped strictly to installation pages via a path guard, the IIFE finds the
element whose exact text is the caption, replaces it with a real `<h3>`, and styles it
(`font-size: clamp(22px,4.6vw,34px)`, centered, comfortable line-height/margin). The
bare `<h3>` inherits the site's global heading font/color so it matches other headings.
It is idempotent (`data-oc-h3` marker) and never touches the "Just 2 days…" quote or
the refinishing pages. See
[`webflow-scripts/octrustreviewsinjector9d-1.0.0.js`](webflow-scripts/octrustreviewsinjector9d-1.0.0.js).

Published live to `nwocflooring.com`, `www.nwocflooring.com`, and the Webflow
subdomain.
