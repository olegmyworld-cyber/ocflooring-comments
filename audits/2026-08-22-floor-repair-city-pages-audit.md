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
