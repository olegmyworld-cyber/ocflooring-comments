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

### Floor Refinishing page — home-page review section replaces Trustindex widget (2026-09-01)

**Page:** `/flooring-services-near-me/floor-refinishing` (Webflow page id
`65f32565e111adbbb806cf36`).

**Problem:** the page showed the old Trustindex "What Our Customers Say" Google
Reviews widget (the `Section // Reviews` component instance, `section.section_reviews`),
not the `#ocf-trust` reviews section used on the home page and the city
`hardwood-floor-refinishing-in-*` pages.

**Change:** added an HTML Embed element in that exact slot (between `Section // CTA 2`
and `Section // Services`) containing the same `#ocf-trust` markup as the home page —
licensing bar, "Loved by Bellevue & the Eastside" heading, 4.7 / 119 Google rating,
the four review cards and the "Read all reviews on Google" button — then removed the
`Section // Reviews` instance from this page only (the component itself is untouched,
so other pages keep it). The home page's trailing map iframe is omitted; the home page
hides it at runtime anyway via `OCRemoveHomeMap`. Mobile keeps the same horizontal
card slider the home page has (`#ocf-trust .rev-grid` under 767px).

Source of record: [`webflow-embeds/floor-refinishing-ocf-trust-reviews.html`](webflow-embeds/floor-refinishing-ocf-trust-reviews.html).

### Vinyl plank hub page rebuilt in the Arlington page's style (2026-09-01)

**Page:** `/flooring-services-near-me/vinyl-plank-flooring-and-laminate-flooring`
(page id `65f32565e111adbbb806d0d7`), previously the old-style layout.

**Change:** ported the distinctive blocks from the "Vinyl Plank Flooring Arlington, WA"
page (`65fc655de6d6ce262918416e`) onto the hub page, with every Arlington-specific line
rewritten for King & Snohomish counties — the interactive vinyl-core guide, the
project-manager process restyle, the "what homeowners want to know first"
warranty/timeline/reviews block, the interactive LVP layer explorer, the service-area
block and the vinyl plank guide & FAQ. The hero now uses the Arlington hero variant,
background image and button label, and the old Trustindex `Section // Reviews` instance
was removed from this page only (reviews now come from the ported block, as on Arlington).

Deployed as six HTML Embed elements placed directly in the page tree rather than page
custom code — Webflow rejects page custom code above roughly 10k characters (HTTP 406).
The two blocks that depend on hosted scripts on the Arlington page (its `#ocarl` CSS from
`ocvinyladv`, its core-guide interactivity from `ocVinylCore`) were made self-contained
here, so this page loads no additional hosted script.

Source of record: [`webflow-embeds/vinyl-plank-hub-arlington-port.html`](webflow-embeds/vinyl-plank-hub-arlington-port.html).

**Follow-up (2026-09-01):** removed six old-style sections from the vinyl plank hub page
at Oleg's request — "Luxury Vinyl Plank – Style & Durability Without the Price Tag"
(`section_vinyl`), "What Vinyl Plank Flooring Costs in King & Snohomish Counties"
(`section_price`), "Why Choose Waterproof Vinyl Plank in the PNW?" (`section_features`),
"Vinyl or Linoleum – What's Best for Your Home?" (`section_benefits`), the "Our Projects"
gallery (`section_gallery`) and the "We Bring the Showroom to You" CTA
(`Section // CTA 2` instance, removed from this page only). What remains is the hero, the
red line, partners, the ported blocks, the 3-step process section, services, why-choose,
areas and the footer.

**Follow-up 2 (2026-09-01):** true copy of the Bellevue vinyl page's native sections onto
the vinyl hub page, done via temporary components: each Bellevue section
(`section_benefits` before/after slider, `section_schedule`, `section_steps`,
`section_features`, the `padding-global` block and the `ocgd` guides section) was
transformed into a temp component, instantiated on the hub page in Bellevue's order,
then unlinked to plain elements on BOTH pages and the temp components deleted — the
Bellevue page is unchanged in effect. A fresh `Section // Galllery` component instance
was also added (its Floor Type filter still needs the one-click "Vinyl" override in the
Designer; the filter prop is not writable via the API). The hub's old 3-step process
section and an empty stray section were removed, and Bellevue-specific wording in the
copied sections was rewritten for King & Snohomish counties (schedule subtitle, two
guide-link labels).

**Follow-up 3 (2026-09-01):** modernized the vinyl hub page hero image — page footer CSS
stretches the cover image to the full hero height beside the text (the same stretch the
city vinyl pages get from `ocvinylheroimg`, which is path-guarded and skips this page),
with `object-fit: cover`, rounded corners and a soft shadow; tablet and phone get scaled
heights. Source: `webflow-embeds/vinyl-hub-hero-css.html`.

**Follow-up 4 (2026-09-01):** vinyl hub page "Why Choose" section image swapped from the
component's default floor-sander photo to the family photo (`shutterstock_1660546246`,
asset `69297010e9eef7401e398228`) — the same family image the Arlington vinyl page uses
in that spot. The other family asset (`shutterstock_1309145173`) already appears in this
page's before/after benefits section, so it was not reused.

**Follow-up 5 (2026-09-01):** vinyl hub page copy pass — every remaining city-generic
title and text rewritten in King & Snohomish counties style. Page title → "Vinyl Plank
Flooring | King & Snohomish Counties"; SEO title → "Vinyl Plank Installation | King &
Snohomish Counties WA"; meta description tightened with both counties and city examples
(OG tags inherit). Section rewrites: steps h2 → "How King & Snohomish County Homeowners
Get Floors They Trust" (now matches the runtime restyle), features h2 → "Advantages of
Vinyl Plank Flooring for Puget Sound Homes" plus a county-flavored subtitle, schedule
h2 → "Let's Get Started on Your New Floors — Anywhere in King & Snohomish Counties",
and the first two process step descriptions now name the counties and cities.
