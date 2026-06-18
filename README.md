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

### Hardwood installation before/after caption → serif heading above photos (2026-06-17)

**Problem:** On the ~30 hardwood floor installation pages (slug contains
`hardwood-floor-installation`), the before/after section's caption *"Love your home.
Love your floors. Love the life lived on them."* was a small italic text block
(class `Text Block 67`). The ask was to present it in the hero-subtitle style
(*"Crafted Just for Your Home — Built to Last"*) and position it with the photos.

**Why a script (not a Designer/class edit):** these are individual static pages (no
shared component for this block), and `Text Block 67` is also used on the refinishing
pages — where it additionally wraps the *"Just 2 days between these photos."* quote —
so restyling the global class would bleed onto other pages and wrongly enlarge that
quote. The Pages custom-code API also returned 404 for these pages (no page-level
custom code), and the site script block is at its 15-per-block limit.

**Iterations:** first attempt turned the caption into a bare `<h3>`. Second attempt
overlaid the line *on top of* the before/after photos — but with the photos stacked on
mobile the centered caption crossed the seam in white text over light areas and looked
bad. **Final:** the caption is restyled to match the hero subtitle (serif font, weight
and color copied at runtime from that subtitle) and moved to sit as a clean centered
heading **directly above** the photo pair.

**Where it lives:** merged into the **`OC Mobile BeforeAfter Fix`
(`oc_mobile_beforeafter_fix`)** script, which already owns the before/after section. It
is scoped to installation pages and the exact caption text, locates the photo pair as
the lowest common ancestor of the visible *Before*/*After* badges (which are kept), and
inserts the caption above it. See
[`webflow-scripts/oc_mobile_beforeafter_fix-1.0.0.js`](webflow-scripts/oc_mobile_beforeafter_fix-1.0.0.js).
(The brief experiment that lived in `OCTrustReviewsInjector9d` was reverted; that script
is back to its loader + area-spacing IIFEs.)

Published live to `nwocflooring.com`, `www.nwocflooring.com`, and the Webflow
subdomain.
