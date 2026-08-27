# Tile installation pages — photo grid redesign (2026-08-27)

Request: "make this pictures in better design frame" — the "Recent work"
photo grid on `/city-of-bellevue/tile-installation-in-bellevue-wa` (and, it
turns out, all 30 `tile-installation-in-{city}-wa` pages that appeared
earlier this session) looked flat and left a jarring solid-grey empty box
when the photo count didn't evenly fill the grid.

## Root cause (from the real global CSS, read via the Style API)

The grid (`.ti-work-grid`) is a plain CSS Grid: `auto-fit, minmax(240px,1fr)`,
1px hairline "grout-colored" (#D5D2C8) gaps, AND the same #D5D2C8 as the
container's own background/border. Any grid cell not covered by a real photo
(e.g. 5 photos not filling a 3×2 grid) simply shows that opaque grey
background — reading as a broken/missing image, not empty space. Each photo
tile (`.ti-shot`) had no border-radius, no shadow — fully flush, no "frame."

## Fix — one edit, all 30 pages

`ti-work-grid`, `ti-shot`, and `ti-imgfill` are genuine Webflow **global**
style classes (confirmed: the Woodinville tile page's grid resolves to the
identical style ID as Bellevue's), so editing them once via
`data_style_tool` updates the design on every tile-installation page
simultaneously — no runtime script needed, unlike the carpet/refinishing
pages whose content comes from an unreachable external bundle.

- `.ti-work-grid`: gap 1px → 14px; removed the 1px solid border and the
  opaque grey background/border; background now matches the section's own
  paper tone (`#FBFAF7`, read from `.ti-sec-paper`) — an uncovered cell now
  reads as normal page background instead of a grey box.
- `.ti-shot`: added `border-radius:16px`, `overflow:hidden` (clips the
  absolutely-positioned image to the rounded corners), a soft card shadow
  (`0 10px 24px rgba(11,31,58,.12)`, deepening on hover), matching this
  site's other photo-card patterns.
- `.ti-imgfill`: matching `border-radius:16px` + a subtle `scale(1.045)`
  zoom on hover for interactivity.

`.ti-shot-wide` / `.ti-shot-tall` (the layout modifiers) were left
untouched — they only ever set `min-height`, so they inherit the new frame
automatically.
