# OC Flooring Blog — Editorial Calendar & Standing Rules

Cadence: **5 posts per week — automated Mon–Fri ~7:00 AM Pacific**
(Routine `trig_01Vufv9d8qercegMJCdceAJT`, bound to the main working session).

> **Routine architecture note (2026-08-31):** the original fresh-session routines
> (`trig_016wNSjucGgwvifoSmFcP3jD` publish, `trig_01GE3NPZkGv6JdtdrEueGC4z` backfill)
> ran without Webflow access — fired sessions got no MCP connectors even after
> attaching the connector in the routines UI — so their runs "succeeded" while
> writing nothing. Both were deleted and replaced by one routine that fires into
> the main session (which holds the Webflow MCP) and also does the daily
> body-sync repair. First scheduled fire: 2026-09-01 14:02 UTC.

> **City-page → blog links (2026-08-31):** every one of the 86 city service pages
> (28 refinishing + 29 tile + 29 carpet) now carries the `ocSvcGuides` footer
> script (`webflow-scripts/ocsvcguides-1.0.0.js`, registered + applied via API,
> site published). It reads the page's service + city from the URL and injects up
> to 5 links to blog posts from the 164-post map embedded in it — own-city posts
> first, then newest same-service posts. **Date-gated**: a post is only linked
> once its publish_date is strictly before today (America/Los_Angeles), so it can
> never link a draft. The section grows automatically as the schedule publishes.
> When adding future posts, regenerate the script's map and bump its version.

**All 100 posts are written.** They exist as **draft** CMS items in the Webflow
**Blogs** collection (`65f32565e111adbbb806ce92`, site `6377e8e6a53936b48ef1cad0`),
each pre-dated to its scheduled slot in `blogs/plan/PLAN.json`
(2026-08-31 → 2027-04-12).

The routine is now in **PUBLISH mode**, not write mode. Each run it:
1. finds the earliest post that is due and not yet in `blogs/PUBLISHED.json`;
2. **image gate** — if that post has no Main Image, it publishes NOTHING and notifies
   Oleg (the queue waits rather than skipping ahead);
3. otherwise sets `isDraft: false`, publishes that one item, records it in
   `blogs/PUBLISHED.json`, and pushes.

Oleg's only recurring task: add **Main Image + Thumbnail** to upcoming drafts in
Webflow CMS → Blogs, working down the queue in date order.

## Standing rules (set by Oleg, 2026-08-28)

1. **City accent rule: 75% of all blogs must be about one of the priority cities**
   (city in title, intro, local section, and links to that city's service page where
   one exists). At 3 posts/week that means at least 2 city posts every week, and
   3/3 most weeks. At most ~1 in 4 posts may be general/topic-only.
2. **Priority cities** — from GSC refinishing-query data (90 days ending 2026-08-28),
   ordered by opportunity:
   | # | City | Impressions | Avg position | Notes |
   |---|------|-------------|--------------|-------|
   | 1 | Seattle | ~2,250 | 26–50 ❌ | Biggest gap — needs content |
   | 2 | Bellevue | ~854 | 16–18 | **No refinishing service page exists** — page gap |
   | 3 | Everett | ~656 | 26–54 ❌ | Needs content |
   | 4 | Sammamish | ~470 | 15–27 | |
   | 5 | Redmond | ~458 | 13–22 | |
   | 6 | Mercer Island | ~418 | 9.3 ✅ | Defend |
   | 7 | Edmonds | ~411 | 23–26 | |
   | 8 | Lynnwood | ~381 | 19–26 | |
   | 9 | Kirkland | ~365 | 8.5 ✅ | Defend |
   | 10 | Renton | ~324 | 4.8 ✅ | Defend |
3. **Interlinks (every post — Oleg's rule, 2026-08-29):** the post's OWN city
   `hardwood-floor-refinishing-in-<city>-wa` service page is mandatory (Bellevue has no
   refinishing page — link Seattle or Kirkland instead; general posts link ≥1 city page),
   PLUS **at least 4 links to other blog posts** (4–6 target, same topic cluster),
   PLUS `/contact`. Validate every href against live slugs before creating the item.
4. **House style:** `.ocb` component system (Quick-answer card with chips, 3-fact grid,
   comparison tables, green-light/red-flag 2-col, FAQ accordion **with FAQPage JSON-LD**,
   dark-red CTA block, "Related reading" footer, reveal-animation script), plus a
   **green published-date pill** (`date_badge()`, #16a34a) as the first visible element
   of every post — set it to the actual publish date, and refresh it if a draft
   publishes on a later day. The **post-summary must also start with the publish
   date** (`August 28, 2026 · …`) so the date shows on the blog-grid cards.
   (All 109 pre-existing posts were backfilled with their original creation dates
   on 2026-08-29.) Generators in `blogs/src/` — reuse `builder.py`.
5. **Consistent facts:** $1.99/sq ft screen & recoat · $3.99 natural refinish ·
   $6.50 stain refinish · stairs $55–$75/tread · 500 sq ft minimum · dust containment
   +$250 · washer/dryer pair +$160, other appliances +$80 · new-install labor $3–$4.25/sq ft ·
   Bona & Pallmann waterborne systems · since 2013, 1,000+ floors, 1-yr warranty,
   licensed & insured, financing · (425) 595-1079 · King & Snohomish County.
6. **SEO/AI-search:** title-tag ≤ 60 chars, meta-description ≤ 160, quotable
   Quick-answer opening (answer in the first sentence), FAQPage schema, post-summary
   2–3 sentences for the grid.
7. **Workflow:** create items as **drafts** → Oleg adds Main Image + Thumbnail →
   publish. Keep slugs stable once other posts link to them.
8. **Inbound links from indexed pages (Oleg's rule, 2026-08-29):** a new post has to be
   *reachable* from pages Google already has, or it sits uncrawled. So every target page
   carries **≥4 inbound links from already-indexed pages**:
   - **City service pages** — all 28 `hardwood-floor-refinishing-in-<city>-wa` pages now
     have ≥4 inbound links from the 109 indexed posts; the 9 GSC-priority cities have ≥6.
     Balance lives in each post's `city-links` field. Re-check after any bulk edit.
   - **New blog posts** — `blogs/plan/INBOUND-PLAN.json` assigns each of the 100 new posts
     4 relevance-matched donor posts drawn from the 109 indexed ones (each donor gives
     out at most 4 links). The publish routine adds those links **at publish time only**
     via `blogs/plan/add_inbound.py` — linking to a draft would serve a 404. The links go
     into the donor's `city-links` field under a "More floor-care guides" list marked
     `data-oc-guides="1"`; donor bodies are never touched and no existing link is removed.
   Verified city-page URL paths are in `blogs/plan/URL-MAP.json` → `CITY_PATH_ALL`.
9. **Tags the Webflow Editor deletes (learned the hard way, 2026-08-29):** saving a
   post in the Editor — which is how a Main Image gets added — re-runs the rich-text
   sanitizer over `post-body` and **silently deletes every `<section>` and every
   inline `<svg>`**. Losing `<section>` takes the `.ocb`, `.ocb-cta` and `.faq-wrap`
   wrapper classes with it, and the site's own `html body .post-body h2/p/a
   {...!important}` rules in the Blogs Template head then win — the CTA turns
   dark-on-dark and the FAQ loses its card. So: **never use `<section>` or inline
   `<svg>` in a post body.** `builder.py` emits `<div>` and draws the chip icons from
   CSS (`.ocb-ic-*`, data-URI backgrounds in `shared_css.html`). The `ocbguard`
   page script on the Blogs Template is the safety net — it re-adds the wrapper
   classes and forces the CTA colors for any post that was sanitized anyway.
   Three do **not** follow the `city-of-<slug>/` pattern: Seattle (`/seattle/…`),
   Newcastle (`/city-of-new-castle/…`) and Bothell (`/hardwood-floor-refinishing/…`).

## Tile & carpet series (added 2026-08-30)

One post per weekday now: **Mon/Wed/Fri refinishing · Tue tile · Thu carpet**,
all at 7 AM Pacific through 2027-04-12. 32 tile + 32 carpet posts, Semrush-anchored
keywords, cities weighted by population (86% city-accented). Plan of record:
`blogs/plan/TILE-CARPET-PLAN.json`; facts sheet `blogs/plan/TILE-CARPET-FACTS.md`;
validator `blogs/plan/tc_validate.py`; writer spec `blogs/plan/TC-AGENT-BRIEF.md`.
Categories: Tile & Backsplash (`6a948233e243f74e3fbca239`), Carpet & Stairs
(`6a948233e243f74e3fbca23b`) — each category page is an indexable hub listing its posts.
The publish routine (cron `0 14 * * 1-5`) reads the unified 164-post queue in
`blogs/plan/INBOUND-PLAN.json`, publishes the earliest due post, syncs the body from
the repo, and adds 4 inbound links from the assigned donors at publish time.

## Published / in progress

| Date | Topic (# from master list) | City | Slug | Webflow item | Status |
|------|---------------------------|------|------|--------------|--------|
| 2026-08-28 | 1. Water-based vs oil-based finish 🔥 | Bellevue | `water-based-vs-oil-based-floor-finish` | `6a92158f27f99832e0f5e272` | **Published 2026-08-28** — images still to add |
| 2026-08-28 | 2. Low-VOC finishes, kids & pets 🔥 | Everett | `low-voc-hardwood-floor-finishes-kids-pets` | `6a92161235db8207e7addc49` | Draft — needs images |
| 2026-08-28 | 26. Refinishing fir floors 🔥 | Seattle | `refinishing-fir-floors-old-seattle-homes` | `6a921686d10d54b94afab8a3` | Draft — needs images |

## Upcoming schedule (3/week; ≥75% city-accented)

- **Week 2:** 5. Bona Traffic HD vs Pallmann 🔥 (Kirkland) · 62. Sandless refinishing 🔥 (Renton) · 67. Engineered hardwood wear layer 🔥 (Sammamish)
- **Week 3:** 77. Mercer Island waterfront refinish 🔥 (Mercer Island) · 38. How long before you can walk on floors 🔥 (Redmond) · 11. Faded, sun-damaged floors 🔥 (Edmonds — angle it "restore", distinct from existing sun-damaged post)
- **Week 4:** 92. Gymnasium refinishing 🔥 (Seattle) · 55. Stair refinishing pricing 🔥 (Bellevue) · 3. Matte, satin or semi-gloss (general slot)
- **Week 5:** 75. 1920s Seattle bungalow (Seattle) · 50. $2/sqft vs $6 quotes (Lynnwood) · 65. Refinishing vs cleaning services 🔥 (Everett)
- **Week 6:** 81. Condo refinishing, HOA & noise (Bellevue) · 30. Douglas fir vs oak in a Craftsman (Seattle) · 17. Deep vs surface scratches (general slot)
- **Week 7:** 82. Refinish before listing (Kirkland) · 72. Best time of year in Western WA (Everett) · 21. Pet scratches: repair, recoat, refinish (Renton)
- **Week 8:** 84. Fix-and-flip flooring, King County (Renton) · 63. Buff & coat vs full sand (Sammamish) · 44. Occupied-home room-by-room scheduling (Redmond)
- Weeks 9+: continue the master list below, assigning cities by the priority table
  (rotate; revisit GSC quarterly). Avoid duplicating existing posts — check
  live slugs first (109 posts as of 2026-08-28; notable overlaps: sun-damaged floors,
  how-many-times-sanded, screen-and-recoat comparison, staining posts, dust-free posts).

## Master topic list (from Oleg, 2026-08-28)

Finishes & products: 1 🔥, 2 🔥, 3, 4, 5 🔥, 6, 7, 8, 9, 10
Problems & diagnosis: 11 🔥, 12–25
Species & floor types: 26 🔥, 27, 28 🔥, 29–37
Process & expectations: 38 🔥, 39–49
Cost angles: 50–61 (55 🔥)
Comparisons: 62 🔥, 63–66 (65 🔥), 67 🔥, 68–71
Seasonal, PNW & local: 72–81 (77 🔥)
Real estate & investors: 82–91
Commercial: 92 🔥, 93–96
Maintenance: 97–100

(Full titles are in the original request; keep numbering when logging above.)

## Images

Each post needs **Main Image** (~1600×900) and **Thumbnail image** (~800×450) —
AVIF/WebP preferred, named `<slug>-main.avif` / `<slug>-thumbnail.avif`.
Upload in Webflow: **CMS → Blogs → (item) → Main Image / Thumbnail image**, or send
files/URLs to Claude to attach via the API before publishing.
