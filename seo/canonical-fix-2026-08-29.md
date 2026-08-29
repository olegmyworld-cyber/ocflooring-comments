# Non-canonical URLs in sitemap — nwocflooring.com — 2026-08-29

Source: Semrush Site Audit, "Wrong pages found in sitemap.xml" → **Non-canonical URL**, 20 URLs (crawled 2026-08-28 20:03 UTC).

## What the error actually was

The most damaging of the four audits worked so far. Each `/flooring-services-near-me/*` page's head custom code declared:

```html
<link rel="canonical" href="https://www.nwocflooring.com/services-near-me/floor-refinishing" />
```

That target is one of the 404 URLs from the 4xx audit. Every service page was telling Google *"the authoritative version of me is a page that does not exist"* — a strong signal to drop the page from the index. The sitemap said "index this URL"; the page said "no, index that dead one". Hence the flag.

The dead URL was not only in the canonical. It repeated in:

- three `<link rel="alternate" hreflang>` tags
- `<meta property="og:url">`
- JSON-LD `@id` and `offers.url`
- on several pages, a JavaScript "Guardrail" that **rewrites the canonical to the dead URL on page load**, so fixing the static tag alone would have been silently undone

**108 stale URL references across 18 service pages**, plus 21 more across 3 Arlington pages found by a wider sweep (below).

## The blocker: Webflow's API refuses canonical links, hreflang links and scripts in head code

Writes to page head custom code fail with **HTTP 406** when the payload contains a `<link rel="canonical">`, a `<link rel="alternate" hreflang>`, or a `<script>` tag. Webflow owns those tags — canonical is a native Page Settings SEO field — so it rejects them in raw head code. Established by bisection against a live page, restoring the original after each test:

| Payload | Result |
|---|---|
| `<meta charset>`, `<meta viewport>`, `<title>`, og/twitter meta | **200 OK** |
| 4,912-byte head with `<template>` blocks | **200 OK** |
| `<link rel="canonical" …>` | **406** |
| `<link rel="alternate" hreflang=…>` | **406** |
| `<script>` (plain or `application/ld+json`) | **406** |

Size is not the cause: a 4.9 KB write succeeded while a 60-byte one containing a canonical link failed. Reads always succeed.

**This means the canonical and hreflang tags cannot be corrected through the API at all.** Moving the JSON-LD into Webflow's native page schema field *is* API-writable and was verified working, but it does not unblock these pages, because the remaining head code still contains the canonical and hreflang links that trigger the rejection. The Designer is the only route.

## What was fixed automatically

Two pages have script-free head code — `hardwood-floor-installation` (it uses `<template>` instead of `<script>`) and `flooring-repair` (meta-only). Both were written via API and verified **byte-exact by SHA256** against the intended content, then published. Their `og:url` and JSON-LD now point at the live paths.

## What needs a manual paste (19 pages)

Corrected, validated head code for every affected page is in `seo/canonical-fixes/`. See the README there for the procedure — it reduces to one find/replace per page:

> `/services-near-me/` → `/flooring-services-near-me/`  (16 service pages)
> `/city-of-arlington/<x>-in-arlington-wa` → `/arlington/<x>`  (3 Arlington pages)

Each file was validated: only URL paths changed, no double-prefixed paths produced, no dead URL left anywhere, and every canonical self-referencing.

### An alternative, if you'd rather not paste

The 406 is triggered purely by the `<script>` tag. Moving each page's JSON-LD out of head custom code and into Webflow's **native page JSON-LD field** (which the API *can* write, and which was used successfully for the structured-data fix) would leave the head script-free and fully API-writable. Same rendered output. This was not done unasked because it relocates where your schema lives — say so and it can be done in one pass.

## Site-wide audit performed beyond the report

Semrush only checks URLs in the sitemap, and it had already missed one broken page (`flooring-store`). A read-only sweep of the remaining **190 pages** found:

- **3 canonical mismatches** — the Arlington pages above, all pointing at 404s. Fixed files provided.
- **0** other pages referencing any dead URL in head code.
- **86** pages with correct self-referencing canonicals.
- **101** pages with no canonical in custom code. This is *not* automatically a defect: a page without one lets Google use the crawled URL, and Webflow can emit a canonical from Page Settings that this API cannot see. Treat as hygiene, not an error.
- **1** `noindex` page (`/changelog`) — appropriate.

## Not resolvable through the API at all

The five city repair pages flagged by the audit — Edmonds, Everett, Lynnwood, Mukilteo, Snohomish — declare **no canonical** in head code, in any page embed, or in site-wide code. All three locations were checked exhaustively. Theirs must be set in **Page Settings → SEO → Canonical Tag URL**, which the Webflow Data API exposes for neither reading nor writing (confirmed: `get_page_metadata` returns only `seo{title,description}`, `openGraph`, `slug`, `draft`, `publishedPath`). Open one in the Designer and check that field — it should be empty or contain the page's own URL.

## Other findings worth a look (not canonical issues, not changed)

- `/city-of-bellevue/hardwood-floor-installation-in-bellevue-wa` — its `og:url` points at a different slug than its own path, suggesting head code copied from a sibling page.
- `/reviews` — its title, meta description and Open Graph tags are all about refinishing cost and pricing, apparently pasted from another page. Its canonical is correct.

## Verification and status

- Two pages fixed via API, SHA256-verified, published to both domains.
- 19 corrected files committed, each validated as described above.
- Live HTML could not be fetched to confirm rendered output — egress policy returns 403 for the domain. Re-run the Semrush audit after pasting the remaining pages.
