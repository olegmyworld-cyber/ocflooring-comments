# Internal broken links — Semrush report, 29 Aug 2026

Source report: `nwocflooring.com_internal_broken_links_20260829.csv` — 22 links, 404 each.
Companion to [`301-redirects-2026-08-29.md`](301-redirects-2026-08-29.md), which covers the
same dead URLs from the destination side.

| Source pages | Broken link | Status |
| --- | --- | --- |
| `/blog/water-based-vs-oil-based-floor-finish` (2 links) | two `/blog/*` posts | **Fixed** — both were unpublished drafts, now published |
| 15 × `/flooring-services-near-me/<slug>` | `/services-near-me/<same slug>` | **Fixed** — `ocLinkFix` rewrites the href |
| 5 × `/city-of-<c>/hardwood-floor-repair-in-<c>-wa` | `/city-of-<c>/laminate-flooring-installation-in-<c>-wa` | **Fixed** — `ocLinkFix` rewrites the href |

## Where the links come from

Each of the 15 service pages links to its own wrong-prefix twin, and each of the 5 repair
pages links to its own city's non-existent laminate page. That self-referential pattern
means the href is computed at runtime from the current path, not authored anywhere.

Confirmed by elimination — none of these contain the dead paths:

- **Designer content** on the source pages (full element trees via the Elements API)
- **HTML embeds** on those pages (all embed `code` settings read individually)
- **Page custom code**, head and footer
- **Site custom code**, head and footer
- **Shared components** — Navbar, Footer, `Section // Services`, `Section // Areas`. The
  navbar's 11 services dropdown items use `linkType: page` with page IDs, which resolve to
  `/flooring-services-near-me/...` correctly.
- **CMS** — all 7 collections; all 209 blog items were scanned field by field

That leaves the CDN-hosted registered scripts. `OCAreaLinksInjector` is applied site-wide,
and `ocLaminateGuides` / `ocInstallGuides` / `ocRefGuides` / `ocVinylGuides` / `ocBlogLinks`
are applied per page. Their sources live on `cdn.prod.website-files.com`, which the session
that wrote this could not reach — the network policy blocks all outbound HTTP, including
the live site itself.

## The fix: `ocLinkFix` 1.0.0

[`webflow-scripts/oclinkfix-1.0.0.js`](../webflow-scripts/oclinkfix-1.0.0.js) — registered
inline via the Scripts API and applied to the 20 source pages, footer, version 1.0.0.

It rewrites `<a>` hrefs matching exactly three dead patterns, after the injector runs
(DOMContentLoaded, load, four timed passes, and a MutationObserver for 15s):

| Pattern | Rewritten to |
| --- | --- |
| `/services-near-me/<slug>` | `/flooring-services-near-me/<slug>` |
| `/services/floor-refinishing` | `/flooring-services-near-me/floor-refinishing` |
| `/city-of-<c>/laminate-flooring-installation-in-<c>-wa` | `/city-of-<c>/vinyl-plank-flooring-installation-in-<c>-wa` |

Safe by construction: every path it matches 404s today, so a rewrite can only improve it.
All 27 `city-of-*` folders were checked to have a vinyl-plank page, so the city rule can
never produce a new 404. Same-origin links only; querystring and hash are preserved.

Semrush found these links even though they are injected by JavaScript, which means its
crawler renders JS — so it will see the corrected hrefs too. The 301 redirects cover the
non-rendering case.

### Pages it is applied to

Service pages (`/flooring-services-near-me/`): buff-and-recoat-hardwood-floors,
dustless-floor-sanding, eco-friendly-floor-refinishing, engineered-hardwood-flooring,
floor-refinishing, flooring-repair, hardwood-floor-installation, hardwood-floor-staining,
laminate-flooring-installation, our-products, solid-hardwood-flooring,
stair-installation-and-remodeling, unfinished-hardwood-floors,
vinyl-plank-flooring-and-laminate-flooring, wood-wall-panels.

Repair pages: `/city-of-{edmonds,everett,lynnwood,mukilteo,snohomish}/hardwood-floor-repair-in-<c>-wa`.

Seven service pages had no page custom-code block at all and one was created for them; the
other thirteen pages kept the scripts they already had.

### Why per-page and not site-wide

The site is at Webflow's cap of **15 applied scripts** (14 footer + `OCHeaderInit` in the
header), so `add_site_script` is rejected in both blocks — the same limit noted in the
BonaMobileFix entry above.

If a re-crawl shows these links on pages beyond the 20 above, apply it site-wide by pasting
this into **Site Settings → Custom Code → Footer** (it needs no script slot) and removing
the 20 page-level applications:

```html
<!-- ocLinkFix 1.0.0 — see github repo webflow-scripts/oclinkfix-1.0.0.js -->
<script src="https://cdn.prod.website-files.com/6377e8e6a53936b48ef1cad0%2F689e5ba67671442434f3ca35%2F6a935037e9a71d4228621255%2Foclinkfix-1.0.0.js" defer></script>
```

### This is a stopgap

`ocLinkFix` patches the symptom. The real fix is correcting the injector that writes
`/services-near-me/` in the first place — the same stale prefix that also leaves four dead
branches in `OCAreasStart` (see the redirects doc). A session with network access to
`cdn.prod.website-files.com` should read the injector scripts, fix the prefix at source,
and then delete `ocLinkFix` and its 20 page applications.

## Publishing

Script applications are staged. They go live on the next Webflow publish. The two blog
posts were published through the CMS API and are already live.
