# Floor Repair City Pages — Conversion Audit (2026-08-22)

Audit of the 30 `hardwood-floor-repair-in-{city}-wa` pages plus the main
`/services/flooring-repair` page after the conversion to repair-focused city
pages (all 31 pages edited 2026-08-22, published 17:45 PT). Reviewed via the
Webflow Data API: full page content including HTML embeds, SEO/OG metadata,
JSON-LD schema markup, shared components (Navbar, Footer, Services slider,
Areas, Partners, Why Choose), registered custom-code scripts, and sitemap
status. Every internal URL found on the pages was validated against the
site's real page inventory (160 pages).

## Must fix

### 1. Seattle page: 29 dead "Floor Repair Service Areas" links

`/seattle/hardwood-floor-repair-in-seattle-wa` has a "Floor Repair Service
Areas" block whose 29 city links all point to
`/city-of-{city}/laminate-flooring-installation-in-{city}-wa`. **No such
pages exist anywhere on the site** (the only laminate pages are
`/services/laminate-flooring-installation` and
`/services/vinyl-plank-flooring-and-laminate-flooring`), so all 29 links 404.
These are leftovers from a pre-conversion template. They should point to the
repair city pages instead:

- `/city-of-{city}/hardwood-floor-repair-in-{city}-wa` for 27 cities
- Bothell: `/hardwood-floor-refinishing/hardwood-floor-repair-in-bothell-wa`
  (the Bothell city folder's slug is `hardwood-floor-refinishing`)
- Newcastle: `/city-of-new-castle/hardwood-floor-repair-in-newcastle-wa`
  (folder slug is `new-castle`)

This was the only stale-URL problem found on any of the 31 pages.

**Fixed (2026-08-22, same session):** the stale embed was replaced with a
native Webflow section (`.ocsa`, element `ed8d99a3-7024-88ff-5bed-1eb5caf762ad`)
carrying the same heading, intro copy, and 30-city grid, with all 29 links
now pointing at the `hardwood-floor-repair-in-{city}-wa` pages (verified to
exist) and "Seattle, WA" kept as the non-linked current-page marker. Because
HTML-embed code cannot be edited through the Data API, the block was rebuilt
as real elements; its styling (including hover, responsive clamp() sizes,
and the 2-column mobile grid) was recreated in a `<style id="ocsa-css">`
block appended to the Seattle page's footer custom code, alongside the
existing `oc-repair-hero-css` block. The old embed element
(`2f264998-ac12-0ef3-c23f-83a67940373d`) was removed and the site
republished to www.nwocflooring.com, nwocflooring.com, and the Webflow
subdomain (publish confirmed 2026-08-22 18:18:58 UTC).

**Revised (same day, follow-up):** per Oleg's feedback the interim custom
`.ocsa` section did not match the sitewide service-areas design, so it was
removed again and replaced with the real shared **Section // Areas** slider
component. Three coordinated changes:

1. **New "Floor Repair Service Areas" slide** appended to the shared
   Section // Areas component (5th `.content-box-area`, same
   `heading-area` / `area-table` / `areas-row` / `area-link-item`
   structure and styles as the existing four slides). Its 30 city entries
   are real links to the `hardwood-floor-repair-in-{city}-wa` pages —
   unlike the other four slides, whose links get hrefs injected at runtime
   by the `ocarealinksinjector` script. Appears on every page carrying the
   Areas section.
2. **OCAreasStart v1.0.0** (inline script appended to the site-wide
   freeform footer code; source of record
   `webflow-scripts/ocareasstart-1.0.0.js`): the Areas slider now opens on
   the slide matching the page — repair pages on Floor Repair, the home
   page and refinishing pages on Hardwood Floor Refinishing, vinyl plank
   pages on Luxury Vinyl Plank, hardwood installation pages on Hardwood.
   It reorders the slide blocks at parse time, before the slider
   (which waits on the deferred Swiper bundle) initializes.
3. **Seattle page** now uses the shared Section // Areas component in
   place of the custom `.ocsa` block (instance
   `64b8c8ad-6a34-14a2-96b0-f7b0f9b9286a`; custom section and its
   `ocsa-css` page-footer styles removed — the hero CSS block was kept).

**Laminate slide removed (same day, per Oleg):** laminate installation is
not an offered category (blog topic only), so the "Laminate Floor Service
Areas" slide was deleted from the shared Section // Areas component. The
slider is now 4 slides — Hardwood Floor Refinishing, Luxury Vinyl Plank,
Hardwood, Floor Repair — with Refinishing as the default first slide on
pages OCAreasStart doesn't reorder. OCAreasStart bumped to v1.0.1
(comment-only change; source of record
`webflow-scripts/ocareasstart-1.0.1.js`).

To verify visually: the areas slider should show 4 dots and no Laminate
slide; repair pages open on "Floor Repair Service Areas" with clickable
city links; the home page opens on "Hardwood Floor Refinishing Service
Areas".

## Minor

2. **Bellevue and Renton pages are missing the "Book Your Free {City} Floor
   Repair Estimate" section** (heading + Schedule CTA + 4 appointment photos)
   that the other 28 city pages have. Not broken — both still carry the
   "Free In-Home Estimate — {City} Floor Repair" CTA inside their content —
   just structurally inconsistent (17 content nodes vs 24–25 elsewhere).
3. **Bothell** trust block reads "We have been repairing and installing
   floors in this corner of the Puget Sound since 2013" — the only
   present-tense "installing" claim on any repair page. Fine if intentional.
4. **Whidbey Island** mixes prepositions: H1 says "Floor Repair **on**
   Whidbey Island" (correct for an island) but the H2s say "What We Repair
   **in** Whidbey Island" / "Floor Repair **in** Whidbey Island, WA — FAQs".
5. The main `/services/flooring-repair` service-area copy names every served
   city **except Oak Harbor and Whidbey Island** (consistent with its
   "King & Snohomish County" framing — both are Island County — but those two
   repair pages get no mention from the main page).
6. The shared before/after photo used on every city page has the old
   filename `floor repair seattle, everett, wa.avif` (filename only; the alt
   text is city-neutral).

## Notes / intent questions

7. The 30 old `hardwood-floor-installation-in-{city}-wa` pages are **still
   live and still in the sitemap** — none were touched in this conversion.
   Fine if the plan is to keep installation and repair city pages side by
   side; if they were meant to be retired, they're still up.
8. The navbar tagline "1,000+ Floors Installed & Restored Across Washington"
   is rewritten to "1,000+ Floor Repairs Across Washington" by a small
   script embedded on each repair page (on Cottage Lake it's bundled at the
   end of the content embed rather than a separate embed — present on all
   30). Works for visitors with JS; non-JS crawlers see the original
   component text.
9. The "Service Areas" section (Laminate / Refinishing / LVP / Hardwood
   lists, on every page) has no hrefs in Webflow — links are injected at
   runtime by the `ocarealinksinjector` footer script, whose hosted source
   could not be fetched from this environment. It has no "Repair" list, so
   the new repair pages receive no internal links from it. Worth a quick
   browser check of where those injected links point.

## Verified clean

- **City names:** every H1, hero paragraph, subheading, image alt, FAQ,
  component override, SEO title/description, and JSON-LD block references
  its own city. Every cross-city mention on all 31 pages was reviewed
  individually — all are legitimate (the Bellevue shop address, road names
  like NE Woodinville-Duvall Rd, rivers/valleys, ferry routes, neighboring-
  town service notes, Seattle-vs-here comparisons). No cloned wrong-city
  copy anywhere.
- **Links:** apart from the Seattle block above, the only links on the city
  pages are `/contact`, `tel:+14255951079`, and (Renton, Seattle)
  `/services/flooring-repair` + `/seattle/hardwood-floor-refinishing-in-seattle-wa`
  — all valid. No `hardwood-floor-installation-*` links on any page.
- **JSON-LD:** correct Service + FAQPage schema per page, right city, right
  own-page URL, no dead URLs.
- **Phone:** (425) 595-1079 everywhere, matching the LocalBusiness schema.
- **Sitemap:** all 30 repair pages + main repair page included.
- **Photo-quote form (`#ocpq`):** submit wiring lives in the shared Footer
  component (formsubmit.co → info.ocflooring@gmail.com, city auto-derived
  from the URL slug) — works on every repair page. The empty
  `#ocpq-donehead` heading is the JS-populated success state, by design.
- **Shared components:** Navbar Services dropdown targets the current
  service pages (Floor Repair → `/services/flooring-repair`); Services
  slider hides its self-referential Floor Repair card only on repair pages
  (scoped `:has(#ocpq)` CSS); footer review-count normalizer (103) matches
  the "103 five-star reviews" used in page copy.
