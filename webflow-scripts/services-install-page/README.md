# Services page — Bellevue content port (2026-08-25)

Request: on `/services/hardwood-floor-installation` (page 65f32565e111adbbb806cf50),
add everything the Bellevue city page
(`/city-of-bellevue/hardwood-floor-installation-in-bellevue-wa`, page
65f32565e111adbbb806d03e) shows that the services page didn't, with matching
design.

Done via native HtmlEmbed ELEMENTS created through the Webflow element-builder
API (not footer scripts), placed directly in the page DOM. City-specific
wording generalized to the page's King & Snohomish County scope; markup, CSS
and JS otherwise copied verbatim from the Bellevue page so the design matches
exactly. Files here are the deployed embed contents (source of record):

| File | Section | Position on the page |
|---|---|---|
| `ochb.html` | Before/after photo slider + "Why Puget Sound Homeowners Choose Real Hardwood" checklist | before the "Here's How It Works" steps section |
| `ocitl.html` | Interactive 5-step technical install timeline (site prep → acclimation → moisture barrier → installation → trim & finish) | after the Installation Methods section |
| `ocse.html` | "Solid or engineered? Get your answer in one tap" interactive picker | after the install timeline |
| `ocflic.html` | Licensing/trust bar — Licensed & Insured / NWFA & Bona / Bonded chips, WA reg # OCFLOFL852KQ + L&I verify link, ★4.7 Google rating pill (verbatim) | after the big SEO section (.ohi) |
| `ocgd.html` | "Flooring Guides & Answers" blog links (uses existing site classes `ocgd-*`; self-moves before the footer) | before the site footer |

Also: a native "Section // Galllery" component instance was inserted before the
appointment CTA (same component as the Bellevue page; its Floor Type filter
stays at the default "any flooring type" because the API rejects writing that
filter prop — switch it to Hardwood in the Designer if wanted), and a small
embed appends three generalized condo/high-rise questions (from the Bellevue
FAQ) into the existing #oc2-faq section at runtime.

Skipped as already present or not visible: reviews (same 3 on both pages), FAQ
basics, city links, flooring types, install methods, guide cards
(#oc-install-guide exists on both), cost calculator (removed at runtime by
ocRemoveCostCalc on both pages), Bellevue neighborhood blocks (city-specific).

## Follow-ups (2026-08-25, same session)

- **Reviews moved:** a small embed repositions the `#oc2-reviews` "What
  Homeowners Say" section directly above `#oc-install-guide` ("Everything our
  hardwood floor installation covers"), re-asserting for 15s so it wins over
  the layout script.
- **Compact card redesign:** `compact-cards.css` (deployed as a page embed)
  restyles the native Flooring Types and Installation Methods sections from
  oversized 2x2 giant-image tiles into a compact 4-across card grid with 150px
  cover images, matching the newer sections' white-card/cream/navy design.
- **Mobile slider:** on phones (≤767px) the compacted Flooring Types and
  Installation Methods sections render as a swipeable horizontal scroll-snap
  slider (cards 86% wide with next-card peek, hidden scrollbar), matching the
  Bellevue page's mobile slider pattern; 768–991px stays a 2-across grid.

## Follow-up (2026-08-27, same session): "5 Steps" slider overlap + duplicate cities section

Request (screenshots): the "1. Book a Free Estimate / 2. In-Home Visit / …"
process-steps slider looked cramped/overlapping on mobile; asked to fix it,
and apply the same fix to the Flooring Types and Installation Methods
sliders too. Also: remove the "Hardwood Installation Across King &
Snohomish County" cities-pill section, since a separate cities section
already exists.

**Steps-slider root cause (confirmed via the Style API, not guessed):** the
steps section uses a native GLOBAL combo class,
`.steps-content-wrapper.is-services`, which sets
`display:flex;flex-direction:row;flex-wrap:wrap` **unconditionally — no
breakpoint override at all**. The plain `.steps-content-wrapper` class does
have a clean single-column mobile rule, but only below 480px, and the combo
class (higher specificity, no media query) wins at every normal phone width
in between — so 5 step cards wrap into a cramped multi-per-row layout with
no breathing room. Fixed by extending `compact-cards.css` (same page embed
as the Flooring Types/Installation Methods fix) with a `@media(max-width:
767px)` rule that turns `.steps-content-wrapper.is-services` into the same
clean horizontal scroll-snap slider pattern (86%-width cards, hidden
scrollbar) — scoped to this page only via the embed, not a global Style API
edit, since `.is-services` could plausibly be reused elsewhere and a page
embed carries zero risk of touching it. Desktop/tablet (>767px) keep the
original wrapping-row layout, unchanged.

**Flooring Types / Installation Methods — verified, not actually broken:**
reproduced both sections in headless Chromium using the *exact* native
Style-API values plus the *exact* live `compact-cards.css`. At 1280/800/390px
neither section shows any card-to-card overlap and the page never overflows
horizontally — the existing mobile-slider fix from 2026-08-25 is working
correctly. No change made to these two sections.

**Cities-list section removed:** "Hardwood Installation Across King &
Snohomish County" isn't native Designer content and isn't in any of this
page's 10 HtmlEmbeds — it also doesn't match the real "Section // Areas"
component (which has different content: "Proudly Serving Homeowners Across
King & Snohomish Counties" broken out per service category). It's almost
certainly rendered by `ocServicesLayout`, a page-scoped **hosted** script
whose source this environment can't read (network egress to
`cdn.prod.website-files.com` is blocked, same constraint hit earlier this
session). Rather than guess at its internals, added a new small registered
script, `ocRmAreasPage`
([`ocrmareaspage-1.0.0.js`](ocrmareaspage-1.0.0.js), 643 chars), applied to
**this page's footer only**: it finds the rendered heading containing
"Installation Across", climbs to the smallest ancestor whose text also
contains "Snohomish" (i.e. the full two-county section, not just the
heading), and removes it. Verified in headless Chromium against a mock with
decoy sections (including one that mentions "King County"/"Snohomish" in an
unrelated sentence, to rule out false positives) — the target section is
removed cleanly and every decoy is left untouched, at every viewport.

Published live to `nwocflooring.com`, `www.nwocflooring.com`, and the
Webflow subdomain.

## Follow-up (2026-08-27, same session): "All problems still stay" — hardened both fixes

User report after the above: both issues were still visible live, despite
the CSS/script being verified correctly saved and the site verified
compiled. Re-checked everything server-side again (embed content, applied
scripts, publish timestamps) — all still exactly as deployed, ruling out a
silent revert or failed publish. That points at a **timing** bug in the
original fixes rather than a wrong selector or bad CSS:

- **`ocRmAreasPage` v1.0.0** polled for the target heading for a fixed 120
  tries × 500ms = 60 seconds, then gave up. If the cities section is
  lazy-rendered by `ocServicesLayout` (e.g. only built once its container
  scrolls into view, or on some other delayed trigger this environment
  can't inspect — the script is externally hosted and unreadable here),
  a real visitor scrolling down the page past the 60s mark would see it
  appear *after* the script had already stopped looking, with nothing to
  remove it.
- The original steps-slider CSS fix could in principle be fought at
  runtime by the same unreadable `ocServicesLayout` script if it reasserts
  its own inline styles on `.steps-content-wrapper.is-services` — plausible
  given its name, though unconfirmed since its source isn't readable here.

**Fix — replaced fixed-timeout polling with indefinite detection:**
- `ocRmAreasPage` → **`ocRmAreasPageV2`**
  ([`ocrmareaspagev2-1.0.0.js`](ocrmareaspagev2-1.0.0.js)): same
  heading-climb removal logic, but now primarily driven by a
  `MutationObserver` on `document.body` (fires immediately whenever new
  content is inserted, no matter how late), with the original 500ms poll
  kept as a much longer (5-minute) belt-and-suspenders fallback.
- New **`ocStepsEnforce`**
  ([`ocstepsenforce-1.0.0.js`](ocstepsenforce-1.0.0.js)): defensively
  re-applies the mobile slider styles to `.steps-content-wrapper.is-services`
  and its `.steps-inner-wrap` children as `!important` **inline** styles
  (via `style.setProperty(..., 'important')`, which beats a stylesheet
  `!important` rule) on load, on resize, on any DOM mutation, and on a
  1-second interval — and cleanly removes those inline overrides above
  767px so desktop is unaffected either way.

**Verified in headless Chromium** against two adversarial scenarios in one
test: (1) a competing script that resets the steps section's `flex-wrap`
back to `wrap` every 150ms — `ocStepsEnforce`'s 1s interval still keeps it
correctly as a non-wrapping slider at mobile widths; (2) the cities section
injected into the DOM 4 seconds in (standing in for a lazy/delayed
render, deliberately timed to be well past what a fixed-poll script would
tolerate) — `ocRmAreasPageV2`'s `MutationObserver` catches and removes it
almost immediately. Resizing back to desktop after all of this correctly
restores the original wrapping-row layout with no leftover inline styles.

## ROOT CAUSE FOUND (2026-08-27): registered inline scripts containing `<` never run

User reported a third time that nothing had changed. Both prior "fixes"
were verified saved server-side and the site verified compiled — yet had
zero effect. The reason: **neither script ever executed.**

This repo's own top-level README already documents the rule, discovered
earlier in the same session on the Calendly card (v1.2.0 → v1.3.0):
Webflow's **registered inline script** pipeline on this site silently
drops scripts containing tag-like `<` sequences — the v1.3.0 fix note
records that "the deployed minified source contains no `<` character at
all" and rewrites comparisons as `len>i` for exactly this reason.

Both `ocRmAreasPageV2` and `ocStepsEnforce` contained `<` in ordinary loop
conditions (`i<hs.length`, `i<kids.length`, `indexOf(...)<0`). So they were
dropped on deploy, every time — which is why two rounds of otherwise-correct
logic produced no visible change whatsoever.

Confirmed the boundary of the rule: **HtmlEmbed *elements* tolerate `<` fine**
— `ocgd.html` (28 `<` characters) renders on this very page, visible in the
user's own screenshot as "Flooring Guides & Answers". It is specifically
*registered inline scripts* that are affected. Every registered inline
script on this site that is known to work (e.g. `ochidefinancingnav`)
contains zero `<`.

**Fix:** both behaviours were merged into a single script delivered as an
**HtmlEmbed element** appended to the page body
([`pagefix-embed.js`](pagefix-embed.js)) — the delivery mechanism proven to
work on this page — and the two dead registered scripts were removed from
the page. (The script is *also* written with zero `<` characters, so it is
valid under either mechanism.)

### A second real bug the tests caught: content-box card overflow

While testing the slider enforcement, the mock showed cards rendering
**385.6px wide inside a 374px track** — wider than their own container,
which is precisely what "overlapping / card clipped at the screen edge"
looks like in the user's screenshot. Cause: the cards carry `padding:2rem`
and, without `box-sizing:border-box`, `width:86%` sets the *content* box —
so 86% + 64px of padding overflows the track. Fixed by also forcing
`box-sizing:border-box` on the cards; card then measures 322px = a correct
86% of the track.

The script is also **structure-aware**: it styles the *actual parent of the
cards* rather than assuming they are direct children of `.services-wrap` /
`.steps-content-wrapper`. If the page's own (externally hosted, unreadable
here) `ocServicesLayout` script nests the cards inside its own track
element, the earlier CSS child-combinator rules
(`.services-wrap>.services-item-wpapper`) would silently stop matching —
the JS handles that case, and neutralises the outer wrapper so the track
spans full width and the percentage math stays correct.

**Verified in headless Chromium** with cards deliberately nested one level
deeper than expected, a heading rendered as a `div` (not an `h2` — the old
selector only searched `h1`–`h4` and would have missed it), the cities
section injected 3s late, and a competing script fighting the layout every
150ms: slider correct at 390px, cards fit the track, no page overflow,
cities section removed, decoy text containing "King County"/"Snohomish"
left untouched, and all inline overrides cleanly removed on resize to
desktop.

Published live to `nwocflooring.com`, `www.nwocflooring.com`, and the
Webflow subdomain.
