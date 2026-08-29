# Corrected head custom code — canonical fix

Source: Semrush Site Audit, "Wrong pages found in sitemap" → **Non-canonical URL**, 20 URLs (crawled 2026-08-28 20:03 UTC).

## The problem

Every `/flooring-services-near-me/*` page's **head custom code** declares a canonical pointing at its OLD `/services-near-me/*` URL — a URL that now returns 404:

```html
<link rel="canonical" href="https://www.nwocflooring.com/services-near-me/floor-refinishing" />
```

A canonical pointing at a 404 tells Google the page's authoritative version does not exist, which is a strong signal to drop the page from the index. The same dead URL is repeated in:

- three `<link rel="alternate" hreflang=…>` tags
- `<meta property="og:url">`
- JSON-LD `@id` and `offers.url`
- on some pages, a "Guardrail" `<script>` whose `var target = …` **actively rewrites the canonical to the dead URL at runtime**, so correcting the tag alone would be undone on load

108 stale URL references across 18 pages.

## Why these files exist instead of the fix being applied

Webflow's Data API **refuses any write to page head custom code that contains a `<script>` tag** — it returns HTTP 406. This was verified directly, not assumed:

| Payload | Result |
|---|---|
| 450 bytes, meta tags only | **200 OK** |
| 60 bytes: `<meta …/>` + `<script>var a=1;</script>` | **406** |
| 4.6 KB corrected head with JSON-LD script | **406** |

16 of the 18 pages carry a JSON-LD `<script>` in head code, so they cannot be written through the API. The two that can (`hardwood-floor-installation`, which uses `<template>` instead of `<script>`, and `flooring-repair`, whose head is meta-only) were applied via API.

## How to apply the rest

For each remaining page: **Webflow Designer → select the page → Page Settings (gear) → Custom Code → Inside `<head>` tag**, then either

- **the one-step way:** find `/services-near-me/` and replace with `/flooring-services-near-me/` — that single substitution fixes the canonical, all three hreflang tags, `og:url`, the JSON-LD, and the guardrail target in one go; or
- **paste wholesale:** replace the whole block with the matching `<slug>.head.html` file here.

Then **Publish**.

## Validation already performed on every file here

- Only URL paths were changed; nothing else was reformatted, reordered, added or removed.
- No `flooring-flooring-services-near-me` double-prefix was produced.
- No `nwocflooring.com/services-near-me/` or `nwocflooring.com/services/` reference remains.
- Every `rel="canonical"` now equals `https://www.nwocflooring.com` + that page's own live path (self-referencing).

`_index.json` lists each page with its replacement count and the resulting canonical.

## Two pages have no canonical tag at all

`hardwood-floor-installation` and `flooring-repair` carry no `<link rel="canonical">` in head code (their stale `/services-near-me/` references were in `og:url` and JSON-LD, now fixed). Their real canonical — if any — is set in Page Settings → SEO → Canonical Tag, which the API does not expose. Worth checking in the Designer.

## Also flagged by the audit, and NOT fixable here

The five city repair pages — Edmonds, Everett, Lynnwood, Mukilteo, Snohomish — were flagged non-canonical too, but they declare no canonical in head code, in any page embed, or in site-wide code (all three were checked exhaustively). Theirs must be set in **Page Settings → SEO → Canonical Tag URL**, which the Webflow API exposes neither for reading nor writing. Open one of those pages in the Designer and check that field: it should either be empty or contain the page's own URL.
