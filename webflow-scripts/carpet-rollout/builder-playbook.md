# Carpet city page builder playbook

You are building ONE carpet-installation city page for OC Flooring (Webflow siteId `6377e8e6a53936b48ef1cad0`) by duplicating the Bellevue template page and applying a city content pack. Follow these steps EXACTLY and in order. Your prompt gives you: `citySlug`, and `pack` (the content). Look up your city's record in the CITIES table below.

First load tools: ToolSearch query `select:mcp__Webflow__data_pages_tool,mcp__Webflow__data_element_tool,mcp__Webflow__data_element_settings_tool,mcp__Webflow__data_scripts_tool,mcp__Webflow__data_element_builder,mcp__Webflow__data_whtml_builder`.

Also Read these files:
- `/tmp/claude-0/-home-user-ocflooring-comments/5b439edc-55c6-5748-8501-db5632544699/scratchpad/rewrite-sheet.json` — `sheet` = 86 ordered entries `{el, sec, bellevue}`; `chipEls` = 16 element ids for neighborhood chips.

On any 429/rate-limit error: retry the same call, up to 6 times; if a batch partially fails, retry only the failed action. On "internal error"/conflict: retry once, then record in errors and continue.

## CITIES table (slug → name; folderId; page path)
arlington; Arlington; 65f32565e111adbbb806cecd; /city-of-arlington/carpet-installation-in-arlington-wa
bellevue; Bellevue; 65f32565e111adbbb806cece; /city-of-bellevue/carpet-installation-in-bellevue-wa
bothell; Bothell; 65f32565e111adbbb806cf70; /hardwood-floor-refinishing/carpet-installation-in-bothell-wa
cottage-lake; Cottage Lake; 65f32565e111adbbb806cecf; /city-of-cottage-lake/carpet-installation-in-cottage-lake-wa
duvall; Duvall; 65f32565e111adbbb806ced0; /city-of-duvall/carpet-installation-in-duvall-wa
edmonds; Edmonds; 65f32565e111adbbb806ced1; /city-of-edmonds/carpet-installation-in-edmonds-wa
everett; Everett; 65f32565e111adbbb806ced2; /city-of-everett/carpet-installation-in-everett-wa
issaquah; Issaquah; 65f32565e111adbbb806ced3; /city-of-issaquah/carpet-installation-in-issaquah-wa
kenmore; Kenmore; 65f32565e111adbbb806ced4; /city-of-kenmore/carpet-installation-in-kenmore-wa
kirkland; Kirkland; 65f32565e111adbbb806ced5; /city-of-kirkland/carpet-installation-in-kirkland-wa
lake-stevens; Lake Stevens; 65f32565e111adbbb806ced6; /city-of-lake-stevens/carpet-installation-in-lake-stevens-wa
lynnwood; Lynnwood; 65f32565e111adbbb806ced7; /city-of-lynnwood/carpet-installation-in-lynnwood-wa
marysville; Marysville; 65f32565e111adbbb806ced8; /city-of-marysville/carpet-installation-in-marysville-wa
medina; Medina; 65f32565e111adbbb806cedc; /city-of-medina/carpet-installation-in-medina-wa
mercer-island; Mercer Island; 65f32565e111adbbb806ceee; /city-of-mercer-island/carpet-installation-in-mercer-island-wa
mill-creek; Mill Creek; 65f32565e111adbbb806ceef; /city-of-mill-creek/carpet-installation-in-mill-creek-wa
monroe; Monroe; 65f32565e111adbbb806cef0; /city-of-monroe/carpet-installation-in-monroe-wa
mukilteo; Mukilteo; 65f32565e111adbbb806cef1; /city-of-mukilteo/carpet-installation-in-mukilteo-wa
newcastle; Newcastle; 65f32565e111adbbb806cef2; /city-of-new-castle/carpet-installation-in-newcastle-wa
north-bend; North Bend; 65f32565e111adbbb806cef3; /city-of-north-bend/carpet-installation-in-north-bend-wa
oak-harbor; Oak Harbor; 65f32565e111adbbb806cef4; /city-of-oak-harbor/carpet-installation-in-oak-harbor-wa
redmond; Redmond; 65f32565e111adbbb806cef6; /city-of-redmond/carpet-installation-in-redmond-wa
renton; Renton; 65f32565e111adbbb806cef7; /city-of-renton/carpet-installation-in-renton-wa
sammamish; Sammamish; 65f32565e111adbbb806cef8; /city-of-sammamish/carpet-installation-in-sammamish-wa
seattle; Seattle; 65f32565e111adbbb806d07d; /seattle/carpet-installation-in-seattle-wa
shoreline; Shoreline; 65f32565e111adbbb806cef9; /city-of-shoreline/carpet-installation-in-shoreline-wa
snohomish; Snohomish; 65f32565e111adbbb806cefa; /city-of-snohomish/carpet-installation-in-snohomish-wa
snoqualmie; Snoqualmie; 65f32565e111adbbb806cefb; /city-of-snoqualmie/carpet-installation-in-snoqualmie-wa
whidbey-island; Whidbey Island; 65f32565e111adbbb806cefc; /city-of-whidbey-island/carpet-installation-in-whidbey-island-wa
woodinville; Woodinville; 65f32565e111adbbb806cefd; /city-of-woodinville/carpet-installation-in-woodinville-wa

Constants: template (Bellevue) pageId `6a8ccb1ebf28596111eed9f2`. Existing Kirkland draft pageId `6a8cff466aa497d30bbcc3cd` (for citySlug `kirkland` SKIP step 1 and use this pageId). OG image assetId `674525d05580d80aca9c5a14`. Phone (425) 595-1079.

## Step 1 — create the page
`data_pages_tool` → `create_page`: site_id, `title` = "Carpet Installation in {CityName}, WA", `slug` = "carpet-installation-in-{citySlug}-wa", `parentFolderId` from table, `duplicateOf` = template pageId, `draft` = true. Record the returned page `id` = PAGEID. (Element ids inside the duplicate are IDENTICAL to the template's, so the ids below all work with component=PAGEID.)

## Step 2 — apply the 86 text replacements
`pack.repl` is an array of exactly 86 strings in the SAME ORDER as `sheet` in rewrite-sheet.json. For i in 0..85: set_text on element `{component: PAGEID, element: sheet[i].el}` with text `pack.repl[i]`. Use `data_element_tool` with ~20 `set_text` actions per call (5 calls). If one action errors, retry it individually.

## Step 3 — neighborhood chips
`pack.neighborhoods` = 16 strings. For i in 0..15: set_text on `{component: PAGEID, element: chipEls[i]}`. Batch into one call.

## Step 4 — nearby-city internal links
Parent: `{component: PAGEID, element: "474b1d83-1342-12a5-2ea8-342a25ead091"}` (the ci-chip-row2 block).
(a) `data_element_builder`, ONE call, 29 actions (all with that parent, creation_position "append", in the CITIES-table order, SKIPPING your own city): each action `element_schema` = `{type:"TextLink", set_style:{style_names:["ci-chip2"]}, set_text:{text:"<CityName>"}, set_link:{link_type:"url", link:"<page path from table>"}}`.
(b) Then remove the 18 old text chips with `data_element_tool` remove_element (component=PAGEID) for these element ids, batched in one call:
474b1d83-1342-12a5-2ea8-342a25ead075, -2ea8-342a25ead077, -2ea8-342a25ead079, -2ea8-342a25ead07b, -2ea8-342a25ead07d, -2ea8-342a25ead07f, -2ea8-342a25ead081, -2ea8-342a25ead083, -2ea8-342a25ead085, -2ea8-342a25ead087, -2ea8-342a25ead089, -2ea8-342a25ead08b, -2ea8-342a25ead08d, -2ea8-342a25ead08f, ... STOP — do NOT guess ids. Instead: query_elements with element_filter {style:"ci-chip2"} limit 50 on PAGEID, and remove every match whose type is "Block" (the old text chips). Your newly created TextLinks have type Link — do not remove those.

## Step 5 — photo-quote embed (city lead)
`data_element_settings_tool` set_settings on `{component: PAGEID, element: "ba9f3312-17ad-cec4-ebb7-d0334fdada88"}`, key `code`, static_text value = the template below with `{{H2}}` → `pack.embedH2` and `{{LEAD}}` → `pack.embedLead` (plain text; escape nothing else):

```
<section id="ocpq" aria-labelledby="ocpq-title"><div class="ocpq-wrap"><header class="ocpq-head"><div class="ocpq-eyebrow"><span></span>No appointment needed</div><h2 id="ocpq-title">{{H2}}</h2><p class="ocpq-lead">{{LEAD}}</p></header><div id="ocpq-shell"></div></div></section>
```

## Step 6 — carpet guides section (blog links)
`data_whtml_builder`, ONE action: parent_element_id `{component: PAGEID, element: "5b129789-e1e6-4224-d4b7-17de3ae29c9f"}` (the ci-cta section), creation_position `before`.
html: `<section class="cg-sec"><div class="cg-wrap"><div class="cg-eyebrow">Carpet guides</div><h3 class="cg-h">Carpet answers for {CityName} homeowners</h3><div class="cg-list">` + for each of the 5 slugs in `pack.guides`: `<a class="cg-link" href="/blog/<slug>"><title from map below></a>` + `</div></div></section>`
css: `.cg-sec{background:#F7F2EC;border-top:1px solid #EDE4DA;padding:56px 28px}.cg-wrap{max-width:1200px;margin:0 auto}.cg-eyebrow{font-size:12.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#8F4F3C}.cg-h{margin-top:12px;font-family:Newsreader,Georgia,serif;font-weight:400;font-size:26px;line-height:1.25;color:#2E2724}.cg-list{margin-top:18px;display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:8px 24px}.cg-link{color:#332D28;font-size:15.5px;line-height:1.5;text-decoration:none;border-bottom:1px solid transparent}.cg-link:hover{color:#A32F26;border-bottom-color:#A32F26}`

Blog post titles map (slug → link text):
- who-sells-mohawk-carpet-find-top-retailers-near-you → Who Sells Mohawk Carpet? Where to Buy It — and When to Skip It
- whats-the-best-carpeting-for-stairs-in-kenmore-wa → What's the Best Carpeting for Stairs?
- what-is-a-good-price-to-pay-for-carpet-in-seattle-wa → Carpet Installation Cost in Seattle: A Fair-Price Guide
- carpet-installation-cost-bothell-wa → How Much Does Carpet Installation Cost in Bothell, WA?
- do-you-have-to-move-furniture-to-stretch-carpet → Do You Have to Move Furniture to Stretch Carpet?
- is-it-worth-it-to-restretch-your-carpet → Is It Worth It to Restretch Your Carpet? The Honest Math
- 5-carpet-options-for-carpet-installation-in-lynnwood-wa → 5 Carpet Options for Lynnwood Homes
- carpet-solution-in-bellevue-wa-your-ultimate-guide-to-impeccable-flooring → Choosing Carpet in Bellevue: An Honest Guide
- the-10-best-carpet-brands-reviews-2023-guide → Carpet vs. Hard Flooring in 2026: An Honest Local Guide
- upkeep-for-carpet-vs-hardwood-flooring → Carpet vs. Hardwood Upkeep: The Honest 10-Year Comparison
- 6-reasons-to-replace-carpet-flooring → 6 Signs Your Carpet Is Done — and What to Replace It With
- how-to-remove-old-carpet → How to Remove Old Carpet Yourself: Tools, Steps & Local Disposal

## Step 7 — image alt texts
`data_element_settings_tool` set_settings, one call, three operations (component=PAGEID):
- element `18914240-b331-c729-b748-a121aa0a5ed5` key `altText` static_text = `pack.heroAlt`
- element `491fff7b-429c-e871-49b5-5f83d8f58f87` key `altText` static_text = `pack.vanAlt`
- element `b3091fa5-ae5b-b0ab-ad25-1fd8e1f29ba3` key `altText` static_text = "Stair carpet installation in a {CityName} home"

## Step 8 — SEO, Open Graph, JSON-LD, undraft
`data_pages_tool` update_page_settings: page_id=PAGEID, `seo` = {title: pack.seoTitle, description: pack.seoDesc}, `openGraph` = {title: pack.ogTitle, titleCopied: false, description: pack.ogDesc, descriptionCopied: false, imageAssetId: "674525d05580d80aca9c5a14"}, `draft` = false, and `jsonLdSchema` = the Bellevue schema adapted as follows (produce ONE JSON string):
Take this structure and substitute: CITY = CityName; PATH = the page path from the table; LAT/LNG = pack.lat/pack.lng; NEIGHBORHOOD_LIST = pack.neighborhoods joined with ", "; the FAQPage mainEntity = the 10 Q&A pairs from pack.repl entries 66..85 (66=Q1,67=A1,68=Q2,69=A2,...84=Q10,85=A10), each as {"@type":"Question","name":Q,"acceptedAnswer":{"@type":"Answer","text":A}}.

```
{"@context":"https://schema.org","@graph":[
{"@type":["HomeAndConstructionBusiness","FlooringContractor"],"@id":"https://www.nwocflooring.com/#business","name":"OC Flooring","description":"Mobile carpet showroom and carpet installation contractor serving CITY, WA and surrounding communities. Carpet, pad, stair carpet, carpet stretching and removal.","url":"https://www.nwocflooring.com/","telephone":"+1-425-595-1079","priceRange":"$$","currenciesAccepted":"USD","foundingDate":"2013","slogan":"Crafting beautiful spaces, one floor at a time.","address":{"@type":"PostalAddress","addressLocality":"Bellevue","addressRegion":"WA","addressCountry":"US"},"geo":{"@type":"GeoCoordinates","latitude":47.622305,"longitude":-122.1623651},"aggregateRating":{"@type":"AggregateRating","ratingValue":"4.7","reviewCount":"119","bestRating":"5"},"areaServed":[{"@type":"City","name":"CITY"}],"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"08:00","closes":"19:00"}],"makesOffer":[{"@type":"Offer","itemOffered":{"@type":"Service","name":"Carpet installation, CITY WA"},"priceSpecification":{"@type":"UnitPriceSpecification","price":"1.49","priceCurrency":"USD","unitText":"square foot"}},{"@type":"Offer","itemOffered":{"@type":"Service","name":"Carpet and pad supplied"},"priceSpecification":{"@type":"UnitPriceSpecification","price":"2.49","priceCurrency":"USD","unitText":"square foot"}},{"@type":"Offer","itemOffered":{"@type":"Service","name":"Stair carpet installation"},"priceSpecification":{"@type":"UnitPriceSpecification","price":"18.00","priceCurrency":"USD","unitText":"step"}},{"@type":"Offer","itemOffered":{"@type":"Service","name":"Carpet stretching and re-stretching"},"priceSpecification":{"@type":"UnitPriceSpecification","price":"99.00","priceCurrency":"USD","unitText":"room"}},{"@type":"Offer","itemOffered":{"@type":"Service","name":"Old carpet removal and haul-away"},"priceSpecification":{"@type":"UnitPriceSpecification","price":"0.50","priceCurrency":"USD","unitText":"square foot"}}]},
{"@type":"Service","@id":"https://www.nwocflooring.comPATH#service","serviceType":"Mobile carpet showroom and carpet installation","name":"Carpet Installation in CITY, WA — Mobile Showroom","provider":{"@id":"https://www.nwocflooring.com/#business"},"areaServed":{"@type":"City","name":"CITY","containedInPlace":{"@type":"State","name":"Washington"}},"availableChannel":{"@type":"ServiceChannel","serviceLocation":{"@type":"Place","name":"Your home in CITY, WA","geo":{"@type":"GeoCoordinates","latitude":LAT,"longitude":LNG}},"servicePhone":"+1-425-595-1079","serviceUrl":"https://www.nwocflooring.com/contact"},"termsOfService":"Free in-home measure and written quote; 1-year workmanship warranty."},
{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://www.nwocflooring.com/"},{"@type":"ListItem","position":2,"name":"Services","item":"https://www.nwocflooring.com/services/our-products"},{"@type":"ListItem","position":3,"name":"Carpet Installation CITY, WA","item":"https://www.nwocflooring.comPATH"}]},
{"@type":"FAQPage","mainEntity":[ ...10 questions... ]}
]}
```

## Step 9 — page scripts
`data_scripts_tool` set_page_scripts: page_id=PAGEID, scripts = `[{"id":"carpetbellevuefontscanonical","location":"header","version":"1.2.0"},{"id":"occarpetbellevue","location":"footer","version":"1.8.0"}]`.

## Step 10 — verify and report
- query_elements: style `ci-h1` children_depth 1 → text must equal pack.repl[2].
- query_elements: style `ci-chip2` limit 50 → exactly 29 matches, all type Link.
- get_page_scripts → the 2 scripts above.
Return via StructuredOutput: citySlug, pageId, ok (true only if ALL steps succeeded and verifications passed), plus per-step booleans and an errors array with exact messages for anything that failed. Do NOT return the pack.
