# Writer-agent brief — OC Flooring blog batch

You are writing OC Flooring (nwocflooring.com) blog posts assigned by `seq` range from
`blogs/plan/PLAN.json`. Work from the repo root `/home/user/ocflooring-comments`.

## Read these FIRST (in order)
1. `blogs/src/builder.py` — the component library you MUST use.
2. `blogs/src/post_water_oil.py` — the canonical exemplar. Match its voice, altitude, structure.
3. `blogs/EDITORIAL-CALENDAR.md` — standing rules.

## Per post, produce
For each assigned PLAN entry `{seq, name, slug, category, city, publish_date}`:
1. A generator script in `/tmp/agentwork-<yourname>/post_<slug>.py` that
   `sys.path.append('/home/user/ocflooring-comments/blogs/src')`, imports from `builder`,
   and via `assemble()` writes `<slug>.body.html` in the CURRENT DIRECTORY — run it from
   `/home/user/ocflooring-comments/blogs/` so bodies land in `blogs/`.
2. `blogs/<slug>.meta.json`: `{"name","slug","title-tag","meta-description","post-summary","blog-category","publish_date","item_id"}`.
3. A Webflow CMS **draft** (see below).

## Required structure (assemble parts in this order)
`date_badge(D)` where D = publish_date as "March 3, 2027" (no leading zero) →
`quick_answer(answer_html, chip2_label)` (bold direct answer first sentence; chip2 = short topic/city label) →
1–2 intro `<p>` → `facts([...])` 3 stats (real numbers) → 4–7 `<h2>` sections with `<p>` prose
(one section MUST be the city-local section when city is set) → at least one `table()` OR one
`two_col()` (comparison topics should use both) → `faq(title, [(q,a)×7–9])` (plain-text answers,
2–4 sentences each) → `cta(h2, sub)` → `related([(url,label)×4–5])` ending with `("/contact","Book a free estimate")`.
Total prose target: 1,800–2,400 words. Use typographic apostrophes (’) and em dashes in prose.

## Voice
Honest contractor, first-person plural ("we"), willing to admit bias and name competitors' valid
points, concrete numbers over adjectives, dry humor sparingly, zero filler. Answer the title's
question in the first bold sentence. Never invent projects/testimonials; "we've seen"-style
generalities are fine.

## Facts you must use consistently (never contradict)
$1.99/sq ft screen & recoat · $3.99 natural refinish · $6.50 stain refinish · stairs $55–$75/tread ·
500 sq ft minimum · dust containment +$250 · washer/dryer pair +$160, other appliances +$80 each ·
new-install labor $3–$4.25/sq ft + materials $4–$10+/sq ft · Bona (Traffic HD, ~65 g/L, GREENGUARD
Gold) & Pallmann waterborne systems, 2–3 coats · waterborne: socks same evening, furniture 48–72h,
rugs 7 days, full cure ~7 days · oil-modified poly: ~450–550 g/L, 1 coat/day, ~30-day cure, ambers ·
Lägler TRIO final pass · since 2013, 1,000+ floors, 1-yr workmanship warranty, licensed & insured,
financing, 120+ Google reviews · (425) 595-1079 · King & Snohomish County · timeline 3–5 days
typical refinish (screen & recoat = 1 day). Janka: fir 660, red oak 1290, white oak ~1360, maple 1450,
hickory 1820, jatoba 2350.

## City accent (when city is set)
City appears in title (already in `name`), the quick answer, and one dedicated `<h2>` local section
with real texture (neighborhoods, housing eras — e.g. Kirkland lake cottages/Juanita ramblers,
Renton Boeing-era ramblers/Highlands, Sammamish plateau 90s–2000s builds, Redmond tech-era homes,
Mercer Island midcentury/waterfront, Edmonds bowl pre-war homes, Lynnwood 60s–80s split-levels,
Everett mill-era + Silver Lake, Seattle Craftsman stock, Bellevue 80s–2000s red oak).
Link that city's service page: `/hardwood-floor-refinishing-in-<city>-wa` (lowercase, spaces→hyphens).
**Exception: Bellevue has NO refinishing city page** — mention Bellevue in prose but link
`/hardwood-floor-refinishing-in-seattle-wa` or `-kirkland-wa` instead. General (city=null) posts
still link ≥1 city refinishing page naturally.

## Link rules (STRICT — validator enforces)
Internal links may ONLY be: `/blog/<slug>` for slugs in `blogs/plan/EXISTING-SLUGS.txt`, exact paths
listed in `blogs/plan/VALID-PAGE-PATHS.txt` for site pages, OR `/blog/<slug>` of a
PLAN.json post whose `publish_date` is STRICTLY EARLIER than yours. **At least 4 distinct `/blog/` links per post**
(4–6 is the target) in prose + related; **the post's own city refinishing page is MANDATORY**
(city service pages live in FOLDERS — use the exact paths in `blogs/plan/URL-MAP.json`,
e.g. `/city-of-kirkland/hardwood-floor-refinishing-in-kirkland-wa` and the Seattle exception
`/seattle/hardwood-floor-refinishing-in-seattle-wa`. NEVER link the bare `/hardwood-floor-...` form —
it 404s. Bellevue posts link Seattle or Kirkland instead);
general posts still link ≥1 city refinishing page; `/contact` in related. No external links except the two already
in cta() (tel: and the Google review URL — builder handles those).

## Metadata rules
- `post-summary`: MUST start `"<Month D, YYYY> · "` (the publish_date), then 2–3 sentences.
- `title-tag` ≤ 60 chars, includes city when set. `meta-description` ≤ 160 chars.
- `blog-category`: use the ID from PLAN.json verbatim.

## Validate BEFORE creating the CMS item
Run: `python3 blogs/plan/validate.py <slug>` — must print `OK <slug>`. Fix anything it flags.

## Create the Webflow draft
Tool `mcp__Webflow__data_cms_tool`, action `create_collection_items`, collection
`65f32565e111adbbb806ce92`, `request.isDraft: true`, one item:
`fieldData: [{name, slug, post-body (full body file contents), post-summary, title-tag,
meta-description, blog-category}]`. **NEVER publish anything. Never set isDraft false.**
Record the returned item `id` into the meta.json `item_id`. If the Webflow tool is unavailable or
errors twice, set `item_id: null` and continue — do not retry endlessly.

## Finish
Write `blogs/status/agent-<yourname>.json`: list of `{seq, slug, item_id, ok: true/false, note}`.
Do NOT run git commands. Do NOT edit shared files (`blogs/src/*`, PLAN.json, calendar, other posts').
Your final report: one line per post (seq, slug, item_id or FAILED+why).
