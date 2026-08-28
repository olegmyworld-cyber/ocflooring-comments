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

## Changes on branch `claude/flooring-near-me-sections-icwi7l`

### "near me" added to city-page hero copy (2026-08-28)

**Request:** Add the phrase "near me" to the hero intro paragraph (the one under the
H1/subheading, above the appointment button) on every city landing page.

**Scope:** 149 city pages across the five service lines —
carpet installation (30), tile installation (30), hardwood floor refinishing (29),
floor repair (30), and vinyl plank installation (30).

**Fix:** Each hero paragraph keeps its existing copy and gains a short lead-in
question in front of it:

> Searching for `<service>` near me in `<City>`? `<existing copy…>`

Whidbey Island and Mercer Island use "near me **on** …". The Cottage Lake vinyl
plank page already opened with "Vinyl plank flooring near me delivers…", so that
stray phrase was dropped to avoid saying "near me" twice.

Depending on how each page was built, the copy lives either in a `Section // Hero`
component instance (`Description` prop) or in a plain hero paragraph
(`paragraph-hero`, `ci-lede`, `ti-hero-lead`). Both were updated via the Webflow
Data API. The full page-by-page list of lead-ins is in
[`content-records/near-me-hero-lead-ins.csv`](content-records/near-me-hero-lead-ins.csv).

Published live to `nwocflooring.com`, `www.nwocflooring.com`, and the Webflow
subdomain.

### "near me" extended to the Home page, service hubs and installation pages (2026-08-28)

Follow-up to the change above, covering the pages the city-page pass had skipped:

- **Home page (`/`)** — the hero shown in the original screenshot ("Dustless Hardwood
  Floor Refinishing in Bellevue, WA"). It lives on the Home page rather than on a
  city page, which is also why the refinishing city count was 29 and not 30.
- **Three service hub pages** — `/services-near-me/floor-refinishing`,
  `/services-near-me/flooring-repair`, and
  `/services-near-me/vinyl-plank-flooring-and-laminate-flooring`. These are
  region-wide, so their lead-in has no city: "Searching for `<service>` near me?"
- **30 `hardwood-floor-installation-in-<city>` pages** — a sixth service line, using
  the same city-specific pattern as the rest.

Same approach as before: the existing copy is preserved and the lead-in question is
prepended. Total across both passes: **183 pages**. Published live to
`nwocflooring.com`, `www.nwocflooring.com`, and the Webflow subdomain.
