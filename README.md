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
applied at the page footers of the Floor Refinishing page and the Home page
(`65f32565e111adbbb806ce6e`), which renders the same section (the site-wide
footer block is at its 15-script limit; page-level blocks are separate). The
5-step process is the right column (`.ots-steps-col`) of the runtime-injected
Bona tone/steps section (`#oc-tone-steps`), so the script polls until that
column exists, then appends a "Book Your Free In-Home Estimate" heading and the
Calendly inline widget, and loads Calendly's `widget.js` once. The embed URL
(`calendly.com/nwwillsflooring/free-in-home-estimate-online-today-clone-1`
with `hide_gdpr_banner=1`) and sizing were copied verbatim from the Contact Us
page's HTML embed.

**v1.1.0:** v1.0.0 anchored on `#oc-tone-steps .ots-steps-col`, which did not
match the Home page's current section markup (nothing appeared). v1.1.0 is
markup-agnostic: it still tries `.ots-steps-col` first, then falls back to
finding the rendered "Final Walkthrough" text (skipping script/style template
strings), climbing to the steps column that holds the "5-Step … Process"
heading, and inserting the calendar right after the last step. Polling extended
15s → 60s in case the section builds late. Verified in headless Chromium
against four mock section structures (exact class, nested list, flat rows,
late-injected) — one insert each, correct position. See
[`webflow-scripts/occalendlysteps-1.1.0.js`](webflow-scripts/occalendlysteps-1.1.0.js).

**v1.2.0:** Accented booking card per follow-up request ("make more accent on
it"): the calendar now sits in a white card with a red top bar, a red
"★ FREE — BOOK ONLINE" pill badge, a larger navy serif heading and a short
sub-line, matching the site's navy/red/cream palette. See
[`webflow-scripts/occalendlysteps-1.2.0.js`](webflow-scripts/occalendlysteps-1.2.0.js).

**Rollout to city pages:** per follow-up request, the script was also applied at
the page footer of all 29 `hardwood-floor-refinishing-in-*-wa` city pages
(published under city folders, e.g. `/seattle/hardwood-floor-refinishing-in-seattle-wa`;
their 5-step section carries the same "Our 5-Step … Process in {City}" heading,
which the text-based placement already handles). Pages that somehow lack the
section are unaffected — the script no-ops after its 60s poll window.

**v1.3.0 — root-cause fix ("nothing appears on any page" after v1.2.0):**
v1.2.0 built the card via `innerHTML` with literal HTML tags inside the inline
script source. Every proven-rendering inline script on this site builds DOM
exclusively with `createElement` (bigger markup lives in external hosted
files); v1.1.0 (createElement-only) worked while v1.2.0 (innerHTML) rendered
nowhere — Webflow's inline custom-code pipeline evidently doesn't tolerate
tag-like sequences in registered inline scripts. v1.3.0 rebuilds the identical
accent card with `createElement` only (the deployed minified source contains no
`<` character at all) and adds visibility-aware anchoring (hidden template
copies of the section can't swallow the card). Verified in headless Chromium
against six mock structures, including hidden-template and true
inline-`<script>` embedding. Applied to all 31 pages (Home, Floor Refinishing,
29 city pages). See
[`webflow-scripts/occalendlysteps-1.3.0.js`](webflow-scripts/occalendlysteps-1.3.0.js).

**v1.4.0 — placement fix:** v1.3.0 rendered, but the card landed below the
whole two-column section — on the live pages the section heading is a sibling
of the column wrap, so climbing to "the ancestor holding the heading" overshot
to section level. v1.4.0 anchors to the steps list itself: climb from the
visible "Final Walkthrough" leaf until the parent also contains step 2's title
("Dustless Sanding") — that parent is the innermost container holding all five
steps and the stopped-on node is the step-5 row; the card is inserted right
after it, exactly under "5 · Final Walkthrough". Heading-climb kept as
fallback; `.ots-steps-col` fast path removed. Verified against six mocks
including one replicating the live layout. Applied to all 31 pages. See
[`webflow-scripts/occalendlysteps-1.4.0.js`](webflow-scripts/occalendlysteps-1.4.0.js).

**Scope-down (2026-08-25):** per follow-up request ("Remove it from all
hardwood floor refinishing pages"), `occalendlysteps` was removed from the 29
`hardwood-floor-refinishing-in-*-wa` city pages and from
`/services/floor-refinishing`, and then (same day, follow-up request) from the
Home page as well. The card is now applied to NO pages. The script stays
registered site-side (`occalendlysteps` v1.4.0, working and position-verified),
so re-adding it to any page is a single `add_page_script` call.

Published live to `nwocflooring.com`, `www.nwocflooring.com`, and the Webflow
subdomain.

### Other work on this branch (2026-08-27), documented in subdirectory READMEs

- [`webflow-scripts/services-install-page/`](webflow-scripts/services-install-page/README.md)
  — ported all content from the Bellevue hardwood-installation page onto
  `/services/hardwood-floor-installation` for a design match, then
  redesigned the flooring-type/installation-method card grids to be
  compact with a mobile slider, and repositioned the reviews section.
- [`webflow-scripts/carpet-pages/`](webflow-scripts/carpet-pages/README.md)
  — mobile-only swatches slider, "Also serving" section removal, trust-bar
  mobile alignment fix, and the `#book` CTA anchor-scroll fix, across all
  30 carpet installation pages.
- [`webflow-scripts/tile-pages/`](webflow-scripts/tile-pages/README.md) —
  "Recent work" photo gallery redesign (framed cards, hover zoom) across
  all tile installation pages.
- [`webflow-scripts/navbar/`](webflow-scripts/navbar/README.md) — icons
  added to all 13 category links in the sitewide "Services" dropdown menu,
  plus the top-level mobile menu items (About Us, Services, Our Work,
  Price, Financing).
- [`webflow-scripts/our-work-page/`](webflow-scripts/our-work-page/README.md)
  — mobile-only slider for the Hardwood Floor Refinishing and Flooring
  Installation gallery categories on `/our-work`.

Published live to `nwocflooring.com`, `www.nwocflooring.com`, and the
Webflow subdomain.

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
