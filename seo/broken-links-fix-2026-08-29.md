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
- **Stale `href` attributes (second pass — 184 removed across 62 pages):** link elements on this site carry *both* a Webflow link setting and a redundant custom HTML attribute named `href`. Correcting the link setting left that custom attribute still holding the old 404 URL, so each element carried two conflicting values. A follow-up pass swept all 208 static pages and **removed the redundant attribute**, leaving the corrected link setting as the single source of truth. Every affected page was re-queried afterwards and returned zero stale matches.
- **Already clean (21 pages):** the city `hardwood-floor-repair` pages and most `/flooring-services-near-me/*` pages had been redesigned and republished at 23:58 UTC on Aug 28 — after the 20:03 crawl — so their flagged links no longer existed.
- **Shared components checked:** Navbar, Footer, Section//Services, Section//Areas, Section//Hero definitions contain no old service links.
- **Full-site sweep:** all remaining 123 static pages were checked for the bad URL patterns (this caught the `/reviews` links above).

The site was published to `www.nwocflooring.com`, `nwocflooring.com`, and the Webflow staging subdomain after all edits.

## Gotcha worth remembering for the next URL change

Webflow links here have **two** places a URL can live, and both must be handled:

1. the **link setting** (what the Designer's link picker edits) — update with `set_link`;
2. a redundant custom **`href` attribute** on the same element — Webflow reserves this name and *rejects* writes to it (`set_attributes` fails with "internal error occurred"), but `remove_attribute` works. Delete it rather than trying to rewrite it.

Fixing only the link setting leaves a contradictory `href` attribute behind, which is what happened on the first pass here.

## Notes

- Live HTML could not be fetched to confirm the rendered output: this session's egress policy returns 403 for `nwocflooring.com` and `oc-flooring.webflow.io`. Removing the conflicting attribute is correct regardless of which of the two values Webflow would have rendered. Re-running the Semrush audit is the way to confirm end to end.
- The Semrush crawl predates the Aug 28 23:58 publish, so a handful of its rows were already stale (e.g. Arlington pages have since moved to `/arlington/…` with short slugs).
- No 301 redirects were added: the Webflow Data API's 301-redirect endpoints are gated to Enterprise hosting plans and this site is not on one (confirmed by an API call). The required rules are written up in `301-redirects-required.md` and must be added by hand in Site Settings → Publishing → 301 redirects.
- Machine-readable details: `broken-links-fix-2026-08-29.json` (per-page and per-post counts).
- Re-run the Semrush audit to confirm the error count drops to zero.
