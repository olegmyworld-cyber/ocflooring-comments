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

## Changes on branch `claude/openai-ads-pixel-tracking-qoqapj`

### OpenAI Ads Manager pixel — `estimate_booked` conversion events (2026-08-10)

**Pixel setup script:** already installed site-wide (Site Settings → Custom Code →
Head Code) with pixel id `KJ9XC2XYzNhirk6GgaXQ86`, loading
`https://bzrcdn.openai.com/sdk/oaiq.min.js`. Left as-is — NOT duplicated. Note the
snippet has `debug:true` enabled.

**Conversion events (`OCOaiqEvents`):** appended to the site-wide **Footer Code**
block (Site Settings → Custom Code → Footer Code) because the applied-scripts
list is at Webflow's 15-script cap. Fires
`oaiq("measure","estimate_booked",{type:"customer_action",amount:0,currency:"USD"})`
on:

1. **Calendly booking completed** — listens for the `calendly.event_scheduled`
   postMessage (origin-checked against `*.calendly.com`), which covers both inline
   embeds and Calendly popup widgets on any page.
2. **External `calendly.com` link click** — only when the page has *no* Calendly
   embed, so embedded pages count real bookings, not clicks (runtime detection;
   no double counting either way).
3. **Successful quote/contact form submission** — hooks every Webflow form
   (currently the "Quiz Form" quote calculator on `/flooring-calculator`) and
   fires only after the `.w-form-done` success state is actually shown, never on a
   failed/attempted submit. Search inputs are excluded.

All calls are guarded (`typeof window.oaiq === "function"`) and deduped per page
load. Readable source: [`webflow-scripts/ocoaiqevents-1.0.0.js`](webflow-scripts/ocoaiqevents-1.0.0.js).

Not yet published — pending review in Webflow. (A registered-script copy
`ocOaiqEvents 1.0.0` also exists in the site's script library but is not applied
anywhere; the footer block is the live copy.)
