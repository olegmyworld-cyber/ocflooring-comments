from builder import *

S = 'tile-shower-waterproofing'

parts = [
date_badge('October 27, 2026'),

quick_answer(
 "<strong>A tile shower is waterproofed by everything you cannot see: a pre-sloped pan, a continuous bonded membrane on the floor and walls, sealed corners and drain connections, "
 "and a flood test before a single tile goes on.</strong> Tile and grout are the wear surface, not the waterproofing &mdash; water passes through grout routinely and the membrane "
 "behind it is what sends that water to the drain instead of into your framing. Every shower we build in Redmond gets a pre-slope, a bonded membrane, and a photographed 24-hour "
 "flood test, because a leak discovered after tile is a demolition, not a repair.",
 'Redmond homes &amp; remodels'),

facts([
 ('24 hours', 'how long every finished pan sits full of water before we tile it. We photograph the flood test and keep it on record &mdash; proof the assembly held before it disappeared behind tile.'),
 ('$14&ndash;$26/sq ft', 'installed tile cost with us, labor from $11/sq ft. In a shower, the waterproofing hours are the biggest share of that number &mdash; and the best money in the whole project.'),
 ('2 years', 'our warranty on tile work, double the one-year most of the trade offers. We can afford the bet because of what goes in behind the tile.'),
]),

'<h2>Grout Is Not Waterproof. Neither Is Tile.</h2>',

"<p>Start with the fact that reorganizes everything else: <strong>a tiled surface leaks by design</strong>. Cement grout is porous &mdash; it absorbs water on every shower's every use "
"&mdash; and even the joints between perfectly set porcelain let moisture migrate through. This is not a defect. The tile industry has never pretended otherwise. Tile and grout are a "
"wear surface: they take the abrasion, the cleaning, the thermal swings, and they look good doing it. Keeping water out of the wall is a different job, done by a different layer.</p>",

"<p>That layer is the membrane behind the tile, and it changes how you should judge any shower quote. A bid that describes beautiful tile and says nothing specific about the "
"waterproofing is describing the paint job on a car with no engine. When the membrane is missing or wrong, the shower still looks perfect on day one &mdash; and water spends the "
"next two or three years quietly reaching the studs, the subfloor, and the ceiling below. By the time anything shows, the fix is demolition. The tile you paid for comes off in "
"pieces, because there is no other way in.</p>",

'<h2>The Full Assembly, Layer by Layer</h2>',

"<p>Here is the complete system in the order it is built. None of these layers is optional, and each one covers a specific way showers fail.</p>",

table('What Is Behind a Properly Built Tile Shower', ['Layer', 'What it does', 'What failure looks like without it'], [
 ('<strong>Pre-slope</strong>', 'A sloped mortar bed <em>under</em> the membrane, pitched to the drain', 'Water that passes the tile sits flat on the membrane forever &mdash; the classic musty shower'),
 ('<strong>Pan membrane</strong>', 'The waterproof layer of the floor, bonded or laid over the pre-slope', 'Subfloor rot, and stains on the ceiling below a second-story bath'),
 ('<strong>Wall membrane</strong>', 'Sheet or liquid coverage over the backer board, lapped into the pan', 'Wet studs and swollen drywall on the far side of the wall'),
 ('<strong>Sealed corners &amp; seams</strong>', 'Preformed corners, banded seams, membrane lapped shingle-style', 'Corners are where most assemblies actually leak &mdash; gravity finds the laps'),
 ('<strong>Drain integration</strong>', 'The membrane clamped or bonded directly to the drain flange', 'A perfect membrane that drains into the joist bay at its lowest point'),
 ('<strong>Curb or curbless slope</strong>', 'Waterproofed curb, or a recessed floor pitched for a curbless entry', 'Water wicking into the curb frame &mdash; the softest spot in old showers'),
 ('<strong>Niche &amp; benches</strong>', 'Every shelf and seat waterproofed like a tiny shower of its own', 'Niches are leak point number two after corners &mdash; they interrupt the membrane'),
 ('<strong>Flood test</strong>', 'The pan plugged and filled for 24 hours, before tile', 'No test means the first real test is your first shower &mdash; with tile already on'),
]),

"<p>Two details in that table deserve emphasis, because they are the ones cheap builds skip most. The <strong>pre-slope</strong> exists because the membrane, not the tile, is the "
"true floor of your shower &mdash; and if the membrane lies flat, the water that reaches it has nowhere to go. And the <strong>niche</strong>: every hole cut into a waterproofed "
"wall is a hole in the waterproofing, which is why niche placement and sealing get their own discipline &mdash; we wrote up how in "
"<a href=\"/blog/shower-niche-placement-size-waterproofing\">our shower niche guide</a>.</p>",

'<h2>Bonded Sheet vs Liquid-Applied: Two Right Answers</h2>',

"<p>There are two legitimate ways to build the membrane, and good tile setters use both. <strong>Bonded sheet membranes</strong> &mdash; Schluter Kerdi is the name most people know "
"&mdash; come off a roll at a factory-controlled thickness and get thin-set directly to the walls and pan. Their strength is consistency: the material is never too thin, and the "
"system's preformed corners and drain assembly take the guesswork out of the hard spots. Their risk lives at the seams, which is why seam technique separates a real installer "
"from someone who watched a video.</p>",

"<p><strong>Liquid-applied membranes</strong> are rolled or troweled on in coats to a measured wet-film thickness. Their strength is that a liquid has no seams &mdash; it flows around "
"corners, valves and odd geometry as one continuous skin. Their risk is thickness: too thin in one pass, or rushed between coats, and the protection is theoretical. The honest "
"summary is that <em>both systems outlast the house when executed and both fail promptly when rushed</em> &mdash; which means the product name on the quote matters less than whether "
"the installer can tell you coverage, thickness, and cure time without looking anything up. What never works is skipping the membrane and trusting cement board: cement board is "
"unbothered by water, but it is not waterproof, and it will happily pass every gallon through to the framing behind it.</p>",

two_col(
 'Signs a shower was built right',
 ['A pre-slope under the membrane, not just under the tile',
  'A named membrane system &mdash; sheet or liquid &mdash; on the quote',
  'Preformed corners and banded seams, or measured liquid thickness',
  'The membrane bonded or clamped to the drain flange',
  'A photographed flood test before tile went on',
  'Silicone, not grout, at every change of plane'],
 'Signs the waterproofing was skipped',
 ['&ldquo;Waterproofing&rdquo; appears nowhere on the quote',
  'Tile going straight onto cement board or green board',
  'A flat pan liner with no pre-slope beneath it',
  'Grout caulked over cracks at the corners every year',
  'Musty smell that cleaning never fixes',
  'A price dramatically below every other bid &mdash; the membrane is the difference']),

'<h2>The Flood Test: One Day That Protects Ten Years</h2>',

"<p>Before tile, we plug the drain and fill the finished pan with water &mdash; and then we leave it alone for 24 hours. If the level holds, the pan is proven tight and we "
"photograph it for the job file. If it drops, we have found the problem at the cheapest possible moment: nothing above the pan has been built, nothing has to be demolished, and "
"the fix is a day instead of a remodel. That photograph stays on record, which means years later there is documented proof your shower held water before the tile ever went on.</p>",

"<p>The test costs us a day of schedule, which is exactly why low bids skip it. But think about what the alternative test is: your family, showering daily, over a finished "
"ceiling. A leak that announces itself through drywall stains has usually been running for months. One day of patience against that outcome is the cheapest insurance in the "
"entire project, and it is standard on every shower we build &mdash; the same assembly logic that runs through our "
"<a href=\"/blog/curbless-shower-build-mercer-island\">curbless shower build guide</a>, where the tolerances are even tighter.</p>",

'<h2>Why This Matters in Redmond Specifically</h2>',

"<p>Redmond's housing stock puts more showers on second floors than almost anywhere we work. The 1980s and 90s subdivisions around Education Hill and Abbey Road, and the newer "
"townhomes near downtown, mostly stack the bathrooms over kitchens and living rooms &mdash; so when a shower assembly fails, it does not fail quietly into a crawlspace. It fails "
"through the ceiling of the room you host in. Those 80s and 90s showers are also now thirty to forty years old, which is past the design life of the original builder-grade pans; "
"a surprising share of the &ldquo;small regrout job&rdquo; calls we get turn out to be original assemblies at end of life.</p>",

"<p>If you are opening a shower anyway, that is the moment to fix everything behind it &mdash; substrate included, which is covered in "
"<a href=\"/blog/tile-underlayment-explained\">our underlayment explainer</a> &mdash; and to think about whether the surrounding floor should be redone in the same mobilization; "
"tiling over what is there is sometimes legitimate on floors, as we lay out in <a href=\"/blog/can-you-tile-over-existing-tile\">tiling over existing tile</a>, but never inside a "
"shower. What the whole rebuild costs is itemized in our <a href=\"/blog/bathroom-tile-installation-cost-seattle\">bathroom tile cost guide</a>, and the full local scope is on the "
"<a href=\"/city-of-redmond/tile-installation-in-redmond-wa\">Redmond tile installation page</a>.</p>",

faq('Tile Shower Waterproofing: What Homeowners Ask Us', [
 ('How do you waterproof a tile shower?',
  'With a system behind the tile: a pre-sloped mortar bed, a continuous bonded membrane over the pan and walls, sealed corners and seams, the membrane integrated with the drain flange, and waterproofed details at the curb, niche and bench. The pan is then flood-tested for 24 hours before tile is installed. The tile and grout on top are the wear surface, not the waterproofing.'),
 ('Is grout waterproof?',
  'No, and it was never meant to be. Cement grout is porous and absorbs water in normal use; sealing slows this but does not stop it. A correctly built shower assumes water gets through the tiled surface and uses the membrane behind it to carry that water back to the drain. If your shower stays dry, it is the membrane doing it, not the grout.'),
 ('What is a shower pre-slope and why does it matter?',
  'A pre-slope is a pitched mortar bed installed under the waterproof membrane, so the membrane itself tilts toward the drain. Without it, the membrane lies flat, and the water that inevitably passes through grout collects on it and sits there permanently. That standing layer is the source of the musty smell in many older showers, and no amount of surface cleaning reaches it.'),
 ('Which is better, a sheet membrane like Kerdi or a liquid membrane?',
  'Both are legitimate, and we use both. Sheet systems give factory-consistent thickness and engineered corners, with seams as the skill point. Liquid systems are seamless and conform to complex geometry, with applied thickness as the skill point. Execution matters more than the brand: an installer who can state coverage, thickness and cure times from memory will build you a dry shower with either.'),
 ('What is a flood test on a shower?',
  'The drain is plugged and the finished pan is filled with water for 24 hours before any tile is installed. If the water level holds, the pan is proven watertight; if it drops, the leak is found while it is still a one-day fix instead of a demolition. We photograph every flood test and keep it on record for the job.'),
 ('Is cement board waterproof on its own?',
  'No. Cement board is water-resistant, meaning water does not destroy it, but water passes through it freely and into the studs behind. It is the correct backing for a shower wall, and it still needs a bonded sheet or liquid membrane over it. Tile set straight onto bare cement board is one of the most common failures we open up.'),
 ('How do I know if my existing shower was waterproofed properly?',
  'From outside, look for the symptoms: grout that cracks at the corners every year, tiles sounding hollow low on the walls, a musty smell that cleaning never kills, or any stain on the ceiling below. None of them is conclusive alone, but each is a reason to investigate before resealing over the problem. The only certain answer comes from opening a small section, which we do and photograph before quoting a rebuild.'),
 ('How much does waterproofing add to the cost of a tile shower?',
  'It is a substantial share of the labor in any honest shower quote, and it is the main reason quotes spread so far apart. Our tile work runs $14 to $26 per square foot installed with labor from $11 per square foot, and in a shower, the membrane system, the details at corners, curb, niche and drain, plus the flood-test day are where those hours go. It is also the entire difference between a shower and a slow leak with nice tile on it.'),
]),

cta('Get a Shower That Was Proven Before It Was Tiled',
    'Pre-slope, bonded membrane, photographed 24-hour flood test &mdash; on every shower, not on request. We will open up what you have, show you exactly what is behind it, and put the rebuild in writing. Free in-home estimates across King &amp; Snohomish County.'),

related([
 ('/blog/shower-niche-placement-size-waterproofing', 'Shower niches done right'),
 ('/blog/curbless-shower-build-mercer-island', 'What a curbless shower takes'),
 ('/blog/tile-underlayment-explained', 'Tile underlayment explained'),
 ('/blog/bathroom-tile-installation-cost-seattle', 'Bathroom tile cost in Seattle'),
 ('/city-of-redmond/tile-installation-in-redmond-wa', 'Tile installation in Redmond'),
 ('/contact', 'Book a free estimate'),
]),
]

assemble(S, parts)
