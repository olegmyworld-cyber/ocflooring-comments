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
- `redirects-existing-2026-09-08.csv` — the 187 rules live in Webflow on 2026-09-08 (export). Already covers all 174.

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

## Done 2026-09-08: product index on Our Products (staged in Webflow, needs publish)

The page's product grid is a Collection List capped at Webflow's 100-item limit, so 91 of 191 products
were linked from nowhere. Added below the grid's CTA buttons: an "All Flooring Products A–Z" block with
two Collection Lists (Products sorted by name; items 1–100 and 101–191), one text link per product bound
to the product name and its product page. Classes: `oc-product-index`, `oc-product-index-list` (3 / 2 / 1
columns by breakpoint), `oc-product-index-link`. The grid's filter buttons only touch `.link-item-product`
cards, so the index is unaffected by them. Not published; publish together with the merged redirects.

## Redirects: nothing to import (checked 2026-09-08 against the live list)

`redirects-existing-2026-09-08.csv` is the export of the 187 rules already live in Webflow. Every one of
the 174 dead URLs in `redirects-2026-09-08.csv` is already covered: 107 with the same target, 67 with a
different one (laminate city pages go to each city's vinyl-plank page, not the main laminate page; a few
old blog slugs go to a specific replacement post). All 187 targets resolve to live pages and none chain.
The live rules stay as they are. Do NOT import anything; Webflow's import replaces the whole list.

Consequence for GSC: "Page with redirect" (104) is the correct, permanent state for those URLs and will
never validate as "fixed". The 36 "Not found (404)" URLs are not in search-analytics data (zero
impressions) and could not be identified from here; the URL-level export of that GSC row is needed.

## Done 2026-09-08 (later): titles and structured data (staged, needs publish)

Titles: main hardwood-installation page shortened to 60 chars; Lake Stevens and Cottage Lake
hardwood-installation pages got "| OC Flooring" appended so the SEO title no longer equals the H1.

Structured data inventory (Webflow page-settings JSON-LD, 216 static pages): 181 already had it
(every city page: FlooringContractor/Service + Breadcrumb, most with FAQ). Semrush's "schema on 0 pages"
was wrong. Added Service + BreadcrumbList to 15 top-level service pages, WebPage/AboutPage/ContactPage/
CollectionPage + Breadcrumb to our-products, hardwood-floor-maintenance, flooring-store, financing,
about-us, contact, reviews, our-work, why-were-different, blog. Corrected flooring-repair and
vinyl-plank pages, whose blocks still used /services/ URLs. All new blocks reference the homepage
LocalBusiness entity (#ocflooring) as provider/about.

Left alone, flagged:
- ~150 city pages have a breadcrumb item pointing at /services/our-products or another retired
  /services/ URL. Those 301 to the right page, so nothing breaks; rewriting 150 blocks is cosmetic.
- Homepage LocalBusiness says open 24/7; the Contact page says Mon–Fri 9am–5pm. Oleg: leave as is (2026-09-08).
- Homepage carries a self-declared aggregateRating (4.7, 103). Google only honours that when the
  reviews are visible on the page; the reviews section makes that defensible, but it is a judgment call.

## Backlinks: disavow filed 2026-09-07 19:34 PT

`disavow-2026-09-08.txt` (71 domains) uploaded to Search Console for https://www.nwocflooring.com/.
Two spam families: a "Buy Backlinks / PBN" ad network using the domain as bait (35 domains, since 2026-06-30,
still growing) and a "Where to buy aged domains" scraper network (32 domains, since 2025-05). Kova confirmed
they built no links. Directories (superpages, dexknows, yellowpages, prosource.app) deliberately not disavowed.
Monthly: re-export Semrush backlinks, append new spam domains, re-upload; check GSC Manual Actions.
Also upload to the non-www property if it is verified.

## Partner links, 2026-09-08 (live)

One link each way between the two sites, brand-name anchors, no ownership disclosed (owner's decision):
- olegsonsremodeling.com/services → "OC Flooring" → /flooring-services-near-me/floor-refinishing
- nwocflooring.com/flooring-services-near-me/commercial-flooring-installation → "Oleg & Sons Remodeling" → olegsonsremodeling.com
Do not add more cross-links between the sites. Expected effect: Authority Score 9 → ~10, no ranking change.

## Review star snippets (aggregateRating), 2026-09-08 (published)

Owner's call after the self-serving-review warning: use the real Google Business Profile figures, 4.7 / 99.
Google may still refuse to render stars for a business's own rating; nothing here fabricates or inflates.

Markup (business node `#ocflooring` carries `aggregateRating` 4.7 / 99 / best 5 / worst 1):
- Homepage: count corrected from 103 to 99.
- Main refinishing page /flooring-services-near-me/floor-refinishing: LocalBusiness + rating + Service + Breadcrumb.
- 29 city refinishing pages (`city-refinishing-schema-2026-09-08.json`): LocalBusiness stub + rating + Service
  node added in front of the existing FAQPage + BreadcrumbList; breadcrumb level 2 repointed from the retired
  /services/floor-refinishing to /flooring-services-near-me/floor-refinishing.
- Installation, vinyl, repair, carpet, tile pages: deliberately no rating (no visible reviews there).

Visible reviews (the condition Google sets): the trust-reviews injector now also fires on the main refinishing
page and on /arlington/hardwood-floor-refinishing, whose slug did not match the city pattern. The old registered
script `octrustreviewsinjector9d` returned 404 on update, so `octrustreviewsinjector10` (same code, wider
guard) was registered, applied in the footer, and the old one removed. Webflow caps applied scripts at 15;
the site is at 15 again.

Consistency pass (every on-site claim now says 99 reviews / 4.7 stars): commercial page "Why choose" copy;
About, Reviews, Our Work SEO + schema descriptions; Reviews SEO title; 14 city-page SEO descriptions and
Service descriptions that still said "103 5-star reviews".

Watch: GSC Enhancements → Review snippets (errors) and Manual Actions, ~2 weeks after publish. When the GBP
count changes, update the number in one place first: the homepage schema, then the city JSON.

## Page weight / Core Web Vitals, 2026-09-08 (published)

PageSpeed Insights on the homepage (Sep 7): real-user (CrUX) data = "No Data", so Core Web Vitals cannot affect
ranking for this site today; lab scores 43 mobile / 66 desktop, page weight 5.6-7.6 MB, image savings ~1.1-1.4 MB,
unused JS 674 KB, blocking time 800-1,160 ms. Hero is already AVIF (181 KB).

Done (owner-approved):
- OpenAI Ads pixel removed from site <head> (saved in webflow-scripts/removed-head-openai-pixel.html).
- Webflow in-place conversion of the 28 JPG/PNG assets >= 150 KB (same asset ids, files replaced):
    18 -> AVIF   9.68 MB -> 0.98 MB   (phone photos, blog images, recent stock uploads)
     3 -> WebP   3.22 MB -> 2.06 MB   (Shutterstock originals too large for the AVIF encoder)
     7 unchanged 3.68 MB              (5,700-8,200 px Shutterstock "-min" JPGs; WebP came out larger)
  Webflow's AVIF encoder stalls on originals above ~4,000 px; a batch containing one such file hangs the whole
  batch and the task reports "failed" at 15 min even though smaller files in it did convert. Keep giants out
  of AVIF batches. 121 JPG/PNG under 150 KB (3.35 MB total) not touched.
- Unchanged giants (asset id, px, KB): 6742a254 8192px 501; 674525d0 7360px 337; 673d4c77 6720px 281;
  673d4aea 6468px 408; 6742ba01 6454px 959; 6742bacf 5753px 523; 66940275 (IMG_8530) 4032px 672.
  Real fix = resize to <= 2,000 px and re-upload, which creates a new asset id and needs every usage re-pointed.
Not done: duplicate Google tag (GTM + separate gtag) - owner to confirm GA4 is inside GTM; script consolidation
(15 registered + 9 inline footer scripts) - not worth the risk without a live test.
Next: re-run PageSpeed on the homepage a day after publish and compare page weight; expect ~1-1.5 MB less.

## Blog grid sort, 2026-09-08 (published)

Symptom: /blog cards showed dates out of order. Cause: the green date badge is not a CMS date. The page script
`ocblogdates` (page-level, blog page only) parses a hand-typed "Month D, YYYY ·" prefix at the start of each
post's Post Summary and renders it as a badge; the collection list was sorting by created-on, which has no
relation to that typed date (old posts were rewritten in Aug/Sep 2026 and given new typed dates).

Fix: new DateTime field "Publish Date" (slug publish-date, id b5a0997cce310cf82a2c0b73e223710f) on the Blogs
collection, seeded on all 273 items from the typed prefix (119 live, 154 scheduled drafts dated Sep 2026 to
Apr 2027). Blog page collection list (element 3d83953f-...-106823d37d9b) now sorts publish-date descending.

Going forward, a new post needs BOTH the typed "Month D, YYYY ·" prefix in Post Summary (what the badge shows)
and the Publish Date field (what the grid sorts by). If they disagree, the grid order will look wrong again.
Cleaner long-term: bind a real date element in the card to publish-date and drop the prefix + script.

API notes: update_collection_items caps at 100 items per call (101 is rejected whole); list_collection_items
pages overlap unless a sort is given (use sortBy slug); no built-in date can be used as a list sort field.

## Blog city buttons -> wrong service page, 2026-09-08 (root cause found, hardened, published)

Owner report: on /blog/tile-installation-cost-per-square-foot the button "Tile Installation in Seattle, WA"
opened the hardwood-installation Seattle page; Bellevue/Redmond/Kirkland worked. "Same problem as before."

Audit (all 273 posts, deterministic + 4 adversarial agents): every one of the 1,157 city-links buttons and 988
in-body internal links has text service+city == href, every href is a live page whose title matches, and the
blog-template link scripts (OCLinkMatch / OCLinkClick, added 09-06/07 as a band-aid) compute the same target as the
href, so they never rewrite these buttons. The Seattle tile page is a genuine tile page (H1 "Waterproofed first.
Tiled second."), no duplicate slug, no redirect rule.

Root cause (GA4-confirmed): the /404 page's page-level "fallback redirect" script guesses a page from URL keywords
and location.replace()s. Its cls() had no tile/carpet branch until 2026-09-06 20:49Z, so while the tile city page
was returning 404 the script classified "tile-installation-in-seattle-wa" by the word "installation" and sent
visitors to /seattle/hardwood-floor-installation-in-seattle-wa. GA4: 6 such landings with the bathroom-tile post
as referrer on 09-06, one at 09-07 10:17 PT, then 09-07 10:18 PT the same click reached the tile page; none since.
GA4 has no 09-08 data yet; if the owner still sees it today it is a cached copy in his browser (test in incognito).

Hardening (published): target() now sends a missing canonical <service>-in-<city>-wa URL to that SERVICE's main
page under /flooring-services-near-me/ and never to a different service; legacy remaps unchanged. Details and
node checks in webflow-scripts/404-fallback-redirects-2026-09-08.md.

Follow-up (not done): oc-area-links-v1-min.js ("Explore More Flooring Services" block on city service pages) has
no tile or carpet entries, so it never links to the 66 new tile/carpet city pages; the two text-driven link
rewriters on the blog template are band-aids that can be removed once nobody edits links by hand.
