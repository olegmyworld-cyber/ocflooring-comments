# Carpet city page — internal-link and guides-section correction

You correct a SET of already-built OC Flooring carpet city pages (Webflow siteId `6377e8e6a53936b48ef1cad0`). Your prompt lists the cities you own as `slug -> pageId`. Handle them ONE AT A TIME, fully finishing each before starting the next.

Load tools first: ToolSearch query `select:mcp__Webflow__data_element_tool,mcp__Webflow__data_element_builder,mcp__Webflow__data_whtml_builder`.

Background: these pages were duplicated from the Bellevue page AFTER Bellevue had been given links to the 29 other cities. So a duplicate typically inherits a chip row that (a) contains a link to ITSELF and (b) is MISSING Bellevue, and it may still carry Bellevue's own blog-guides section. Both must be corrected. Some pages were already fixed by their builder — verify, and only change what is actually wrong.

Retry any 429/rate-limit error up to 6 times. On "internal error", retry once, then record it and continue.

## CITY TABLE (name -> page path). The full set is 30 cities.
Arlington -> /city-of-arlington/carpet-installation-in-arlington-wa
Bellevue -> /city-of-bellevue/carpet-installation-in-bellevue-wa
Bothell -> /hardwood-floor-refinishing/carpet-installation-in-bothell-wa
Cottage Lake -> /city-of-cottage-lake/carpet-installation-in-cottage-lake-wa
Duvall -> /city-of-duvall/carpet-installation-in-duvall-wa
Edmonds -> /city-of-edmonds/carpet-installation-in-edmonds-wa
Everett -> /city-of-everett/carpet-installation-in-everett-wa
Issaquah -> /city-of-issaquah/carpet-installation-in-issaquah-wa
Kenmore -> /city-of-kenmore/carpet-installation-in-kenmore-wa
Kirkland -> /city-of-kirkland/carpet-installation-in-kirkland-wa
Lake Stevens -> /city-of-lake-stevens/carpet-installation-in-lake-stevens-wa
Lynnwood -> /city-of-lynnwood/carpet-installation-in-lynnwood-wa
Marysville -> /city-of-marysville/carpet-installation-in-marysville-wa
Medina -> /city-of-medina/carpet-installation-in-medina-wa
Mercer Island -> /city-of-mercer-island/carpet-installation-in-mercer-island-wa
Mill Creek -> /city-of-mill-creek/carpet-installation-in-mill-creek-wa
Monroe -> /city-of-monroe/carpet-installation-in-monroe-wa
Mukilteo -> /city-of-mukilteo/carpet-installation-in-mukilteo-wa
Newcastle -> /city-of-new-castle/carpet-installation-in-newcastle-wa
North Bend -> /city-of-north-bend/carpet-installation-in-north-bend-wa
Oak Harbor -> /city-of-oak-harbor/carpet-installation-in-oak-harbor-wa
Redmond -> /city-of-redmond/carpet-installation-in-redmond-wa
Renton -> /city-of-renton/carpet-installation-in-renton-wa
Sammamish -> /city-of-sammamish/carpet-installation-in-sammamish-wa
Seattle -> /seattle/carpet-installation-in-seattle-wa
Shoreline -> /city-of-shoreline/carpet-installation-in-shoreline-wa
Snohomish -> /city-of-snohomish/carpet-installation-in-snohomish-wa
Snoqualmie -> /city-of-snoqualmie/carpet-installation-in-snoqualmie-wa
Whidbey Island -> /city-of-whidbey-island/carpet-installation-in-whidbey-island-wa
Woodinville -> /city-of-woodinville/carpet-installation-in-woodinville-wa

## PART A — chip row (target: exactly 29 links = all 30 cities EXCEPT this page's own city)
1. `data_element_tool` query_elements on the page: element_filter `{style:"ci-chip2"}`, children_depth 1, limit 60. For each match record: element id, type, its String child's text, and its link href.
2. Build `have` = map of text -> element id (Link matches only). Build `want` = the 30 city names minus this page's own city (29 names).
3. **Remove** (one batched `remove_element` call, component = pageId): every match whose type is "Block"; every Link whose text equals THIS page's own city (the self-link); and any duplicate Link beyond the first for the same city name.
4. **Add** (one `data_element_builder` call, parent `{component: pageId, element: "474b1d83-1342-12a5-2ea8-342a25ead091"}`, one action per missing name, creation_position "append"): `{type:"TextLink", set_style:{style_names:["ci-chip2"]}, set_text:{text:"<CityName>"}, set_link:{link_type:"url", link:"<path from table>"}}`. Skip this call if nothing is missing.
5. Also confirm each remaining Link's href matches the table for its city; if one is wrong, fix it with `set_link` (linkType "url").
6. Re-query and confirm: exactly 29 matches, all type Link, texts exactly equal `want`.

## PART B — carpet guides section (target: exactly 1 cg-sec, this city's heading and this city's 5 blog links)
1. Read this city's pack: `/tmp/claude-0/-home-user-ocflooring-comments/5b439edc-55c6-5748-8501-db5632544699/scratchpad/packs/<citySlug>.json` and take `guides` (5 slugs).
2. query_elements element_filter `{style:"cg-sec"}` limit 5, and separately `{style:"cg-h"}` children_depth 1 and `{style:"cg-link"}` children_depth 1 (limit 20).
3. Decide:
   - If there are 0 cg-sec sections -> insert one (step 4 below).
   - If there are 2+ -> remove all but keep none, then insert one fresh (simplest and safest).
   - If there is exactly 1: check the cg-h text equals `Carpet answers for <CityName> homeowners` AND the five cg-link hrefs are exactly this city's 5 guide slugs. If both are already correct, DO NOTHING for Part B. Otherwise remove that section and insert a fresh one.
4. Insert with `data_whtml_builder`, ONE action, parent_element_id `{component: pageId, element: "5b129789-e1e6-4224-d4b7-17de3ae29c9f"}` (the ci-cta section), creation_position `before`, and this html (substitute the city name and the 5 slugs/titles):
`<section class="cg-sec"><div class="cg-wrap"><div class="cg-eyebrow">Carpet guides</div><h3 class="cg-h">Carpet answers for <CityName> homeowners</h3><div class="cg-list">` then five `<a class="cg-link" href="/blog/<slug>"><Title></a>` then `</div></div></section>`
   Pass NO css parameter (the styles already exist on the site). A "Font Newsreader unavailable" warning is expected and harmless.
5. Re-query cg-sec: must be exactly 1, with the correct heading and hrefs.

### Blog slug -> link title
who-sells-mohawk-carpet-find-top-retailers-near-you -> Who Sells Mohawk Carpet? Where to Buy It — and When to Skip It
whats-the-best-carpeting-for-stairs-in-kenmore-wa -> What's the Best Carpeting for Stairs?
what-is-a-good-price-to-pay-for-carpet-in-seattle-wa -> Carpet Installation Cost in Seattle: A Fair-Price Guide
carpet-installation-cost-bothell-wa -> How Much Does Carpet Installation Cost in Bothell, WA?
do-you-have-to-move-furniture-to-stretch-carpet -> Do You Have to Move Furniture to Stretch Carpet?
is-it-worth-it-to-restretch-your-carpet -> Is It Worth It to Restretch Your Carpet? The Honest Math
5-carpet-options-for-carpet-installation-in-lynnwood-wa -> 5 Carpet Options for Lynnwood Homes
carpet-solution-in-bellevue-wa-your-ultimate-guide-to-impeccable-flooring -> Choosing Carpet in Bellevue: An Honest Guide
the-10-best-carpet-brands-reviews-2023-guide -> Carpet vs. Hard Flooring in 2026: An Honest Local Guide
upkeep-for-carpet-vs-hardwood-flooring -> Carpet vs. Hardwood Upkeep: The Honest 10-Year Comparison
6-reasons-to-replace-carpet-flooring -> 6 Signs Your Carpet Is Done — and What to Replace It With
how-to-remove-old-carpet -> How to Remove Old Carpet Yourself: Tools, Steps & Local Disposal

## Report
Return via StructuredOutput a `cities` array with one entry per city you own:
`{citySlug, pageId, chipsFinal (int), chipsAdded (int), chipsRemoved (int), guidesAction ("none"|"replaced"|"inserted"), ok (bool), errors[] }`.
`ok` is true only when Part A ends at exactly 29 correct links AND Part B ends at exactly 1 correct cg-sec. Report honestly.
