# Move the Calendly scheduler to the top of a tile city page

Applies the layout already built on Bellevue (page `6a8f63898db417f9f6632e49`)
to the other 29 tile city pages. Bellevue is DONE — do not touch it.

siteId: `6377e8e6a53936b48ef1cad0`
pageId per city: `tile-pageids.json` → `<slug>.pageId`
City display name: `packs/<slug>.json` → `cityName`

All 29 pages are duplicates of Bellevue, so these element ids are **identical on
every page** — use them as-is with `component` set to that page's pageId:

| what | element id |
|---|---|
| trust bar section (insert the new section after this) | `59dd19c2-7005-0f91-6f9c-98da541fb361` |
| the Calendly card to move (`.ti-cal-card`) | `5474fc9a-654f-7679-2121-368c4da8d896` |
| closing CTA heading that currently holds `id="book"` | `5474fc9a-654f-7679-2121-368c4da8d88d` |
| closing CTA lead paragraph (insert button after this) | `5474fc9a-654f-7679-2121-368c4da8d88f` |

All CSS classes used below already exist site-wide from the Bellevue build
(`ti-booktop`, `ti-booktop-in`, `ti-booktop-eyebrow`, `ti-booktop-h`,
`ti-anchor`, `ti-cta-btnrow`, `ti-btn`). Do **not** pass a `css` argument —
the classes must be reused, not redefined.

## Steps per page

**1. Clear the old anchor** — `data_element_settings_tool` → `set_settings`,
one operation on the CTA heading, settings `[{"key":"domId","clear":true}]`.
Must happen before step 2 so `id="book"` is not duplicated.

**2. Build both new pieces** — `data_whtml_builder`, two actions in one call:

- after `59dd19c2-7005-0f91-6f9c-98da541fb361`:
  `<section class="ti-booktop"><div class="ti-anchor" id="book"></div><div class="ti-booktop-in"><p class="ti-booktop-eyebrow">Book in about a minute</p><h2 class="ti-booktop-h">Pick a time for your free {CITY} tile estimate</h2></div></section>`
- after `5474fc9a-654f-7679-2121-368c4da8d88f`:
  `<div class="ti-cta-btnrow"><a href="#book" class="ti-btn">Pick your estimate time</a></div>`

`{CITY}` is the pack's `cityName`. For Whidbey Island write
"your free Whidbey Island tile estimate" (the pack's own preposition style is
only used in body copy, not here).

**3. Find the new inner container** — `data_element_tool` → `query_elements`
with `element_filter: {"style":"ti-booktop-in"}`. It is created fresh per page,
so its id is NOT shared; read it from this response.

**4. Move the Calendly card into it** — `data_element_tool` → `move_element`,
`id` = the `.ti-cal-card` id above, `anchor_element_id` = the id from step 3,
`creation_position` `"append"`. Move it — never rebuild it — so the
`#ti-cal-mount` div the JS bundle initialises travels with the card.

**5. Verify** — one `query_elements` call with two queries:
- `element_filter: {"attribute_name":"id","attribute_value":"book"}` → must be
  exactly **1** match (the new `.ti-anchor`).
- `element_filter: {"attribute_name":"id","attribute_value":"ti-cal-mount"}`
  with `return_parent: "ancestor"` → the ancestors must include `ti-booktop`.

Final page order must be: crumbs, hero, trust, **ti-booktop**, cost, …, cta.

## Gotchas

- `set_dom_id` and `set_attributes` are rejected on these pages with
  `MPS rejected update … [Conflict] The operation could not be applied to the
  component map` when assigning an id that was just cleared. That is why the
  anchor is created with its `id` inline through the WHTML builder — that path
  works first time. Do not try to set the id any other way.
- Webflow rate-limits per action: keep ~8–10 s between calls and retry an
  identical call once after 45 s on a 429/5xx. Every step here is idempotent
  except step 2 (running it twice would create a second section) — so if a
  step 2 call errors, check with a query before re-running it.
