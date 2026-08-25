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
