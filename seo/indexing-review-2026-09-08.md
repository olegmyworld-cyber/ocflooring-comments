# nwocflooring.com — Search Console "Page indexing" review (2026-09-08)

Source data: GSC page-indexing export (312 not indexed / 428 indexed, sitemap 520 URLs),
GSC search-analytics by page (Windsor connector, last 90 days + prior 12 months),
Webflow site inventory (223 static pages, 273 blog items, 191 products, 62 galleries, 9 blog categories),
Semrush site audit snapshot of 2026-09-08 (444 pages crawled).

## What the six GSC rows actually are

| GSC reason | Pages | What it is on this site | Fix |
|---|---|---|---|
| Page with redirect | 104 | Old URLs Google remembers: `/services/*` (folder renamed to `/flooring-services-near-me/`), `/city-of-arlington/*` (renamed to `/arlington/`), pre-June messy city slugs | Redirect map below; then "Validate fix" |
| Not found (404) | 36 | Same families, the ones with no redirect rule at all. Includes the ~30 deleted city laminate pages | Redirect map below |
| Alternate page with proper canonical | 15 | Blog pagination `/blog?43f680e2_page=N` and http/non-www variants | Nothing |
| Crawled - currently not indexed | 91 | Mostly product pages: 95 of 101 sitemap orphans are `/product/*` with zero internal links | Link products from the Our Products page / category pages |
| Excluded by noindex | 3 | Flooring calculator, changelog, utility pages | Nothing |
| Discovered - currently not indexed | 63 | The 56 carpet + tile city pages created Aug 28–Sep 3, plus a few products | Wait; internal links help |

Semrush crawl today: 0 errors, 0 broken internal links, 11 redirects (all blog pagination), 101 sitemap orphans, 89 pages with a single internal link, schema.org markup on 0 of 430 pages.
So the redirect/404 problem is not internal linking. It is 174 historical URLs that Google still holds and that currently go nowhere.

## What those dead URLs are worth

| Family | URLs | Impressions last 90d | Clicks prior 12 months |
|---|---|---|---|
| `/services/*` renamed folder | 27 | 25,271 | 263 |
| Deleted city laminate pages (clean slugs) | ~30 | ~19,000 | 0 (created after June) |
| Old messy city slugs | ~93 | ~2,300 | 365 |
| `/city-of-arlington/*` renamed folder | 10 | 1,387 | 13 |
| Deleted blog posts, product, thank-you, Bellevue refinishing | 14 | 0 | 52 |
| **Total** | **174** | **49,679 (25% of site impressions)** | **693** |

The live `/flooring-services-near-me/` pages have 105 impressions and 0 clicks in 90 days. All of that folder's search visibility is still parked on the old `/services/` URLs.

## Traffic by page type, last 90 days (live pages only)

| Type | Live pages | Impressions | Clicks |
|---|---|---|---|
| Home | 1 | 23,521 | 289 |
| Blog posts | 118 | 49,964 | 205 |
| Products | 191 | 5,559 | 189 |
| City: hardwood refinishing | 29 | 20,148 | 42 |
| City: vinyl plank | 30 | 22,465 | 17 |
| City: hardwood installation | 30 | 21,133 | 16 |
| City: hardwood repair | 30 | 1,968 | 5 |
| City: carpet (new) | 30 | 1,167 | 2 |
| City: tile (new) | 31 | 421 | 0 |
| Service pages `/flooring-services-near-me/` | 21 | 105 | 0 |

## Files

- `redirects-2026-09-08.csv` — 174 rows: old path, new path, traffic, reason. Review this one.
- `redirects-webflow-import.csv` — same 174 rows, two columns, for Webflow Site settings → Publishing → 301 redirects → import.

Mapping rules used: `/services/X` → `/flooring-services-near-me/X` (8 renamed slugs mapped by hand);
`/city-of-arlington/<service>-in-arlington-wa` → `/arlington/<service>`;
messy city slugs → the clean slug for the same service in the same city folder;
every laminate city URL → `/flooring-services-near-me/laminate-flooring-installation` (see decision below);
deleted blog posts → `/blog`; `/thank-you` → `/contact`; Bellevue refinishing → `/` (the homepage is the Bellevue refinishing page).

## Laminate mapping (decided 2026-09-08)

The laminate city pages were deleted on purpose. All 61 laminate URLs redirect to
`/flooring-services-near-me/laminate-flooring-installation`. Confirmed by Oleg; keep as is.

## Small cleanup, manual

`/checkout`, `/paypal-checkout`, `/order-confirmation` are in the sitemap. The Webflow API refuses to change sitemap status on ecommerce utility pages, so untick "include in sitemap" in each page's settings in the Designer, then publish.

## Not done here

- Redirect rules cannot be created through the Webflow MCP tools available in this session; import the CSV manually.
- Direct crawl of nwocflooring.com is blocked from this environment; the 104/36 split per URL comes from GSC's own export, which I did not have at URL level.
