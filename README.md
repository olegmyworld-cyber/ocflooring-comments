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

### Floor-refinishing CTA — invisible "Free 30-Minute In-Home Flooring Visit" button (2026-09-01)

**Problem:** On [`/flooring-services-near-me/floor-refinishing`](https://www.nwocflooring.com/flooring-services-near-me/floor-refinishing)
the red CTA card near the bottom rendered its white pill button completely blank.

**Cause:** The site-footer "green contact CTA" tweak adds the class `oc-cta-green`
(`background` + `color:#fff !important`) to every `a[href="/contact"]` whose class matches
`/button|btn|cta/i`. That also catches Webflow's layered `.button-wrapper` buttons (`Button White`
inside `Section // CTA`): those paint their own `.button-background` pill *on top of* the anchor, so
the green never shows, while the forced white `color` is inherited by `.button-text` — a white
"Schedule Free In-Home Estimate" label on a white pill. The button text was there all along, just
invisible, which is why the earlier `oc-fix-empty-cta` page script never fired (it only fills links
whose text is actually empty).

**Fix:** New registered inline script `OCCtaGreenLayerFix` (`occtagreenlayerfix`) — keeps the green
treatment for flat custom CTAs and takes the class back off the layered Webflow buttons so they
return to their designed colors, plus a guard rule that greens the inner pill so the label stays
legible in the window before the class is removed. See
[`webflow-scripts/occtagreenlayerfix-1.0.0.js`](webflow-scripts/occtagreenlayerfix-1.0.0.js).

Applied at the **page** footer for Floor Refinishing (page id `65f32565e111adbbb806cf36`): the site
script block is at its 15-script cap, so it could not be applied site-wide. The same class collision
affects any other page that still shows a `.button-wrapper` CTA pointing to `/contact` — `siteCleanupD`
already hides this CTA section on the home, city-refinishing and installation pages, so those are
unaffected.
