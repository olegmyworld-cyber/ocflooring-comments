# OC Flooring Blog — Editorial Calendar & Standing Rules

Cadence: **3 posts per week — automated Mon/Wed/Fri ~7:00 AM Pacific** (Routine
`trig_016wNSjucGgwvifoSmFcP3jD`, one post per run), written in the OC Flooring house
style and created as **draft** CMS items in the Webflow **Blogs** collection
(`65f32565e111adbbb806ce92`, site `6377e8e6a53936b48ef1cad0`). Publishing happens
only after Oleg adds Main Image + Thumbnail.

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
3. **Interlinks (every post):** at least one city `hardwood-floor-refinishing-in-<city>-wa`
   service page + 3–6 related blogs (same topic cluster) + `/contact`. Validate every
   href against live slugs before creating the item.
4. **House style:** `.ocb` component system (Quick-answer card with chips, 3-fact grid,
   comparison tables, green-light/red-flag 2-col, FAQ accordion **with FAQPage JSON-LD**,
   dark-red CTA block, "Related reading" footer, reveal-animation script). Generators
   in `blogs/src/` — reuse `builder.py`.
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

## Published / in progress

| Date | Topic (# from master list) | City | Slug | Webflow item | Status |
|------|---------------------------|------|------|--------------|--------|
| 2026-08-28 | 1. Water-based vs oil-based finish 🔥 | Bellevue | `water-based-vs-oil-based-floor-finish` | `6a92158f27f99832e0f5e272` | Draft — needs images |
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
