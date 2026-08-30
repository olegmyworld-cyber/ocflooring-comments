# Tile & Carpet writer-agent brief

You are writing OC Flooring blog posts. Everything you need is in this repo at
/home/user/ocflooring-comments (already checked out; work there, do NOT run git
commit or git push — the coordinator commits).

## Per assigned slug, in publish-date order

1. **Read your row** in `blogs/plan/TILE-CARPET-PLAN.json` (search your slug).
   It fixes: title (use EXACTLY), slug, publish_date, blog-category id, city,
   keyword, own_service_page. `plan['service_pages']` maps `service|city-slug`
   → verified URL path for every city page. NEVER invent a path.
2. **Study the canonical examples** before your first post:
   `blogs/src/post_tile_01_seattle_cost.py` and `blogs/src/post_carpet_02_pets.py`
   (generators), and their outputs `blogs/bathroom-tile-installation-cost-seattle.body.html`.
   Match this house style exactly: tone (an honest contractor at the kitchen
   table — direct, concrete, no fluff, willing to say "you don't need us for
   this"), structure, and components.
3. **Facts**: quote ONLY the numbers in `blogs/plan/TILE-CARPET-FACTS.md`.
   Tile: labor from $11/sq ft, $14–$26 installed, pre-slope + bonded membrane +
   photographed 24-hour flood test, 2-year warranty. Carpet: from $1.49/sq ft
   installed, mobile showroom with 20+ samples + 3 pad grades, written price
   same visit. Shared: since 2013, 1,000+ floors, (425) 595-1079.
4. **Write a generator** `blogs/src/post_<service><seq>_<short>.py` using
   `from builder import *` and the same component calls as the examples:
   date_badge, quick_answer, facts (3), raw '<h2>' + '<p>' strings, table
   and/or two_col, faq (8 Q&A), cta, related, then `assemble(SLUG, parts)`.
   Target 1,800–2,900 words. Use &mdash;/&ndash; entities inside component
   strings. NEVER emit <section> or inline <svg> — builder handles everything.
5. **Links** (validator-enforced):
   - City post: link `own_service_page` in the body. General post: link ≥1
     service page of your service (Seattle's is a good default).
   - ≥4 `/blog/...` links. Allowed targets ONLY: slugs in
     `blogs/plan/EXISTING-SLUGS.txt`, OR any slug in `blogs/plan/PLAN.json` /
     `TILE-CARPET-PLAN.json` whose publish_date is STRICTLY EARLIER than yours.
     Pick topically relevant ones (tile/carpet/waterproof/kitchen/stairs
     existing posts; your own series' earlier posts).
   - `/contact` once (cta does this).
6. **Meta file** `blogs/<slug>.meta.json` — same shape as the examples: name,
   slug, title-tag (≤60 chars, include service + city/keyword), meta-description
   (120–160 chars), post-summary (STARTS with "Month D, YYYY · ", 2–3 sentences),
   blog-category (from plan), publish_date, service, city, city-links.
   city-links html: `<h3><Service> Installation near you</h3><p>OC Flooring
   serves King and Snohomish County. Jump straight to your city:</p><ul
   role="list">` + 4 `<li><a href=...>` from service_pages — own city FIRST for
   city posts, then 3 large/nearby cities; general posts use Seattle, Bellevue,
   Everett, Renton.
7. **Validate**: `python3 blogs/plan/tc_validate.py <slug>` — fix until OK.
   Do not create anything in Webflow until it passes.
8. **Create the CMS draft**: mcp__Webflow__data_cms_tool →
   create_collection_items on collection `65f32565e111adbbb806ce92`, isDraft
   true, fieldData = {name, slug, title-tag, meta-description, post-summary,
   blog-category, city-links}. NO post-body in this call.
   ⚠ If the call TIMES OUT it may still have succeeded: list_collection_items
   with filter.slug.eq = your slug before any retry. Never create twice.
9. **Push the body**: read `blogs/<slug>.body.html`, then ONE
   update_collection_items call with that item id and fieldData containing
   ONLY `post-body` (the whole ~27 KB file content verbatim). One item per
   call. If the response overflows to a file, grep it for your slug to confirm.
10. **Record**: add `"item_id"` to `blogs/<slug>.meta.json`.
11. Do NOT publish anything. Do NOT touch TILE-CARPET-PLAN.json or any file
    outside your own posts' generator/body/meta files.

## Report back
One line per slug: `<slug>: validated OK, item <id>, body pushed (<n> chars)`
plus anything that failed and why. If Webflow errors persist after 2 retries,
finish the repo files for that post and report it as needing a body push.
