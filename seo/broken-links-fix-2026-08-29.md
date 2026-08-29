# Broken internal links fix — nwocflooring.com — 2026-08-29

Source: Semrush Site Audit export (crawled 2026-08-28 20:03 UTC) reporting **308 broken internal links** (HTTP 404), all pointing at old URL paths that were renamed when the services section moved to `/flooring-services-near-me/`.

## Root cause

The services section URL structure changed over time (`/services/…` → `/services-near-me/…` → `/flooring-services-near-me/…`), but links in blog post bodies, city landing pages, and a few embeds were never updated. Six links also pointed at city pages that no longer exist (five city laminate pages and the old Bellevue refinishing page, whose role is now filled by the homepage).

## URL mapping applied

| Old URL | Replacement |
|---|---|
| `/services/<slug>` | `/flooring-services-near-me/<slug>` |
| `/services-near-me/<slug>` | `/flooring-services-near-me/<slug>` |
| `/city-of-{edmonds,everett,lynnwood,mukilteo,snohomish}/laminate-flooring-installation-in-<city>-wa` | `/flooring-services-near-me/laminate-flooring-installation` |
| `/city-of-bellevue/hardwood-floor-refinishing-in-bellevue-wa` | `/` (homepage targets this keyword) |

Absolute forms (`https://www.nwocflooring.com/…`) were rewritten to the same site-relative paths.

## What was changed (via Webflow API, published 2026-08-29 ~01:30 UTC)

- **Blog CMS (Blogs collection):** 107 posts updated, **265 link replacements** in `post-body` rich text. Every updated body was byte-compared against the intended content after the push; all 107 verified exact.
- **Static pages:** **185 link elements fixed** across 64 pages — city carpet/tile landing pages (breadcrumb + footer links), the tile gallery, and 4 stale links on `/reviews` found by a full-site sweep the audit had missed.
- **HTML embeds:** **5 code blocks fixed** — two in-copy links and three CSS attribute selectors (`a[href="/services/…"]`) used by the related-services sliders to hide the current page's own card; updated so the hide logic keeps working.
- **Stale `href` attributes (second pass):** link elements on this site carry *both* a Webflow link setting and a custom HTML attribute named `href`. Updating the link setting alone left the custom attribute pointing at the old 404 URL, so a follow-up pass swept all 208 static pages and brought every stale `href` attribute in line with its corrected link setting. Worth knowing for future URL changes: **both** have to be updated.
- **Already clean (21 pages):** the city `hardwood-floor-repair` pages and most `/flooring-services-near-me/*` pages had been redesigned and republished at 23:58 UTC on Aug 28 — after the 20:03 crawl — so their flagged links no longer existed.
- **Shared components checked:** Navbar, Footer, Section//Services, Section//Areas, Section//Hero definitions contain no old service links.
- **Full-site sweep:** all remaining 123 static pages were checked for the bad URL patterns (this caught the `/reviews` links above).

The site was published to `www.nwocflooring.com`, `nwocflooring.com`, and the Webflow staging subdomain after all edits.

## Notes

- The Semrush crawl predates the Aug 28 23:58 publish, so a handful of its rows were already stale (e.g. Arlington pages have since moved to `/arlington/…` with short slugs).
- No 301 redirects were added (the Webflow MCP connector doesn't expose the redirects API). If old `/services/…` URLs have external backlinks, adding wildcard 301s in Webflow Site Settings → Publishing → 301 redirects would preserve that equity: `/services/(.*)` → `/flooring-services-near-me/%1` and `/services-near-me/(.*)` → `/flooring-services-near-me/%1`.
- Machine-readable details: `broken-links-fix-2026-08-29.json` (per-page and per-post counts).
- Re-run the Semrush audit to confirm the error count drops to zero.
