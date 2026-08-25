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
