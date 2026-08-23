# OC Flooring — Webflow fix scripts

Source records for custom code applied to the OC Flooring Webflow site
(`nwocflooring.com`, site id `6377e8e6a53936b48ef1cad0`). These are registered as
inline scripts via the Webflow Scripts API and applied at the site footer.

## Changes on branch `claude/hero-before-after-overlap-8pookw`

### Flooring-repair hero — before/after composite cropped by the card (2026-08-23)

**Problem:** On `/services/flooring-repair`, the hero's right-hand image is a single
650×550 composite (BEFORE photo / caption strip / AFTER photo, with the pills baked
into the image). The `.hero-cover-img` class sizes the card to its grid cell
(`width: calc(100% - 48px); height: calc(100% - 80px)`) with `object-fit: cover` —
and on desktop that box is *taller* than the image's 1.18 aspect ratio, so cover
cropped the photos' sides and clipped the BEFORE pill at the card's edge. (A first
attempt anchored the crop with `object-position: 0% 0%`, which un-clipped the pill
but visibly cut the right side of the photos instead — cropping direction was the
wrong knob; the box shape was the problem.)

**Fix:** Page-scoped CSS in the existing `<style id="ocrep-tweaks">` HtmlEmbed on
that page (not the global class — `hero-cover-img` is used by every other page's
hero). `height: auto` makes the card follow the image's own aspect ratio at the
same width as before, vertically centered by the existing `align-self: center`, so
the whole composite renders uncropped. An `@media (min-width: 1930px)` fallback
sizes by height and centers the card once natural height would outgrow the section.
Verified against a local replica of the hero built from the real Webflow styles,
rendered headless at 1280/1512/1728/1920/2560 px — the card holds the image's exact
1.182 aspect (zero crop) at every width. Mobile is unaffected (the `small`
breakpoint already renders the image uncropped). See
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
