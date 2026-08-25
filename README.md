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

## Changes on branch `claude/remove-why-different-nav-qwpgea`

### Navbar — removed "Why We're Different" link (2026-08-25)

**Request:** Remove the "Why We're Different" item from the site's navigation bar.

**Change:** Made directly in the Webflow site (no custom code involved). Deleted
the `NavbarLink` element (style `Nav Link`, element id
`8f0a51f1-09ac-f0dd-7a56-830df8c0e54d`) containing the "Why We're Different" text
from the shared `Navbar` component (component id
`6f76eb68-426e-d4a4-55b1-e419a08b720a`, used on 154 pages), via the Webflow MCP
Data API. The remaining nav links (About Us, Services, Our Work, Price, Financing,
phone) are untouched, and the `/why-were-different` page itself still exists — only
the nav link was removed.

Published live to `nwocflooring.com`, `www.nwocflooring.com`, and the Webflow
subdomain.
