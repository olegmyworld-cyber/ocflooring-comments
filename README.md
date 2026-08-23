# OC Flooring — Webflow fix scripts

Source records for custom code applied to the OC Flooring Webflow site
(`nwocflooring.com`, site id `6377e8e6a53936b48ef1cad0`). These are registered as
inline scripts via the Webflow Scripts API and applied at the site footer.

## Changes on branch `claude/hero-before-after-overlap-8pookw`

### Flooring-repair hero — BEFORE badge clipped on the before/after image (2026-08-23)

**Problem:** On `/services/flooring-repair`, the hero's right-hand image is a single
650×550 composite (BEFORE photo / caption strip / AFTER photo, with the pills baked
into the image). The `.hero-cover-img` class renders it with `object-fit: cover;
object-position: 50% 50%`, so on desktop — where the card box is wider than the
image's aspect ratio — the vertical overflow was cropped evenly top and bottom,
slicing the red **BEFORE** pill in half at the card's top edge.

**Fix:** Page-scoped CSS added to the existing `<style id="ocrep-tweaks">` HtmlEmbed
on that page (not the global class — `hero-cover-img` is used by every other page's
hero): `.section_hero .hero-cover-img{object-position:0% 0%!important}`. The pills
and caption all sit in the image's top-left/center, so anchoring the crop to the
top-left corner means overflow is always trimmed from the bottom/right — plain
flooring — and the badges stay visible at any card shape. Mobile is unaffected
(the `small` breakpoint already renders the image uncropped). See
[`page-embeds/flooring-repair-ocrep-tweaks.html`](page-embeds/flooring-repair-ocrep-tweaks.html).

Published live to `nwocflooring.com`, `www.nwocflooring.com`, and the Webflow
subdomain.

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
