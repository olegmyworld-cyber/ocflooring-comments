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

## Follow-up 2026-09-07: still lands on hardwood after the fixes

Re-verified after the user reported the Seattle tile link still opening the Seattle
hardwood installation page:

- The live CMS item carries `/seattle/tile-installation-in-seattle-wa` in both places the
  text appears (body "Related reading" and the City Links block).
- The tile page is real tile content (31 headings, `ti-*` styles, title "Tile Installation
  Seattle, WA | OC Flooring") and is not a draft.
- Semrush's crawl of 2026-09-03 fetched `/seattle/tile-installation-in-seattle-wa` and got
  the tile page (200, tile title), so the server does not redirect that URL.
- No Webflow redirect (all 187 rows exact, none match), no Cloudflare worker on the domain
  (only `llms-txt`), the 404 script leaves the URL alone, and every readable script on blog
  pages (ocblogdates, ocbguard, ocseofixes3, siteCleanupD, ocjunkcleanup, ocarealinksinjector,
  site head/footer code) is link-neutral for this URL. `ocrelatedposts` is hosted with an SRI
  hash and cannot be read from this environment.
- The live site and Webflow's CDN are unreachable from this environment (egress blocked), so
  the rendered page could not be inspected directly.

This is the third time the same symptom was chased (Woodinville carpet, Mukilteo carpet,
now Seattle tile) with every stored link correct; the prior branch concluded the hop is
HTTP-level or a browser-cached 301.

**Added:** `webflow-scripts/oclinkclick-1.0.0.min.js`, registered as inline script
`oclinkclick` 1.0.0 and applied to the blog post template and the home page footers. It
intercepts the click in the capture phase and navigates to the page matching the link's
service + city text, so a late href rewrite or a competing click handler cannot redirect the
visitor. It ignores modified clicks (ctrl/cmd/shift/alt/middle), external hosts, multi-city
labels and long text. `oclinkmatch-1.1.0.js` is the combined (href rewrite + click guard)
version for site-wide use once a custom-code slot is available; it is 2,472 chars, over the
2,000-char inline-script limit, and the site footer code is too close to its 10k limit.

If the symptom survives this, the remaining causes are outside Webflow content: a
browser-cached 301 (test in an incognito window), a Google Tag Manager tag
(container GTM-PR94PQZW is loaded on every page and can inject code), or the
`ocrelatedposts` hosted script.
