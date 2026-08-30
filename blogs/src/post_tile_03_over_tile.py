from builder import *

S = 'can-you-tile-over-existing-tile'

parts = [
date_badge('September 15, 2026'),

quick_answer(
 "<strong>Yes &mdash; over a sound, well-bonded tile floor in a dry room, tiling over existing tile is a legitimate shortcut, not a hack.</strong> "
 "It fails predictably in three places: wet areas, where you would be burying waterproofing you cannot inspect; floors with hollow or loose spots, "
 "where the new tile inherits a failure already in progress; and walls, where weight and bond work against you. And the deal-breaker almost nobody "
 "checks first is height &mdash; the extra half inch has to get along with every door, transition, and toilet in the room.",
 'Remodels &amp; older homes'),

facts([
 ('~1/2 inch', 'what a new layer of tile and mortar adds on top of the old floor. That half inch is the quiet deal-breaker &mdash; it has to clear doors, transitions, appliances and the toilet flange before the first bag of thinset is opened.'),
 ('$11/sq ft', 'where our tile labor starts either way. Skipping demolition trims the bill, but going over old tile still means degreasing, priming and flattening &mdash; installed cost still lands in the $14&ndash;$26 range.'),
 ('2 years', 'our warranty on tile work &mdash; and it applies over an old floor only when that floor passes our checks. If we will not stand behind tile over your existing tile, we say so at the estimate, not after.'),
]),

'<h2>The Honest Answer Up Front</h2>',

"<p>This question gets asked constantly, and for a good reason: tile demolition is the worst part of a tile job. It is loud, it is dusty in a way that finds "
"every room in the house, it fills a trailer, and you pay for all of it. So the appeal of setting new tile straight over the old floor is obvious, and the "
"trade answer is more generous than most homeowners expect: <em>existing tile is actually a decent substrate</em>. It is hard, it is dimensionally stable, "
"and modern polymer-modified mortars bond to it reliably once the glaze is scuffed or primed. Europe has been tiling over tile for decades without ceremony.</p>",

"<p>What the generous answer hides is that it is conditional on everything being right underneath. Tile over tile does not fix anything &mdash; it photocopies "
"the old floor, flaws included, half an inch higher. A well-bonded floor stays well-bonded with another layer on top. A floor that is quietly letting go "
"lets go on schedule, and now the crack runs through two layers of your money instead of one. So the real question is never <em>can</em> you tile over tile. "
"It is whether <em>this particular floor</em> has earned the right to stay.</p>",

'<h2>When It Genuinely Works</h2>',

"<p>Here is the checklist we run before we will set over an existing floor, and every item has to pass &mdash; four out of five is a tear-out.</p>",

"<p><strong>The old tile is bonded, everywhere.</strong> We sound the whole floor with a mallet or a chain. Solid tile rings tight; a failed bond sounds "
"hollow, like knocking on a door. A couple of hollow tiles in a closet corner can sometimes be removed and filled; hollow zones in the middle of the room "
"end the conversation.</p>",

"<p><strong>The room is dry.</strong> Bathroom and kitchen floors qualify. Showers, tub surrounds and anything a shower sprays do not &mdash; more on that "
"below, because it is the failure mode with the highest stakes.</p>",

"<p><strong>The floor is flat and the structure is sound.</strong> Tile over tile still has to meet the same flatness the new tile demands, and a bouncy "
"subfloor fails twice as expensively under two layers. If the old floor has a structural crack telegraphing through it, the crack is coming from below, and "
"covering it is not a repair. What sits under the tile decides more than the tile does &mdash; the same lesson as our primer on "
"<a href=\"/blog/all-about-subfloors-what-you-need-to-know\">subfloors and what you need to know about them</a>.</p>",

"<p><strong>The height works.</strong> Half an inch sounds like nothing until you meet it at a door that no longer clears, a dishwasher that can never come "
"out again, or a step-down into the hallway that trips guests. This one gets its own section.</p>",

"<p><strong>The old surface can take a bond.</strong> Glossy glazed tile gets mechanically scuffed or primed with a bonding primer, degreased within an inch "
"of its life &mdash; a kitchen floor carries a film of cooking grease that no mortar forgives. This is prep labor, which is why going over tile is cheaper "
"than tear-out but never free.</p>",

table('Tile Over Tile, Situation by Situation', ['Situation', 'Our verdict', 'Why'], [
 ('<strong>Bathroom floor, dry and solid</strong>', 'Usually yes', 'Best case for the shortcut &mdash; small area, sound substrate, demolition savings are real'),
 ('<strong>Kitchen floor</strong>', 'Often yes, check heights', 'Dishwasher and range clearances shrink; degreasing is non-negotiable prep'),
 ('<strong>Laundry / mudroom / entry</strong>', 'Usually yes', 'Dry-room rules apply; check the transition to adjoining floors'),
 ('<strong>Shower pan or shower walls</strong>', 'No', 'You would be burying waterproofing nobody can inspect, test or trust'),
 ('<strong>Tub surround</strong>', 'No', 'Same problem &mdash; the wet-area assembly behind the old tile is unknown and unfixable from outside'),
 ('<strong>Any wall, dry or not</strong>', 'Rarely', 'Doubled weight hanging on the old bond; walls also demo far more cheaply than floors'),
 ('<strong>Hollow, loose or cracked old tile</strong>', 'No', 'New tile inherits the failure in progress &mdash; the crack transfers through on schedule'),
 ('<strong>Heated floor wanted</strong>', 'Tear out instead', 'The cable or mat belongs in a fresh assembly, not stacked on old tile at even more height'),
]),

'<h2>The Tap Test: What Hollow Spots Are Telling You</h2>',

"<p>The tap test deserves a plain-English explanation, because it is the whole inspection in miniature. Tile does not stay on a floor by magic; it stays "
"because a thin layer of mortar is gripping both the tile and the substrate. When that grip fails &mdash; from deflection, from a bad original install, from "
"seasonal movement the assembly could not absorb &mdash; the tile is resting in place rather than bonded in place, and the air gap underneath makes a "
"hollow sound when struck.</p>",

"<p>A hollow tile is not a cosmetic problem. It is a structural report from underneath the floor, telling you the bond has already lost, and anything built "
"on top of it stands on that loss. Mortar over a hollow zone bonds the new floor to tiles that are themselves attached to nothing. The new layer may hold "
"things together for a year or two by sheer bridging, and then a grout line opens, a corner rocks, and the repair now involves two layers of demolition "
"instead of one. When a floor fails the tap test in more than a couple of isolated spots, tear-out is not us being conservative &mdash; it is us declining "
"to charge you twice.</p>",

'<h2>Height: The Half Inch That Fights the Whole House</h2>',

"<p>A new tile layer &mdash; mortar plus tile &mdash; adds roughly half an inch, a bit less with thin porcelain, a bit more with anything rustic. Nothing in "
"your house was designed with that half inch in mind, and it picks fights in every direction.</p>",

"<p><strong>Doors</strong> are first. Interior doors can usually be trimmed; a front door with a weatherstripped threshold often cannot, at least not well. "
"<strong>Transitions</strong> are second: the step between the new tile and the hallway hardwood gets taller, and past a certain point it is not a "
"transition, it is a trip hazard that inspectors and grandparents both notice. <strong>Toilets</strong> need the flange extended to the new height &mdash; "
"a cheap part and a standard step, but skipping it is how wax rings fail and toilets rock. <strong>Appliances</strong> are the sneaky one: tile up to a "
"dishwasher's toe and you may have permanently installed it; the countertop above does not move, and the extra half inch is exactly the clearance it needed "
"to slide out. We walk every one of these in the room before quoting, because any one of them can turn the cheap option into the expensive one.</p>",

'<h2>Why We Refuse in Wet Areas</h2>',

"<p>Every shower we build gets a pre-slope, a bonded waterproofing membrane, and a 24-hour flood test that we photograph and keep on record before a single "
"tile is set. That sentence is the entire argument against tiling over a shower: <em>none of it is possible over existing tile</em>. We cannot see the old "
"membrane, if there ever was one. We cannot test the pan. We cannot fix the slope. Grout is not waterproof and never was, so water has been passing through "
"that old surface into the assembly behind it for years &mdash; and whatever condition that assembly is in, tiling over it seals the question shut where "
"nobody can ever answer it cheaply again.</p>",

"<p>A shower that leaks behind new tile is not a repair, it is a demolition of your brand-new work, plus whatever the water did on its way to the ceiling "
"below. This is why the wet-area rule has no exceptions in our book, and why a contractor who happily quotes tile-over-tile in your shower has told you "
"something important about the rest of their assembly. The same logic runs through our "
"<a href=\"/blog/bathroom-tile-installation-cost-seattle\">bathroom tile cost breakdown</a>: in a shower, the waterproofing is the product, and the tile is "
"just the part you can see.</p>",

two_col(
 'When we will set over existing tile',
 ['Dry-room floors: bathrooms, kitchens, laundry, entries',
  'The old floor passes the tap test across its whole area',
  'Height clears doors, appliances, transitions and the flange',
  'Surface degreased, scuffed or primed &mdash; prep priced honestly',
  'Flatness brought to what the new tile format demands',
  'Movement joints honored, not grouted over and forgotten'],
 'When we insist on tear-out',
 ['Showers, tub surrounds, and any wall a shower sprays',
  'Hollow, loose, or cracked tile beyond an isolated spot',
  'Structural cracks telegraphing up from the substrate',
  'A heated floor is in the plan &mdash; it belongs in a fresh assembly',
  'Height fights the house and trimming will not fix it',
  'The old floor is the second or third layer already stacked']),

'<h2>What You Save &mdash; and What You Do Not</h2>',

"<p>Here is the honest arithmetic. Going over the old floor saves demolition and disposal &mdash; the dustiest labor and the dumpster. It does not save the "
"prep: degreasing, priming or scarifying, flattening, and dealing with every height conflict the half inch creates. Our tile labor starts at $11 per square "
"foot either way, and installed cost lands in the same $14&ndash;$26 per square foot range, toward the lower end when the shortcut is clean. On a small "
"bathroom floor the savings are real but modest; on a large kitchen with a trapped dishwasher, the \"savings\" can quietly go negative. The honest way to "
"compare is per project, not per square foot &mdash; the trap we unpack in "
"<a href=\"/blog/tile-installation-cost-per-square-foot\">our per-square-foot price breakdown</a>.</p>",

"<p>One more alternative worth naming: if the goal is a fresh floor in a dry room at the lowest cost, tile over tile is not the only candidate. A quality "
"vinyl plank floats over sound existing tile at a fraction of the height and cost, and in a laundry room or basement it is often the better answer &mdash; "
"an argument we make honestly in <a href=\"/blog/hardwood-vs-tile-in-the-kitchen\">hardwood vs tile in the kitchen</a> and in our guide to "
"<a href=\"/blog/the-benefits-of-waterproof-flooring-in-seattle-wa\">waterproof flooring</a>. Tile over tile earns its place when you want tile's "
"permanence and the old floor has earned its keep.</p>",

'<h2>How We Decide at the Estimate</h2>',

"<p>When we look at a tile-over-tile candidate, the visit is short and concrete. We sound the floor corner to corner. We put a straightedge on it. We "
"measure the height against every door, transition and appliance in play, and we look at what the room is &mdash; wet or dry &mdash; before anything else. "
"Then you get one of two answers in writing: a price for setting over the old floor with the prep spelled out, or a plain explanation of why this "
"particular floor needs to come out, with the tear-out priced next to it so you can see the difference rather than take it on faith. Either way you are "
"deciding with the facts, which is the whole point. The full scope of what we install &mdash; floors, showers, backsplashes, heated floors &mdash; is on our "
"<a href=\"/seattle/tile-installation-in-seattle-wa\">Seattle tile installation page</a>.</p>",

faq('Tiling Over Existing Tile: What Homeowners Ask Us', [
 ('Can you tile over existing tile on a floor?',
  'Yes, when the old floor passes the checks: solidly bonded everywhere (it passes a tap test), flat, structurally sound, in a dry room, and with enough clearance that the added half inch does not fight doors, appliances, transitions, or the toilet flange. When all of that is true, tiling over tile is a legitimate, durable install — not a shortcut you will regret.'),
 ('Can you tile over tile in a shower?',
  'No, and we will not do it. A shower depends on the waterproofing assembly behind the tile — the pre-slope, the membrane, the pan. Over existing tile, none of that can be inspected, repaired, or flood-tested, and grout has never been waterproof. Burying an unknown assembly under new tile turns a future leak into a demolition of brand-new work.'),
 ('How much height does tiling over tile add?',
  'Roughly half an inch — mortar plus the new tile — a little less with thin porcelain, more with thick or rustic tile. The height itself is not the problem; the conflicts are. Doors may need trimming, transitions get taller, the toilet flange must be extended, and a dishwasher can lose the clearance it needs to ever slide out again.'),
 ('Do you need special thinset to tile over tile?',
  'You need the right prep and the right mortar, yes. The old surface gets degreased and either mechanically scuffed or coated with a bonding primer, and the new tile is set in a high-quality polymer-modified mortar rated for the job. Standard thinset over glossy, greasy glaze is how tile-over-tile got its bad reputation.'),
 ('Will the new tile crack if the old tile has cracks?',
  'If the old crack came from movement or a structural problem below — and most do — then yes, it will eventually telegraph through the new layer, usually along the same line. A crack is a message from the substrate, and covering the messenger does not change the message. Isolated bond failures can sometimes be cut out and patched; structural cracks mean tear-out.'),
 ('Is it cheaper to tile over tile than to remove it?',
  'Usually, but by less than people hope. You save the demolition and disposal, which is real money and real mess. You still pay for prep, priming, flattening, and solving every height conflict, and labor still starts at $11 per square foot with installed cost in the $14–$26 range. On some jobs — a trapped appliance, a threshold that cannot be fixed — the savings evaporate.'),
 ('Can you tile over a tile backsplash?',
  'We usually advise against it. Walls carry the doubled weight on the old bond, outlets and switches all need extending, and the honest math is different: a backsplash is a small area that demolishes quickly and cheaply, so the savings from going over it are minimal. Tear-out gets you a fresh, flat wall for very little extra.'),
 ('How do I know if my old tile floor is bonded well enough?',
  'Tap it. Use a mallet handle, a chain, or even a golf ball across the whole floor and listen: bonded tile sounds tight and solid, failed bond sounds hollow. Also look for cracked grout lines that keep coming back, corners that rock underfoot, and any tile that has moved. We do this across every square foot at the estimate — it takes minutes and settles the question.'),
]),

cta('Not Sure If Your Old Floor Qualifies?',
    'We will tap the whole floor, check every height in the room, and give you both numbers in writing &mdash; over the old tile or tear-out &mdash; so you can decide with facts instead of hope. Free in-home estimates across King &amp; Snohomish County.'),

related([
 ('/blog/bathroom-tile-installation-cost-seattle', 'What bathroom tile really costs'),
 ('/blog/tile-installation-cost-per-square-foot', 'Tile cost per square foot, decoded'),
 ('/blog/all-about-subfloors-what-you-need-to-know', 'All about subfloors'),
 ('/blog/hardwood-vs-tile-in-the-kitchen', 'Hardwood vs tile in the kitchen'),
 ('/seattle/tile-installation-in-seattle-wa', 'Tile installation in Seattle'),
 ('/contact', 'Book a free estimate'),
]),
]

assemble(S, parts)
