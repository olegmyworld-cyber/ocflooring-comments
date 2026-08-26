# Tile city-pack composition playbook

You are composing the per-city content pack for one or more OC Flooring
tile-installation city pages (nwocflooring.com). The Bellevue master page is the
baseline; your job is a genuinely different-reading page for your city that keeps
every business fact intact.

## Inputs (repo paths, relative to webflow-scripts/tile-rollout/)
- `rewrite-map.json` — role → { el, type, bellevue } : the Bellevue baseline text
  for every rewritable field. Your pack must provide new text for these roles.
- `tile-angles.json` — your city's region name, writing angle, and voice.
- `../carpet-rollout/packs/<city>.json` — the carpet pack: `neighborhoods`
  (use these for chips), `lat`/`lng` (for JSON-LD), and its texts show the city's
  established character (do NOT copy its phrasing).
- `tile-pageids.json` — pageId, folder, tilePath, carpetPath per city.

## Output
Write `packs/<citySlug>.json` (in tile-rollout/) with EXACTLY these keys:

- `citySlug`, `cityName`
- `seoTitle` — ≤ 60-ish chars form: "Tile Installation in <City>, WA | ..." (vary the tail per city)
- `seoDesc` — 140–160 chars, unique phrasing, must include city, a price anchor, waterproofing/flood-test idea, and (425) 595-1079
- `ogTitle`, `ogDesc` — unique variants (not equal to seoTitle/seoDesc)
- `roles` — object mapping EVERY role in rewrite-map.json (except the `chip1..chip16`
  and `carpetLink` roles — see below) to its new text:
  crumb, heroEyebrow, heroLead, statRegion, trustCell, costH2, costP1, costP2,
  costNote, layersLead, whyP1, whyP2, scopeH2, scopeIntro, cardShower, cardFloors,
  cardBacksplash, cardHeated, cardRepair, cardDemo, materialsLead, materialsNote,
  estEyebrow, estIntro, daysLead, workH2, reviewsH2, faqH2, faqQ1..faqQ11,
  faqA1..faqA11, hoodsH2, hoodsOut, guidesH2, ctaH2, ctaLead, ctaFine, footerTag
- `chips` — array of up to 16 neighborhood names for the chip row (use the carpet
  pack's `neighborhoods`; if more than 16, pick the best 16; keep real place names)
- `carpetLinkText` — e.g. "carpet installation in <City>" (the href comes from tile-pageids.json)
- `alts` — object with keys hero, membrane, work1, work2, work3, work4, work5 —
  image alt texts, each mentioning the city naturally, each different from Bellevue's
- `lat`, `lng` — copy from the carpet pack

## Rules

1. **Facts are fixed, phrasing is yours.** These must survive, worded your way:
   $14–$26/sq ft installed; labor from $11/sq ft; tub/shower surround $3,200–$6,800;
   full bathroom $6,500–$14,000; bathroom floor (~45 sq ft) $900–$1,600; kitchen
   backsplash (~30 sq ft) $1,100–$2,200; demo & haul-away from $3.50/sq ft; repair/
   regrout from $8/sq ft; heated floor $11–$16/sq ft installed; bonded waterproofing
   membrane + pre-sloped base + documented 24-hour flood test, photographed, before
   any tile; TCNA / ANSI A118.10; porcelain absorbs <0.5% water; 4–6 working days
   for a bathroom; 24 hours grout cure; 2-year workmanship warranty; since 2013;
   4.7★ · 119 Google reviews; licensed/bonded/insured WA OCFLOFL852KQ;
   (425) 595-1079; company is family-owned and Bellevue-based.
2. **Structural fields keep their function**:
   - `crumb`: "Tile Installation <City> WA" (breadcrumb — keep this exact form).
   - `costH2` and `faqQ1..faqQ11`: keep each question's search intent and city
     mention where Bellevue had one; you may vary word order slightly but these are
     treated as mandated fields in the dedup audit.
   - `heroEyebrow`: "Tile installation · <City>, Washington" form.
   - `estEyebrow`: mention the city + calculator idea; `hoodsH2`: city + neighborhoods
     idea; `guidesH2`: city + tile reading/guides idea; `footerTag`: keep the
     slogan "Crafting beautiful spaces, one floor at a time." then vary the rest,
     keep phone; `trustCell`: 12 years · family owned · Bellevue based — vary
     separators/order, keep facts; `statRegion`: "<region> floors since 2013"
     (region from tile-angles.json, ≤ 30 chars).
   - `reviewsH2`/`workH2`: the three reviews are real Google reviews from Bellevue/
     Eastside clients — do not claim they are from your city. Frame as e.g.
     "What clients around Puget Sound say" / "Recent tile work nearby", varied.
   - `ctaFine`: "Tile installation in <City>, WA · Licensed, bonded & insured ·
     WA Reg # OCFLOFL852KQ · 2-year workmanship warranty" — keep this form, only
     the city changes (mandated field).
   - `hoodsOut`: "Not on the list? ..." idea — within about an hour of <City>,
     ask when you book. Unique phrasing per city. Do NOT include links here (the
     link sentence is separate and fixed).
3. **Uniqueness (the hard requirement).** For every prose field (everything except
   the mandated fields above): no run of 8 consecutive words may match the Bellevue
   baseline or any other city's pack. Different sentence openings, different
   ordering of ideas, different examples. Use your city's angle: neighborhoods,
   housing stock, weather, commute, landmarks. Do not fabricate specific claims
   about jobs in that city ("we tiled 50 homes in X") — speak to the housing stock
   and conditions instead, which is factual and safe.
4. **Length parity.** Keep each field within ~±25% of the Bellevue baseline length
   so the layout stays balanced.
5. **Tone**: same brand voice as the baseline — confident installer talking to a
   homeowner, no marketing fluff, wry but professional. Your city's `voice` from
   tile-angles.json colors it.
6. Plain text only (no HTML, no markdown) in every field. Use · and — and ’ as the
   baseline does. FAQ answers are single paragraphs.
7. `faqA10` (neighborhoods question) must name your city's real neighborhoods/areas
   (from chips) and nearby cities we also serve.

Validate your JSON parses before finishing (python3 -c "import json;json.load(open(...))").
