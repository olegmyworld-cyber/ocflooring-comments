# Client-experience changes — 2026-09-01

Applied directly in Webflow (site `oc-flooring`, id `6377e8e6a53936b48ef1cad0`) after a
customer-perspective audit. Everything is reversible; element/prop IDs listed for rollback.

## 1. Homepage service cards (new)
Added an `HtmlEmbed` section (`#oc-services-cards`, element `96f10d01-83f6-7bb5-d510-07facd3e78ff`
on Home page `65f32565e111adbbb806ce6e`) right after the hero. Six cards:
Refinishing, Hardwood Installation, Tile, Vinyl/Laminate, Carpet, Stairs & Repair —
each linking to its service page under `/flooring-services-near-me/`, plus a
"Not sure? call (425) 595-1079" line and a link to /reviews.
**Rollback:** delete that embed element.

## 2. Navbar (component `6f76eb68-426e-d4a4-55b1-e419a08b720a`)
- "Tile Installation" link: `/city-of-bellevue/tile-installation-in-bellevue-wa` → page `6a9453a9cc7f108e72cc420d` (generic Tile page). Element `8e56386e-c6ca-defb-5938-c9e6588b033e`.
- "Carpet Installation" link: Bellevue city page → page `6a9453aa5038df1a06154847` (generic Carpet page). Element `2bc942db-22b5-42ee-e81b-e8b713d3d7bc`.
- Hidden (visibility=false, pages stay live for SEO): Floor Staining `d026682a-e069-dc4f-30f7-a73b0d0dc75a`, Dustless Floor Sanding `5d51b682-9626-86b6-47c0-0ef074ef2953`, Eco-Friendly Finishing `177de391-cfce-7c60-cacd-608ef5e6b394`, Screen and Recoat `e59093f6-21ee-67df-87f6-8acbbc36a913`.
- Hidden navbar tagline "Floors as Strong as a Bear" (`c5bd0c5a-ad7f-70b1-3e18-1caf947db620`).
**Rollback:** set visibility=true / restore old link hrefs.

## 3. Homepage "Our Services" subtitle
Prop `025a02f6-0feb-8101-0bfe-1ae3c9267a57` on instance `c0e1a6d2-34c2-1921-45cf-03bf175ee6ce`:
was "See why we're the area's most trusted hardwood floor refinishing service." →
now "Hardwood, tile, vinyl plank, carpet and stairs — one trusted local team for every floor in your home."

## 4. Footer component (`15405ed6-2aad-39be-8f76-459753cd14ca`) defaults
- Heading prop `8e109212-a622-ad37-f4f0-a8674f47d174`: "Block Pages" → "Quick Links".
- Social link prop `a3410f70-e761-5ac0-ddfc-c50fdec8762e`: was Webflow's own LinkedIn URL → now `/reviews`.

## Not changed
- No visible "Shop" item in navbar (first nav link is About Us) — nothing removed.
- Sub-service pages (staining, dustless, eco, recoat) remain published; only unlinked from menu.

## Revision (same day, per Oleg)
Homepage stays refinishing-only:
- Big 6-card grid replaced with a compact "Looking for a different flooring service?" pill strip
  (same embed element `96f10d01-83f6-7bb5-d510-07facd3e78ff`), moved down to sit just before the FAQ section.
- "Our Services" subtitle restored to the refinishing-only original.
Menu fixes, hidden dropdown items, and footer fixes kept as-is.

## Revision 2 — dropdown reorder + rename
- Dropdown toggle text "Services" → "Flooring Services" (String `f58347ea-...120ff`).
- Dropdown order now: Floor Refinishing, Floor Installation, Tile, Vinyl Plank, Carpet,
  Stairs, Laminate, Floor Repair, Our Floor Products (hidden sub-services unchanged).

## Revision 3 — direct category links on navbar
- Added 5 TextLinks (style "Nav Link") in nav-menu-inner-wrapper, before the dropdown:
  Refinishing `531e0fff-f59d-52a1-bf1a-373e47a71450`, Installation `b4aabd7b-a03a-54c6-a634-eff4b1622429`,
  Carpet `c2c7005f-4c1e-2512-c058-79586176c8ab`, Tile `8bd56900-c5da-1a56-152b-58be1535c394`,
  Vinyl `be644278-0695-910b-fc19-bf386fd7750e` — each linked to its main service page.
- Dropdown toggle renamed "Flooring Services" → "More" (still holds all services incl. stairs/laminate/repair/products).
- "About Us" NavbarLink `6f76eb68-...7214` hidden to free space (rollback: visibility=true).

## Revision 4 — navbar icons, link fix, dropdown reorg
- Added SVG icons (matching existing 17px stroke style) to the 5 direct links.
- Fixed 5 direct links: builder had left them as "#": now page links (refinishing cf36, install cf50,
  carpet 6a9453aa..., tile 6a9453a9..., vinyl d0d7).
- Moved "Our Work" (`...7212`) and "About Us" (`...7214`, re-shown) to the TOP of the More dropdown,
  restyled to "Nav Link Dropdown".

## Revision 5 — dedupe More dropdown
Hidden (visibility=false) dropdown items now duplicated by direct navbar links:
Floor Refinishing `5ceda1a3...2521`, Floor Installation `f58347ea...12101`,
Vinyl Plank `f58347ea...12103`, Carpet `2bc942db...d7bc`, Tile `8e56386e...033e`.
More now shows: Our Work, About Us, Stairs, Laminate, Floor Repair, Our Floor Products.

## Revision 6 — Repair on navbar
- Added "Repair" TextLink `3ad5cada-4cbf-7dfd-8c2a-c5563f43efaa` (wrench icon, icon moved before text)
  after Vinyl, linked to flooring-repair page `65f32565e111adbbb806cf4f`.
- Hidden the now-duplicate "Floor Repair" dropdown item `f58347ea...12105`.

## Revision 7 — service links 20% bigger
- New combo class `is-service-big` on "Nav Link" (font-size: 1.2em) applied to the 6 service links.
- Their SVG icons enlarged 17px → 20px (width/height attrs).

## Revision 8 — Blog in More; More toggle sized up
- Added "Blog" TextLink `60a89032-bd52-1dec-203f-e7b9f60b20ad` at bottom of More dropdown → blog page `65f32565e111adbbb806ceaa`.
- More toggle block `f58347ea...120fe` now uses `Nav Link is-service-big`; its icon bumped to 20px.

## Revision 9 — More dropdown final order
- "Blog" renamed "Blogs"; verified link → blog page ceaa.
- More order now: About Us, Our Work, Blogs, Stairs, Laminate, Our Floor Products.
- Confirmed no duplicate Blog link anywhere else in navbar.

## Revision 10 — remove top-bar Blogs on homepage
- Homepage navbar instance (`3932c992-...45d1`) used variant `eb34f5cc-...` which rendered a "Blogs"
  top-bar link and hid Price/Financing. Switched its Variant prop to `base` — same navbar as all
  other pages. Rollback: set Variant prop back to `eb34f5cc-d07b-9ebe-86a1-ef47e25b0e94`.

## Revision 11 — kill injected top-bar Blogs link
- The top-bar "Blogs" link is injected at runtime by one of the site's 15 footer/header scripts
  (source unreachable from this env; likely OCHeaderInit or siteCleanupD).
- Added a guard script inside the navbar component embed (`c6e17660-...7931`): hides any anchor
  with text "Blog"/"Blogs" in the nav that is NOT inside a .w-dropdown-list. The Blogs link inside
  the More dropdown is unaffected.

## Revision 12 — phone spacing
- `.nav-phone` style: added margin-left: 28px to separate the phone number from the More dropdown.

## Revision 13 — mobile hero H1 sizing
Hero title styles `heading-hero` and `heading-hero-custom` grew on smaller breakpoints
(2.85rem tiny vs 2.6rem desktop). Now: medium 2.5rem, small 2.2rem, tiny 2rem (line-height 1.15)
so mobile matches desktop proportions. Note: OCHeroTitleSize script may also touch this at runtime.

## Revision 14 — force mobile hero H1 size
Breakpoint style change alone didn't take on the phone (a legacy script appears to set the size
at runtime). Added to the navbar embed:
- `#oc-hero-mobile-size` CSS: h1.heading-hero/.heading-hero-custom → 34px !important (<=767px),
  30px !important (<=479px).
- Guard script that strips inline font-size/line-height on those H1s on mobile (MutationObserver
  on style attr), so injected inline styles can't win.

## Revision 15 — universal mobile H1 clamp
Class-scoped fix didn't take (hero title appears script-rebuilt; red "Hardwood" span indicates
runtime rewrite, class unknown). Replaced with universal clamp in navbar embed:
- CSS: all `h1` → 34px !important (≤767px), 30px !important (≤479px).
- JS: sets inline `font-size`/`line-height` with priority "important" on every h1 at ≤767px,
  re-asserting via MutationObserver + 60s interval; no-op check prevents observer loops.

## Revision 16 — mobile H1 bigger per Oleg
Clarified direction: Oleg wants a PROMINENT mobile title (desktop feel), 30px was too small.
Clamp raised: ≤479px → 38px, 480–767px → 40px (line-height 1.15). Breakpoint styles set to
2.4rem (tiny) / 2.5rem (small) to match.

## Verification — navbar/fix coverage (12-agent scan of all 223 pages)
216/223 pages contain the shared Navbar component (carries menu, H1 clamp, Blogs guard).
Missing (utility/template pages only): detail_blog-category, detail_gallery, detail_vinyl-gallery,
detail_sku, detail_category, 401, 404. Blog post template (detail_blog) IS covered.

## Revision 17 — duplicate FAQ on vinyl plank page
Page `65f32565e111adbbb806d0d7` had TWO full FAQ embeds, each with its own FAQPage JSON-LD:
- KEPT `bfe41d78-57a1-ad41-abe4-dbb250242335` (.ocvg, "Vinyl Plank Flooring Guide & FAQ", 8 Qs).
- HIDDEN `a4f7efe7-cc7e-2d6d-598e-474c05acff1d` (.faq-section, 8 Qs; also duplicated the city
  list already rendered by embed `0df921ef`). Rollback: set its visibility back to true.
Note: the two FAQs gave conflicting pricing (kept one: ~$2.50/sq ft labor + $2-7 materials;
removed one said $4-7/sq ft installed) — worth confirming which is current.

## Revision 18 — vinyl page hero image matched to Bellevue
The Bellevue vinyl page (65fa23dd7a54eca64ae7a9de) sets its hero image at runtime via the
page-level script `ocvinylheroimg` (its Hero Cover Image prop is just the component default).
Applied the same script to the general vinyl page 65f32565e111adbbb806d0d7 (footer, v1.0.0).
Hero Cover Image prop left as-is (65f32565e111adbbb806cf98) so the page still shows a vinyl
photo if the script is path-gated. Rollback: remove_page_script ocvinylheroimg from that page.

## Revision 19 — LVP Collections section on the general vinyl page
"Luxury Vinyl Plank Collections" (mobile-showroom card + collection/shade filters + color carousel)
is rendered by page script `oclvpc`. Added it (footer, v1.0.0) to the general vinyl page
65f32565e111adbbb806d0d7.
Deliberately NOT added there: ocvinylcore, ocvinylguides, ocvinyladv, ocarlpos — that page already
carries hand-ported EMBED copies of those sections (.occore core guide, .ocvg guide+FAQ, layer
diagram, trust cards), so adding the scripts would duplicate them.
Audited all 30 vinyl plank city pages (King/Snohomish + Whidbey/Oak Harbor): every one already
carries the full 6-script reference set incl. oclvpc. No changes needed there.

## Revision 20 — remove "Advantages of Vinyl Plank Flooring"
Hidden `section_features` block `158c602f-1e01-11dd-9824-eb99752e6765` on page
65f32565e111adbbb806d0d7 (the 5-card "Advantages of Vinyl Plank Flooring" section).
Rollback: set that element's visibility back to true.

## Revision 21 — vinyl page gallery shows vinyl photos only
The "Our Gallery" section is the shared Gallery component; which photos show is controlled by its
"Floor Type" CMS filter prop. General vinyl page had `flooring-type isSet` (ALL photos → hardwood
refinishing shots); Bellevue has `flooring-type equals c0d7e4f67b0ed913a5918154f299fdb4`
(= "Vinyl Plank Flooring Installation", 7 items in the Galleries collection 6729ca872c3650b83417285e).

Filter-type component props CANNOT be set via the Webflow API (set_component_instance_prop_values
returns "Collection not found"; confirmed unsupported). Workaround: added HtmlEmbed
`bb1f8de6-9828-5d0b-c690-86e3f1cc2e09` after `dd475bb1...` that hides any `.w-dyn-item` in the
Our Gallery section whose caption does not match /vinyl|lvp|waterproof plank/i.

PERMANENT FIX (2 clicks in Designer): select the Gallery instance on this page, set Floor Type
filter to "Vinyl Plank Flooring Installation", then delete that embed.
Caveat: new vinyl gallery items must have "vinyl" or "LVP" in the caption to survive the filter.

## Revision 22 — REVERTED the client-side gallery filter (it broke the carousel)
Hiding `.w-dyn-item` slides with display:none corrupted the gallery carousel's measurements
(site scripts GalleryArrowsMultiFix / ocareasslider size and position the track), so slides
overflowed and overlapped the section below. Deleted embed
`bb1f8de6-9828-5d0b-c690-86e3f1cc2e09`. Gallery is back to its original working state
(showing all flooring types).
CONCLUSION: the ONLY safe fix is changing the Gallery instance's "Floor Type" filter prop to
"Vinyl Plank Flooring Installation" in the Webflow Designer — that prop type is not writable
via the API. Do not retry a client-side slide filter.

## Revision 23 — new self-contained vinyl gallery slider
Replaced the stock CMS gallery on page 65f32565e111adbbb806d0d7:
- Old `Section // Galllery` instance `ff3c0fe3-...` cannot be hidden via API
  ("Element does not support setVisibility"), so it is hidden with CSS
  `.section_gallery{display:none!important}` inside the new embed (page-scoped).
- New embed `d5923f4d-9623-976b-7cb7-e408b68a0484` inserted before `dd475bb1-...`:
  heading "Our Gallery", subtitle, red "Check More Here" -> /our-work, and a scroll-snap
  flex track with the 7 vinyl CMS images + captions, red prev/next buttons.
- Deliberately NOT a Webflow slider and not touching `.w-dyn-item` — this is what caused the
  overlap in Revision 21. Arrows are absolutely positioned only inside `.ocvgal-rel`
  (position:relative), so nothing can overflow into neighbouring sections.
Image URLs are hardcoded from the Galleries collection; new CMS photos will NOT appear here
automatically. Cleanest long-term fix remains: set the Gallery instance Floor Type filter to
"Vinyl Plank Flooring Installation" in Designer, delete this embed, unhide the stock gallery.

## Revision 24 — Our Work hero image
Page /our-work (65f32565e111adbbb806d079). Hero image element
`d6b1ee80-37ff-5b41-bc06-6d4b6574bd5a` (.hero-cover-img, assetId 6a18afd7f1bbd4795f420612).
Requested photo: "Red oak dining room — natural matte finish", found in the Our Work gallery
embed `7a1aafb3-...` (JS DATA array, Hardwood Floor Refinishing category, 3rd photo):
https://cdn.prod.website-files.com/6377e8e6a539368c54f1cadd/6a1a5278656dbb77c2095be1_Refinished%20red%20oak%20hardwood%20floor%20with%20natural%20matte%20finish%20in%20a%20Bellevue%20living%20room.avif
That file is NOT in the site asset library (checked all 1245 assets — no hostedUrl match), so
set_image_asset was not possible. Added embed `c492a4b9-4fd4-ed3a-3ab1-9af2f1936a64` after the
hero section that swaps the hero img src/alt and strips srcset/sizes.
Permanent fix: upload that image to Assets, set it on the hero image element, delete the embed.

## Revision 25 — Our Work category filter
Gallery embed `7a1aafb3-...` renders 2 stacked `.ocw-sec` sections inside `#ocw-gal`:
"Hardwood Floor Refinishing" (14 photos) and "Flooring Installation" (15 photos). No filter existed.
Added embed `d5294c65-4e15-af77-e868-e96a2a7a04b8` immediately BEFORE the gallery embed:
pill filter bar (All Work / Hardwood Floor Refinishing / Flooring Installation) that toggles
`display:none` on whole `.ocw-sec` sections.
Safe by design: the bar lives OUTSIDE `#ocw-gal` (the gallery sets `gal.innerHTML` once, which
would wipe anything inside), sections are CSS grid / flex-scroll with no JS width measurement,
and cards keep their `data-c`/`data-i` so the lightbox still works.
Adding a 3rd category later = add one button with data-f="2".

## Revision 26 — Our Work: mobile labels + Tile & Carpet categories
- Filter labels now responsive: full text on desktop, short on ≤640px
  (All / Refinishing / Installation / Tile / Carpet) via .lg/.sm spans.
- New embed `4278760d-4c74-35e6-e1ec-1113578f24a9` (after the gallery embed) adds two sections
  using `.ocx-*` classes, OUTSIDE #ocw-gal so the original widget is untouched:
  * Tile Installation — 8 photos from the Tile Gallery page (6a8fb630bf19a48fafa6a9e5)
  * Carpet Installation — 3 photos from the Carpet Installation page (6a9453aa5038df1a06154847)
  Includes its own minimal fixed-overlay lightbox (#ocx-lb) so cards zoom like the originals.
- Filter embed `d5294c65-...` now toggles both `#ocw-gal .ocw-sec` (index 0/1) and
  `.ocx-sec[data-cat=tile|carpet]`.
Notes: Tile Installation service page has NO photos of its own; 13 more tile photos are available
on the Tile Gallery page if we want to expand. Image srcs are the assets' hostedUrl
(s3.amazonaws.com/webflow-prod-assets/...) since embeds cannot reference asset IDs.
