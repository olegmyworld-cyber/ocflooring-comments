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

---

## Blog activation & rewrite (2026-08-22, same session)

Per Oleg's request to unify all blogs on the reference design
(`/blog/hardwood-floor-refinishing-process-timeline`), activate inactive
posts, and rewrite them as answer-first content:

- Inventory: 109 blog items — 98 already live in the ocb design system
  with FAQs and fresh metadata (a prior work pass had modernized them);
  11 archived, never-published posts (all carpet/tile topics) held the
  old thin content.
- All 11 were rewritten from scratch in the ocb template (Quick-answer
  card, fact tiles, city-specific sections, 6–8 item FAQ accordion with
  exactly matching FAQPage JSON-LD, CTA card), researched against real
  Reddit/Google/forum questions via web search, interlinked to live
  blogs, service pages, and city pages, and assigned to the current
  category set. Positioning follows the live carpet posts: OC Flooring
  is a hard-surface company and does not sell or install carpet; carpet
  figures are market rates.
- All 11 were un-archived and published; the live collection now counts
  109/109 active, all included in the sitemap. Slugs and images were
  left unchanged. Originals: `blog-backup/blogs-original-2026-08-22.json`;
  new content: `blog-backup/rewrites-2026-08-22/`.

---

## Blog SEO/AEO follow-ups (2026-08-22, same session, per Oleg)

- **Slug cleanup:** the two never-indexed carpet slugs were shortened —
  `carpet-installation-cost-bothell-wa` and `flooring-guide-mill-creek-wa`
  (both republished; the old slugs were never published before today).
- **Category cleanup:** the 7 orphaned legacy blog categories (General,
  City Guides, Comparisons & Guides, Repair & Care, Vinyl & Laminate,
  Installation, Refinishing) were unpublished and deleted; exactly the
  current 7 remain, and every post is assigned to one of them.
- **Article schema:** the Blogs Template page head now emits static
  BlogPosting JSON-LD per post (headline/description/url from CMS field
  tokens, author + publisher = OC Flooring, publisher linked to the
  site-wide LocalBusiness `#ocflooring` entity). Static markup, so AI
  crawlers that don't execute JavaScript can read it.
- **Outbound links in 8 vinyl posts:** 21 contextual links added
  surgically (existing phrases wrapped; bodies otherwise byte-identical)
  and republished.
- **Inbound links for indexing:** all 119 city service pages
  (repair/installation/refinishing/vinyl × cities) now carry a
  "Flooring Guides & Answers" section above the footer with 5 blog links
  each, assigned so that **every one of the 109 blog posts receives 4–7
  inbound links from Google-indexed pages**, matched by service type and
  city (map: `blog-backup/guides-link-map-2026-08-22.json`). Styling via
  builder-applied `ocgd` classes plus the `#ocgd-css` block in the
  site-wide footer code.

### Blog hero images (same session, per Oleg)

The blog template's hero used the shared Section // Hero component, whose
image is a fixed photo inside the component — so every post showed the
same sander picture regardless of its CMS Main Image. Fix, using the
proven CMS-token support in collection-page custom code:

- Template head now emits per-post `og:image` / `twitter:image` metas and
  a BlogPosting `image` property from the Main Image field (also fixes
  social-share previews, which had no image at all).
- A small `oc-blog-hero-img` script in the template footer swaps the hero
  `.hero-cover-img` to the og:image URL at parse time (guarded: a post
  with no Main Image keeps the default photo; the post title becomes the
  image alt).

### Blog image cropping fix (same session, per Oleg)

The new blog images are infographics with text at the edges; both the
post hero and the blog cards were crop-filling them (object-fit: cover),
clipping the text. Fixes:
- Blog template footer: `#oc-blog-hero-img-css` — the post hero image now
  displays whole (object-fit: contain, centered, max-height 560/600px,
  rounded with shadow), mirroring the city pages' hero treatment.
- Site-wide footer: `#oc-blog-card-img-css` — `.blog-image` cards on the
  blog listing, related-posts grids, and home now use contain with a warm
  letterbox background instead of cover-cropping.
- Not fixable by CSS: the "Dustless vs. Traditional" thumbnail has a
  "DOWNLOAD BOTH IMAGES (MAIN + THUMBNAIL) – AVIF" button baked into the
  image file itself — that image needs re-exporting/replacing in the CMS.

### Blog image cropping — round 2, fixed at the class level (same session, per Oleg)

Oleg reported the /blog listing cards were still cropping the infographic
text after the round-1 CSS overrides. Root cause: the Webflow class
`.blog-image` itself (style id 219526ce-56b4-db04-9f23-084ca4d31bff) sets
`height: 16rem; object-fit: cover`, and depending on load/cascade order it
could win over the late-injected footer override. Fix moved to the source:

- **`.blog-image` class updated via the Style API** (base + main
  breakpoint): `object-fit: contain` with `background-color: #f6f2ec`
  (warm letterbox), keeping `width: 100%; height: 16rem` so the card grid
  layout is unchanged. This applies everywhere the class renders — /blog
  listing, related-posts grids, home — with no dependence on custom-code
  ordering.
- **Blog template head** (`oc-blog-readable` block): its own
  `.blog-image` rule flipped from `object-fit: cover; background-size:
  cover` to `object-fit: contain; background-size: contain;
  background-repeat: no-repeat; background-color: #f6f2ec` so the
  head-level `!important` rule no longer re-crops the related-posts cards
  on blog post pages. Everything else in the block byte-identical.
- Site republished to www.nwocflooring.com, nwocflooring.com, and the
  Webflow subdomain.

Reminder for review: browsers cache the old HTML/CSS aggressively — check
with a hard refresh (Cmd+Shift+R / Ctrl+F5). The dustless-vs-traditional
thumbnail still carries the baked-in "DOWNLOAD BOTH IMAGES" band inside
the image file; only replacing the image in the CMS fixes that one.

### Blog card images — root cause isolated to the image files (same session, per Oleg)

Oleg reported edge text still cut off on /blog cards after the class-level
contain fix. Full verification pass this round:

- The /blog card is a plain `<img class="blog-image">` (element
  3d83953f-...37da0 on page 65f32565e111adbbb806ceaa) — confirmed via the
  element API, so `object-fit` genuinely governs it.
- Live CSS chain re-verified end to end: the `.blog-image` class is
  contain (base + main); the site-wide footer `#oc-blog-card-img-css`
  contain override has been live since the 23:04 publish; the listing
  page's own head block styles only card typography (no image rule); the
  template-head cover rule was fixed in the 02:37 publish. Nothing in the
  cascade crops anymore — and `object-fit: contain` cannot cut pixels.
- The screenshot's cuts are **asymmetric** (left edge of each infographic
  intact, right edge cut mid-word: "MAXIMIZ…", "…help you choos"),
  which centered CSS cropping can never produce. Conclusion: the text is
  cut **inside the generated AVIF files themselves** — the generator ran
  the right-hand text column past the canvas edge on at least the
  species-guide and real-estate-playbook thumbnails (plus the previously
  noted dustless-vs-traditional thumbnail with the baked-in download
  button). CDN egress is blocked from this environment and CMS-uploaded
  files are not in the site asset library, so the files could not be
  opened here; the raw URLs were given to Oleg for a 10-second visual
  check.
- Presentation hardening shipped anyway: the /blog listing page footer
  (previously empty) now carries `#oc-blog-card-inset-css` — a 10px
  parchment inset (padding + border-box) on `.blog-image`, so any
  edge-hugging text in a healthy file renders with breathing room.
  Published to both domains + subdomain.

Files flagged for re-export/replacement in the CMS (text must stay inside
the canvas, ideally ≥5% margin):
- what-type-of-wood-is-best-species-guide-thumbnail.avif
- flooring-real-estate-success-playbook-thumbnail.avif
- dustless-vs-traditional thumbnail (download button baked in)

### Blog duplicate audit + de-duplication rewrites (2026-08-23, per Oleg)

Oleg asked for a full duplicate check across all blogs, with rewrites for
anything found. Scan of all 109 posts (fresh CMS pull, saved locally as
scratchpad blogs-current-flat.json):

- **Clean at the surface level:** no duplicate names, title-tags, or
  meta-descriptions anywhere; no copied body content (max 6-gram shingle
  similarity between any two posts: 4.7%).
- **Four topic/identity duplicate pairs found** (same search intent
  targeted twice) and resolved by re-angling the weaker post while the
  stronger stays canonical; rewritten bodies validated (FAQ = JSON-LD,
  links checked against live slugs, first .ocb embed byte-identical,
  images untouched) and pushed byte-exact:
  1. `solid-v-s-engineered-wood-floors-whats-right-for-your-home` — was a
     second "Solid vs Engineered" post; now **"Wood Floors on Slabs,
     Basements & Radiant Heat: What Your House Allows"** (installation-
     situations guide). Canonical comparison remains
     `solid-vs-engineered-hardwood-which-is-right-for-your-home`.
  2. `benefits-of-vinyl-plank-flooring-for-seattle-wa-homes-...` — was a
     second "vinyl plank is great for Seattle" post; now **"How to Choose
     Vinyl Plank for a Seattle Home: A Buyer's Spec Guide"** (wear-layer
     mils, SPC/WPC cores, 2026 Seattle price tiers). Canonical case-for
     post remains `why-vinyl-plank-flooring-is-perfect-for-seattle-homes`.
  3. `cost-to-refinish-hardwood-floors` — competed with the canonical 43K
     price guide for the same head query; now **"Hardwood Refinishing
     Budgets: 5 Real Projects, Line by Line (2026)"** (worked examples,
     linked to the canonical guide 5×). Canonical remains
     `how-much-does-it-cost-to-refinish-hardwood-floors`.
  4. `hardwood-floor-refinishing-near-me-seattle-wa` — was an UNPUBLISHED
     DRAFT colliding with both the contractor-hiring checklist and the
     day-by-day timeline post; now **"Booking Hardwood Floor Refinishing
     in Seattle: Timing & Logistics"** (lead times, seasonal windows,
     condo/HOA + parking logistics, re-entry times) and **flipped live**
     — 109/109 posts are now published.
- Every pair now cross-links its mate with descriptive anchors instead of
  competing. CMS items published (live immediately); site republished so
  sitemap.xml includes the newly live URL.
- **Borderline-adjacent pairs reviewed and intentionally left** (bodies
  and intents already differentiated): refinish-or-replace trio
  (cheaper-math / damage-guide / worth-it), Seattle-climate vs
  PNW-climate, dustless-vs-traditional vs living-through-dust-free, and
  the two OC-process posts ("our process" vs "what it fixes").

### Full site audit (2026-08-23, per Oleg — "let me know if everything works")

Layers checked: 160 pages + SEO/OG metadata (full), 109 blogs (full),
sitemap inclusion (full), site scripts (full), forms + Calendly booking
(verified live via API), GA4 + Search Console (Windsor connectors,
nwocflooring property isolated from willsflooring/olegsonsremodeling),
content sweep of 41 pages (all 29 core/service/static + 12 city sample)
via a 9-agent workflow. Report artifact:
https://claude.ai/code/artifact/98983a76-4636-44c3-a671-e1a0db76e58d

WORKS: publishing clean (0 drafts); unique SEO titles/descriptions on
all pages; blogs 100% complete; 0 broken internal links found; both lead
forms present; Calendly event active; GA4 collecting (40–192
sessions/day, generate_lead ×16 / form_submit ×5 in 14d); 46,485
impressions / 243 clicks 28d and rising; sitemap complete.

CRITICAL FINDINGS:
1. 32 dead URLs still ranked in Google (7,621 impressions/28d → 404):
   the old laminate city pages (converted to repair pages without
   redirects) + renamed service slugs. Redirect map delivered
   (audits/redirect-map-2026-08-23.csv); must be pasted into Webflow UI
   (301 API is Enterprise-only on this plan).
2. /services/eco-friendly-floor-refinishing names the business "Fisher
   Hardwood Flooring" twice.
3. Carpet offered as a service in 5 places (calculator step 1,
   commercial, flooring-store, our-products, stairs FAQ) + Calendly
   question offers Carpet/Tile.
4. Wrong-city copy on vinyl city pages (Edmonds hero says Lynnwood;
   Renton/Edmonds/Whidbey CTAs say "Arlington homeowners"; Kirkland/
   Arlington alt texts) — 3/3 sampled vinyl pages affected.
5. /reviews contains only pricing content, no reviews (H1 "How Much Does
   Hardwood Floor Refinishing Cost in Bellevue?").
6. GA4 has no key events marked (conversions read 0 though leads fire).

MEDIUM: stairs draft heading "TYPES OF STAIRS / MATERIALS" live; blog
hero leftover editorial note; unfinished-hardwood duplicated heading;
"No items found" on our-products + vinyl service Projects; "adress"
typo; staining page vinyl alt texts; financing empty description; wood
wall panels Marble Oak missing description; 3 titles >65 chars, 2
descriptions >170; booking on old nwwillsflooring Calendly slug
(functional, cosmetic).

WATCH: 30 new repair pages + ~40 older blogs at 0 impressions (new URLs
/ interlinks just shipped — resubmit sitemap, recheck in 3–4 weeks);
"oc flooring" brand query at avg position 5.8.

### Audit fixes applied (2026-08-23, per Oleg's approval)

Redirects: Oleg had already added them in Webflow (171 rules; old laminate
city URLs 301 → the repair pages) — the audit's "404" concern was wrong;
old ranked URLs redirect correctly and Google will catch up on its own.

Fixes shipped and published:
1. **Wrong brand name** — /services/eco-friendly-floor-refinishing: both
   "Fisher Hardwood Flooring" mentions → "OC Flooring"; H1 trailing space
   removed. Page-wide "Fisher" search: 0 matches.
2. **Carpet-as-a-service removed everywhere approved**:
   - Calculator: "Carpet" service radio removed (form script verified
     safe — selects by group name; tear-out carpet options kept);
     "adress" typo fixed.
   - Commercial page: install-list, services card (now "Commercial Floor
     Removal & Prep", honest tear-out copy under the carpet-tile photo),
     both FAQ embeds + their FAQPage JSON-LD, SEO meta description; also
     fixed placeholder H2 ("Commercial Services Section" → real heading)
     and the residential "Arlington homeowners" CTA → Puget Sound
     businesses. Only remaining "carpet" = legitimate tear-out sentence.
   - Flooring-store page: carpet card removed from the selection grid,
     rich-text bullet + sentence, FAQ embed (4 answers) + JSON-LD made
     verbatim-matching, SEO title/description. "carpet" matches: 0.
   - Our-products page: carpet dropped from product lists, 3 FAQ answers
     + JSON-LD, SEO meta description. "carpet" matches: 0.
   - Stairs page: FAQ "carpeted stairs" → "luxury vinyl plank treads"
     (JSON-LD matched); draft heading replaced with "Stair Materials:
     Wood, Engineered & Laminate Options".
   - SHARED "Section // Services" component: "Flooring Materials" card
     description "...vinyl, or carpet..." → "...or vinyl..." — fixes the
     claim on every page rendering that section.
3. **Vinyl city pages — cross-city leak fixed on all 30** (plus North
   Bend hardwood-installation page): every page had the CTA subtitle
   hardcoded to "Arlington homeowners" and 4 benefits-image alts
   hardcoded to Kirkland; Edmonds' hero additionally said Lynnwood.
   All corrected to each page's own city; service-area lists, county
   names, showroom address, and blog-guide links left intact. Verified
   0 "Arlington"/"Kirkland" leaks remaining per page. (One agent found
   5 stale page ids in its manifest and re-resolved them via list_pages
   before editing — all paths verified.)
4. **/reviews rebuilt as a real reviews page**: pricing content removed
   (5 elements incl. the pricing FAQ embed), the live Google-reviews
   widget (Elfsight — the site's only true review source) moved up under
   a new H1 "OC Flooring Reviews — What King & Snohomish County
   Homeowners Say", new service-grouped section (Refinishing / Repair /
   Vinyl / Installation cards linking each service) + CTA; "Why Choose"
   copy now review-focused; page title "Price" → "Reviews", SEO
   title/description updated. No reviews were invented — the widget
   pulls the real 103 Google reviews.

Flagged for Oleg (not changed): commercial page still lists epoxy /
polished concrete / rubber (confirm if offered); flooring-store still
has a "Tile and Stone" card (confirm if the store sells tile); Calendly
booking question still offers Carpet/Tile choices (Calendly side).

### Service-scope corrections (2026-08-23, per Oleg: "no, we dont do that")

- **Commercial page** — epoxy flooring, polished concrete, and rubber
  flooring removed as offered services: three install-list items replaced
  with real services (commercial laminate installation, commercial
  hardwood refinishing, floor removal & subfloor prep); warehouse and gym
  industry lines rewritten to LVT/rigid-core vinyl; cost FAQ re-tiered to
  laminate/vinyl vs LVT/hardwood (JSON-LD matched verbatim); SEO meta
  description rewritten without epoxy/concrete. Page sweep: 0 matches for
  epoxy/concrete/rubber/tile; only carpet mention is the allowed
  tear-out sentence.
- **Flooring-store page** — "Tile and Stone" card removed from the
  selection grid (3 cards remain: Hardwood, Laminate, Luxury Vinyl); rest
  of page, FAQ, SEO, and the Products CMS (all 191 items) verified
  tile/stone-free (only false positives: brand "Stonewood", color "Slate
  Grey", laminate "look of wood or stone" comparison).
- **Calendly booking question** ("What services are you interested in?"
  offering Carpet/Tile) — NOT editable via the Calendly API (custom
  questions aren't exposed by update_event_type); Oleg must remove the
  two choices in the Calendly dashboard on the "OC Flooring" event type.
- Note: the store page's "Brands We Carry" strip is an external Elfsight
  widget — its brand logos are managed in Elfsight, not Webflow.

### Repair pages: photo-upload buttons + new sections on all 30 (2026-08-24, per Oleg)

Oleg asked for three more photo-upload touchpoints at the bottom of every
repair city page, with animation. Iterated on Mukilteo first (per his
request), he chose "Radar Rings" from a 10-option animation demo
(claude.ai artifact), then approved the full rollout.

Shipped to all 30 floor-repair city pages:
- **Three "Upload Your Photos" ring buttons** per page (end of What We
  Repair, end of Repair-or-Refinish, end of FAQ), all anchoring to the
  existing #ocpq photo-quote form — five upload touchpoints per page
  total. Animation: continuous green radar rings (pure CSS, ::before/
  ::after, prefers-reduced-motion respected) + hover lift.
- **Three new city-localized photo sections** between FAQ and the closing
  CTA: solid-hardwood sand-outs (Bona sander photo), squeaks/gaps/
  subfloor (parquet repair photo), stairs/thresholds (staircase photo).
  Copy localized per city from each page's own local prose (honest
  framing where a city has little solid wood; Newcastle's no-framing-work
  exclusion honored; Seattle adapted to its different lmb/lmf embed
  structure across three embeds).
- Process: every write was byte-exact string surgery verified by full
  sha256 of the STORED value (authoritative get_settings read) — adopted
  after one agent corrupted the Mukilteo draft by eliding a middle span
  when retyping (caught pre-publish, restored, never live). Webflow
  get_page_content can serve stale cache after writes; get_settings is
  authoritative.
- Earlier iterations on Mukilteo: rise/fade entrance (rejected), Webflow
  IX2 native classes investigated (per-element data-w-id bindings, not
  attachable via API), 10-option demo built, Radar Rings chosen.

Published to www.nwocflooring.com, nwocflooring.com + subdomain.
