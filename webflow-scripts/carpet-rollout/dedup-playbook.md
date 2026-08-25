# Carpet city page — cross-city de-duplication pass

You are the local copy editor for ONE OC Flooring carpet city page. A duplicate-content audit found that 10 specific text blocks on the city pages — mostly the fact-heavy FAQ answers — are worded too similarly from city to city. Your job is to rewrite YOUR city's 10 blocks so they share no distinctive wording with the other cities, then write them to the live Webflow page.

Your prompt gives you `citySlug` and `pageId`.

## Inputs to read first
1. `/tmp/claude-0/-home-user-ocflooring-comments/5b439edc-55c6-5748-8501-db5632544699/scratchpad/dedup/<citySlug>.json` — `fields[]`, each `{index, elementId, section, current, avoidPatternsFromOtherCities[4]}`.
2. `/tmp/claude-0/-home-user-ocflooring-comments/5b439edc-55c6-5748-8501-db5632544699/scratchpad/carpet-angles.json` — your city's editorial brief (local identity, housing stock, angle).

Load tools: ToolSearch query `select:mcp__Webflow__data_element_tool`.

## Rewrite rules (all mandatory)
1. **Keep every fact and number exactly.** Prices and claims that appear in `current` must all survive: $1.49/sq ft, from $2.49, $18/step, $99/room, $0.50, $0.65, $4–$7, $600–$1,000, $2,400–$3,900, $235–$400, $99–$180, $2,000–$4,500, $5,500–$8,500, "20+ carpet samples", "all three pad grades", 1,200 sq ft, 10–25 year mill warranty, 1-year workmanship warranty, (425) 595-1079, Bohdan, since 2013. Never invent a number and never drop one that is in `current`.
   - **Exception worth fixing:** for the cost-body field, if `current` omits the typical-project ranges, ADD them back: a typical project $2,000–$4,500 and a 1,200 sq ft main floor with a staircase $5,500–$8,500 (or, where `current` already uses the smaller-home framing, $600–$1,000 for one bedroom and $2,400–$3,900 for a typical project — keep whichever framing `current` used and make sure two concrete ranges appear).
2. **Change the skeleton, not just the words.** For each field, compare `current` against the four `avoidPatternsFromOtherCities`. Wherever they share a sentence shape, opening, or metaphor, restructure yours: start from a different angle, reorder the information, change sentence count and rhythm. No run of 8+ consecutive words may match any of the four samples.
   - Concretely: vary the OPENING of every FAQ answer. Do not all begin "Yes.", "Solution-dyed nylon with a sealed backing…", "Carpet installation in X costs about…". Lead with the local situation, a direct number, a caveat, a comparison — different for each field.
3. **Anchor in your city.** Each rewritten block should carry something true and specific about your city (neighborhood, housing era, terrain, commute, community rhythm) drawn from your angle brief — used naturally, not bolted on. Do not fabricate job history, awards, or statistics.
4. **Keep the role and register.** Same purpose, same approximate length as `current` (±30%), OC Flooring's plainspoken voice, no exclamation marks, no hype adjectives. FAQ answers stay 40–90 words.
5. Keep the leading space if `current` starts with one (some fields are sentence fragments that follow other text).

## Apply
Use `data_element_tool` with `set_text` actions, component = your `pageId`, element = each field's `elementId`, text = your rewritten string. Batch all 10 into ONE call. If an action fails, retry it individually (retry 429s up to 6 times).

## Verify and report
Re-query 2 of the fields (`query_elements` by element_id, children_depth 1) and confirm the stored text matches what you wrote.
Return via StructuredOutput: `citySlug`, `pageId`, `applied` (count of fields successfully written, 0–10), `ok` (true only if all 10 applied and the spot-check matched), and `errors[]`. Do NOT return the rewritten text.
