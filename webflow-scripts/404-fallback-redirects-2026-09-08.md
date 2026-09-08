# 404 page fallback redirect script (page-level footer code on /404, page id 65f32565e111adbbb806cea8)

Why this file exists: on 2026-09-06/07 visitors clicking "Tile Installation in Seattle, WA" from a blog post
landed on /seattle/hardwood-floor-installation-in-seattle-wa. Root cause (GA4-confirmed, 7 pageviews with the
blog post as referrer): the tile city page was returning 404 for a stretch, and this script's `cls()` had no
tile/carpet branch, so it classified the slug by the word "installation" and location.replace()d to the hardwood
page in the same city. The tile/carpet branches were added 2026-09-06 20:49Z; from 2026-09-07 10:18 PT the click
lands on the tile page. The CMS links and the blog template scripts (OCLinkMatch / OCLinkClick) were never wrong.

Hardening applied 2026-09-08 (change inside target()): when the missing URL is itself the canonical
`<service>-in-<city>-wa` page (i.e. the keyword mapping would just reproduce the same path), fall back to that
service's main page under /flooring-services-near-me/, never to a different service. Legacy remaps
(/city-of-arlington/* -> /arlington/*, laminate -> vinyl, old slugs) are unchanged.

Node check of the new target():
  /seattle/tile-installation-in-seattle-wa            -> /flooring-services-near-me/tile-installation   (was: hardwood in Seattle before 09-06)
  /city-of-bellevue/carpet-installation-in-bellevue-wa -> /flooring-services-near-me/carpet-installation
  /city-of-arlington/tile-installation-in-arlington-wa -> /arlington/tile-installation                 (legacy remap kept)
  /city-of-everett/laminate-flooring-installation-in-everett-wa -> /city-of-everett/vinyl-plank-flooring-installation-in-everett-wa (legacy laminate mapping kept)
  /seattle/stair-installation-in-seattle-wa           -> /seattle/hardwood-floor-installation-in-seattle-wa (still a keyword guess; add a branch if stair city pages are ever built)

Full current script: see the /404 page footer custom code in Webflow (data_scripts_tool get_page_freeform_code).
