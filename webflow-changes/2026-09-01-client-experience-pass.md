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
