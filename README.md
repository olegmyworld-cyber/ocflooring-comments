# OC Flooring — Webflow fix scripts

Source records for custom code applied to the OC Flooring Webflow site
(`nwocflooring.com`, site id `6377e8e6a53936b48ef1cad0`). These are registered as
inline scripts via the Webflow Scripts API and applied at the site footer.

## Changes on branch `claude/oc-flooring-carpet-page-ig4q1w`

### New page: Carpet Installation in Bellevue, WA (2026-08-24)

Built the "Carpet Mobile Showroom v2" Claude Design
([`design/Carpet Mobile Showroom v2.dc.html`](design/Carpet%20Mobile%20Showroom%20v2.dc.html))
as a native Webflow page in the **City of Bellevue** folder:

- **Page:** `/city-of-bellevue/carpet-installation-in-bellevue-wa`
  (page id `6a8ccb1ebf28596111eed9f2`, folder id `65f32565e111adbbb806cece`).
  Created via the Pages API with the design's SEO title/description and Open
  Graph metadata; JSON-LD (`FlooringContractor` + `Service` + `BreadcrumbList` +
  `FAQPage`) written through the schema-markup API with URLs updated to the
  real published path.
- **Content:** all eleven sections (hero + nav, trust bar, cost answer,
  how-it-works, services & prices, sample gallery, cost estimator, stretch vs
  replace, reviews, FAQ, service areas, CTA, footer) built as native Webflow
  elements with `ci-*` prefixed classes via the WHTML builder. 13 images
  (hero, 8 carpet swatches, 3 job photos, logo) uploaded as site assets with
  SEO file names and bound to the image elements.
- **Interactive code:** the cost estimator + FAQ accordion live in
  [`webflow-scripts/oc-carpet-bellevue-1.0.0.js`](webflow-scripts/oc-carpet-bellevue-1.0.0.js),
  uploaded as a Webflow asset and loaded by the registered inline script
  [`webflow-scripts/occarpetbellevue-1.0.0.js`](webflow-scripts/occarpetbellevue-1.0.0.js)
  (page footer). Google Fonts (Newsreader + Hanken Grotesk) and the canonical
  link are injected by
  [`webflow-scripts/carpetbellevuefontscanonical-1.0.0.js`](webflow-scripts/carpetbellevuefontscanonical-1.0.0.js)
  (page header) because the custom-code API rejects markup containing external
  URLs. Estimator styles + font fallbacks are in the page's head custom code.
- **Not published:** the page is staged in the Designer only — publish the site
  to take it live.

### Carpet page fixes after first publish (2026-08-24)

Three problems surfaced on the live page; all fixed in the Designer (republish
to take effect):

1. **Unstyled cost estimator.** The `es-*` styles written to the page's head
   custom code via the API did not survive to the published page (the stored
   head block came back empty). Fix: bundle
   [`webflow-scripts/oc-carpet-bellevue-1.1.0.js`](webflow-scripts/oc-carpet-bellevue-1.1.0.js)
   now injects its own `<style>` at load, so the estimator no longer depends on
   page custom code. Loader
   [`webflow-scripts/occarpetbellevue-1.1.0.js`](webflow-scripts/occarpetbellevue-1.1.0.js)
   registered as v1.1.0 and applied to the page footer.
2. **Stretch-vs-replace gallery broke at desktop widths.** The
   `auto-fit/minmax` column template fit three tracks at full width, throwing
   the two-row layout off. Fix: `ci-gal-grid` locked to
   `repeat(2, minmax(0,1fr))` (1 column on mobile portrait) and the cells got
   explicit heights (`476px` tall stairs cell, `230px` others) with
   `overflow:hidden` + radius on the cell itself.
3. **Duplicate navigation.** The design's own nav row duplicated the site-wide
   injected header. Fix: removed the `ci-nav-row` element and its styles — the
   standard site header (injected by the existing site scripts) is the only nav
   now.

Also added per Oleg's request: the **Calendly scheduler** from the Contact page
(`calendly.com/nwwillsflooring/free-in-home-estimate-online-today-clone-1`) as
an HTML embed with the identical widget code.

### Second round of layout changes (2026-08-24, same day)

- **Calendly moved** from the top of the page to a new two-column section
  (`ci-book-sec` / `ci-book-grid`) directly under the "How much does carpet
  installation cost" section: info column on the left (eyebrow, heading, what
  the visit includes, phone line) and the scheduling calendar in a white card
  on the right (`ci-book-cal`). The old top booking card and its styles were
  removed.
- **Standard site navbar added.** The carpet page now starts with the same
  "Global Styles" and "Navbar" component instances as the home page, with the
  navbar's prop overrides copied from the home page instance (variant
  `eb34f5cc…`, "Get a Free Estimate" button, "Contact Us" / "Service Areas"
  labels). The earlier assumption that the site header was injected by
  scripts was wrong — it is a Webflow component placed per page.

### Navbar overlap fix (2026-08-25)

The site navbar is `position:fixed`, so after adding it the page content slid
underneath it (breadcrumb hidden, hero cropped). Fix: `ci-page` got a `7rem`
baseline `padding-top`, and bundle
[`webflow-scripts/oc-carpet-bellevue-1.2.0.js`](webflow-scripts/oc-carpet-bellevue-1.2.0.js)
now measures the rendered navbar (announcement strip included) on load/resize
and sets the wrapper's exact top clearance. Loader registered as v1.2.0.

### Van photo in booking section (2026-08-25)

Added the OC Flooring van photo (asset `6a8cdcef02643a402aaa9e4a`,
`oc-flooring-van-150kb.avif`, uploaded by Oleg) under the "Prefer the phone?"
line in the booking section's info column — full-width, 340px tall,
object-fit cover, 20px radius (`ci-book-photo`).

### Photo-upload CTA in the stretch section (2026-08-25)

Under the "Stretch it / Replace it" cards, a white card now offers "Not sure
which one you're looking at?" with the same pulsing green **Upload Your
Photos** button used on the hardwood floor repair page, linking to that
page's photo-quote widget
(`/city-of-bellevue/hardwood-floor-repair-in-bellevue-wa#ocpq`) so carpet
visitors can send pictures and get a stretch-or-replace answer by email.
The ring animation keyframes live in bundle
[`webflow-scripts/oc-carpet-bellevue-1.3.0.js`](webflow-scripts/oc-carpet-bellevue-1.3.0.js)
(Webflow styles cannot hold @keyframes); loader registered as v1.3.0.

### Marketing hook + on-page photo uploader (2026-08-25)

- **Red marketing hook band** (`ci-hook`) directly under the hero: "Skip the
  carpet store. Our mobile showroom brings it to you — and you leave the visit
  with your exact price," with three stat cards (1 visit / from $1.49 per sq ft
  / 1 day) and a white "Bring the showroom to me" button that scrolls to the
  booking section (`#book`, id set at runtime by the bundle — the settings API
  rejected writing it).
- **On-page photo uploader** (`ci-pq` section, `#ci-photo-quote`, between the
  service areas and final CTA): a **native Webflow form** named "Carpet Photo
  Quote" — name/email (required), phone, project-type select (HTML select via
  WHTML; the API select's options were not editable), details textarea, and
  THREE native Webflow file-upload fields (Photo 1/2/3, 10 MB each, supported
  by the site's Ecommerce plan). Submissions land in Webflow's Forms panel and
  email notifications like the existing Quiz Form. Includes an "or text your
  photos to (425) 595-1079" line. The stretch-section "Upload Your Photos"
  button now scrolls to `#ci-photo-quote` instead of the repair page.
- **Important finding:** the hardwood repair page's `#ocpq` uploader has NO
  JavaScript behind it anywhere (checked all 1,200 assets — every one of the
  95 .js assets downloaded and grepped — all 15 applied site scripts, page
  scripts, embeds, and custom code). It is dead UI: none of its buttons or its
  submit can work. Consider replacing it with a native Webflow form like the
  carpet page's.
- Bundle
  [`webflow-scripts/oc-carpet-bellevue-1.4.1.js`](webflow-scripts/oc-carpet-bellevue-1.4.1.js)
  (loader
  [`webflow-scripts/occarpetbellevue-1.4.1.js`](webflow-scripts/occarpetbellevue-1.4.1.js))
  adds the form styling, runtime placeholders (the API reserves the
  placeholder attribute), and the `#book` anchor.

### Natural hook band + repair-page-style uploader (2026-08-25)

Oleg's feedback on the previous round: the red hook band was too loud ("make it
natural and not in red color fon") and the plain stacked form "looks old — I
want same as I have on hardwood floor repair."

- **Hook band restyled to the page's natural palette** (Designer style
  updates, no markup change): cream `#F7F2EC` background with a hairline top
  border instead of the red gradient; dark serif heading, muted body copy;
  stat cards are now white with the numbers as the only red accent; the
  "Bring the showroom to me" button is now the standard red pill (white on
  red, hover darkened). Same copy, same stats, same anchor.
- **Photo-quote form rebuilt into the repair page's uploader design.** Bundle
  [`webflow-scripts/oc-carpet-bellevue-1.5.0.js`](webflow-scripts/oc-carpet-bellevue-1.5.0.js)
  (loader
  [`webflow-scripts/occarpetbellevue-1.5.0.js`](webflow-scripts/occarpetbellevue-1.5.0.js))
  restructures the form at runtime into the `#ocpq` widget's visual language:
  a white card with three dashed **photo drop-tiles** ("The worst spot / A few
  feet back / The whole room", tap to add, `accept="image/*"` so phones open
  the camera roll), a **chip row** for the project type (the chips drive the
  hidden native select, now submitting as "Project type"), block titles with
  subtitles ("Tell us about it in your own words", "Where should the price
  go?"), a 3-column labeled field grid, the red pill submit next to the
  "sent before 3pm" note, and a 3-card promise row (Same day / A person, not
  a bot / No obligation). The native Webflow form and its file-upload widgets
  stay intact underneath — nodes are only moved/wrapped, so Webflow's upload
  handlers and Forms-panel/email delivery keep working; if the runtime
  rebuild ever fails the form falls back to the previous stacked layout.
  Also fixed: the real `w-file-upload-input` is kept visually hidden again
  (the v1.4.x fallback rule could reveal it on the published page).
- Note: the repair page's own `#ocpq` widget has no CSS or JS anywhere on the
  site (see previous entry) — so this round recreates its intended design
  from its markup rather than copying live styles.
- **1.5.1** (same day, per Oleg): removed "New carpet installation" from the
  project-type chips (and the hidden select) — the chips are now Carpet
  stretching / Carpet repair / Stair carpet / Not sure. Bundle
  [`webflow-scripts/oc-carpet-bellevue-1.5.1.js`](webflow-scripts/oc-carpet-bellevue-1.5.1.js),
  loader
  [`webflow-scripts/occarpetbellevue-1.5.1.js`](webflow-scripts/occarpetbellevue-1.5.1.js).

### The real repair-page uploader, wired the real way (2026-08-25, v1.6.0)

Oleg tested the live page: the redesigned native Webflow form uploaded the
photo but **failed on submit**, and he asked for "the same email address and
format as on hardwood floor repair page and their design for upload photo."

- **Root cause of the earlier "dead UI" verdict found.** The repair pages'
  `#ocpq` widget is NOT dead: its styles and submit script live in an HTML
  embed inside the shared **Footer component** (documented in the city-pages
  audit on branch `claude/oc-flooring-city-pages-review-cvv1u7`) — a location
  the earlier asset/site-script sweep never looked. It submits a multipart
  POST to **formsubmit.co** (account token for `info.ocflooring@gmail.com`),
  `_template=table`, subject `Photo quote - <City> - <Name> - <N> photos`,
  photos attached, city derived from the URL slug. The carpet page uses the
  design's own footer, so it never had that wiring.
- **Carpet page now runs the identical widget.** Bundle
  [`webflow-scripts/oc-carpet-bellevue-1.6.0.js`](webflow-scripts/oc-carpet-bellevue-1.6.0.js)
  (loader
  [`webflow-scripts/occarpetbellevue-1.6.0.js`](webflow-scripts/occarpetbellevue-1.6.0.js))
  injects the same `#ocpq` CSS, renders the widget section before the final
  CTA, and runs the same submit script — same formsubmit.co token, same email
  format to info.ocflooring@gmail.com, subject
  `Photo quote - Bellevue, WA - <Name> - <N> photos` — with carpet wording
  and carpet chips (Ripples & waves / Matted traffic paths / Pet damage or
  odor / Seams splitting or fraying / Stairs & landings / Water damage /
  Not sure; no "new carpet" chip, per the 1.5.1 request). Widget source of
  record:
  [`webflow-scripts/carpet-ocpq-embed-1.0.0.html`](webflow-scripts/carpet-ocpq-embed-1.0.0.html)
  (self-guarded with `data-init`, so adding the site Footer component to the
  page later cannot double-bind). Verified end-to-end locally with a stubbed
  formsubmit.co (multipart POST with attachment observed, success state
  rendered).
- **Old native form removed** (the `ci-pq` section) — its submissions were
  failing on the live site; the FormWrapper-based uploader is gone.
- **Stretch-section button fixed for real:** the "Upload Your Photos" button
  had carried a literal `href` attribute to the repair page since the first
  build, silently overriding every later `set_link` repoint — clicks were
  leaving the page. The stale attribute is removed and the link setting now
  targets `#ocpq` on the carpet page.
- Fonts script bumped to
  [`webflow-scripts/carpetbellevuefontscanonical-1.1.0.js`](webflow-scripts/carpetbellevuefontscanonical-1.1.0.js)
  (adds Playfair Display 700/800, which the widget's headings use).

### SEO/AI-search visibility for the widget (2026-08-25, v1.6.1)

Per Oleg's question whether the page is "clearly seen for SEO and AI search":
everything except the JS-rendered widget already was — the thirteen content
sections, H1, FAQ, prices, meta/OG and the JSON-LD schema are native
server-rendered HTML. To close the one gap, the photo-quote section's header
(eyebrow, H2 "Send photos of your carpet…", lead including
installation/stretching/repair keywords) now ships as a real HTML embed on the
page — visible to non-JS crawlers (GPTBot, ClaudeBot, PerplexityBot, CCBot)
the same way the repair pages' widget markup is. The embed carries an empty
`#ocpq-shell`; bundle
[`webflow-scripts/oc-carpet-bellevue-1.6.1.js`](webflow-scripts/oc-carpet-bellevue-1.6.1.js)
(loader
[`webflow-scripts/occarpetbellevue-1.6.1.js`](webflow-scripts/occarpetbellevue-1.6.1.js))
fills the shell with the interactive interior, keeping the full
section-render as a fallback when the embed is absent. Both paths verified
locally end-to-end against a stubbed formsubmit.co. The cost estimator's
internals remain JS-only by design (it is a calculator; its section heading
and copy are native elements).

### Icon layer for the text-heavy sections (2026-08-25, v1.7.0)

Per Oleg ("i need more icons for this page… because here most text
information"): bundle
[`webflow-scripts/oc-carpet-bellevue-1.7.0.js`](webflow-scripts/oc-carpet-bellevue-1.7.0.js)
(loader
[`webflow-scripts/occarpetbellevue-1.7.0.js`](webflow-scripts/occarpetbellevue-1.7.0.js))
adds ~25 decorative inline-SVG stroke icons (aria-hidden, currentColor,
1.8-stroke — same visual language as the photo-quote widget and the repair
pages), each matched to its element's meaning by keyword so edited or
reordered cards keep sensible icons:

- Trust bar: house ("12 years, family owned"), shield-check ("Licensed,
  bonded & insured").
- Hook stat cards: showroom van (1 visit), price tag ($1.49/sq ft),
  clock (1 day).
- How-it-works cards: calendar / van / written-quote clipboard / house-check
  in the top-right corner of each step.
- Services & prices cards: pad layers, carpet roll, stairs, stretch arrows.
- Extras cards: van (haul-away), sofa (furniture moving), paw (pet pad).
- Pad tiles: check (Standard), star (Recommended), paw (Pets & kids).
- Stretch it / Replace it: stretch arrows vs swap arrows.
- Service-areas heading: map pin. CTA buttons: calendar + phone. The green
  "Upload Your Photos" button: camera.

Icons are injected at runtime into soft rounded chips (cream `#F5EDE4`, rust
strokes); idempotent per element and wrapped in try/catch, so a failure
leaves the page exactly as before.

### Same icon treatment on the Bellevue floor-repair page (2026-08-25)

Per Oleg ("do the same icons on hardwood floor repair page"): new page-scoped
bundle
[`webflow-scripts/oc-repair-icons-1.0.0.js`](webflow-scripts/oc-repair-icons-1.0.0.js)
(loader
[`webflow-scripts/ocrepairicons-1.0.0.js`](webflow-scripts/ocrepairicons-1.0.0.js),
applied at the page footer of
`/city-of-bellevue/hardwood-floor-repair-in-bellevue-wa` — that page's first
page-level script). The repair page already carries icons in its embeds
(What-We-Repair card icons, green ✓ list bullets, numbered photo steps,
FAQ +/-), so this fills only the gaps, in the page's own palette (tan chips,
`#be1e2d` strokes):

- camera inside all four green "Upload Your Photos" pills (`.ocbp-btn`);
- wrench / swap chips in the top-right of the "Repair it if / Refinish it
  if" decision cards, tinted green/red to match each card's accent;
- the two quick-test glyphs (● water drop, ☀ rug test) upgraded to matching
  stroke SVGs;
- a book icon on the "Flooring Guides & Answers" heading.

**Rolled out to all 30 repair city pages** (same day, per Oleg): the
registered `ocrepairicons` 1.0.0 loader is now applied at the page footer of
every `hardwood-floor-repair-in-*` page (Arlington, Bellevue, Bothell,
Cottage Lake, Duvall, Edmonds, Everett, Issaquah, Kenmore, Kirkland, Lake
Stevens, Lynnwood, Marysville, Medina, Mercer Island, Mill Creek, Monroe,
Mukilteo, Newcastle, North Bend, Oak Harbor, Redmond, Renton, Sammamish,
Seattle, Shoreline, Snohomish, Snoqualmie, Whidbey Island, Woodinville) —
**plus the main `/services/flooring-repair` service page** (page id
65f32565e111adbbb806cf4f), added per Oleg's follow-up. None of these pages
had page-level scripts before, so each page's scripts list is exactly this
one entry. The decorator is selector-driven and no-ops on any element it
can't find, so pages with structural quirks (e.g. Seattle's split embeds,
or any repair-widget sections the main service page doesn't have) degrade
safely.

### Carpet category rollout: 30 city pages, nav, slider, internal links (2026-08-25)

Per Oleg: carpet pages "for all city names", a Services nav entry, the carpet
category in the service-areas slider "as shown in the screenshot", internal
links between all carpet pages, carpet blog links on the city pages, unique
per-city text, and no duplicate content.

**Pages.** `/…/carpet-installation-in-<city>-wa` now exists for all 30 cities
that have a floor-repair page (Arlington, Bellevue, Bothell, Cottage Lake,
Duvall, Edmonds, Everett, Issaquah, Kenmore, Kirkland, Lake Stevens,
Lynnwood, Marysville, Medina, Mercer Island, Mill Creek, Monroe, Mukilteo,
Newcastle, North Bend, Oak Harbor, Redmond, Renton, Sammamish, Seattle,
Shoreline, Snohomish, Snoqualmie, Whidbey Island, Woodinville), each in that
city's existing folder. Every page is a duplicate of the Bellevue design, so
layout, styles, icons, estimator and photo-quote widget are identical.

**Text.** Each page carries a full content pack written for that city alone —
86 replaced strings (breadcrumb through footer), 16 real neighborhood names,
SEO title/description, Open Graph copy, image alt texts, map coordinates,
and a 10-question FAQ. The angle per city comes from its own identity:
Boeing shift work in Everett, Deception Pass and PCS move dates in Oak
Harbor, ferry-bluff stairs in Mukilteo, Ridge builder-grade upgrades in
Snoqualmie, estate discretion in Medina, Craftsman-vs-townhouse wear in
Seattle. Packs are stored in
[`webflow-scripts/carpet-rollout/packs/`](webflow-scripts/carpet-rollout/packs/)
as the source of record. Prices and claims are identical everywhere by
design ($1.49/sq ft install, from $2.49 carpet+pad, $18/step, $99/room
stretch, $0.50 haul-away, $0.65 pet pad, 20+ samples, three pad grades,
1-year workmanship warranty).

**Schema.** Every page gets its own JSON-LD graph: FlooringContractor +
Service (city-scoped, with that city's coordinates) + BreadcrumbList +
FAQPage carrying its 10 unique Q&As.

**Navigation and category.**
- The site Navbar's Services dropdown gained a "Carpet Installation" entry
  (component-level, so it appears site-wide).
- The shared "Section // Areas" component gained a fifth slide, **Carpet
  Installation Service Areas**, listing all 30 cities — the same pattern as
  the Hardwood/LVP/Repair slides in Oleg's screenshot. Bundle v1.8.0 moves
  that slide to the front on carpet pages, mirroring the site's existing
  OCAreasStart behavior for the other categories.

**Internal linking.** The "Also serving" chip row on every carpet page is now
29 real links — one to each of the other 29 carpet city pages — giving the
category a complete mesh (870 internal links total). Each page also gained a
**Carpet guides** section linking five of the site's existing carpet blog
posts, chosen per city (local posts preferred where one exists).

**Scripts.** All carpet pages run
[`oc-carpet-bellevue-1.8.0.js`](webflow-scripts/oc-carpet-bellevue-1.8.0.js)
(city derived from the URL slug for the estimator label and the areas-slider
promotion) and
[`carpetbellevuefontscanonical-1.2.0.js`](webflow-scripts/carpetbellevuefontscanonical-1.2.0.js)
(fonts + a canonical derived from the page path).

**Three defects found and fixed during the rollout** (recorded here
because the automated builders reported them rather than hiding them):
1. *Self-links.* The Bellevue page was given its 29 city links before being
   used as the duplication source, so every copy inherited Bellevue's set —
   linking to itself and missing Bellevue. A correction pass re-audited all
   30 pages by actual link target (not count), removed each self-link and
   added the missing Bellevue link. Final state: 30/30 pages at exactly 29
   correct links.
2. *Stale guides section.* Copies made after Bellevue got its guides section
   inherited Bellevue's five blog links. The same pass replaced those with
   each city's own five (affected Arlington, Bothell, Cottage Lake, Duvall).
3. *Slider cells published as placeholders* (caught by Oleg on the live
   site, fixed 2026-08-26). Inside a component definition, the Webflow MCP
   element builder silently downgrades nested `TextBlock`s to plain divs
   and drops their `set_text`/`set_link` setup, so the new carpet slide's
   30 city cells rendered Webflow's stock "This is some text inside of a
   div block." text (the hrefs, set separately, were fine). The cells were
   rebuilt through the WHTML builder — `<a class="area-link-item"
   href="…"><div class="area-text">City, WA</div></a>` — which matches the
   original slides' exact markup and persists text correctly; all 30 were
   then read back and verified ("City, WA" + correct href, in the same
   order as the other slides). The same creation bug had eaten the nav
   dropdown's "Carpet Installation" link target (label stored, href
   missing); its URL is now set and verified.

### Areas slider on every carpet page + Woodinville link audit (2026-08-26)

**Slider on carpet pages.** Per Oleg's follow-up, every one of the 30 carpet
city pages now carries an instance of the shared "Section // Areas" slider,
inserted between the final CTA section and the footer — the same position
the repair/installation pages use. The carpet bundle (v1.8.0) already
promotes the "Carpet Installation Service Areas" slide to the front on
carpet pages, so the slider opens on the carpet slide there. Verified on
Woodinville: `…ci-cta → Section // Areas → ci-footer`.

**"Woodinville goes to hardwood installation" audit.** Oleg reported that
following the carpet link for Woodinville lands on the hardwood-floor
installation page. A full audit found every stored link correct:

- All 30 pages' real `publishedPath`s match the link table exactly
  (including the quirks: Seattle `/seattle/…`, Bothell
  `/hardwood-floor-refinishing/…`, Newcastle `/city-of-new-castle/…`);
  none are drafts.
- The carpet slide's 30 cell hrefs, the 29-chip rows, and the nav
  dropdown link were all read back correct.
- Every site script was audited for link rewriting: `oc-area-links-v1`
  (loads on `*-installation-in-*` paths but exits unless the path is in
  its hardwood/laminate/vinyl map — carpet paths are not), the areas
  slider script (moves DOM only, never touches hrefs), `siteCleanupD`
  (rewrites only two `/services/…` links), plus OCSeoFixes3,
  OCJunkCleanup, OCGreenCta, OCAreasStart, OCUtmLead and the carpet
  bundle — none rewrite city links.

The only remaining mechanism is a **legacy 301 redirect in Webflow site
settings** (redirects are applied before page resolution and shadow real
pages; the Data API does not expose the redirect list, and the live site
is not reachable from this environment). Fix is manual: Site settings →
Publishing → 301 redirects → search "carpet" → delete any rule whose old
path matches a `carpet-installation-in-…` URL, then publish.

### Mukilteo follow-up: full client-side audit rules everything out but HTTP redirects (2026-08-26)

After Oleg deleted the 301 redirects, clicking "Mukilteo, WA" on the home
page's carpet slide still landed on hardwood installation. A complete
audit of every layer that could rewrite that click found nothing:

- All 30 carpet-slide hrefs are stored correctly (as both the link
  setting and a literal `href` attribute baked into the markup).
- Every piece of custom code on the site was read end-to-end: the site
  head/footer code, all 15 registered site scripts *and* the 7 hosted
  sub-scripts they load (`oc-area-links-v1`, `oc-areas-slider-v4`,
  `bona-pkg-loader-v2`, `oc-faq-v5`, `oc-whytrust-v15`,
  `oc-trust-reviews-v9d`, `oc-recoat-refinish-v9`), the home page's 3
  page scripts + head/footer code + all 5 body embeds, and the Footer
  and Areas components' embeds. None touch `.area-link-item` links.
- Notable: the hardwood/LVP/refinishing slides' cells have **no links at
  all** (`linkType: none`) — only the repair and carpet slides are
  clickable. No runtime link-assigner exists.
- DNS resolves straight to `cdn.webflow.com` — no Cloudflare or other
  proxy layer that could hold redirect rules.

Conclusion: the browser leaves the click with the correct URL; the bounce
is HTTP-level. Remaining causes are (a) the redirect deletions not being
published yet, (b) a wildcard rule (`(.*)`) that a "carpet" search
doesn't surface — search the redirect list by the *destination*
(`hardwood-floor-installation`) instead, and (c) Chrome's permanent 301
cache replaying the old redirect locally even after the server is fixed —
which only an incognito window or cache clear reveals.

### Dedup pass 2, chip-section removal, blog-link audit (2026-08-26)

Three follow-ups from Oleg on the carpet pages, all applied and verified:

**"Also serving" chip section removed from all 30 pages.** The `ci-areas`
section (the "Also serving the Eastside & Seattle" chip row) duplicated
the new service-areas slider, so it was removed page by page and its
absence verified. The 29-city internal mesh survives intact through the
carpet slide in the shared slider, which every carpet page now carries.
(The four `ci-areas` fields also drop out of the duplication ledger.)

**Second de-duplication pass — the next 10 worst blocks.** A fresh
8-gram audit over the live text (packs + pass-1 verify snapshots) found
the first pass's 10 fields fixed but the next tier still converged: the
how-it-works samples card, cost lead-in and footnote, booking lede, hook
heading, price card, estimator note, and the stairs/timeline/furniture
FAQ answers (shared in up to 164 of 435 city pairs). All 10 were
rewritten per city — 290 blocks, composed with per-city structure
rotation, validated locally to **zero shared 8-grams** across all 30
pages (Bellevue anchors included) with every price and claim preserved
($4–$7/sq ft with city name, $18/step + waterfall/cap-and-band, the
$235–$400 staircase range only where it already appeared, "August 2026",
the six carpet styles + three pad grades, tack strip/heat seams/power
stretch) — then applied via 290 `set_text` writes and spot-verified.
Sources: [`webflow-scripts/carpet-rollout/dedup2/`](webflow-scripts/carpet-rollout/dedup2/)
(`current.json` = before, `applied.json` = after). Post-pass audit:
duplicate field-pairs are down to ~4% of all field×pair combinations,
and the survivors are the mandated shared facts — "all three pad grades
and 20+ carpet samples", the install-steps list, FAQ question wording —
which must read the same on every page.

**Blog links audited.** All 12 carpet blog posts are linked from the
carpet city pages: every page carries 5 guide links (150 total), and
every post appears on 2–30 pages (the restretch guide on all 30, the
Mohawk retailer post on 2).

### Crawlability audit + JSON-LD backfill on 7 pages (2026-08-26)

Oleg asked whether the carpet pages are "in embed code" or readable for
SEO/AI search. Audit result: the pages are almost entirely **native
Webflow elements** — every heading, city paragraph, FAQ (real
`h3`+paragraph markup), chip link, guides link and slider link is plain
HTML in the page source, readable without JavaScript. The single embed
per page is the `#ocpq` photo-quote widget, and its visible header (H2 +
city-specific lead paragraph) is static HTML inside the embed — verified
on Everett — so crawlers index it too; only the upload form itself is JS.

The audit also caught a real gap: **7 of the 30 pages had no JSON-LD**
(Everett, Newcastle, North Bend, Arlington, Bothell, Cottage Lake,
Duvall — the pages whose original builder agents were killed by usage
limits mid-run; their resumed builds skipped the schema step). Each got
a full graph rebuilt to match the 23 complete pages — business +
city-scoped Service (pack coordinates) + BreadcrumbList + FAQPage — with
the FAQ text **read back from the live page elements** (post-dedup
wording), so the schema matches the visible content exactly. Sources in
[`webflow-scripts/carpet-rollout/jsonld-fix/`](webflow-scripts/carpet-rollout/jsonld-fix/)
(per-city FAQ extracts + `build.py` generator). Verified after writing:
30/30 pages now store a complete city-specific schema with 10 FAQ
entries each. Needs a site publish to go live.

**De-duplication (measured, not assumed).** A deterministic 8-gram audit
across all 406 city pairs showed the marketing copy was well differentiated
but the fact-heavy blocks converged. The ten worst blocks — cost paragraph,
hero lede, photo-upload prompt, booking checklist line and six FAQ answers —
were rewritten per city with different sentence skeletons, varied openings
and local anchors, keeping every number identical. Driven by
[`webflow-scripts/carpet-rollout/dedup-playbook.md`](webflow-scripts/carpet-rollout/dedup-playbook.md).

The rewritten text was then read back OUT of Webflow and re-audited (copies
in [`webflow-scripts/carpet-rollout/verify/`](webflow-scripts/carpet-rollout/verify/)).
Share of the 406 city pairs sharing an 8-word run, before → after:

| field | before | after |
|---|---|---|
| mobile-showroom FAQ | 96.6% | 21.4% |
| pet-carpet FAQ | 95.6% | 22.7% |
| cost paragraph | 84.2% | 16.7% |
| stretch-or-replace FAQ | 84.2% | 5.4% |
| install-cost FAQ | 84.0% | 16.5% |
| warranty FAQ | 79.1% | 24.1% |
| photo-upload prompt | 69.7% | 8.6% |
| hero lede | 51.7% | 12.8% |
| booking checklist line | 45.3% | 22.4% |
| stretching-cost FAQ | 41.6% | 4.4% |

2,972 → 630 duplicate pairs (**78.8% reduction**); all 290 blocks confirmed
changed on the live pages; all 29 blocks unique per field; zero price figures
lost and zero stray "Bellevue" mentions. The residual overlap is the
mandated shared facts (rates, "20+ carpet samples", warranty terms), which
must read the same on every page. Every page names its own city in the
breadcrumb, eyebrow, H1, cost sentence, SEO title and SEO description.

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
