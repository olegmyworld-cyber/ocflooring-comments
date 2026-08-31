from builder import *

S = 'rental-property-carpet'

parts = [
date_badge('February 18, 2027'),

quick_answer(
 "<strong>The right carpet for a rental is a solution-dyed polyester or nylon in a flecked mid-tone neutral, over a mid-grade pad &mdash; not the cheapest thing on the rack, "
 "and not what you would put in your own bedroom either.</strong> Landlord math is not price per square foot, it is cost per tenant-year: a bargain carpet that survives one "
 "tenancy costs more than a mid-grade one that survives three. Solution-dyed fiber shrugs off the aggressive cleaning a turnover needs, the mid pad keeps the carpet from "
 "wearing out from below, and the flecked neutral photographs well in every listing for a decade.",
 'Woodinville rental owners'),

facts([
 ('From $1.49/sq ft', 'where installed carpet starts with us, pad and labor included. On a rental unit the spread between builder-grade and the rental spec is small money against one month of vacancy &mdash; which is the number that actually hurts.'),
 ('Cost per tenant-year', 'the only metric that matters. Divide installed cost by the tenancies the carpet survives. A cheap carpet replaced every turnover loses that arithmetic to a mid-grade carpet every single time.'),
 ('One day', 'how long most units take to install once the carpet is in. We schedule between tenants &mdash; measure before the old tenant leaves, install the day after the unit empties, listing photos by the weekend.'),
]),

'<h2>Landlord Math: Cost per Tenant-Year</h2>',

"<p>Homeowners buy carpet on feel and looks. Landlords should buy it on arithmetic. Take the installed cost, divide by the number of tenancies it survives, and compare "
"<em>that</em> number. The cheapest carpet on the rack looks like the obvious rental choice right up until you run it: bargain goods with a bargain pad routinely need replacing "
"after a single hard tenancy &mdash; matted traffic lanes, stains that will not lift, a smell the next applicant notices in the doorway. The mid-grade spec costs modestly more "
"on install day and routinely survives three tenancies. Per tenant-year it is not close.</p>",

"<p>The hidden line in the math is vacancy. Worn-out carpet does not just cost its replacement price &mdash; it costs the days the unit sits while you scramble a contractor, "
"and it costs applicants who walked through, wrinkled their nose, and applied somewhere else. A durable, honest floor is cheap insurance against both. How long each grade "
"actually lasts is a subject we covered straight in <a href=\"/blog/how-long-does-carpet-last\">how long carpet lasts</a>; rentals sit at the hard end of every range there.</p>",

'<h2>The Rental Spec, Line by Line</h2>',

"<p>Here is what we actually recommend when an owner tells us the unit is a rental. It is a short list, and every line is chosen for the same reason: it survives tenants who "
"did not buy the carpet and will not baby it.</p>",

table('What Landlords Should Buy, and Why', ['Decision', 'The rental answer', 'Why'], [
 ('<strong>Fiber</strong>', 'Solution-dyed polyester or nylon', 'Color runs through the fiber, so turnover-strength cleaning cannot fade it &mdash; you can attack year-two stains at full strength'),
 ('<strong>Pad</strong>', 'Mid-grade, 8 lb density class', 'The cheap pad is what actually kills rental carpet &mdash; it collapses, then the carpet mats. The premium pad is comfort you are giving away'),
 ('<strong>Color</strong>', 'Flecked mid-tone neutral', 'Hides traffic lanes and sins between deep cleans, photographs well in listings, offends no applicant'),
 ('<strong>Pile</strong>', 'Short-to-medium textured cut pile', 'Dense and low wears best; deep plush mats and holds odors; textured hides vacuum tracks between showings'),
 ('<strong>Style</strong>', 'One carpet, every carpeted room', 'One dye lot, one leftover roll for future patches, one repurchase decision instead of five'),
 ('<strong>Extras worth it</strong>', 'Moisture-barrier pad if pets are allowed', 'Accidents stop at the pad instead of soaking the subfloor &mdash; the difference between a cleaning bill and a replacement'),
 ('<strong>Extras not worth it</strong>', 'Premium softness, wool, deep pile', 'Tenants do not pay more rent for plush &mdash; spend the difference on paint and fixtures they do notice'),
]),

"<p>The one line worth expanding: <strong>solution-dyed fiber</strong>. Ordinary carpet is dyed after the fiber is made, so the color sits on the surface and aggressive "
"cleaning slowly strips it &mdash; which is exactly the cleaning a turnover requires. Solution-dyed fiber has the pigment mixed in before extrusion; the color goes all the way "
"through, like a carrot rather than a radish. Between tenants you can hot-water extract, spot-treat with enzymes, and scrub the traffic lanes hard, year after year, without "
"bleaching pale patches into the floor. The full fiber rundown is in <a href=\"/blog/carpet-fiber-types\">nylon, polyester, or wool</a> &mdash; for rentals, the solution-dyed "
"column wins regardless of which polymer you pick.</p>",

'<h2>The Pad Is Where Cheap Rentals Go Wrong</h2>',

"<p>When a landlord shows us a unit with carpet that died young, the carpet is usually not the culprit &mdash; the pad is. Builder-grade pad crushes flat in the traffic lanes "
"within a couple of years; once it does, every footstep lands on the carpet backing directly, and the fibers mat permanently no matter what the carpet cost. Replacing carpet "
"over a dead pad is throwing good money after bad.</p>",

"<p>The fix costs very little: specify the mid-grade pad, the 8-pound density class, under every room. Not the premium pad &mdash; that is comfort spend, and comfort is not "
"what a rental sells &mdash; but never the bottom grade. We wrote the longer argument in <a href=\"/blog/carpet-padding-thickness\">carpet padding: the half of the job nobody "
"shops for</a>, and it applies to rentals double: the pad is invisible in the listing photos and decisive in year three.</p>",

'<h2>Turnovers: Clean, Patch, or Replace</h2>',

"<p>Not every scuffed carpet needs replacing at move-out, and replacing too early is its own leak in the budget. The honest triage: <strong>clean</strong> when the problem is "
"soil &mdash; a professional hot-water extraction between tenants recovers more carpet than most owners expect, especially solution-dyed goods. <strong>Patch and restretch</strong> "
"when the damage is local &mdash; a burn, a bleach spot, a pet corner, ripples from years of traffic; this is exactly why we tell owners to keep the leftover roll from the "
"install. <strong>Replace</strong> when the traffic lanes are matted flat and will not recover, when odor has reached the pad, or when the backing is delaminating &mdash; the "
"same signals we listed in <a href=\"/blog/when-to-replace-carpet\">five signs it is time to replace carpet</a>.</p>",

"<p>Two bookkeeping notes worth knowing. Keep the install invoice: carpet in a rental is a depreciable improvement, and your accountant will want the date and amount. And "
"document condition with photos at every move-in and move-out &mdash; normal wear is the owner's cost, genuine damage is a deposit conversation, and the difference is much "
"easier to demonstrate with pictures than with adjectives. When the old carpet does come out, <a href=\"/blog/carpet-removal-cost\">removal and haul-away</a> is part of our "
"number, not a surprise line at the end.</p>",

'<h2>Where Carpet Belongs in a Rental &mdash; and Where It Does Not</h2>',

"<p>Honest answer: not everywhere. In most rentals we would put a hard surface in the entry, kitchen, baths and main living path, and carpet in the bedrooms and upstairs. "
"Carpet wins bedrooms on cost, warmth, and sound &mdash; in a two-story rental or anything with neighbors below, carpeted upstairs floors quietly prevent the most common "
"noise complaint there is. Hard surface wins everywhere water, food, and shoes concentrate. That split also localizes your turnover cost: the rooms that take the abuse have "
"the floor that shrugs it off, and the carpet you do replace is a bedroom at a time, not the whole unit.</p>",

"<p>We work with a lot of owners and property managers on exactly this split &mdash; multiple units, phased schedules, same spec across a portfolio so every future repair "
"matches. That side of the shop is described in <a href=\"/blog/flooring-services-tailored-for-real-estate-success\">flooring services for real estate</a>, and the local "
"details are on our <a href=\"/city-of-woodinville/carpet-installation-in-woodinville-wa\">Woodinville carpet installation page</a>. Woodinville rentals skew toward "
"single-family houses and townhomes rather than big complexes, which raises the stakes per unit: one house, one tenant, one carpet &mdash; buy the spec that survives the "
"tenancy after this one.</p>",

two_col(
 'Our rental spec',
 ['Solution-dyed polyester or nylon, textured cut pile, short to medium',
  'Mid-grade 8 lb-class pad in every room &mdash; never the bottom grade',
  'Flecked mid-tone neutral, one carpet across all carpeted rooms',
  'Moisture-barrier pad wherever pets are allowed',
  'Leftover roll labeled and stored for future patches',
  'Install scheduled inside the turnover window, photos before listing'],
 'Mistakes that cost landlords money',
 ['Buying the cheapest carpet and the cheapest pad together',
  'Premium plush a tenant will never pay extra rent for',
  'White or solid pale carpet in a unit with real turnover',
  'Replacing whole units when a patch and a deep clean would do',
  'Different carpet in every room &mdash; five dye lots, five repurchases',
  'No move-in photos, then arguing about the deposit from memory']),

faq('Rental Property Carpet: What Landlords Ask Us', [
 ('What is the best carpet for a rental property?',
  'Solution-dyed polyester or nylon, short-to-medium textured cut pile, flecked mid-tone neutral, over a mid-grade pad. Every element is chosen to survive tenants and turnover cleaning rather than to feel luxurious. It costs modestly more than builder-grade and routinely lasts two or three times as many tenancies, which wins the math decisively.'),
 ('How much does carpet cost for a rental unit?',
  'Installed carpet starts at $1.49 per square foot with us, including pad and labor, and the rental spec sits toward the affordable end of the range on purpose. We measure the unit, quote it in writing the same visit, and can schedule the install inside a turnover window so the carpet is done before the listing photos.'),
 ('How long should carpet last in a rental?',
  'Rentals are the hard end of every lifespan range — expect fewer years than the same carpet would give an owner-occupier. Builder-grade goods over cheap pad can be done after a single hard tenancy; the rental spec over a mid pad routinely survives three or more. The pad is usually what decides it, not the carpet.'),
 ('Do I have to replace carpet between every tenant?',
  'No, and doing so wastes money. Triage instead: professional hot-water extraction handles soil, a patch from your leftover roll handles local damage, and a restretch handles ripples. Replace only when traffic lanes are matted flat, odor has reached the pad, or the backing is failing. Solution-dyed carpet makes the clean-and-keep option succeed far more often.'),
 ('Is cheap carpet ever the right call for a rental?',
  'Occasionally — a unit you plan to gut-renovate in two years does not need carpet built for ten. But as a standing policy, the cheapest carpet plus the cheapest pad is the most expensive combination landlords buy, because it gets repurchased every turnover. If the budget forces a cut, cut the carpet grade before you ever cut the pad.'),
 ('Should I put LVP everywhere instead of carpet?',
  'In the wet and high-traffic rooms, hard surface usually is the better rental answer, and we will tell you so. Carpet keeps winning bedrooms and upper floors: it is cheaper per square foot, warmer in the photos, and it is the difference between a quiet duplex and a noise complaint. The split — hard surface in the path, carpet in the bedrooms — is what we install most for landlords.'),
 ('Can you handle multiple units or coordinate with my property manager?',
  'Yes. We keep the spec on file so every unit and every future patch matches, schedule installs against turnover dates rather than our convenience, and can work directly with a property manager on access and timing. Most single units are measured in one visit and installed in a day.'),
 ('What about tenants with pets?',
  'If you allow pets, spec the moisture-barrier pad — it stops accidents at the pad line instead of letting them reach the subfloor, which is where permanent odor lives and where a cleaning bill becomes a replacement bill. Pair it with solution-dyed fiber and most pet tenancies end with a deep clean instead of a tear-out.'),
]),

cta('Get a Rental Spec and a Written Number',
    'Tell us the unit and the turnover date. We measure in one visit, quote the rental spec in writing &mdash; solution-dyed carpet, mid-grade pad, haul-away included &mdash; and install in a day so the listing photos happen on schedule. Free estimates across King &amp; Snohomish County.'),

related([
 ('/blog/how-long-does-carpet-last', 'How long carpet actually lasts'),
 ('/blog/carpet-padding-thickness', 'Carpet padding, explained honestly'),
 ('/blog/carpet-fiber-types', 'Carpet fibers compared'),
 ('/blog/when-to-replace-carpet', 'Five signs it is time to replace carpet'),
 ('/city-of-woodinville/carpet-installation-in-woodinville-wa', 'Carpet installation in Woodinville'),
 ('/contact', 'Book a free estimate'),
]),
]

assemble(S, parts)
