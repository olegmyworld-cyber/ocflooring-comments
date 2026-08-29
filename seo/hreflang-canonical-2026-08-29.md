# Incorrect hreflang links — Semrush, 29 Aug 2026

Semrush reported **15 issues** (12 broken hreflang 404s, 3 hreflang 301s). Tracing them
found the same stale URLs in the **canonical tag** too, which matters far more, and on more
pages than the report listed.

## What is actually wrong

Every affected page carries a hand-written head block. On a service page it reads:

```html
<link rel="canonical" href="https://www.nwocflooring.com/services-near-me/<slug>" />
<link rel="alternate" hreflang="en-US" href="…/services-near-me/<slug>" />
<link rel="alternate" hreflang="en"    href="…/services-near-me/<slug>" />
<link rel="alternate" hreflang="x-default" href="…/services-near-me/<slug>" />
<meta property="og:url" content="…/services-near-me/<slug>" />
…
<script> /* Guardrail */
  var target = 'https://www.nwocflooring.com/services-near-me/<slug>';
  // rewrites canonical, deletes every hreflang link and re-adds all three at the same target
</script>
```

The page's real address is `/flooring-services-near-me/<slug>`. So each page tells Google
its canonical version lives at a URL that returns 404 — and the Guardrail script re-asserts
that at runtime even if the static tags were corrected. **A canonical pointing at a 404 is
the serious problem here; the hreflang errors Semrush flagged are the same bug, reported
under a different check.**

The 3 Arlington rows are the same pattern one step better off: they point at
`/city-of-arlington/…`, which already has a 301 to the live `/arlington/…` page, so they
register as "Hreflang redirect (301)" rather than 404.

**Scope is 20 pages, not 15.** Semrush listed 12 service pages; a sweep of every page's
head custom code via the API found `commercial-flooring-installation`, `flooring-store`,
`hardwood-floor-maintenance` and `insurance-restoration-services` with the same defect, plus
a fourth Arlington page. Already correct and left alone:
`/flooring-services-near-me/vinyl-plank-flooring-and-laminate-flooring`.

## Fixed

`/arlington/hardwood-floor-repair` — its head block had no `<script>`, so the API could
write it. `og:url` now points to `/arlington/hardwood-floor-repair`.

## Not fixable through the API — 19 pages need a manual edit

Webflow's page custom-code endpoint rejects **any** block containing a `<script>` tag with
`HTTP 406`. Verified with a minimal probe: a block of plain `<meta>` tags is accepted, and
the same block plus an inert `<script type="application/ld+json">` is refused. Every one of
these 19 head blocks carries the LocalBusiness/Service JSON-LD and the Guardrail script, so
writing them back is impossible without deleting that markup — which is not worth doing to
fix a URL string.

In the Designer, open each page's **Settings → Custom code → Inside `<head>` tag** and
replace the dead URL with the live one. It appears 5–7 times per page (canonical, three
hreflang, `og:url`, and the Guardrail `target`), so a find-and-replace on the path fragment
catches them all in one pass.

For the 16 service pages, replace `/services-near-me/` with `/flooring-services-near-me/`:

| Page | occurrences |
| --- | --- |
| `/flooring-services-near-me/buff-and-recoat-hardwood-floors` | 7 |
| `/flooring-services-near-me/commercial-flooring-installation` | 7 |
| `/flooring-services-near-me/dustless-floor-sanding` | 6 |
| `/flooring-services-near-me/eco-friendly-floor-refinishing` | 6 |
| `/flooring-services-near-me/engineered-hardwood-flooring` | 7 |
| `/flooring-services-near-me/floor-refinishing` | 7 |
| `/flooring-services-near-me/flooring-store` | 6 |
| `/flooring-services-near-me/hardwood-floor-maintenance` | 6 |
| `/flooring-services-near-me/hardwood-floor-staining` | 7 |
| `/flooring-services-near-me/insurance-restoration-services` | 6 |
| `/flooring-services-near-me/laminate-flooring-installation` | 5 |
| `/flooring-services-near-me/our-products` | 5 |
| `/flooring-services-near-me/solid-hardwood-flooring` | 7 |
| `/flooring-services-near-me/stair-installation-and-remodeling` | 6 |
| `/flooring-services-near-me/unfinished-hardwood-floors` | 7 |
| `/flooring-services-near-me/wood-wall-panels` | 7 |

For the 3 Arlington pages the whole path changes:

| Page | replace | with |
| --- | --- | --- |
| `/arlington/hardwood-floor-installation` | `/city-of-arlington/hardwood-floor-installation-in-arlington-wa` | `/arlington/hardwood-floor-installation` |
| `/arlington/hardwood-floor-refinishing` | `/city-of-arlington/hardwood-floor-refinishing-in-arlington-wa` | `/arlington/hardwood-floor-refinishing` |
| `/arlington/vinyl-plank-flooring-installation` | `/city-of-arlington/vinyl-plank-flooring-installation-in-arlington-wa` | `/arlington/vinyl-plank-flooring-installation` |

Once a page's static tags are right, its Guardrail script becomes a no-op that re-asserts
the correct URL, so it can be left in place.

### Why this was not patched with JavaScript instead

`ocLinkFix` could have been extended to rewrite canonical and hreflang in the DOM. It was
deliberately not: Semrush renders JS and would have gone green, while Google would likely
keep reading the wrong canonical out of the raw HTML. That hides the problem rather than
fixing it. The 301 redirects are the honest interim mitigation — they turn a
canonical-to-404 into a canonical-to-301, which Google follows.

## Also found: 155 dead URLs in structured data on 152 pages

Auditing every page's JSON-LD schema field (all 220 pages) turned up BreadcrumbList entries
pointing at a third dead prefix, `/services/…`:

| Dead URL in schema | pages |
| --- | --- |
| `/services/our-products` | 61 |
| `/services/flooring-repair` | 34 |
| `/services/vinyl-plank-flooring-and-laminate-flooring` | 31 |
| `/services/floor-refinishing` | 29 |

This field *is* API-writable, unlike the head blocks. It was still not rewritten here: the
152 corrected schema objects total 862 KB, and hand-transmitting that much JSON-LD risks
silently corrupting rich-result markup on pages where nothing was wrong. The
`/services/(.*)` wildcard redirect resolves all 155 in one line, which is a far better
trade. If the schema should be corrected properly later, do it from a session that can
script the write rather than retype it.

## Redirects — now more important than they looked

See [`301-redirects-2026-08-29.md`](301-redirects-2026-08-29.md). Two wildcards cover every
dead prefix found across all three reports:

| Old path | Redirect to |
| --- | --- |
| `/services-near-me/(.*)` | `/flooring-services-near-me/%1` |
| `/services/(.*)` | `/flooring-services-near-me/%1` |

Until the 19 head blocks are edited, these are what keep the wrong canonicals resolving to
the right pages.
