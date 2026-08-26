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
- Batch aggressively: one data_element_tool call can carry MANY actions. Use
  ~12–15 set_text actions per call.
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
7. **Verify.** One query_elements call checking 3 fields (heroLead, faqA1,
   footerTag) now return the pack text. If a set_text silently failed, redo it.

Log progress per city to
/home/user/ocflooring-comments/webflow-scripts/tile-rollout/apply-log-<slug>.txt
(one line per step). Do not run git commands.
