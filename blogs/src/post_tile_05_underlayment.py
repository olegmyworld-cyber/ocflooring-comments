from builder import *

S = 'tile-underlayment-explained'

parts = [
date_badge('September 29, 2026'),

quick_answer(
 "<strong>Tile underlayment is the layer between your subfloor and your tile, and it &mdash; not the tile &mdash; decides whether the floor cracks.</strong> "
 "There are three families that matter in a house: cement board, the screwed-down default; uncoupling membranes like Ditra, a thin mat that absorbs the "
 "movement between wood and porcelain; and waterproof foam boards, which own the shower. Which one belongs under your tile depends on what is beneath it, "
 "whether the room gets wet, and how much height the room can spare &mdash; not on which product the installer happens to have in the van.",
 'Floors, showers &amp; remodels'),

facts([
 ('1/8 inch', 'the thickness of an uncoupling membrane like Ditra &mdash; the thinnest route to a crack-resistant tile floor, and the reason it wins remodels where every fraction of height is spoken for at a door or an appliance.'),
 ('$14&ndash;$26/sq ft', 'installed tile with us, labor from $11/sq ft. The underlayment and the prep live inside that number &mdash; a bid that skips the layer is cheaper on paper and cracked in practice.'),
 ('2 years', 'our warranty on tile work &mdash; twice what most of the trade offers. We can carry it because the underlayment is chosen for the floor you actually have, and the wet areas behind it are flood-tested for 24 hours, on camera.'),
]),

'<h2>What Underlayment Actually Does</h2>',

"<p>Start with the physics, because every product in this article exists to solve one problem: <strong>tile does not bend, and houses never stop "
"moving</strong>. Wood framing swells in November and shrinks in July. Joists deflect underfoot. Concrete develops hairline cracks as it cures and keeps "
"developing them for years. Set a rigid, brittle surface directly on top of all that motion and the motion wins &mdash; as cracked tiles, cracked grout "
"lines, and corners that pop loose. Underlayment is the referee between the two: a layer that either stiffens the assembly, absorbs the movement, keeps "
"water out of it, or some combination of the three.</p>",

"<p>A quick word on terms, because the trade uses them loosely. The <em>subfloor</em> is the structural deck &mdash; plywood or OSB over joists, or a "
"concrete slab. The <em>underlayment</em> is what this article covers: the layer prepared or added on top of the subfloor to receive tile. And a "
"<em>membrane</em> may be part of that layer &mdash; for uncoupling, waterproofing, or both. If the words in your bid are vague, the assembly usually is "
"too; our primer on <a href=\"/blog/all-about-subfloors-what-you-need-to-know\">subfloors</a> covers the deck itself, and this one covers what goes on "
"top.</p>",

'<h2>Cement Board: The Default That Earned It</h2>',

"<p>Cement backer board &mdash; Durock, HardieBacker, wonderboard and their cousins &mdash; is exactly what it sounds like: a rigid sheet of cement-based "
"material, usually 1/4 or 1/2 inch thick, screwed down over a bed of thinset mortar, with the seams taped and mudded. It has been the default tile "
"underlayment in American bathrooms for forty years because it does the fundamental thing well: it gives tile a hard, stable, cement surface that mortar "
"loves and water cannot rot.</p>",

"<p>Two things cement board does <em>not</em> do, and both surprise homeowners. <strong>It is not waterproof.</strong> Water will not destroy it the way "
"it destroys drywall, but water passes through it freely &mdash; in a shower, cement board still needs a waterproofing membrane over its face or behind "
"it, sheet or liquid. \"Cement board because it is a shower\" is half an answer. <strong>And it does not uncouple.</strong> Screwed to the subfloor, it "
"moves with the subfloor; it stiffens the sandwich but does not absorb lateral movement the way a true uncoupling mat does. On a sound, flat, stiff floor "
"that is fine. On a bouncy 1950s plank subfloor, stiffness alone may not be enough &mdash; which is where the next product enters.</p>",

'<h2>Uncoupling Membranes: What Ditra Is Actually For</h2>',

"<p>An uncoupling membrane &mdash; Schluter Ditra is the household name, and every major brand now makes one &mdash; is a polyethylene mat about 1/8 inch "
"thick with a grid of dovetailed cavities, bonded to the subfloor in thinset, with the tile set directly on top. The geometry is the trick: the tile "
"locks into the cavities mechanically, but the mat lets the subfloor and the tile shear sideways past each other in tiny amounts. Wood expands under the "
"tile; the tile never feels it. That lateral give is what \"uncoupling\" means, and it is the modern answer to the old-school mortar bed that let "
"century-old tile floors float free of the structure beneath them.</p>",

"<p>When is it the right call? <strong>Over wood subfloors, almost always</strong> &mdash; it is what we reach for on most floor tile in wood-framed "
"houses, which around Puget Sound is most houses. <strong>Over cracked or green concrete</strong>, where it bridges hairline cracks and isolates the tile "
"from new ones. <strong>In height-critical remodels</strong>, where its 1/8 inch beats cement board&rsquo;s quarter-to-half inch plus thinset &mdash; the "
"same arithmetic that decides <a href=\"/blog/can-you-tile-over-existing-tile\">whether you can tile over an existing floor</a>. And with sealed seams "
"and banded edges, the same mat doubles as a waterproofing layer, which is why a laundry room or bathroom floor done in Ditra is cheap insurance. The "
"honest caveat: it is a system, and it works when installed as one &mdash; right mortar, right coverage, seams treated. A mat slapped down dry-lapped is "
"decoration.</p>",

table('Which Underlayment Goes Where', ['Your situation', 'What we reach for', 'Why'], [
 ('<strong>Bathroom floor, wood subfloor</strong>', 'Uncoupling membrane', 'Absorbs seasonal wood movement; seams sealed, it waterproofs the floor as a bonus'),
 ('<strong>Kitchen or large floor over wood</strong>', 'Uncoupling membrane', 'Big fields of tile need the movement relief most; low height at appliances'),
 ('<strong>Shower walls</strong>', 'Foam board, or cement board + membrane', 'Walls must be waterproof, not just water-tolerant &mdash; the membrane is the point'),
 ('<strong>Shower pan</strong>', 'Pre-slope + bonded membrane system', 'The pan is its own engineered assembly, flood-tested before tile'),
 ('<strong>Sound, flat concrete slab</strong>', 'Often none &mdash; prime and set', 'Concrete is already rigid and bonded tile does well; movement joints honored'),
 ('<strong>Cracked or newer slab</strong>', 'Uncoupling membrane', 'Bridges hairline cracks and isolates tile from ones still coming'),
 ('<strong>Heated tile floor</strong>', 'Uncoupling heat mat (e.g. Ditra-Heat)', 'Cable snaps into the same mat &mdash; one layer does heat, uncoupling and height control'),
 ('<strong>Dry-area wall or backsplash</strong>', 'Drywall is honestly fine', 'No water, no movement problem &mdash; paying for backer board here buys nothing'),
]),

'<h2>Foam Boards: Light, Waterproof, and Priced Like It</h2>',

"<p>The third family &mdash; Wedi, Kerdi-Board, GoBoard and similar &mdash; is an extruded foam core faced with cement or fleece. The pitch is simple: the "
"board itself is already waterproof. Screw it up, seal the seams and fastener heads with the manufacturer&rsquo;s sealant or banding, and the wall is done "
"&mdash; no separate membrane step. The boards weigh a fraction of cement board, cut with a utility knife instead of a grinder, and come as preformed "
"niches, benches and curbs, which is why they have taken over shower construction: fewer steps means fewer places for the install to go wrong, and in a "
"shower the places-it-can-go-wrong list is the whole game. It is the same logic we walk through for the trickiest detail in the stall in our "
"<a href=\"/blog/shower-niche-placement-size-waterproofing\">shower niche guide</a>.</p>",

"<p>The trade-off is money and honesty about where it matters. Foam board costs several times what cement board costs as material, and it earns that back "
"in labor and reliability <em>in wet areas</em>. On a dry floor it is usually the wrong spend &mdash; it adds height and cost to solve a waterproofing "
"problem the room does not have. A contractor who specs foam board everywhere is simplifying their inventory, not your project.</p>",

'<h2>The Substrates That Should Never See Tile</h2>',

"<p>The list of things people tile over, found later during demolition, is long and expensive. <strong>Bare plywood or OSB</strong>: mortar bonds to it "
"poorly and the wood&rsquo;s movement cracks the field &mdash; every wood subfloor needs one of the layers above. <strong>Drywall in a shower</strong>: it "
"is paper and gypsum; wet, it is compost, and no membrane painted over it changes what it is. <strong>Vinyl, laminate and hardwood</strong>: flexible, "
"cushioned or finished surfaces that mortar cannot grip for the long haul. And the evergreen: <strong>\"the grout will keep the water out.\"</strong> "
"Grout is porous. It has never once been waterproof, and every failed shower we open was built by someone who believed otherwise. Which layer goes under "
"the tile is also most of the difference between tile bids &mdash; the spread we decode in "
"<a href=\"/blog/tile-installation-cost-per-square-foot\">the per-square-foot breakdown</a> and the "
"<a href=\"/blog/bathroom-tile-installation-cost-seattle\">bathroom cost guide</a>.</p>",

two_col(
 'A bid that takes the layer seriously',
 ['Names the underlayment product, not just "backer board"',
  'Says what happens to the seams, edges and fastener heads',
  'Treats flatness as a line item &mdash; patch, grind or self-leveler',
  'Puts a real membrane in every wet area, over or instead of CBU',
  'Flood-tests the shower pan for 24 hours before tile, with photos',
  'Prices the assembly for your subfloor, not a one-spec-fits-all'],
 'Red flags worth walking away from',
 ['"We tile straight over the plywood, it&rsquo;s fine"',
  'Cement board in the shower with no membrane mentioned',
  'No flatness plan for large-format tile',
  'Foam board specced on dry floors "to be safe" &mdash; at your expense',
  'Grout and caulk carrying the waterproofing story',
  'A price that never asks what your subfloor is made of']),

'<h2>How We Choose on a Real Job</h2>',

"<p>On an estimate visit the decision usually takes five minutes, because the house answers most of it. What is the subfloor &mdash; wood or slab, and how "
"flat, how stiff? Is the room wet, damp-adjacent, or dry? Is height constrained by doors, appliances, or a transition to hardwood? Is floor heat in the "
"plan? Those four questions map almost mechanically onto the table above: uncoupling membrane over wood, membrane-or-foam in the wet, nothing but primer "
"on a good slab, the heat mat when cable is coming. What we do not do is bend the answer toward whatever is stacked in the shop &mdash; the underlayment "
"is picked for the floor, then the tile goes on it, in that order. That discipline is most of why we can put a 2-year warranty on the finished work. The "
"full scope &mdash; floors, showers, backsplashes, heated floors, large format &mdash; is on our "
"<a href=\"/seattle/tile-installation-in-seattle-wa\">Seattle tile installation page</a>.</p>",

faq('Tile Underlayment: What Homeowners Ask Us', [
 ('What is tile underlayment and do I really need it?',
  'Underlayment is the layer between the structural subfloor and the tile — cement board, an uncoupling membrane, or foam board, depending on the job. Over any wood subfloor you genuinely need one, because tile is rigid and wood never stops moving; the underlayment is what keeps that fight from ending in cracked grout. The main exception is a sound, flat concrete slab, which can often take tile directly.'),
 ('Is Ditra better than cement board?',
  'They solve different problems. Ditra and other uncoupling membranes absorb the sideways movement between wood and tile and add only 1/8 inch of height; cement board stiffens the assembly and gives a cheap, hard setting surface. Over wood-framed floors we reach for uncoupling most of the time. On walls, cement board or foam board wins because uncoupling matters much less vertically.'),
 ('Can you tile directly on plywood?',
  'No. Mortar bonds to plywood poorly, and the wood expands and contracts with every season, which cracks tile and grout over time. Every wood subfloor needs an underlayment — an uncoupling membrane or properly installed cement board — between it and the tile. Tiling straight over plywood is the single most common cause of the cracked floors we get called to replace.'),
 ('Is cement board waterproof?',
  'No — this is the most common misconception in tile. Cement board tolerates water without rotting, but water passes straight through it. In a shower, cement board must be paired with a waterproofing membrane, either sheet-applied or liquid, or replaced with a foam board system that is waterproof by itself. Cement board alone in a shower is a slow leak with a schedule.'),
 ('Do I need underlayment over a concrete slab?',
  'Often not. A sound, flat, cured slab is an excellent tile substrate on its own — primed and set, with the slab’s movement joints honored in the tile layout. Where a slab earns a membrane is when it has hairline cracks, is young enough to still be curing, or has a moisture problem; an uncoupling membrane there isolates the tile from cracks that exist and cracks still coming.'),
 ('What underlayment do heated tile floors use?',
  'The cleanest modern answer is an uncoupling heat mat — Ditra-Heat is the common one — where the heating cable snaps into the same studded mat that provides uncoupling. One layer handles movement, holds the cable at a consistent depth, and keeps total height down. The alternative, cable or mats buried in self-leveler, works too but adds height and a step.'),
 ('How much height does underlayment add to a floor?',
  'An uncoupling membrane adds about 1/8 inch plus thinset; cement board adds 1/4 to 1/2 inch plus the thinset bed beneath it. With the tile and mortar on top, the difference between the two assemblies can be close to half an inch — which is why remodels with tight door clearances and appliance heights usually push toward the membrane.'),
 ('Do walls need backer board too?',
  'Only where water is part of the job. Shower and tub-surround walls need a waterproof assembly — foam board, or cement board plus a membrane. A dry-area wall or a kitchen backsplash is honestly fine on drywall; tile and mastic or thinset over painted drywall has a decades-long track record in dry service, and paying for backer board there buys you nothing.'),
]),

cta('Not Sure What Belongs Under Your Tile?',
    'Tell us what the room is and we will tell you what the assembly should be &mdash; named products, flatness plan, and waterproofing spelled out in writing. Free in-home estimates across King &amp; Snohomish County.'),

related([
 ('/blog/can-you-tile-over-existing-tile', 'Can you tile over existing tile?'),
 ('/blog/shower-niche-placement-size-waterproofing', 'Shower niches done right'),
 ('/blog/all-about-subfloors-what-you-need-to-know', 'All about subfloors'),
 ('/blog/bathroom-tile-installation-cost-seattle', 'What bathroom tile really costs'),
 ('/seattle/tile-installation-in-seattle-wa', 'Tile installation in Seattle'),
 ('/contact', 'Book a free estimate'),
]),
]

assemble(S, parts)
