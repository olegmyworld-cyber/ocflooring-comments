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

### OpenAI Ads Manager pixel — `appointment_scheduled` conversion events (2026-08-10)

**Pixel setup script:** already installed site-wide (Site Settings → Custom Code →
Head Code) with pixel id `KJ9XC2XYzNhirk6GgaXQ86`, loading
`https://bzrcdn.openai.com/sdk/oaiq.min.js`. Left as-is — NOT duplicated. Note the
snippet has `debug:true` enabled.

**Conversion events (`OCOaiqEvents`):** appended to the site-wide **Footer Code**
block (Site Settings → Custom Code → Footer Code) because the applied-scripts
list is at Webflow's 15-script cap. Fires
`oaiq("measure","appointment_scheduled",{type:"customer_action",amount:0,currency:"USD"})`
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

### Head Code — unclosed `<style>` tag fix (2026-08-10)

**Problem:** In the site-wide Head Code, the `body, html {overflow-x: hidden}`
`<style>` block was never closed. Browsers treated everything up to the next
`</style>` (the site-wide LocalBusiness JSON-LD schema and the four font preload
links) as raw CSS text, so the schema markup and preloads were dead on every page.

**Fix:** Added the missing `</style>` immediately after the overflow rule. No
other characters in the head block were changed. Takes effect on next publish.

### Event renamed to standard `appointment_scheduled` (2026-08-10, follow-up)

The originally requested custom name `estimate_booked` is not valid as a direct
`oaiq("measure", ...)` event: OpenAI Ads only accepts its standard event
taxonomy there (custom names require the separate
`oaiq("measure","custom",{type:"custom"},{custom_event_name:...})` form and
can't be picked as a base event in Ads Manager's conversion dialog). Switched
all three triggers to the standard `appointment_scheduled` event
(`customer_action` shape, amount 0 USD) so it matches the "Appointment
scheduled" base event in Ads Manager. Verified with a 10-case headless-Chromium
test suite (postMessage booking, origin spoofing, link click, embed
suppression, form success/failure, missing-pixel guard) — all passing.

### Head font-override removed — typography reverted (2026-08-10, follow-up)

Closing the unclosed `<style>` tag had a side effect: a long-inert font-override
block (`ocfontstyle-static` — Playfair Display headings / Mulish body, plus
Google Fonts preloads) came alive and changed the site's look. Oleg preferred
the original typography, so that block was removed from the head entirely and
the site republished. The JSON-LD schema fix remains in place. The removed
block is archived in
[`webflow-scripts/removed-head-font-override.html`](webflow-scripts/removed-head-font-override.html)
with restore instructions.

### Green booking CTA accent (2026-08-10)

Oleg wants the "See Available Appointment" booking button to stand out from the
site's red/navy palette. Added `OCGreenCta` to the site-wide Footer Code block:
finds buttons/links by their visible text (robust to class changes) and applies
green `#1e7a3c` (hover `#166132`, white text, green focus ring). Published live.
Source: [`webflow-scripts/ocgreencta-1.0.0.js`](webflow-scripts/ocgreencta-1.0.0.js).
