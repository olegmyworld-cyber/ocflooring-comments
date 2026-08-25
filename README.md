# OC Flooring — Webflow fix scripts

Source records for custom code applied to the OC Flooring Webflow site
(`nwocflooring.com`, site id `6377e8e6a53936b48ef1cad0`). These are registered as
inline scripts via the Webflow Scripts API and applied at the site footer.

## Changes on branch `claude/calendly-calendar-install-jo56hm`

### Calendly booking calendar under the 5-step refinishing process (2026-08-25)

**Request:** Install the Calendly calendar (the one used on the Contact Us page)
in the free space under step 5 ("Final Walkthrough") of the "Our 5-Step Hardwood
Refinishing Process in Bellevue" column on the Floor Refinishing page
(`/services/floor-refinishing`, page id `65f32565e111adbbb806cf36`).

**Fix:** New registered inline script `OCCalendlySteps` (`occalendlysteps`),
applied at the page footer of the Floor Refinishing page only (the site-wide
footer block is at its 15-script limit; page-level blocks are separate). The
5-step process is the right column (`.ots-steps-col`) of the runtime-injected
Bona tone/steps section (`#oc-tone-steps`), so the script polls until that
column exists, then appends a "Book Your Free In-Home Estimate" heading and the
Calendly inline widget, and loads Calendly's `widget.js` once. The embed URL
(`calendly.com/nwwillsflooring/free-in-home-estimate-online-today-clone-1`
with `hide_gdpr_banner=1`) and sizing were copied verbatim from the Contact Us
page's HTML embed. See
[`webflow-scripts/occalendlysteps-1.0.0.js`](webflow-scripts/occalendlysteps-1.0.0.js).

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
