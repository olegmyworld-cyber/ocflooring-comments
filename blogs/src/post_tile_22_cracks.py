from builder import *

S = 'why-tile-floors-crack'

parts = [
date_badge('January 26, 2027'),

quick_answer(
 "<strong>Tile almost never cracks on its own. A cracked tile floor is the floor filing a report about what is underneath it &mdash; a subfloor flexing past what rigid tile can "
 "tolerate, a missing uncoupling membrane, a slab crack telegraphing up, or hollow voids where thinset never made contact.</strong> One chipped tile under a dropped cast-iron pan "
 "is an accident; a line of cracks marching across a room is a structural message. Read the crack pattern correctly and it tells you the cause, whether a repair is honest, and "
 "whether new tile over the same subfloor would simply crack again on schedule.",
 'Mukilteo homes'),

facts([
 ('L/360', 'the maximum deflection a floor can have under ceramic tile &mdash; stiffer still for stone. Most cracked floors we autopsy failed this test before the first box of tile was opened.'),
 ('80%', 'of thinset coverage is the minimum under a dry-area floor tile. Tap a cracked floor and the hollow drum sound tells you where coverage never happened &mdash; and where cracks come from.'),
 ('$14&ndash;$26/sq ft', 'installed, labor from $11/sq ft, when the honest answer is a rebuild &mdash; which is why diagnosing the cause first matters more than matching the tile.'),
]),

'<h2>A Crack Is a Message, Not a Defect</h2>',

"<p>Porcelain is, for practical purposes, a rock &mdash; harder than the concrete and wood it sits on, and good for decades of traffic. What it cannot do is bend. Ask a tile to "
"follow a subfloor that moves and it answers the only way rigid material can: it cracks, precisely along the line where the movement lives. That is why an experienced tile setter "
"looks at a cracked floor the way a doctor reads an X-ray &mdash; the crack's shape, location and company tell you what happened below. And it is why the two questions we get "
"&mdash; <em>can you fix it?</em> and <em>why did it happen?</em> &mdash; have to be answered in reverse order. A repair that ignores the cause is a countdown to the same crack in "
"the replacement tile.</p>",

'<h2>Reading the Crack Pattern</h2>',

table('What the Crack Is Trying to Tell You', ['What you see', 'Likely cause', 'The honest fix'], [
 ('<strong>One tile, crescent chip at the center</strong>', 'Impact &mdash; something heavy landed', 'Replace the tile; no deeper meaning'),
 ('<strong>A straight crack crossing many tiles</strong>', 'Slab crack or joist line telegraphing through', 'Fix the movement path; membrane on the rebuild'),
 ('<strong>Cracks radiating near a doorway or hall</strong>', 'Deflection &mdash; the floor flexes where traffic bounces it', 'Framing or subfloor stiffening, then retile'),
 ('<strong>Grout cracking everywhere, tiles intact</strong>', 'Seasonal movement, no perimeter gap, or dead thinset', 'Investigate before it graduates to tile cracks'),
 ('<strong>Hollow-sounding tiles, cracked or loose</strong>', 'Voids &mdash; poor thinset coverage or bond failure', 'Those tiles were never attached; open and reset'),
 ('<strong>Cracks along one clean line at a room seam</strong>', 'Un-honored expansion joint or plywood seam', 'Soft joint belonged there; rebuild honors it'),
 ('<strong>Corners cracking near walls</strong>', 'Tile hard against the wall, no room to move', 'Cut relief at the perimeter, re-grout with flexible joint'),
]),

"<p>Two patterns account for most of the calls we get, so they deserve their own sections: the bouncy wood floor, and the slab that cracked underneath.</p>",

'<h2>Deflection: The Bouncy-Floor Problem</h2>',

"<p>Wood-framed floors flex &mdash; that is normal. The question is how much. The industry line for ceramic tile is deflection no worse than <strong>L/360</strong>: a floor spanning "
"ten feet may sag no more than about a third of an inch under load, and natural stone demands twice that stiffness. Walk across a marginal floor and the china cabinet rattles; set "
"tile on it and every one of those flexes works the grout, then the bond, then the tile itself. The crack shows up in year one or two, usually where traffic concentrates &mdash; "
"doorways, the path around the kitchen island, the hallway spine.</p>",

"<p>This is a framing question before it is a tile question &mdash; joist depth, span, spacing, and subfloor thickness, the fundamentals in "
"<a href=\"/blog/all-about-subfloors-what-you-need-to-know\">our subfloor guide</a>. Mukilteo's housing stock makes it a live one: the 1960s&ndash;80s split-levels and tri-levels "
"up on the bluff carry long joist spans over garages and daylight basements, and the newer Harbour Pointe construction went to wider joist spacing that meets code handily but "
"needs checking before stone. None of it is a reason not to tile &mdash; it is a reason the estimate includes a walk across the floor and, where it matters, a look at the framing "
"from below. Stiffening a floor &mdash; sistering joists, adding a plywood layer &mdash; is unglamorous money that makes the pretty money permanent.</p>",

'<h2>Membranes: The Cheap Insurance That Was Skipped</h2>',

"<p>The second epidemic cause is a floor built rigid-on-rigid: tile thinset straight to plywood or straight to a slab, nothing between to absorb the difference in how the two "
"materials move. Wood swells and shrinks with every Puget Sound season; concrete cracks as it cures and keeps creeping afterward; tile does neither. An uncoupling membrane "
"&mdash; the orange mat in <a href=\"/blog/ditra-vs-cement-board\">our Ditra vs cement board comparison</a> &mdash; sits between the layers and lets each move without informing "
"the other. Over a cracked slab, that separation is the entire difference between a crack that stays a slab problem and one that redraws itself in your tile within a year or "
"two. The full stack &mdash; what goes over wood, what goes over concrete, and why &mdash; is in <a href=\"/blog/tile-underlayment-explained\">tile underlayment explained</a>.</p>",

"<p>Alongside the membrane sit two humbler details that fail more floors than any product: <strong>coverage</strong> and <strong>movement joints</strong>. Thinset has to be "
"combed and the tile set so mortar actually supports it &mdash; the standard is at least 80% contact in dry areas, more under big tile, which is why "
"<a href=\"/blog/large-format-tile-installation\">large-format floors</a> get back-buttered. Skip it and the unsupported corners crack under a chair leg years later, announced by "
"that hollow drum sound. And every tile field needs room to breathe: a soft joint at the perimeter and at specified intervals. Tile gripped hard by the walls on all sides has "
"nowhere to put seasonal expansion except into itself.</p>",

'<h2>Repair or Redo: The Honest Economics</h2>',

"<p>Now the money question. <strong>A repair is honest when the cause was local:</strong> an impact chip, a hollow tile or two from lazy coverage, one seam that needed a soft "
"joint. We cut out the casualties, fix the local condition, and reset &mdash; if you have spare tiles from the original install. (Keep spare boxes forever; dye lots do not "
"repeat, and a close-but-wrong replacement tile reads worse than the crack did.) <strong>A repair is a bandage when the cause is systemic:</strong> deflection, no membrane over "
"a moving slab, thinset that never bonded across the room. New tiles set into the same conditions inherit the same fate, and you pay for the repair twice on the way to the "
"rebuild you needed. Installed tile work runs $14&ndash;$26 per square foot with labor from $11 &mdash; real money, which is exactly why it should be spent once, on an assembly "
"built to the standards, rather than twice on the same floor.</p>",

"<p>Our rule at the estimate is simple: we tell you which case you have and show you the evidence &mdash; the tap test, the deflection walk, the crack map &mdash; before we "
"talk price. Sometimes that costs us a retile job because the honest answer was a $300 repair. We consider that advertising. The full scope of what we build is on our "
"<a href=\"/city-of-mukilteo/tile-installation-in-mukilteo-wa\">Mukilteo tile installation page</a>.</p>",

two_col(
 'When a repair is the honest answer',
 ['One or two tiles, clearly impact or local voids',
  'The rest of the floor taps solid and the grout is sound',
  'You have spare tiles from the original dye lot',
  'The floor passes the bounce test where it cracked',
  'A missing soft joint explains the one clean crack line',
  'The fix addresses the cause, not just the casualty'],
 'When only a rebuild fixes it',
 ['Cracks recur or march in lines across multiple tiles',
  'The floor flexes underfoot &mdash; deflection past L/360',
  'Tile was set rigid to a cracked or curing slab, no membrane',
  'Widespread hollow sounds &mdash; the bond never happened',
  'Grout failure is general, not local, and getting worse',
  'The subfloor needs structural work tile cannot sit over']),

faq('Cracked Tile Floors: What Homeowners Ask Us', [
 ('Why did my tile floor crack if nothing was dropped on it?',
  'Because something under it moved. Tile is rigid; it cracks when the subfloor flexes past what it can tolerate, when a slab crack telegraphs upward, when seasonal wood movement has no membrane to die in, or when voids under the tile leave corners unsupported. The crack pattern — one tile versus a marching line — tells you which. Impact cracks are the exception, and they look different: a crescent chip at the point of the hit.'),
 ('What does a crack running across several tiles mean?',
  'That is the most diagnostic pattern there is: a continuous crack crossing tiles and grout joints in a line means the substrate cracked or moved along that line, and the tile simply traced it. Over concrete it is usually a slab crack; over wood, a joist line or a plywood seam. Replacing the tiles without decoupling them from that line means the new tiles crack along it too.'),
 ('Can you just replace the cracked tiles?',
  'When the cause is local — an impact, a couple of hollow tiles — yes, and it is the honest fix, provided you have spares from the original dye lot. When the cause is systemic, spot replacement is a subscription: deflection, a moving slab, or floor-wide bond failure will crack the replacements on the same schedule. We diagnose first, then tell you which case you have and why.'),
 ('What is L/360 and does my floor meet it?',
  'It is the deflection limit for floors under ceramic tile: a floor may flex no more than its span divided by 360 under load — about a third of an inch over a ten-foot span. Natural stone requires double that stiffness. Long spans, undersized joists, and thin subfloors are the usual failers. A tile setter checks span and framing before quoting, which is one way to tell a real bid from a fast one.'),
 ('Do I need a membrane under floor tile?',
  'Over wood-framed floors and over any slab with cracks or curing left to do — strongly yes. An uncoupling membrane separates tile from substrate movement, which is the leading cause of cracking that is not structural. It is a thin line item next to what it prevents. What it does not do is fix deflection or flatten anything; membranes absorb movement, they do not add stiffness.'),
 ('Why do my tiles sound hollow when I tap them?',
  'Hollow means the tile is not fully supported — either the thinset coverage was inadequate on install day, or the bond has since let go. Hollow tiles are the ones that crack under a chair leg or a dropped jar, because the load lands on unsupported porcelain. Scattered hollows near a crack explain the crack; widespread hollows mean the install failed and the floor is living on borrowed time.'),
 ('Is cracked grout as serious as cracked tile?',
  'It is the earlier, cheaper chapter of the same story. Grout cracks first because it is the weakest material in the assembly — seasonal movement, a missing perimeter gap, or early bond failure all show up in the joints before the tile. Localized grout cracking can be routine; general, recurring grout failure is the floor asking for a diagnosis while the fix is still affordable.'),
 ('What does it cost to redo a cracked tile floor properly?',
  'Installed tile work runs $14 to $26 per square foot with labor from $11. The honest quote for a cracked floor also names what caused the failure and includes the cure — subfloor stiffening, a membrane, proper coverage, movement joints — because without that line, you are paying to install the next set of cracks. We put the diagnosis and the fix in writing, backed by a 2-year warranty.'),
]),

cta('Get a Diagnosis Before You Buy a Floor',
    'We will map the cracks, tap the field, and walk the bounce &mdash; then tell you honestly whether your floor needs a $300 repair or a rebuild, with the evidence either way. Free in-home estimates across King &amp; Snohomish County.'),

related([
 ('/blog/ditra-vs-cement-board', 'Ditra vs cement board'),
 ('/blog/tile-underlayment-explained', 'Tile underlayment explained'),
 ('/blog/all-about-subfloors-what-you-need-to-know', 'All about subfloors'),
 ('/blog/large-format-tile-installation', 'Large-format tile installation'),
 ('/blog/regrouting-vs-retiling-a-shower', 'Regrouting vs retiling a shower'),
 ('/city-of-mukilteo/tile-installation-in-mukilteo-wa', 'Tile installation in Mukilteo'),
 ('/contact', 'Book a free estimate'),
]),
]

assemble(S, parts)
