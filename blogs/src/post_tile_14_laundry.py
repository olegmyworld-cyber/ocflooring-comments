from builder import *

S = 'laundry-room-tile'

parts = [
date_badge('December 1, 2026'),

quick_answer(
 "<strong>The laundry room is the one floor in the house you should choose on the assumption that it will someday be underwater.</strong> Washing machine supply hoses fail, drains back up, "
 "and a load of water arrives with nobody home to see it. Tile is the right surface for that room &mdash; but tile alone is not waterproof, because grout never is. What makes a laundry floor "
 "survive a leak is the assembly underneath: a bonded membrane that turns the floor into a shallow pan, silicone where the floor meets the wall, and &mdash; where the framing allows it &mdash; "
 "a floor drain that gives the water somewhere to go. Installed tile runs $14&ndash;$26 per square foot with labor from $11/sq ft, and in a small room the leak protection is most of the value.",
 'Bothell homes'),

facts([
 ('$14&ndash;$26', 'per square foot installed, labor from $11/sq ft. A laundry room is small, so the whole floor &mdash; done right, membrane and all &mdash; usually costs less than the deductible on the flood it is built to shrug off.'),
 ('24 hours', 'how long we flood-test every shower pan we build, photographed and kept on file. A laundry floor gets the same leak-first thinking: assume the water, then build the floor that does not care.'),
 ('2 years', 'our warranty on tile work &mdash; double the one-year most of the trade offers. We can afford that on laundry floors because the membrane under the tile does the real work.'),
]),

'<h2>The Laundry Room Is a Wet Room in Denial</h2>',

"<p>Bathrooms get waterproofing because everyone can picture the shower. The laundry room gets vinyl and hope, even though it holds the two most likely flood sources in the house: a washing "
"machine fed by two pressurized hoses that are under mains pressure around the clock, and a drain standpipe that takes a full-throttle pump-out every cycle. A rubber supply hose is a wear "
"item with a service life measured in single-digit years, and when one lets go it does not drip &mdash; it pours, at somewhere around house pressure, until someone notices. If the machine "
"is running its own drain can also overflow quietly, one cycle at a time, soaking the same corner for months.</p>",

"<p>So the design question for a laundry floor is not <em>which surface looks nice with the cabinets</em>. It is <em>what happens in this room during the bad hour</em> &mdash; and in the "
"months of slow seep you have not discovered yet. Sheet vinyl actually sheds water reasonably well until its seams and edges let go; laminate is done the day it gets wet; hardwood in a "
"laundry room is a buckling story waiting for its date. Tile is the surface that does not care. The catch is that tile <em>alone</em> only protects the spot it covers, and water is "
"patient about finding the edges. We compare the whole field of options in "
"<a href=\"/blog/how-to-choose-laundry-room-flooring\">choosing laundry room flooring</a> &mdash; this post is about doing the tile version properly.</p>",

'<h2>Why Tile Alone Is Not Enough</h2>',

"<p>Here is the part most homeowners have never been told: grout is not waterproof and never was. Cement grout absorbs water; even sealed, it slows water down rather than stopping it. A "
"tiled floor with nothing underneath is a colander with excellent style. During a real leak, water passes through the grout lines, hits the plywood or OSB below, and does what water does "
"to wood-based subfloors &mdash; swells it, delaminates it, and feeds the framing below for days after the surface looks dry.</p>",

"<p>What makes tile a flood-proof floor is the waterproofing layer bonded under it &mdash; the same sheet or liquid-applied membranes we build showers with, run across the floor and a few "
"inches up the wall behind the baseboard, corners treated, seams lapped. Now the floor is a shallow pan: water that gets through the grout stops at the membrane and sits there until it "
"evaporates or drains, instead of raining through the ceiling of the room below. The membrane also uncouples the tile from seasonal movement in the subfloor, which is the difference "
"between grout lines that last and grout lines that crack &mdash; the layer-by-layer logic we lay out in <a href=\"/blog/tile-underlayment-explained\">tile underlayment explained</a>.</p>",

table('Three Levels of Laundry-Floor Protection', ['Level', 'What it is', 'What it buys you'], [
 ('<strong>1. Tile over membrane</strong>', 'Bonded waterproofing membrane under the tile, turned up the wall behind the base, silicone at every edge', 'The floor itself survives anything; a modest leak stays in the room long enough to be found'),
 ('<strong>2. Membrane + drain pan</strong>', 'A shallow pan under the washer that catches drips and hose failures, plumbed or alarmed', 'Catches the most likely failure at its source; cheap insurance under any washer, any floor'),
 ('<strong>3. Membrane + floor drain</strong>', 'The floor sloped gently to a real drain, membrane tied into it &mdash; a shower pan with a washer standing in it', 'The bad hour becomes a non-event: water arrives, water leaves. The gold standard where framing and plumbing allow'),
]),

"<p>Level three is the one worth explaining, because it is the one nobody offers unless asked. If the laundry room sits over a crawlspace or basement where a drain line can be run, the "
"floor can be built exactly like a giant shower pan: pre-sloped toward a drain, membrane bonded over the slope and clamped into the drain flange, tile on top. A quarter inch per foot of "
"fall is invisible underfoot in a room this size, and it changes the failure math completely &mdash; a burst hose becomes a mop-up, not an insurance claim. On a slab or over a finished "
"ceiling it is harder and sometimes not worth the surgery; that is an honest conversation to have at the estimate, with the framing open to argument. The mechanics are the same ones we "
"describe in <a href=\"/blog/tile-shower-waterproofing\">shower waterproofing</a>, because it is the same build.</p>",

'<h2>The Details That Decide Whether It Works</h2>',

"<p><strong>The perimeter is the weak point.</strong> Water that cannot get through the field of the floor will find the joint where floor meets wall. The membrane has to turn up the "
"wall a few inches &mdash; behind the baseboard, where nobody sees it &mdash; and the joint gets silicone, not grout, because that corner moves and grout in a moving corner cracks. The "
"same goes for the joint around the standpipe and any supply penetrations.</p>",

"<p><strong>The doorway is the spillway.</strong> In a flood, the door is where water escapes into the hallway with the nice floors. A marble or stone threshold set a fraction higher "
"than the tile, siliconed at both edges, buys you real containment volume &mdash; a room-sized pan holds a surprising amount of water behind a half-inch dam. It is a $60 detail that "
"protects thousands of dollars of adjacent flooring.</p>",

"<p><strong>Slip resistance matters more here than in the bathroom.</strong> This is a floor that gets walked in socks while carrying a basket that blocks your view of the ground, in a "
"room where standing water is a design assumption. We spec a matte or textured porcelain in laundry rooms &mdash; the glassy polished looks belong somewhere drier. Smaller formats with "
"more grout lines also grip better underfoot; a laundry room is one of the places where a 12&times;12 or a mosaic-scale tile is the engineering answer, not the budget one &mdash; the "
"opposite end of the spectrum from the <a href=\"/blog/large-format-tile-installation\">large-format floors</a> we flatten substrates for elsewhere in the house.</p>",

'<h2>Laundry Floors in Bothell Homes</h2>',

"<p>Bothell's housing stock splits into two laundry-room stories. The split-levels and ramblers of the 70s and 80s usually keep the laundry downstairs &mdash; on a slab or over a "
"crawlspace, which is the good news, because a slab-level laundry room is the easy case: the flood damage is contained, and a floor drain is often plumbable. The newer townhomes and "
"two-story houses filling in around Canyon Park and North Creek put the laundry upstairs, next to the bedrooms, directly over the living room. That is convenient for socks and brutal "
"for failure modes: every leak is a ceiling event, and the drywall, insulation, and hardwood below join the claim.</p>",

"<p>Upstairs laundries are where we argue hardest for the full assembly &mdash; membrane turned up at the walls, raised threshold, pan under the washer, braided stainless hoses while "
"we are at it. The cost difference between tile-with-membrane and tile-with-hope is a few hundred dollars in a room this size. The cost difference between a contained leak and a "
"ceiling-and-hardwood claim is not close. Scope and scheduling for the area are on our "
"<a href=\"/hardwood-floor-refinishing/tile-installation-in-bothell-wa\">Bothell tile installation page</a>.</p>",

two_col(
 'What a leak-ready laundry floor includes',
 ['Matte, slip-rated porcelain &mdash; not a polished surface',
  'Bonded waterproof membrane across the floor, turned up the walls',
  'Silicone, not grout, at the perimeter and every penetration',
  'A raised, siliconed threshold at the door &mdash; the dam',
  'Drain pan under the washer; floor drain where framing allows',
  'Braided stainless supply hoses before the washer goes back'],
 'What the usual laundry floor gets',
 ['Whatever tile was left over from the bathroom',
  'Cement board or bare plywood &mdash; no membrane anywhere',
  'Grout run straight into the corners, cracking by year two',
  'A flat transition that hands the flood to the hallway',
  'The washer set back on rubber hoses from the 2000s',
  'A conversation with an insurance adjuster, eventually']),

'<h2>What It Costs, and What It Is Worth</h2>',

"<p>A laundry room is one of the smallest tile jobs we do &mdash; most are 30 to 60 square feet &mdash; which means the economics follow the small-room rule: high cost per square foot, "
"low total. The $14&ndash;$26 installed range applies, and small rooms land toward the top of it because mobilization, membrane work, and the appliance dance (disconnect, move, level, "
"reconnect) cost the same whether the room is tiny or twice the size. Expect the whole floor, done properly, to land in the four figures &mdash; usually the low four figures. The "
"per-square-foot arithmetic and where rooms land in the range is the same story we tell in "
"<a href=\"/blog/tile-installation-cost-per-square-foot\">tile cost per square foot</a>.</p>",

"<p>Against that number, weigh what the floor is protecting. Water damage from washing machine failures is one of the most common homeowner insurance claims in the country, and the "
"average claim runs well into five figures once a ceiling or a hardwood floor downstream is involved. A membrane, a threshold, and a pan do not show up in photographs, and they are the "
"best money in the whole project. If a heated floor is on your wish list &mdash; and a tile laundry room in a Pacific Northwest winter is a fair place to want one &mdash; the mat adds "
"modestly to the build and shares the same logic we priced out in <a href=\"/blog/heated-bathroom-floor-cost\">heated bathroom floors</a>.</p>",

faq('Laundry Room Tile: What Homeowners Ask Us', [
 ('What is the best flooring for a laundry room?',
  'Tile over a bonded waterproof membrane, with silicone at the perimeter and a slip-resistant matte porcelain on top. Tile is the only common floor that is genuinely indifferent to standing water, but the membrane underneath is what makes the room leak-proof — grout is not waterproof, and tile without a membrane only protects the spots it covers.'),
 ('Is tile alone waterproof?',
  'No. The tile body itself may be nearly impervious, but grout absorbs and passes water, and the perimeter joints move and open over time. A tiled floor with no membrane underneath will pass a real leak through to the subfloor. Waterproof is a property of the assembly — membrane, treated corners, siliconed perimeter — not of the tile.'),
 ('Can you put a floor drain in a laundry room?',
  'Often, yes — it depends on what is under the room. Over a crawlspace or unfinished basement, running a drain line is usually straightforward, and the floor can be built like a shallow shower pan with a gentle slope to the drain. On a concrete slab or over a finished ceiling it means real surgery, and a drain pan under the washer plus a raised threshold may be the smarter spend. We answer it house by house at the estimate.'),
 ('What does it cost to tile a laundry room?',
  'The installed range is $14 to $26 per square foot with labor from $11, and small rooms land toward the top of the range because setup, membrane work, and moving the appliances cost the same regardless of size. Most laundry rooms total in the low four figures done properly, including the waterproofing that makes the project worth doing.'),
 ('Should the tile go under the washer and dryer?',
  'Yes, always. Tiling only the visible apron leaves the most likely leak zone — directly under the machines — on bare subfloor, and it creates a height step that makes the machines rock and walk. The appliances come out, the whole floor gets tiled and membraned wall to wall, and the machines go back on a leveled, protected surface.'),
 ('What tile is safest underfoot in a laundry room?',
  'A matte or textured porcelain with a real slip rating, in a small or medium format. More grout lines mean more grip, and a honed surface sheds soap and water without turning into a skating rink. Polished porcelain and glassy glazes are the wrong finish for a room where standing water is part of the job description.'),
 ('Is a heated floor worth it in a laundry room?',
  'It is the same calculus as a bathroom: the mat and thermostat add a modest amount during the build and cannot be added later without redoing the floor. In a room where you fold clothes barefoot on tile all winter, most people who add it are glad they did. If the budget is tight, spend on the membrane and threshold first — comfort second, containment first.'),
 ('What else should change while the floor is open?',
  'Two cheap upgrades while the machines are out: braided stainless supply hoses in place of rubber ones, and a drain pan under the washer — plumbed to the drain if possible, or fitted with a leak alarm if not. Hose failure is the most common laundry flood, and both upgrades together cost less than one visit from a drywall contractor.'),
]),

cta('Build a Laundry Floor That Does Not Care',
    'We will look at what is under your laundry room, tell you whether a floor drain is realistic, and price the membrane, threshold, and tile in writing &mdash; the whole leak-ready assembly, not just the pretty part. Free in-home estimates across King &amp; Snohomish County.'),

related([
 ('/blog/how-to-choose-laundry-room-flooring', 'Choosing laundry room flooring'),
 ('/blog/tile-underlayment-explained', 'Tile underlayment explained'),
 ('/blog/tile-shower-waterproofing', 'Shower waterproofing'),
 ('/blog/tile-installation-cost-per-square-foot', 'Tile cost per square foot'),
 ('/blog/large-format-tile-installation', 'Large-format tile installation'),
 ('/hardwood-floor-refinishing/tile-installation-in-bothell-wa', 'Tile installation in Bothell'),
 ('/contact', 'Book a free estimate'),
]),
]

assemble(S, parts)
