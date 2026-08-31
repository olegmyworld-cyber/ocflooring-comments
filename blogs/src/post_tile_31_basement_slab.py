from builder import *

S = 'tiling-over-concrete-basement-slab'

parts = [
date_badge('March 30, 2027'),

quick_answer(
 "<strong>A concrete basement slab is the best substrate tile ever gets &mdash; stiff, quiet, and immune to the bounce that cracks tile over wood framing "
 "&mdash; but only after it passes three checks: dry enough, flat enough, and stable enough.</strong> Moisture testing comes first, every time, because a "
 "slab that wicks ground water will push that water at your tile assembly forever. Then cracks and flatness get dealt with, usually with an uncoupling "
 "membrane and some self-leveler. And when a slab fails the checks &mdash; active water, moving cracks &mdash; the honest answer is to fix the water "
 "problem first, not to tile over it and hope.",
 'Snohomish &amp; river-valley homes'),

facts([
 ('$11/sq ft', 'where our tile labor starts. Installed tile runs $14&ndash;$26/sq ft, and basement slabs often land kindly in that range &mdash; concrete needs prep, but not the joist surgery an old wood-framed floor can demand.'),
 ('2 years', 'our warranty on tile work &mdash; and the reason the moisture test happens before the quote is signed, not after the tile is down. We do not warranty hope.'),
 ('1,000+', 'floors since 2013 across King &amp; Snohomish County, a healthy share of them basements &mdash; which is exactly where you learn to respect what a slab does when nobody tests it.'),
]),

'<h2>Why Tile Loves a Slab &mdash; With Conditions</h2>',

"<p>Most tile failures over wood framing trace back to movement: joists deflect, seasons swell and shrink the structure, and the grout lines keep score. "
"Concrete does not bounce. A basement slab is the one substrate in the house where deflection is simply off the table, which is why tile over concrete, "
"done right, is about as permanent as residential flooring gets. Add the fact that basements are where water heaters fail and laundry hoses let go, and "
"tile starts to look less like a style choice and more like the correct engineering answer for the room.</p>",

"<p>The conditions matter, though, because concrete has its own habits. It cracks as it cures and keeps creeping for years. It sits on soil, and soil "
"holds water, and water moves through concrete as vapor whether you invite it or not. And builder-poured basement slabs were rarely finished flat enough "
"for modern large-format tile. None of these is a deal-breaker. All of them are the actual job.</p>",

'<h2>Moisture Testing Comes First, Every Time</h2>',

"<p>Before anything is quoted in a basement, the slab gets tested for moisture &mdash; not glanced at, tested. The quick screen is a taped-down plastic "
"sheet left for a day or two: condensation or a dark patch underneath means the slab is moving vapor. The serious tools are calcium chloride kits and "
"in-slab relative humidity probes, which put a number on how much moisture is coming up. The number decides the assembly: a reasonably dry slab takes a "
"standard membrane and tile; a damp one needs a vapor-rated membrane system; a wet one needs a drainage conversation, not a tile conversation.</p>",

"<p>Snohomish basements earn extra caution here. Plenty of the housing stock &mdash; farmhouse-era homes, 1960s and 70s ramblers, daylight basements on "
"the valley slopes &mdash; predates the routine use of vapor barriers under slabs, and the river valley keeps the water table honest. The tells are "
"familiar: a white mineral bloom on the concrete (efflorescence), a musty smell that deep cleaning never quite kills, paint peeling off the slab in "
"sheets. None of them says <em>never tile</em>. All of them say <em>test before you spend a dollar on porcelain</em>.</p>",

'<h2>Cracks, Joints, and the Uncoupling Membrane</h2>',

"<p>Every slab has cracks; the question is which kind. Hairline shrinkage cracks &mdash; thin, stable, flat across the break &mdash; are cosmetic, and an "
"uncoupling membrane bridges them safely. The membrane is a thin polyethylene layer between slab and tile that lets the two move independently, so an old "
"crack that creeps a hair wider never telegraphs into your floor. It is the single most valuable layer in a slab-tiling assembly, and the options are "
"compared in <a href=\"/blog/ditra-vs-cement-board\">DITRA vs cement board</a> &mdash; over concrete, the membrane wins that argument nearly every "
"time.</p>",

"<p>Two crack types do not get papered over. A crack with vertical displacement &mdash; one side higher than the other &mdash; means the slab has moved "
"structurally, and tile goes nowhere until a professional says why. And a slab&rsquo;s control joints, the straight saw-cuts poured in on purpose, are "
"designed to keep moving; they get honored with a matching soft joint up through the tile or isolated by the membrane system, never grouted rigid. Skip "
"that discipline and you get the signature diagonal crack march that fills our inspection calendar &mdash; the full taxonomy is in "
"<a href=\"/blog/why-tile-floors-crack\">why tile floors crack</a>.</p>",

'<h2>Flat Is Not Level &mdash; and Flat Is What Tile Needs</h2>',

"<p>Basement slabs often slope gently toward a floor drain or a corner, and that is fine &mdash; tile does not care about level. What tile cares about is "
"<em>flat</em>: no humps, no dishes, no quarter-inch waves that turn large-format tile into a see-saw. The fix is unglamorous and effective &mdash; grind "
"the high spots, fill the low ones with self-leveling compound, and check with a straightedge until the surface earns the tile going on it. Old adhesive "
"from long-dead carpet or vinyl gets scraped or ground off along the way, because thinset bonds to concrete, not to 1978&rsquo;s glue. Where each layer "
"sits in the final stack &mdash; slab, leveler, membrane, tile &mdash; is diagrammed in <a href=\"/blog/tile-underlayment-explained\">our underlayment "
"guide</a>.</p>",

table('What the Slab Shows Us, and What We Do About It', ['Condition', 'Verdict', 'The fix'], [
 ('<strong>Clean, dry, flat slab</strong>', 'Green light', 'Membrane, tile, done &mdash; the easiest substrate we ever meet'),
 ('<strong>Hairline shrinkage cracks</strong>', 'Normal', 'Uncoupling membrane bridges them; no drama'),
 ('<strong>Control joints</strong>', 'By design', 'Honored through the tile as soft joints, or isolated by the membrane'),
 ('<strong>Moderate moisture readings</strong>', 'Workable', 'Vapor-rated membrane system, and ventilation habits worth keeping'),
 ('<strong>Out of flat</strong>', 'Common', 'Grind the humps, self-level the dishes, verify with a straightedge'),
 ('<strong>Old adhesive or paint</strong>', 'Prep item', 'Mechanical removal &mdash; thinset needs bare, sound concrete'),
 ('<strong>Crack with displacement</strong>', 'Stop', 'Structural evaluation before any flooring conversation'),
 ('<strong>Active water intrusion</strong>', 'Stop', 'Drainage, grading, or sump work first &mdash; tile does not fix hydrology'),
]),

'<h2>When the Slab Says No</h2>',

"<p>Some basements are not ready for tile, and the respectful thing is to say so at the estimate. Water seeping at the cove joint after a hard rain, a "
"sump pump that runs like a metronome, hydrostatic pressure pushing moisture through the floor &mdash; these are drainage problems, and tile laid over "
"them becomes a very durable lid on a mess. The money goes to gutters, grading, footing drains, or a sump system first; the tile happily waits. We would "
"rather lose a month than warranty a floor fighting the water table.</p>",

"<p>And occasionally the honest answer is a different floor entirely. Tile is the champion for wet-risk and permanence, but it is hard and cold underfoot, "
"and a basement rec room where kids sprawl on the floor may serve the family better in carpet over a proper pad &mdash; we make that case in "
"<a href=\"/blog/carpet-for-basement\">carpet for basements</a> &mdash; while solid hardwood stays off the menu below grade for reasons covered in "
"<a href=\"/blog/can-i-install-hardwood-flooring-in-a-basement-or-other-moisture-prone-areas\">wood in moisture-prone rooms</a>. The cold-feet problem, "
"for what it is worth, has a tile-native fix: heated cable snapped into the same uncoupling membrane, which we compared honestly in "
"<a href=\"/blog/heated-floor-mat-vs-cable\">mats vs loose cable</a>.</p>",

'<h2>The Snohomish Basement, Specifically</h2>',

"<p>Around Snohomish the basement conversation has a local accent. The valley floor keeps ground moisture generous year-round; the older homes in and "
"around downtown carry slabs poured decades before under-slab vapor barriers were standard practice; and the daylight basements on the hillsides mix "
"slab-on-grade sections with framed sections in the same room, which changes the assembly mid-floor. All of it is workable &mdash; it just has to be "
"seen and tested before it is priced. We test the slab, name the membrane, and put the prep in writing, and the full scope is on the "
"<a href=\"/city-of-snohomish/tile-installation-in-snohomish-wa\">Snohomish tile installation page</a>.</p>",

two_col(
 'Signs your slab is ready for tile',
 ['Plastic-sheet test comes back dry after 48 hours',
  'Cracks are hairline, stable, and flat across the break',
  'Straightedge shows no humps or dishes worth naming',
  'Bare concrete &mdash; old glue and paint already dealt with',
  'No musty smell, no efflorescence bloom on floor or walls',
  'Sump and gutters handle storms without drama'],
 'Signs to stop and fix first',
 ['Dark, damp patch under the taped plastic sheet',
  'A crack where one side sits higher than the other',
  'Water at the wall-floor joint after hard rain',
  'Efflorescence &mdash; the slab is moving mineral-laden water',
  'A sump pump that cycles constantly in winter',
  'Peeling slab paint &mdash; vapor pressure is pushing from below']),

faq('Tiling a Basement Slab: What Homeowners Ask Us', [
 ('Can you tile directly over a concrete basement slab?',
  'Structurally, concrete is the best base tile can have - but we still put an uncoupling membrane between slab and tile rather than bonding directly. The membrane bridges the hairline cracks every slab develops and keeps future concrete movement from telegraphing into grout lines. Direct-bond installs work until the slab twitches; the membrane makes that not your problem.'),
 ('How do you test a basement slab for moisture?',
  'The quick screen is a plastic sheet taped tight to the slab for a day or two - moisture underneath means the slab is moving vapor. For a real number we use calcium chloride tests or in-slab relative humidity probes. The result decides the assembly: standard membrane, vapor-rated membrane, or a drainage conversation before any tile at all.'),
 ('Do cracks in the slab mean I cannot tile?',
  'Usually not. Hairline shrinkage cracks are normal concrete behavior, and an uncoupling membrane bridges them safely. The exceptions are cracks with displacement - one side higher than the other - which need a structural opinion first, and control joints, which must be honored up through the tile as soft joints rather than grouted rigid.'),
 ('My basement slab is not level. Is that a problem for tile?',
  'Slope is fine; waviness is not. Tile tolerates a floor that leans gently toward a drain, but large-format tile demands flatness - no humps or dishes. We grind high spots and pour self-leveler into low ones until a straightedge stops arguing. It is unglamorous work and it is most of the difference between a good basement tile job and a lippage museum.'),
 ('What about old carpet glue or paint on the slab?',
  'It comes off. Thinset needs to bond to sound, bare concrete, not to decades-old adhesive, so residue is scraped or ground away as part of prep. It adds hours, not drama, and it is far cheaper than the alternative, which is tile bonded to a layer that lets go.'),
 ('Is a heated floor worth it over a basement slab?',
  'It is the single best comfort upgrade a basement tile floor can get. Slabs hold ground temperature all year, and heating cable snapped into the studded uncoupling membrane warms the surface for the hours you actually use the room. The membrane does double duty - crack isolation and cable placement - so the incremental cost is mostly the wire and the electrician.'),
 ('When should a basement not be tiled?',
  'When the water problem is still winning: seepage at the cove joint, a sump running constantly, moisture readings that stay high after a dry week. Tile over active water is a durable lid on an ongoing mess. Fix drainage, grading, or the sump first - the slab will still be there, and so will we. Occasionally the answer is also that carpet simply suits the room better, and we will say so.'),
 ('What does it cost to tile a basement over concrete?',
  'Our installed tile runs $14 to $26 per square foot, labor from $11. Basements often price in the friendlier half of the range - concrete needs membrane and flattening but not the structural work an old wood-framed floor can demand. Moisture results and how much leveling the slab needs are the two variables that move the number, and both are known before you sign anything.'),
]),

cta('Get the Slab Tested Before You Get It Tiled',
    'We will test the moisture, walk the cracks, check the flatness, and tell you straight whether your basement is ready for tile &mdash; and what to fix first if it is not. Free in-home estimates across King &amp; Snohomish County.'),

related([
 ('/blog/tile-underlayment-explained', 'Tile underlayment, explained'),
 ('/blog/why-tile-floors-crack', 'Why tile floors crack'),
 ('/blog/ditra-vs-cement-board', 'DITRA vs cement board'),
 ('/blog/heated-floor-mat-vs-cable', 'Heated floor mats vs loose cable'),
 ('/blog/carpet-for-basement', 'Carpet for basements'),
 ('/city-of-snohomish/tile-installation-in-snohomish-wa', 'Tile installation in Snohomish'),
 ('/contact', 'Book a free estimate'),
]),
]

assemble(S, parts)
