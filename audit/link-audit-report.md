# Site-wide link audit — nwocflooring.com (2026-09-06/07)

Trigger: on the blog post `/blog/bathroom-tile-installation-cost-seattle` the link
"Tile installation in Seattle" opened the Seattle *hardwood installation* page.
Request: check every link on every page and make each one match its service and city.

## What was checked

| Layer | Count | How |
|---|---|---|
| Static pages (incl. home, 404, utility pages) | 223 | Designer element tree, component-instance link props, HTML embeds (`data_element_tool`, `data_element_settings_tool`) |
| Links found on pages | 3,145 | text + resolved target (page id → live path) |
| Shared components (Navbar, Footer, Section // Areas, Services, CTA, Hero, …) | 23 | element trees inside component definitions |
| Links found in components | 271 | incl. 183 city links in Section // Areas |
| Page / site custom code (head + footer) | 66 pages, 1,179 URL refs | `get_page_freeform_code`; `<a href>`, canonical, hreflang, og:url, schema |
| CMS blog posts (live) | all | body + city-link fields |
| Registered scripts | 15 | source read where inline; hosted ones listed |

Rule applied: for any link whose visible text names a service and a city, the target
must be that city's page for that service (`/city-of-<x>/<service>-in-<x>-wa`,
`/seattle/…`, `/arlington/<service>`, Bothell under `/hardwood-floor-refinishing/`).
The target must also be a live page.

## Defects found and fixed (37 edits, all published)

| # | Where | Problem | Fix |
|---|---|---|---|
| 1 | 29 tile city pages, element `1c802dfa-…-fe6edce3ca72` ("carpet installation in <city>") | Designer link was correct, but a stale custom `href` attribute forced every page to `/city-of-bellevue/carpet-installation-in-bellevue-wa` | attribute removed on all 29 pages |
| 2 | Hubs commercial-flooring-installation, flooring-store, hardwood-floor-maintenance, insurance-restoration-services | canonical, 3 hreflang tags, og:url and schema `@id`/`url` pointed at retired `/services-near-me/…` (404) | head code rewritten to the live `/flooring-services-near-me/…` URL |
| 3 | `/city-of-bellevue/hardwood-floor-installation-in-bellevue-wa` | og:url and Service schema pointed at `/city-of-bellevue/flooring-installation-in-bellevue-wa` (404) | rewritten to the page's own URL |
| 4 | Section // Areas component, "Lake Forest Park, WA" (installation tab) | pointed at the Lake Stevens installation page | now the hardwood installation hub (no Lake Forest Park page exists) |
| 5 | Section // Areas component, "Lake Forest Park, WA" (vinyl/laminate tab) | pointed at the Lake Stevens vinyl page | now the vinyl-plank / laminate hub |
| 6 | Footer component CSS embed `3eb254f7-…` | rule that hides the "Floor Repair" cross-sell card on repair pages was keyed on the retired `/services/flooring-repair` href, so it matched nothing | rule added for the live `/flooring-services-near-me/flooring-repair` href |

Full log: [`fixes.json`](fixes.json).

## Guard script

[`../webflow-scripts/oclinkmatch-1.0.0.js`](../webflow-scripts/oclinkmatch-1.0.0.js)
(registered as inline script `oclinkmatch` 1.0.0, footer of the blog post template
`65f32565e111adbbb806cf1a`). After load and on DOM changes it rewrites any internal
anchor whose text names a service + city to that city's page, but only when the
current target is already a city/hub page. Reason: the reported wrong link was **not
present in any stored content** (CMS fields, page code and components all carry the
correct Seattle tile URL); the only unreadable code on blog pages is the hosted
`ocrelatedposts` script, so the guard neutralises a runtime rewrite whatever its source.

## Left as-is (needs a content decision)

- **Footer "Privacy Policy" / "Terms & Conditions"** have no target (no such pages exist on the site).
- **"Lake Forest Park, WA"** appears in three Areas tabs but has no city pages; the links now go to the service hubs.
- **Navbar Dark** component links to three deleted page ids, but no page uses that component.
- **Section // Areas "Bellevue, WA" (refinishing tab)** goes to the refinishing hub, not a Bellevue city page (none exists; the home page covers Bellevue refinishing).

## Tooling

- `linkcheck.py` — text → expected path rules and live-page check.
- `analyze_pages.py` — consumes the extraction JSON (`{pages:[…], components:[…]}`) and reports `dead`, `mismatch`, `dead-pageid`, `attr-mismatch`.
- `extract_links.py` — helper used by the extraction agents.
