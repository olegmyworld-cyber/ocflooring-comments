# 301 redirects still required — nwocflooring.com

Source: Semrush Site Audit, "4xx client errors" (crawled 2026-08-28 20:03 UTC) — 21 URLs returning 404.

**Status: needs 2 minutes of manual work in the Webflow dashboard.** These cannot be created through the API — the Webflow Data API's 301-redirect endpoints (`/sites/{id}/redirects`) are gated to **Enterprise** hosting plans, and this site is not on one. Confirmed by an API call, which returned: *"This site does not have an Enterprise hosting plan."*

## Context

All 21 URLs are pages that no longer exist after the services section was renamed to `/flooring-services-near-me/`. Every **internal link** pointing at them has already been fixed (see `broken-links-fix-2026-08-29.md`), so the site no longer links to any of them. What remains is the URLs themselves: external backlinks, Google's index, and bookmarks still hit a 404. A 301 preserves that accumulated link equity and sends visitors somewhere useful.

## Where to add them

Webflow dashboard → **Site Settings → Publishing → 301 redirects** → add each pair → **Publish**.

Webflow supports wildcards, so 15 of the 21 collapse into a single rule.

## The rules

| # | Old path (`fromUrl`) | Redirect to (`toUrl`) | Covers |
|---|---|---|---|
| 1 | `/services-near-me/(.*)` | `/flooring-services-near-me/%1` | 15 URLs |
| 2 | `/city-of-edmonds/laminate-flooring-installation-in-edmonds-wa` | `/flooring-services-near-me/laminate-flooring-installation` | 1 |
| 3 | `/city-of-everett/laminate-flooring-installation-in-everett-wa` | `/flooring-services-near-me/laminate-flooring-installation` | 1 |
| 4 | `/city-of-lynnwood/laminate-flooring-installation-in-lynnwood-wa` | `/flooring-services-near-me/laminate-flooring-installation` | 1 |
| 5 | `/city-of-mukilteo/laminate-flooring-installation-in-mukilteo-wa` | `/flooring-services-near-me/laminate-flooring-installation` | 1 |
| 6 | `/city-of-snohomish/laminate-flooring-installation-in-snohomish-wa` | `/flooring-services-near-me/laminate-flooring-installation` | 1 |
| 7 | `/city-of-bellevue/hardwood-floor-refinishing-in-bellevue-wa` | `/` | 1 |
| 8 | `/services/(.*)` | `/flooring-services-near-me/%1` | *recommended, see below* |

**Rule 7** goes to the homepage because the homepage is now the Bellevue hardwood-refinishing page — its title and schema are "OC Flooring — Hardwood Floor Refinishing Bellevue". There is no other Bellevue refinishing page on the site.

**Rule 8** is not in this audit (nothing links to `/services/…` any more, so the crawler never reached it), but that path family was the site's service URLs for years and is the most likely to hold external backlinks. Adding it is cheap insurance.

## Safety check performed

- All 21 URLs confirmed genuinely absent from the site's page list — they are real 404s, not crawl artifacts.
- Every redirect **target** confirmed to be a live page, so none of these rules redirects to another 404.
- No live page exists under `/services/` or `/services-near-me/`, so the two wildcard rules cannot shadow real content.

## After adding

Publish the site, then re-run the Semrush audit. The 4xx count should go to zero. In Google Search Console, the affected URLs will move out of "Not found (404)" over the following crawls.
