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

## Changes on branch `claude/nwocflooring-blog-sections-470kqm`

### Blog listing page — removed three trailing sections (2026-08-29)

**Request:** remove the "See Available Appointments" CTA, the Google Reviews
carousel, and the "More services" carousel from `/blog`.

**Change:** removed three component instances from the Blog page
(`65f32565e111adbbb806ceaa`) via the Webflow Data API. No component definitions
were touched, so every other page that uses these sections is unaffected.

| Removed instance | Component | Rendered as |
| --- | --- | --- |
| `fb218189-298c-5985-be04-6be23ffba878` | `Section // CTA 2` | "See Available Appointments" + image grid + *Schedule Free In-Home Estimate* button |
| `e8f86afb-d7cf-889a-5692-3a73ef388a65` | `Section // Reviews` | Elfsight Google Reviews widget (`elfsight-app-48ef4cd4-…`) |
| `8f988b5e-0fe5-5afa-8f20-343cc2093e03` | `Section // Services` | "More services" carousel + *Book Appointment* button |

Page body order is now: Global Styles, Navbar, `section_hero-services`,
`Line RED`, `Section // Partners`, `section_blog`, `Section // Areas`, `Footer`.

No script change was needed: neither `octrustreviewsinjector9d` nor
`ocreviewsmover` runs on `/blog` (both guard on home / city / about-us /
our-work / why-were-different paths), so nothing re-injects a review section
there.

Published live to `nwocflooring.com`, `www.nwocflooring.com`, and the Webflow
subdomain.

### Blog → city page interlinking (2026-08-29)

**Request:** every blog post should carry an interlink block to the service's
city pages, with 4 links.

**Starting state:** the city pages already linked *out* to blogs (5 links on
refinishing/vinyl/installation/repair via `ocgd-a`, 5 on carpet via `cg-link`,
3 on tile via `tg-card`). The reverse direction was almost absent — only 14 of
147 posts linked to any city page.

**Change:** added a `City Links` rich text field (`city-links`,
id `a3e27844e563d32fec69afea52253809`) to the Blogs collection, populated it on
all 147 posts, and bound it in the Blogs Template
(`65f32565e111adbbb806cf1a`) as a rich text element `#oc-geo-links` placed
directly after the `post-body` element, with a scoped stylesheet in a sibling
HTML embed. Post bodies were **not** modified — the block lives in its own
field, so it can be regenerated or removed without touching post content.

**Link selection** (`seo/assign.py`, output in `seo/blog-city-links.json`):
each post gets 4 links — 2 for the post's own service and 2 for a neighbouring
service — chosen by (1) the city the post actually names, (2) the least-linked
city page, capped so no page exceeds 10 inbound links and no single city
appears more than twice in one block. A repair pass guarantees full coverage.

Result: 588 new internal links; all 173 city pages receive between 1 and 10;
90% of the 71 posts that name a city link to that city's page.

`seo/classify.py` assigns each post to one of the six services by keyword
scoring, with manual overrides for posts the scoring got wrong.

**URLs** come from each page's Webflow `publishedPath`, which is irregular but
authoritative — most cities sit under `/city-of-<city>/`, Seattle under
`/seattle/`, Bothell under a legacy `/hardwood-floor-refinishing/` folder, and
Newcastle under `/city-of-new-castle/`.

Published live to `nwocflooring.com`, `www.nwocflooring.com`, and the Webflow
subdomain.

#### Known gaps (not addressed)

- There is no `hardwood-floor-refinishing-in-bellevue-wa` page. Refinishing is
  the only service missing a Bellevue city page; the other five have one.
- 82 in-body links across the older posts point at root-level city URLs
  (e.g. `/hardwood-floor-refinishing-in-seattle-wa`) instead of the real
  folder paths. They presumably rely on redirects. New links use the real paths.
- Tile city pages carry 3 blog links where other services carry 5. A fourth
  could not be added through the Webflow MCP surface: `data_element_builder`
  silently ignores `set_text`, and the divs it creates reject `set_text`
  afterwards, so the card text cannot be authored via the API.
- Webflow rewrote 21 post bodies on save, repointing legacy `/services/<x>`
  links to `/flooring-services-near-me/<x>`. This was Webflow's own link
  repair, not an edit of ours, and it fixed stale links.
