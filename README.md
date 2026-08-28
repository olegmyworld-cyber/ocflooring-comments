# OC Flooring — Webflow fix scripts

Source records for custom code applied to the OC Flooring Webflow site
(`nwocflooring.com`, site id `6377e8e6a53936b48ef1cad0`). These are registered as
inline scripts via the Webflow Scripts API and applied at the site footer.

## Changes on branch `claude/oc-flooring-webflow-fixes-amosur`

### Bona sealer widget — "CUSTOMER FAVORITE" badge overlap (2026-06-14)

**Problem:** On mobile, the red `★ CUSTOMER FAVORITE` badge overlaid on the room
image overlapped the `LIVING / KITCHEN` room toggle pills in the Bona tone/sealer
widget (`#oc-tone-steps` / `#bona-tone-widget`).

**Fix:** Merged a badge-overlap guard into the existing `BonaMobileFix`
(`bonamobilefix`) script rather than adding a new one (the site footer was at its
15-script-per-block limit). The guard finds the badge and toggle by their visible
text (robust to the minified widget bundle's class names), measures their live
bounding boxes, and only repositions the badge (nudges it just below the toggle row)
when they actually overlap. Also keeps the badge on one line / slightly smaller on
phones. See [`webflow-scripts/bonamobilefix-1.0.0.js`](webflow-scripts/bonamobilefix-1.0.0.js).

Published live to `nwocflooring.com`, `www.nwocflooring.com`, and the Webflow
subdomain.

## Changes on branch `claude/slug-updates-website-bg10nn`

### Arlington folder + page slug change — sitewide link fixes (2026-08-28)

**Problem:** The `City of Arlington` folder slug changed from `city-of-arlington`
to `arlington`, and each of its six category pages dropped the `-in-arlington-wa`
suffix. Webflow auto-updates links stored as *page references*, but not links
stored as plain URLs — so anything hardcoded still pointed at the old
`/city-of-arlington/<service>-in-arlington-wa` paths.

| Old URL | New URL |
| --- | --- |
| `/city-of-arlington/hardwood-floor-refinishing-in-arlington-wa` | `/arlington/hardwood-floor-refinishing` |
| `/city-of-arlington/hardwood-floor-installation-in-arlington-wa` | `/arlington/hardwood-floor-installation` |
| `/city-of-arlington/vinyl-plank-flooring-installation-in-arlington-wa` | `/arlington/vinyl-plank-flooring-installation` |
| `/city-of-arlington/hardwood-floor-repair-in-arlington-wa` | `/arlington/hardwood-floor-repair` |
| `/city-of-arlington/carpet-installation-in-arlington-wa` | `/arlington/carpet-installation` |
| `/city-of-arlington/tile-installation-in-arlington-wa` | `/arlington/tile-installation` |

**Fixes applied via the Webflow Data API:**

1. **`Section // Areas` component** (203 instances — the "areas we serve" city
   grid on nearly every page). Three Arlington entries — Floor Repair, Carpet
   Installation and Tile Installation — were `url`-mode links on the old paths.
   Repointed them to `page`-mode links on the actual page IDs, matching how the
   Refinishing / Installation / Vinyl tabs already work, so a future slug change
   updates them automatically instead of silently breaking them.
2. **JSON-LD schema on all six Arlington pages.** Rewrote every stale absolute
   and relative URL in `@id`, `url`, `mainEntityOfPage` and `BreadcrumbList`
   entries (`#service`, `#faq`, `#bc`, `#breadcrumb` anchors included).

**Audited and clean — no changes needed:**

- The other 25 components, Navbar and Footer included.
- Page-level link elements on all 221 pages.
- All 17 HTML embeds on the six Arlington pages (including the JSON-LD inside
  the vinyl and installation FAQ embeds).
- CMS collections: Blogs (109 items), Galleries, Vinyl Galleries, Blog Categories.

**Still open (owner action):** add 301 redirects from the six old
`/city-of-arlington/...` URLs to the new ones in Site settings → Publishing, so
existing Google rankings and inbound links survive the move. Unrelated to this
change, the breadcrumb schema on the Arlington pages points at `/services/...`
paths (e.g. `/services/floor-refinishing`) while the live service pages sit
under `/flooring-services-near-me/...`.
