# OC Flooring — Webflow fix scripts

Source records for custom code applied to the OC Flooring Webflow site
(`nwocflooring.com`, site id `6377e8e6a53936b48ef1cad0`). These are registered as
inline scripts via the Webflow Scripts API and applied at the site footer.

## Changes on branch `claude/all-oc-flooring-audit-n6ezfd` (2026-08-30)

Full-site audit fixes applied via the Webflow Data API (flooring-calculator page
deliberately left untouched):

1. **Site head custom code** — three targeted edits, everything else unchanged:
   - LocalBusiness schema `sameAs`: `facebook.com/ocflooring` →
     `facebook.com/nwocflooring`; `linkedin.com/company/ocflooring` →
     `linkedin.com/company/oc-flooring` (the previous handles were not the real
     profiles; Instagram was already correct).
   - Removed `debug:true` from the `oaiq` (OpenAI pixel) init.

2. **Page metadata (70 pages, bulk_update_pages)**:
   - 29 static pages: SEO titles shortened to ≤60 chars (mostly the carpet-
     installation city set, several service hubs, about-us, why-were-different).
   - 6 static pages: meta descriptions shortened to ≤165 chars (worst was
     tile-installation-in-bellevue-wa at 211).
   - OG image (`og:image`) set on all 30 tile-installation city pages +
     tile-gallery (`tile-gallery-splash-01.webp`) and on the 5 utility pages
     (401/404/checkout/paypal-checkout/order-confirmation), which had a dead
     `uploads-ssl` default from another Webflow template.
   - CMS templates: `detail_gallery`, `detail_vinyl-gallery`,
     `detail_blog-category`, `detail_sku` were missing SEO title+description —
     added ({{wf name}} binding + static description); `detail_category` got a
     description; `detail_blog` (all blog posts) had OG title/description copy
     OFF — turned on, and a fallback og:image set on all templates.

3. **Internal linking — crawlable "cities we serve" sections**
   ([`webflow-scripts/city-links/`](webflow-scripts/city-links/)): the Semrush
   crawl showed ~101 sitemap-orphaned pages and ~89 one-link pages, almost all
   city landing pages, and Search Console showed tile/carpet city pages getting
   near-zero impressions. The hardwood-installation hub already had a
   server-rendered links pack (`ocsvc2`); the same pattern was added as
   page-footer custom code (static HTML, no JS — crawlable) on:
   - `/flooring-services-near-me/floor-refinishing` → 29 refinishing city pages
   - `/flooring-services-near-me/vinyl-plank-flooring-and-laminate-flooring` → 30 LVP city pages
   - `/flooring-services-near-me/flooring-repair` → 30 repair city pages
   - `/tile-gallery` → 30 tile city pages (no tile hub exists)
   - `/flooring-services-near-me/our-products` (mobile showroom) → 30 carpet
     city pages (no carpet hub exists)

Published to `nwocflooring.com`, `www.nwocflooring.com` and the Webflow
subdomain on 2026-08-30 (owner-approved publish via the Data API).

### Tile + Carpet service hub pages (2026-08-30, same branch)

Neither service had a main hub page (a key reason the tile/carpet city pages
were invisible in search). Created via the Data API:

- `/flooring-services-near-me/tile-installation` (page `6a9453a9cc7f108e72cc420d`)
- `/flooring-services-near-me/carpet-installation` (page `6a9453aa5038df1a06154847`)

Both were created with `duplicateOf` the changelog page (to inherit the
Navbar/Footer components and Page Hero), then the H1 was retitled and the
changelog content section removed via the element API. The full hub content —
price/trust chips, service cards, how-it-works, FAQ, the 30-city links grid,
and CTA — is server-rendered page-footer custom code
([`hub-tile.html`](webflow-scripts/city-links/hub-tile.html),
[`hub-carpet.html`](webflow-scripts/city-links/hub-carpet.html)), in the same
oc2/ocsvc-pack design language used on the hardwood-install hub.
The existing city-links blocks on `/tile-gallery` and
`/flooring-services-near-me/our-products` were updated with a one-line link to
the new hubs (`links-tile.html` / `links-carpet.html` updated in place).

Also set up outside the repo: a weekly Monday self-check Routine (Semrush
audit score, GSC clicks + tile/carpet city-page impressions, GA4 sessions and
generate_lead conversions, latest form submission, new Calendly bookings) that
alerts Oleg only when something needs attention.

Not changed on purpose: the flooring-calculator page (owner's request — kept
as is, including its sitemap exclusion and page-level custom code), live URL
slugs (Arlington/Bothell inconsistencies — renaming indexed URLs would drop
rankings temporarily), and the 24/7 `openingHoursSpecification` in the schema
(business decision).

### Blog hero images: restoration attempted, then reverted (2026-08-30, same branch)

A bulk edit on ~Aug 24 had replaced the hero (`main-image`) and thumbnail on
99 older blog posts with generated "-main.avif" images. At first request the
pre-Aug-24 originals were restored on 78 posts (recovered from each post's own
`post-body` rich text). The owner then preferred the newer images, so all 78
posts were reverted to their Aug-24 "-main.avif" heroes from the saved
pre-change snapshot and re-published — the blogs now look exactly as they did
before today's edits. Mechanics for future reference: CMS image fields are
updated via `update_collection_items` with `cmsLocaleId` (required) and
re-published via `publish_collection_items`; URL-set images get re-ingested
under a new asset-id prefix but keep the original file content/name.

## Changes on branch `claude/oc-flooring-webflow-fixes-amosur`

### Bona sealer widget — "CUSTOMER FAVORITE" badge overlap (2026-06-14)

**Problem:** On mobile, the red `★ CUSTOMER FAVORITE` badge overlaid on the room
image overlapped the `LIVING / KITCHEN` room toggle pills in the Bona tone/sealer
widget (`#oc-tone-steps` / `#bona-tone-widget`).

**Fix:** Merged a badge-overlap guard into the existing `BonaMobileFix`
(`bonamobilefix`) script rather than adding a new one (the site footer was at its
15-script-per-block limit). The guard finds the badge and toggle by their visible
text (robust to the minified widget bundle's class names), measures their live
bounding boxes, and only repositions the badge (nudges it just below the toggle row)
when they actually overlap. Also keeps the badge on one line / slightly smaller on
phones. See [`webflow-scripts/bonamobilefix-1.0.0.js`](webflow-scripts/bonamobilefix-1.0.0.js).

Published live to `nwocflooring.com`, `www.nwocflooring.com`, and the Webflow
subdomain.
