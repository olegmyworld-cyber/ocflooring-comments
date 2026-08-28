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

### Floor refinishing hub redesign reverted (2026-08-28)

The redesign above was not wanted and has been undone. `/flooring-services-near-me/floor-refinishing`
is back to its previous layout and copy:

- Removed the added Benefits, FAQ, Flooring Guides, Cost and Schedule sections.
- Restored the `Section // Reviews` and `Section // CTA` blocks and the original
  section order (Hero · Partners · Features · Gallery · CTA 2 · Reviews · Services ·
  CTA · Why Choose · Areas).
- Hero back to the static background image (no video), H1 back to
  "Love your floors again".
- CTA 2, Why Choose and Cost copy reset to their previous values.
- Cleared the `FAQPage` / `BreadcrumbList` JSON-LD that the redesign added; the page
  again has no structured data, as before.

The only thing intentionally kept is the "near me" lead-in in the hero paragraph, which
predates the redesign and is part of the site-wide near-me work.

Two pre-existing issues were restored along with everything else, and are still live:
the Why Choose body copy ends with the stray note "what h tag i need to use?", and it
describes Bellevue rather than the whole service area.

Published live to `nwocflooring.com`, `www.nwocflooring.com`, and the Webflow subdomain.

---

## 2026-08-28 — Floor refinishing hub: process steps become a mobile slider

Page: `/flooring-services-near-me/floor-refinishing` (`65f32565e111adbbb806cf36`)

On phones the six "Step 1 … Step 6" process cards rendered as very tall, full-width
stacked blocks — roughly six screens of scrolling for one section. They are now a
horizontal, snap-scrolling slider on mobile.

What changed on the page (two edits only — nothing was restructured):

1. The card grid `.services-wrap.is-repair` (`4067ffcc-0e2a-216b-fd30-631bda5723f4`)
   was given the DOM id `oc-steps`. All new CSS is scoped to that id, so the shared
   `services-wrap` / `services-item-wpapper` classes are untouched on every other page.
2. A new HTML Embed, "Steps Mobile Slider (embed)"
   (`a52292c8-9137-8dc6-b17f-938caa63cf97`), was appended inside `container-main`
   directly after the card grid. Its source is kept in
   `webflow-scripts/floor-refinishing-steps-mobile-slider.html`.

Behaviour by breakpoint:

- **≤ 479px** — one card per screen at 84% width, so the next card peeks in and signals
  the swipe; scroll-snaps to centre.
- **480–767px** — same slider, two cards visible at 46% width.
- **≥ 768px** — completely unchanged. The slider CSS lives entirely inside
  `max-width: 767px` media queries and the dots are hidden.

Design changes on mobile (mobile only):

- Card padding removed so the photo is full-bleed at the top, fixed 11rem height with
  `object-fit: cover` (previously the images were free-height and dominated the card).
- Rounded 1rem corners, a soft shadow, left-aligned text.
- The "Step N" line of each `h3` is turned into a small red pill badge by the embed's
  script; the heading's `<br>` is hidden with CSS rather than removed from the DOM, so
  the desktop two-line heading still renders exactly as before.
- Progress dots below the slider; the active dot widens into a pill. Dots are clickable
  and track scroll position.
- The accent colour is read at runtime from the computed background of `.line-red`, so
  the badge and dots always match the site's brand red (fallback `#c0392f`).

Verified before publishing by rendering the section structure and its Webflow base
styles locally in Chromium at 390px, 700px and 1280px.

To undo: delete the embed element and clear the `oc-steps` DOM id. Nothing else was
modified.

Published live to `nwocflooring.com`, `www.nwocflooring.com`, and the Webflow subdomain.

---

## 2026-08-28 — Vinyl plank & laminate page: removed the in-home visit CTA

Page: `/flooring-services-near-me/vinyl-plank-flooring-and-laminate-flooring`
(`65f32565e111adbbb806d0d7`)

Removed the "Free 30-Minute In-Home Flooring Visit" banner — the red full-bleed card
with the copy "We come to you, measure the space, photograph the condition, and email
you a written quote within 24 hours…" and the green "Schedule Free In-Home Estimate"
button. It sat between the LVP FAQ embed and the Why Choose section.

It was the `Section // CTA` component instance (`d477cb1b-09ef-c408-ea75-a86d119c2f7d`,
component `da0eab0d-9168-89a7-b68f-090ba8869879`). The headline, body copy and button
label are not props on that instance — they are overrides on the nested `CTA Wrapper`
instance inside the component definition, which is why a page text search did not find
them.

Only this page's instance was deleted. The `Section // CTA` component definition is
untouched, so every other page that uses it is unaffected.

`Section // CTA 2` ("We Bring the Showroom to You") is still on the page — that is a
different section and was left alone.

To undo: re-insert a `Section // CTA` instance between the FAQ embed
(`a4f7efe7-cc7e-2d6d-598e-474c05acff1d`) and `Section // Why Choose`
(`b35db868-9429-1318-2882-2d5b280a731c`).

Published live to `nwocflooring.com`, `www.nwocflooring.com`, and the Webflow subdomain.

---

## 2026-08-28 — Seattle vinyl plank page: new hero photo

Page: `/city-of-seattle/vinyl-plank-flooring-installation-in-seattle-wa`
(`65fa331a9d90d967c68994a3`)

The hero photo was a man running a Hummel drum sander on bare hardwood — a refinishing
image on a vinyl plank page. It is now the plank-floor close-up (wide oak-look planks
with a chair and side table), asset `65f32565e111adbbb806d223`.

That photo was not a prop. It was hardcoded on the `hero-cover-img` image element
(`90853aa2-42b4-3cbd-decf-9484f6779ce6`, asset `6a1a756e28c89451e4068776`) inside the
shared `Section // Hero` component (`859df468-e2b7-0f08-0168-07d7647bc860`), so every
page using that hero rendered the same sander photo and there was no way to override it
per page.

Changes:

1. Added a new prop to `Section // Hero` — **Hero Cover Image**
   (`de38cb5d-bad1-346f-8c74-ae9220d21eda`, type `image`), default
   `6a1a756e28c89451e4068776`, i.e. the photo that was already there.
2. Bound the `hero-cover-img` element's `assetId` to that prop.
3. Set the prop to `65f32565e111adbbb806d223` on the Seattle page's hero instance
   (`42a381c2-d362-3575-9a43-c784ee32bbf4`) only.

Because the prop default is the original asset, every other page is byte-identical —
verified on the vinyl + laminate hub page, whose hero still resolves to
`6a1a756e28c89451e4068776` with no override.

Useful side effect: the hero photo is now overridable per page from the Designer. Any
other page can get its own hero image by setting **Hero Cover Image** on its instance,
with no further component work.

Note: the hero's separate **Background Image** prop is unrelated and was left alone —
on the Seattle page it is still the family-in-kitchen photo (`68adb3df42707c30bd24f000`).

To undo: clear the Hero Cover Image override on the Seattle instance (it falls back to
the default sander photo).

Published live to `nwocflooring.com`, `www.nwocflooring.com`, and the Webflow subdomain.

---

## 2026-08-28 — Vinyl plank hub page retargeted to King & Snohomish counties

Page: `/flooring-services-near-me/vinyl-plank-flooring-and-laminate-flooring`
(`65f32565e111adbbb806d0d7`)

The page carried a generic H1 and Bellevue-only body copy. It now targets King and
Snohomish counties throughout, and the copy is about vinyl plank installation rather
than hardwood.

**Hero** (`3101a4ea-758c-0a9b-e2f0-95429c683b54`)

- H1: "Vinyl & Laminate Flooring Installation " →
  "Vinyl Plank Flooring Installation in King & Snohomish Counties"
- Subheading: "Love Your Floors Again — Without the Mess" (a refinishing line) →
  "Waterproof Floors Built for Northwest Homes"
- Description now names both counties and anchor cities on each side of the line.
  The "near me" lead-in was preserved.

**Body copy**

- Cost H2: "What Vinyl Flooring Costs in Bellevue & King County" →
  "What Vinyl Plank Flooring Costs in King & Snohomish Counties"
- Cost lead-in: "Most vinyl plank installs in Bellevue…" → "…across King and Snohomish
  counties…". Edited the String node directly so the bold "$2,000–$4,000" survived.
- Waterproof bullet: "perfect for Seattle's wet weather" → "built for wet Puget Sound
  winters, from Seattle to Everett".

**Why Choose** (`b35db868-9429-1318-2882-2d5b280a731c`)

- Heading → "Luxury Vinyl Plank Flooring Installation Across King & Snohomish Counties"
- Subtitle was "Trusted Experts in Hardwood Refinishing and Installation" — a hardwood
  refinishing line inherited from the component default, on a vinyl page. Now
  "Waterproof LVP Installed by Licensed Local Pros".
- Body rewritten county-wide, ending with an explicit city list split by county.

**FAQ embed** (`a4f7efe7-cc7e-2d6d-598e-474c05acff1d`)

- Retitled to "…in King & Snohomish Counties".
- Added a new first question, "Which cities do you install vinyl plank flooring in?",
  listing all served cities by county.
- The cost question and its answers now reference both counties, and the FAQPage JSON-LD
  inside the embed was updated to match the visible text (8 questions, was 7).

**SEO / head code**

- Page-settings SEO title and description retargeted to both counties.
- **Fixed a real bug:** the head custom code's canonical, hreflang, `og:url` and Service
  `@id`/`url` all pointed at `https://www.nwocflooring.com/services-near-me/vinyl-plank-flooring-and-laminate-flooring`,
  but the page's actual published path is `/flooring-services-near-me/…`. The page was
  canonicalising itself to a different URL. All five now use the correct path.
- Removed the duplicate `<title>` and `<meta name="description">` from the head code —
  Webflow already emits both from page settings, so the page was shipping two of each.
  They now come only from page settings.
- Schema `areaServed` is now the two counties as `AdministrativeArea` entries, plus the
  city list on the Service node.

Left alone deliberately: the "Vinyl or Linoleum – What's Best for Your Home?" comparison
section (a legitimate buyer question), the 3-step process copy (already vinyl-correct and
location-neutral), and the CTA 2 block.

Published live to `nwocflooring.com`, `www.nwocflooring.com`, and the Webflow subdomain.

---

## 2026-08-28 — Vinyl plank hub page: new hero photo

Page: `/flooring-services-near-me/vinyl-plank-flooring-and-laminate-flooring`
(`65f32565e111adbbb806d0d7`)

Replaced the floor-sanding hero photo (a refinishing image) with a vinyl plank
installation photo — a fitter laying a plank over underlayment, asset
`65f32565e111adbbb806cf98`.

One prop write, no component changes: set **Hero Cover Image**
(`de38cb5d-bad1-346f-8c74-ae9220d21eda`) on the hero instance
`3101a4ea-758c-0a9b-e2f0-95429c683b54`. This is the prop added earlier today for the
Seattle page, so the swap is now a single value per page.

Known cosmetic issue: this same photo also appears further down the page in the
`section_vinyl` block (`79cc8021-4b53-0f8b-7521-061d70ca6e1f`), so it now shows twice.
Flagged to the owner; either image can be swapped in one call if they want them
different.

Still outstanding: the ~30 vinyl plank **city** pages
(`vinyl-plank-flooring-installation-in-<city>-wa`) all still inherit the sander photo
from the component default. Offered as a batch.

Published live to `nwocflooring.com`, `www.nwocflooring.com`, and the Webflow subdomain.

---

## 2026-08-28 — Home page: H2 changed to "Wood Floor Refinishing"

Page: Home (`65f32565e111adbbb806ce6e`)

Audited every H2 the home page renders, then changed the one that carried the phrase
"Hardwood Floor Refinishing".

Changed:

- FAQ embed (`45677bd5-6464-5d02-0495-73d844d53c95`, nested inside `section_faq`):
  `<h2 id="faqx-title">Hardwood Floor Refinishing FAQ – Bellevue, WA</h2>` →
  `Wood Floor Refinishing FAQ – Bellevue, WA`. It is plain HTML in the embed, so it is
  in the served markup — no JS involved, crawlable as-is.

Full H2 inventory of the home page, for reference:

| H2 | Source | Contains the phrase? |
|---|---|---|
| Wood Floor Refinishing FAQ – Bellevue, WA | FAQ embed `45677bd5` | **yes — changed** |
| The hardwood floors we refinish in Bellevue & Seattle | embed `9e0bbd5f` (`#oc-refinish-guide`) | no — says "hardwood floors", left alone |
| Why Homeowners Trust OC Flooring | native heading `b66eb083` | no |
| Our Gallery | `Section // Galllery` | no |
| Like What You See? Let's Make It Yours | `Section // CTA 2` | no |
| Our Services | `Section // Services` | no |
| Why Choose OC Flooring in Bellevue, WA | `Section // Why Choose` | no |
| Proudly Serving Homeowners Across King & Snohomish Counties | `Section // Areas` | no |
| Refinishing Cost Guide – Bellevue & Nearby Areas | `Section // Cost` | no — and the section is hidden (`Section Visibility` = false) |

Notes for future work:

- "Hardwood Floor Refinishing Service Areas" is an **h3**, not an h2, and lives in the
  shared `Section // Areas` component — editing it would change every page on the site.
- The `Section // Services` subtitle ("…most trusted hardwood floor refinishing
  service.") and the `Section // Why Choose` subtitle ("Trusted Hardwood Floor
  Refinishers") are not heading elements, so they were out of scope.
- Query gotcha: `element_filter {tag: "h2"}` matches Block/DOM elements only and returns
  nothing for Webflow Heading elements — use `{type: "Heading"}` and read
  `settings.headingLevel` instead.
- The agent proxy blocks `cdn.prod.website-files.com`, so hosted script sources could not
  be fetched to check for script-injected H2s. The locally mirrored scripts in
  `webflow-scripts/` contain no `<h2>`.

Published live to `nwocflooring.com`, `www.nwocflooring.com`, and the Webflow subdomain.
