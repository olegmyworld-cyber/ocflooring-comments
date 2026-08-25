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
