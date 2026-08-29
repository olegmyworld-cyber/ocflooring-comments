# Invalid structured data fix — nwocflooring.com — 2026-08-29

Source: Semrush Site Audit, "30 structured data items are invalid" (crawled 2026-08-28 20:03 UTC).
Reported error, on all 30 rows: **Local Business → `address` → "A value for the address field is required."**

All 30 flagged URLs are the `hardwood-floor-installation-in-<city>-wa` city pages.

## Root cause

Each of these pages renders a customer-reviews section (the `oc-ocf-reviews` HTML embed, the 4th of 8 embeds on the page). At the end of that section sits a `LocalBusiness` JSON-LD block carrying only:

```
@context, @type, name, telephone, areaServed, review
```

Google requires `address` on `LocalBusiness` — and this block also carries `review` markup, which makes a missing business address more serious, since review rich results are attached to a business that is not properly identified.

There *was* an `address` in the block, but nested **inside `areaServed`** — that describes the *city being served*, not the business's location, so it does not satisfy the requirement. The page-level JSON-LD (Service / WebPage / BreadcrumbList) contained no LocalBusiness at all, which is why the fix had to go into the embed.

## Fix applied

Inserted the company's real postal address — taken from the canonical `#ocflooring` LocalBusiness already defined on the homepage — into the `LocalBusiness` object on all 30 pages:

```json
"address": {
  "@type": "PostalAddress",
  "streetAddress": "13343 NE Bel Red Rd #210",
  "addressLocality": "Bellevue",
  "addressRegion": "WA",
  "postalCode": "98005",
  "addressCountry": "US"
}
```

Applied by exact single-occurrence string substitution inside each embed, so nothing else in the reviews section (CSS, markup, review text) changed. Resulting key order: `@context, @type, name, telephone, address, areaServed, review`.

## Second defect fixed in the same pass

Every one of the 30 pages had a `BreadcrumbList` whose item URL pointed at:

`https://www.nwocflooring.com/services/hardwood-floor-installation`

That URL 404s since the services section was renamed — a dead link living inside the structured data, same root cause as the 308 broken internal links fixed earlier the same day. Replaced on all 30 pages with:

`https://www.nwocflooring.com/flooring-services-near-me/hardwood-floor-installation`

## Verification

- All 30 page schemas re-fetched: **0** still contain the old `/services/` URL; **30** contain the new one.
- Byte-level check: each page's schema differs from its pre-fix version by **only** that URL — nothing else was altered.
- 7 embeds re-read and independently parsed: the address appears exactly once, the JSON-LD parses, and each page's `areaServed` city matches its own URL.
- Template-integrity check: embeds normalized by city name are byte-identical across pages, confirming no page-specific review copy was overwritten during the edits.
- Site published to `www.nwocflooring.com`, `nwocflooring.com` and the Webflow staging subdomain.

## Notes and recommendations

- Live HTML could not be fetched to confirm rendered output — this session's egress policy returns 403 for the domain. Re-run the Semrush audit (or Google's Rich Results Test) to confirm the error count drops to zero.
- **Worth considering:** these 30 pages each declare their own standalone `LocalBusiness` with the same name, phone and now the same address, but no `@id`. Google may read them as 30 separate business entities. Adding `"@id": "https://www.nwocflooring.com/#ocflooring"` to each block would merge them into the single canonical business defined on the homepage, which is the cleaner modelling. Not done here because it changes entity semantics beyond the reported error — worth a decision.
- The same three canned reviews appear on all 30 city pages. That is legal markup, but review snippets duplicated verbatim across a site are a known target for Google's spam filtering; genuinely per-city reviews would be safer.
- Machine-readable detail: `structured-data-fix-2026-08-29.json`.
