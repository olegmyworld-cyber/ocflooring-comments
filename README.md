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

## SEO

### Semrush 4xx client errors (2026-08-29)

23 URLs returning 404. Two were unpublished blog drafts linked from a live post — both
published via the CMS API, no redirect needed. The other 21 are paths that never existed
(`/services-near-me/*` instead of the real `/flooring-services-near-me/*`, plus five
city-level laminate pages that were never created) and need 301 redirects, which the
Webflow Data API cannot set.

Redirect table, verified targets, and the one remaining manual code fix:
[`seo/301-redirects-2026-08-29.md`](seo/301-redirects-2026-08-29.md).

### Semrush internal broken links (2026-08-29)

The companion report, from the source side: 22 links on 21 pages. The two blog links were
the drafts above. The other 20 are injected at runtime by a CDN-hosted script whose source
is unreadable from a sandboxed session, so they are corrected in the DOM by
`ocLinkFix` ([`webflow-scripts/oclinkfix-1.0.0.js`](webflow-scripts/oclinkfix-1.0.0.js)),
applied to the 20 source pages. Details, evidence, and the site-wide alternative:
[`seo/broken-internal-links-2026-08-29.md`](seo/broken-internal-links-2026-08-29.md).

### Semrush incorrect hreflang links (2026-08-29)

15 reported issues, traced to hand-written head custom code that names a stale URL in the
page's canonical tag, its three hreflang tags, `og:url`, and a "Guardrail" script — so 20
pages (not 15) tell Google their canonical version lives at a 404. One was fixable through
the API; the other 19 head blocks contain `<script>`, which Webflow's custom-code endpoint
refuses with HTTP 406, so they need a one-pass find-and-replace in the Designer. The same
audit found 155 dead `/services/…` URLs in the JSON-LD of 152 pages. Full findings, the
per-page edit list, and why none of it was patched with JavaScript:
[`seo/hreflang-canonical-2026-08-29.md`](seo/hreflang-canonical-2026-08-29.md).
