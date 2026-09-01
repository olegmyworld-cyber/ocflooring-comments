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
