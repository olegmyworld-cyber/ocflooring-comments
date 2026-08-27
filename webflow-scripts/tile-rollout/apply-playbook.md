# Tile city-page apply playbook

You are applying a composed city pack to a live Webflow page via the Webflow MCP
tools. Everything you need is in /home/user/ocflooring-comments/webflow-scripts/tile-rollout/.

Constants:
- siteId: `6377e8e6a53936b48ef1cad0`
- pageId per city: `tile-pageids.json` → `<slug>.pageId`
- element ids per role: `rewrite-map.json` → `<role>.el` (identical on every city
  page — the pages are duplicates of the Bellevue master)
- pack: `packs/<slug>.json`

Tools: use ToolSearch first to load `mcp__Webflow__data_element_tool`,
`mcp__Webflow__data_element_settings_tool`, `mcp__Webflow__data_pages_tool`.

## Rate-limit discipline (shared 60 req/min budget with sibling agents)
- **Webflow counts individual actions, not tool calls.** A call carrying 29
  set_text actions can return HTTP 200 while the later actions inside it fail
  with `init-multiplayer-connection returned 429` — a partial write that looks
  like success. ALWAYS inspect every action's status in the response, not just
  the call's. Keep batches to **≤15 actions** and ~18 s between calls; re-send
  only the failed actions after a 45 s wait.
- Sleep ~10 seconds between MCP calls (`sleep 10` via Bash with run_in_background
  NOT needed — foreground `sleep 10` alone in a Bash call is fine; if a hook blocks
  it, use `python3 -c "import time;time.sleep(10)"`).
- On a 429 or 5xx/stream error: wait 45 s and retry the identical call once. These
  writes are idempotent.

## Steps per city (do cities sequentially)

1. **Prose fields.** For every role in `rewrite-map.json` EXCEPT
   `chip1..chip16` and `carpetLink`: one `set_text` action
   `{id: {component: <pageId>, element: <role.el>}, text: <pack.roles[role]>}`.
   That's 56 set_text actions → 4 batched calls.
2. **Chips.** The pack's `chips` array (N ≤ 16 names): set_text chip1..chipN with
   the names. If N < 16, `remove_element` on chip(N+1)..chip16's element ids
   (same call is fine).
3. **Carpet link.** set_text on `carpetLink.el` → pack `carpetLinkText`, and
   set_link `{id, linkType: "url", link: <tile-pageids.json[slug].carpetPath>}`.
4. **Image alts.** data_element_settings_tool set_settings — one call, 7
   operations; element ids in `tile-manifest.json` → `image_elements`
   (hero, membrane, work1..work5), key `altText`, static_text = pack `alts.*`.
5. **SEO/OG.** data_pages_tool update_page_settings with the pack's seoTitle,
   seoDesc, ogTitle, ogDesc (openGraph titleCopied/descriptionCopied false).
   Do NOT change title/slug/parentFolderId.
6. **JSON-LD.** Run `python3 build-jsonld.py <slug>` and pass the printed string
   verbatim as jsonLdSchema in data_pages_tool bulk_update_pages_schema_markup
   (site_id + one page entry).
7. **Verify.** `query_elements` with `element_id` alone returns the element's
   type/styles/settings but NO text — it cannot confirm a set_text landed. Use
   either `element_id` + `children_depth: 1` (returns the String child with
   `textContent`) or `element_filter: {text: "<distinctive substring>"}`.
   Check heroLead, faqA1 and footerTag against the pack; redo any that differ.

   Whole-rollout audit (cheaper than per-field checks): the Bellevue baseline
   has 30 of 57 fields containing the word "Bellevue", while a correctly
   applied city page should contain it only in `trustCell` ("Bellevue based"),
   the static Google-review byline "Richard L. · Bellevue · Google", and
   `faqA10` where the pack lists Bellevue as a neighbouring city. Query each
   page for text "Bellevue" and compare the count to that expectation — any
   excess is an unapplied field. Cover the remaining 27 fields by querying for
   baseline-only phrases such as "curb or curbless entry, then tile",
   "Nothing left in your driveway", "not just cement board and thinset",
   "no reason to say yes on the spot" and
   "photograph the membrane and the flood test", which must return zero
   matches on every city page.

Log progress per city to
/home/user/ocflooring-comments/webflow-scripts/tile-rollout/apply-log-<slug>.txt
(one line per step). Do not run git commands.
