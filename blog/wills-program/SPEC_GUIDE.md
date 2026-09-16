# Wills Flooring blog program: spec-writing guide

Each blog post is a JSON spec in `specs/NNN-<slug>.json`. `render.py` turns it into the Apple-style
Webflow rich-text body and a CMS manifest. Writers only write specs; never hand-write HTML embeds.

Validate every spec you write:

```
python3 blog/wills-program/render.py blog/wills-program/specs/NNN-*.json
```

It must print one line per spec (`<slug>: N embeds, max <n>, total <n>, words ~<n>`) with no traceback.
Target `words` between 1,150 and 1,700.

## Brand facts (use only these; never invent others)

- Company: **Wills Flooring**, mobile flooring showroom, Lynnwood WA. Showroom at 2109 196th St SW #106, Lynnwood, WA 98036. Phone (425) 350-4435. Since 2013. Licensed and insured. 1-year workmanship warranty. Bona Certified Craftsmen (refinishing). 4.8 stars, 100+ five-star Google reviews. Metropolitan Hardwood distributor (hardwood). Serves Snohomish and King County. Free in-home estimates: they bring samples to the house, measure, check subfloor, give a firm written quote on the spot.
- The renderer automatically adds: the FAQ accordion, JSON-LD schema, the navy CTA, a closing paragraph with links to the service page, city page, price list and `related` posts, and the reveal animation. Do not write those in blocks.

## Published prices (Wills Flooring price list; the only numbers you may state as Wills prices)

| Service | Rate | Notes |
|---|---|---|
| Sand and refinish, natural (3 coats Bona water-based) | $3.99 / sq ft | 500 sq ft minimum |
| Sand, stain and finish | $6.50 / sq ft | 500 sq ft minimum |
| Screen and recoat | $1.99 / sq ft | 500 sq ft minimum, only if old finish is intact |
| Refinish stairs | $55–$75 per tread | |
| Dust containment | +$250 | plastic sealing + air scrubber; sanders are already vacuum-connected |
| Move washer and dryer | +$160 per pair | |
| Other appliances | +$80 each | |
| Hardwood installation, engineered or solid | $3.25 / sq ft | installation labor; material quoted separately; 500 sq ft min |
| Hardwood installation, unfinished (site-finished) | $2.75 / sq ft | plus refinishing rates for sanding/finishing; 500 sq ft min |
| Hardwood on stairs | $125 per stair | |
| Laminate installation | $2.50 / sq ft | labor; 500 sq ft min; $100 per stair |
| Vinyl plank (LVP) installation | $2.50 / sq ft | labor; 500 sq ft min; stairs $100 per stair |
| Carpet installation | **not published** | never state a Wills carpet price or "from $X" |

Rules: refinishing prices are all-in (labor + finish). Installation prices are labor; material, underlayment,
old-floor removal and subfloor prep are "quoted at the free estimate". For carpet posts, talk about what
drives price, fiber and pad tiers, and comparisons, but never a Wills dollar figure. Industry-wide ranges are
allowed only if clearly labeled as national/regional averages, not Wills prices, and used sparingly.

## Voice and content rules

- Question-led. The title is a real question people ask Google, Reddit or ChatGPT. The first block is a
  `quick` block that answers it in one bold sentence, then explains.
- Plain, direct, specific. Short paragraphs. No fluff, no "in today's world", no "look no further".
  Contractions are fine. Sound like an experienced flooring contractor explaining to a neighbor.
- Every post must be distinct. Do not reuse whole sections between posts. Different questions get
  different structures, examples and FAQs. Only the calculator repeats.
- City angle: every spec has a `city`. Weave it in naturally 4–8 times: neighborhood names, home eras,
  climate/moisture, commute to the Lynnwood showroom, condo/HOA realities, local buyer expectations. Never
  paste a generic "we serve X" paragraph; the renderer adds the service-area line.
- Use `<strong>`, `<em>` and `<a href="...">` inside text; no other HTML. Internal links allowed:
  `/services/floor-refinish`, `/services/hardwood-flooring`, `/services/lvp-vinyl-flooring`,
  `/services/carpet-installation`, `/services/laminate-flooring-installation`, `/flooring-installation-cost`,
  `/contact`, `/blog-posts/<slug of another post in plan.json>`. Use 1–3 inline internal links per post.
- Numbers: show the math when you quote a job example (e.g. `900 × $3.99 + 13 × $55 = $4,306`). Always
  respect the 500 sq ft minimum in examples.
- Write `&amp;` for ampersands inside text values. Escape double quotes inside JSON strings.
- Do not mention competitors by name. Do not mention Reddit users or quote them; you may say "a common
  Reddit thread asks..." and answer it.
- No em dashes in text. Use commas, periods or colons.

### City notes

- **Seattle**: Ballard, Wallingford, Green Lake, Capitol Hill, Queen Anne, West Seattle, Magnolia, Beacon Hill. 1900s–1950s Craftsman, Tudor and bungalows with old-growth fir or oak; condos with elevator/quiet-hour rules; parking permits; tight staircases; higher resale expectations.
- **Everett**: Riverside and Bayside 1900s–1920s homes, Silver Lake and Eastmont 1990s–2000s builder-grade oak, Boeing commuters, Port Gardner condos, about 15 minutes from the Lynnwood showroom.
- **Lynnwood**: home of the showroom (196th St SW); Alderwood, Meadowdale, Martha Lake, 1960s–80s ramblers and split-levels, lots of oak under carpet, light rail growth, townhomes.
- **Kirkland**: Juanita, Houghton, Totem Lake, Rose Hill, Finn Hill, Bridle Trails; lakefront and 1970s–90s homes, Eastside remodel budgets, tech buyers, high resale standards.
- **Edmonds**: the Bowl, Seaview, Perrinville, Westgate, Esperance; 1950s–70s ramblers, waterfront humidity, ferry-town character, retirees downsizing, older homes near downtown.
- **Sammamish**: Pine Lake, Beaver Lake, Klahanie, Trossachs, Sahalee; 1990s–2010s large plateau homes with builder oak, big families, dogs, open-plan main floors, HOA aesthetics.
- **Snohomish**: historic downtown Victorians and farmhouses, acreage, Blackmans Lake, Fobes Hill, Clearview; crawlspaces, mud and dogs, well water, wood stoves, DIY-minded owners.

## Spec format

```json
{
 "slug": "must match plan.json exactly",
 "title": "must match plan.json exactly",
 "meta": "150–158 chars. Answer + hook + Wills Flooring. Include the city and the main keyword.",
 "category": "refinish | hardwood | lvp | carpet",
 "city": "Seattle | Everett | Lynnwood | Kirkland | Edmonds | Sammamish | Snohomish",
 "time": "8 mins",
 "date": "copy from plan.json",
 "keywords": "4–6 comma-separated search phrases people type",
 "offers": [["Sand and refinish, natural finish", "3.99", "per square foot"]],   // only priced services; omit for carpet
 "blocks": [ ... ],
 "faq": [{"q": "...", "a": "..."}],           // 5–7 items, 35–70 words each, direct answers, no HTML
 "faq_title": "...", "faq_sub": "...",
 "related": [["slug-from-plan", "anchor text"], ["slug-from-plan", "anchor text"]],   // 2–3, prefer same category
 "cta_title": "...", "cta_sub": "..."
}
```

`offers` names for priced services: refinish → the three refinishing rates; hardwood → "Hardwood floor installation, engineered or solid" 3.25 and "Unfinished hardwood installation" 2.75; lvp → "Vinyl plank flooring installation" 2.50.

## Block types (use 6–10 blocks between the `quick` block and the end; exactly one `calc` or `estimator`)

Icons available: dollar, clock, ruler, shield, home, factory, layers, leaf, palette, refresh, calendar, wind, washer, plug, stairs, vent, scissors, frame, clipboard, hammer, droplet, brush, done, paw, snow, sun, flame, award, lock, pin, sparkle, water, search, truck, box, baby, sofa, thermo, tag, chart, grid, moon, volume, key, phone, star, x, alert, wallet, tree, mop, dog, basement, moisture, ruler2.

```json
{"type":"quick","eyebrow":"Short answer","lead":"One bold sentence that answers the title.","detail":"Two sentences of context.","tiles":[{"icon":"dollar","label":"Label","value":"$3.99 / sq ft"}, ... exactly 4 tiles ...],"cta":"Try the calculator"}
```
Use `"cta": false` when the post has an `estimator` instead of a `calc`, or set `"cta":"Scope your project"`.

```json
{"type":"h2","text":"Section heading"}
{"type":"h3","text":"Sub heading"}
{"type":"p","html":"Paragraph with optional <strong>, <em>, <a href=\"/contact\">links</a>."}
{"type":"ul","items":["plain list item","another"]}
{"type":"cards","cols":2,"panel":false,"note":"optional small note","items":[{"icon":"layers","tag":"optional tag","num":"optional big number like 3–4 days","title":"Card title","text":"40–70 words.","gold":false}]}
{"type":"prices","note":"...","items":[{"icon":"brush","tag":"When it applies","price":"$3.99","unit":"/ sq ft","title":"Sand and refinish","text":"...","gold":true}]}
{"type":"table","head":["Col","Col","Col"],"rows":[["a","b","c"]],"note":"optional"}
{"type":"steps","wide":true,"items":[{"icon":"home","d":"Day 1 or a short label","text":"What happens.","note":"optional second line, good for math"}]}
{"type":"list","icons":true,"items":[{"icon":"search","html":"<strong>Bold lead.</strong> Rest of the item."}]}
{"type":"compare","a":{"icon":"done","tag":"Option A","title":"Choose this when","items":["...","..."]},"b":{"icon":"x","tag":"Option B","title":"Choose that when","items":["...","..."]}}
{"type":"callout","icon":"alert","gold":true,"title":"Lead-in: ","text":"One important warning or tip."}
{"type":"calc","kind":"refinish | hardwood | lvp","note":"optional one-line note shown under the result"}
{"type":"estimator","title":"Scope Your Carpet Project","sub":"Tell us the rooms; we bring samples and a firm price."}
{"type":"quiz","title":"Should you refinish or replace?","sub":"Answer three questions.","min":3,
 "items":[{"k":"age","q":"How old is the floor?","opts":[["new","Under 20 years"],["old","20+ years"]]}, ...],
 "rules":[{"when":"a.age==='old'&&a.damage==='deep'","h":"Verdict heading","p":"Verdict text."}],
 "default":{"h":"Default heading","p":"Default text."}}
```
Quiz `when` is a JavaScript expression over the answers object `a` (keys are the `k` values, values are the option keys).

`calc` kinds: refinish (natural/stain/recoat + stairs + dust + washer/dryer + appliances), hardwood (engineered/solid/unfinished + stairs $125), lvp (vinyl plank/laminate + stairs $100). Carpet posts use `estimator`.

## Structure that works

1. `quick` (answer + 4 tiles)
2. `p` framing the question the way people actually ask it (mention the city)
3. 5–7 `h2` sections, each with one visual block (`cards`, `table`, `steps`, `compare`, `list`, `prices`, `callout`) and optional short `p`
4. The `calc`/`estimator` under an h2 like "Price your {city} floor right now" roughly in the middle
5. A "when NOT to" or "mistakes" section (honesty builds trust and ranks)
6. A "how to get the best result / what to ask" list
7. FAQ (5–7), related, CTA copy specific to the question

See `specs/001-refinish-seattle-cost.json` for a complete example.
