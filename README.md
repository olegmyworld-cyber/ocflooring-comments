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

### "near me" extended to the remaining service pages (2026-08-28)

I had wrongly claimed the previous pass covered every hero on the site. It did not:
the `/flooring-services-near-me/` folder holds **19** service pages and only 3 had
been updated. The other **16** are now done:

hardwood-floor-installation · laminate-flooring-installation ·
stair-installation-and-remodeling · hardwood-floor-staining · dustless-floor-sanding ·
eco-friendly-floor-refinishing · buff-and-recoat-hardwood-floors ·
hardwood-floor-maintenance · solid-hardwood-flooring · engineered-hardwood-flooring ·
unfinished-hardwood-floors · commercial-flooring-installation ·
insurance-restoration-services · wood-wall-panels · flooring-store · our-products

These are region-wide, so the lead-in carries no city: "Searching for `<service>`
near me?" The buff-and-recoat page already opened with "Buff & Coat near me
refreshes hardwood…", so that stray phrase was reworded to avoid saying "near me"
twice.

Running total: **199 pages**.

**Deliberately left alone** — three pages use the same hero but are not service
pages, so a "near me" lead-in would not fit the copy: Our Work, Why We're
Different, and Financing. About Us, Contact, Reviews, Blog, the flooring
calculator and the galleries do not use this hero section at all.

Published live to `nwocflooring.com`, `www.nwocflooring.com`, and the Webflow
subdomain.

### Floor refinishing hub page rebuilt to match the Seattle city page (2026-08-28)

`/flooring-services-near-me/floor-refinishing` (page `65f32565e111adbbb806cf36`) now
mirrors the Seattle refinishing page section-for-section, with region-wide copy so the
two pages don't compete for the same terms.

**Section order — now identical to Seattle:**
Navbar · Hero · Line RED · Partners · Benefits · Features · Gallery · Cost ·
Schedule · CTA 2 · Services · FAQ · Why Choose · Areas · Flooring Guides · Footer

**Added**
- Benefits section, rebuilt natively with the Seattle classes (`section_benefits`,
  `container-main is-benefits`, `benefits-item`, …) plus the red
  "Get My Free In-Home Estimate" button.
- `Section // Cost` and `Section // Schedule` component instances.
- A 5-question FAQ block using the `sea-faq*` classes, with region-wide questions,
  plus matching `FAQPage` + `BreadcrumbList` JSON-LD (the page had none before).
- "Flooring Guides & Answers" links section, pointing at the five refinishing-related
  service pages rather than Seattle-specific blog posts.

**Changed**
- Hero switched from the static background image to the video treatment Seattle uses;
  H1 is now "Dustless Hardwood Floor Refinishing in Bellevue & Seattle, WA".
- CTA 2, Why Choose and Cost copy rewritten region-wide. The Why Choose text had been
  falling through to the component default, which ended with the stray note
  "what h tag i need to use?" — that is gone.

**Removed** (as agreed): the `Section // Reviews` and second `Section // CTA` blocks,
which the Seattle page does not have.

**Known deviations from Seattle** — API limits, not choices:
- The gallery still shows all flooring types; Seattle's is filtered to hardwood. The
  Designer's filter prop type is not writable through the Data API.
- Benefit items render as plain text; Seattle bolds the leading question. `Strong` /
  `Span` elements cannot be created through the element builder.
- The guides list uses styled divs rather than `ul`/`li` for the same reason.

Published live to `nwocflooring.com`, `www.nwocflooring.com`, and the Webflow
subdomain.
