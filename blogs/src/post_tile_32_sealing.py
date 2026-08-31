from builder import *

S = 'sealing-and-maintaining-tile'

parts = [
date_badge('April 6, 2027'),

quick_answer(
 "<strong>Most tile never needs sealing. Porcelain and glazed ceramic are effectively sealed at the factory, and epoxy grout is sealed by "
 "chemistry &mdash; the only things in your bathroom that genuinely drink a sealer are cement grout and natural stone.</strong> That one sentence "
 "saves most homeowners a weekend a year and a cabinet of products. The honest maintenance list is short: a pH-neutral cleaner, no vinegar or "
 "acid anywhere near stone, sealer on cement grout every year or two in wet areas, and the knowledge that dingy grout usually needs a deep clean, "
 "not another coat of sealer.",
 'Cottage Lake &amp; Woodinville area'),

facts([
 ('2 materials', 'in a tiled room actually absorb sealer: cement grout and natural stone. Porcelain, glazed ceramic, and epoxy grout do not need it &mdash; ever.'),
 ('1&ndash;2 years', 'the honest resealing cadence for cement grout in a working shower. Dry-area floors stretch far longer &mdash; and stone follows the water-drop test, not the calendar.'),
 ('2 years', 'our warranty on tile work. The maintenance that protects it is unglamorous: neutral cleaner, sealed cement grout, and silicone renewed when it fails.'),
]),

'<h2>What Actually Needs Sealing</h2>',

"<p>The sealer aisle is built on a misunderstanding, so let us clear it up. Sealer exists for porous materials &mdash; things with microscopic openings "
"that drink liquid. In a tiled room, exactly two things qualify.</p>",

"<p><strong>Cement grout.</strong> Ordinary sanded or unsanded grout is a cement product, and cement is porous. Unsealed, it absorbs water, soap, oils, "
"and whatever is in them, which is how grout lines end up stained two shades darker in the shower and along the cooking side of a backsplash. A "
"penetrating sealer soaks into those pores and buys you time to wipe things up before they soak in. It does not make grout waterproof &mdash; nothing "
"makes cement grout waterproof &mdash; it makes it slower to stain.</p>",

"<p><strong>Natural stone.</strong> Marble, travertine, limestone, slate, and most granite are porous rock, tile shape notwithstanding. They need a "
"penetrating sealer on the tile itself, not just the grout, and they need it on a recurring basis. If you have a stone floor or a marble shower, "
"sealing is genuinely part of ownership &mdash; which is one of the honest costs we put on the table when someone is choosing between stone and "
"porcelain in the first place.</p>",

'<h2>What Never Needs Sealing</h2>',

"<p><strong>Porcelain tile</strong> is fired so dense that it absorbs almost nothing &mdash; that near-zero absorption is practically the definition of "
"porcelain, and it is a big part of why we set it in most wet areas (the full comparison is in "
"<a href=\"/blog/porcelain-vs-ceramic-tile\">porcelain vs ceramic</a>). Sealer has nowhere to go; on a polished porcelain surface it can even sit on "
"top as a hazy film you then get to strip. <strong>Glazed ceramic</strong> is the same story for a different reason: the glaze is a fired glass "
"coating, and glass does not absorb. The unglazed edges buried in thinset do not matter.</p>",

"<p><strong>Epoxy grout</strong> is sealed by chemistry &mdash; it is a resin, not a cement, so there are no pores to fill. It never needs sealer, "
"which is exactly why we push it in heavy-use showers despite the higher install cost; that trade is laid out in "
"<a href=\"/blog/epoxy-vs-cement-grout\">epoxy vs cement grout</a>. If a product or a contractor offers to seal your porcelain tile or your epoxy "
"grout for money, you have learned something useful about the product or the contractor.</p>",

table('Seal It or Skip It', ['Surface', 'Needs sealer?', 'The honest cadence'], [
 ('<strong>Cement grout, shower</strong>', 'Yes &mdash; penetrating sealer', 'Every 1&ndash;2 years; water stops beading and darkens the line when it is due'),
 ('<strong>Cement grout, dry floor</strong>', 'Yes, less urgently', 'Every few years; kitchens and entries sooner than bedrooms and halls'),
 ('<strong>Epoxy grout</strong>', 'Never', 'It is resin &mdash; there is nothing for sealer to soak into'),
 ('<strong>Porcelain tile</strong>', 'No', 'Near-zero absorption from the kiln; sealer just films on the surface'),
 ('<strong>Glazed ceramic</strong>', 'No', 'The glaze is fired glass &mdash; already the best sealer there is'),
 ('<strong>Natural stone</strong>', 'Yes &mdash; tile and grout both', 'When water stops beading on the stone; showers before dry floors'),
 ('<strong>Silicone joints</strong>', 'No &mdash; replaced, not sealed', 'Recaulk changes of plane when the bead cracks or peels'),
]),

'<h2>Cleaner Honesty: What to Use and What to Keep Away</h2>',

"<p>Daily and weekly maintenance is where most tile damage actually happens, and the villains are usually under the sink already. The rule that matters "
"most: <strong>no vinegar, no lemon, nothing acidic on natural stone, ever.</strong> Acid does not clean marble or travertine &mdash; it dissolves them. "
"The dull spot vinegar leaves on polished marble is not residue; it is an etch, a change to the surface of the rock, and no cleaner takes it back out. "
"Acidic cleaners are also hard on cement grout over time, eating the paste at the surface until the line goes sandy.</p>",

"<p>What we actually recommend is boring: a <strong>pH-neutral tile cleaner</strong> &mdash; or warm water and a drop of dish soap &mdash; a microfiber "
"mop, and a squeegee in the shower, which does more for grout than any product because it removes the water before minerals and soap settle in. Skip "
"oil and wax &ldquo;shine&rdquo; products that build a film, abrasive powders and steel wool on glazed surfaces, and the habit of letting bleach sit in "
"grout lines &mdash; occasional and diluted is survivable on cement grout, but it is a stain-hider, not a cleaner, and it does stone no favors. On "
"colored grout, harsh chemistry is also how a carefully chosen shade drifts &mdash; picking one that ages gracefully is its own decision, covered in "
"<a href=\"/blog/choosing-grout-color\">choosing a grout color</a>.</p>",

two_col(
 'On our own floors',
 ['pH-neutral cleaner, or warm water with a drop of dish soap',
  'Microfiber mop or cloth &mdash; and vacuuming grit before it scratches',
  'A shower squeegee &mdash; 30 seconds that outperforms any sealer',
  'Enzyme or oxygen cleaners for organic grout stains, rinsed well',
  'Penetrating sealer on cement grout and stone, on schedule',
  'Fresh silicone at corners the moment the old bead fails'],
 'Kept away from tile and stone',
 ['Vinegar, lemon, or any acid on natural stone &mdash; it etches on contact',
  'Acidic "grout brighteners" used as routine cleaners',
  'Oil soaps and wax shines that build a dull, slippery film',
  'Abrasive powders and steel wool on glazed surfaces',
  'Bleach as a habit &mdash; it whitens stains without removing them',
  'Sealer sold for porcelain or epoxy grout &mdash; it has no job to do']),

'<h2>How Often to Reseal &mdash; and the 10-Second Test</h2>',

"<p>Forget memorizing a schedule; the material tells you. <strong>Drip water on the grout line or the stone and watch it.</strong> If it beads or sits "
"on the surface, the sealer is working. If it soaks in and darkens the material within a minute or two, it is time. In practice that means cement "
"grout in a daily-use shower wants sealer every year or two, dry-area floors stretch to several years, and stone runs its own schedule depending on "
"how porous it is and how much water it sees. Sealing day is undramatic: clean the grout properly, let it dry fully, apply a penetrating sealer, wipe "
"the excess off the tile faces before it hazes. The cleaning is the hard part &mdash; which brings us to the next section.</p>",

'<h2>When Dingy Grout Means Cleaning, Not Resealing</h2>',

"<p>Here is the misdiagnosis we see most: grout has gone grey or blotchy, the homeowner reseals it, nothing improves &mdash; because sealer is "
"prevention, not restoration. <strong>Sealing dirty grout locks the dirt in.</strong> Uniformly darker grout in traffic lanes and shower floors is "
"almost always embedded soil and soap film sitting in the pores, and the fix is a proper deep clean &mdash; an alkaline or oxygen-based grout cleaner, "
"a stiff nylon brush, patience &mdash; followed by sealer once it is clean and dry. Done in that order, ten-year-old grout frequently comes back two "
"shades lighter and stays there.</p>",

"<p>Being honest about the boundaries: if grout is cracking, crumbling, or coming out in pieces, that is not a cleaning problem or a sealing problem "
"&mdash; that is a regrout, and sometimes evidence of movement underneath that deserves a look. The decision tree for that is in "
"<a href=\"/blog/regrouting-vs-retiling-a-shower\">regrouting vs retiling a shower</a>. And one distinction worth engraving: <strong>sealer is not "
"waterproofing.</strong> A shower stays out of the framing because of the membrane system behind the tile &mdash; the pre-slope, bonded membrane, and "
"the 24-hour flood test we photograph on every pan &mdash; not because of anything applied to the grout. If a shower is leaking, sealer is not the "
"conversation; <a href=\"/blog/tile-shower-waterproofing\">how showers are actually waterproofed</a> is.</p>",

'<h2>Tile Maintenance in Cottage Lake</h2>',

"<p>Around Cottage Lake and the Woodinville area, most of what we install is porcelain over proper membranes with, increasingly, epoxy grout in the "
"showers &mdash; which is a polite way of saying we mostly build tile that does not want your weekends. Where homeowners here do the most damage is "
"well-intentioned: vinegar habits brought to a new stone floor, and shower grout that needed a deep clean getting coat after coat of sealer instead. "
"Both are cheap to avoid now that you know.</p>",

"<p>If your tile is past what maintenance can fix &mdash; cracked lines, crumbling grout, a shower you no longer trust &mdash; we will tell you "
"plainly which it is and what it costs, with labor from $11/sq ft and $14&ndash;$26/sq ft installed on full rebuilds, backed by that 2-year warranty. "
"The local details are on our <a href=\"/city-of-cottage-lake/tile-installation-in-cottage-lake-wa\">Cottage Lake tile installation page</a>.</p>",

faq('Sealing and Maintaining Tile: What Homeowners Ask Us', [
 ('Does porcelain tile need to be sealed?',
  'No. Porcelain is fired dense enough that it absorbs almost nothing, so penetrating sealer has nowhere to go and surface sealers just build a hazy film you eventually have to strip. The cement grout between porcelain tiles is the part that drinks sealer — seal the lines, skip the tile.'),
 ('How often should I seal shower grout?',
  'Cement grout in a daily-use shower wants a penetrating sealer every year or two. The water test beats the calendar: drip water on the line — if it beads, you are fine; if it soaks in and darkens the grout within a minute or two, it is time. Epoxy grout never needs sealing at all.'),
 ('Can I use vinegar to clean tile floors?',
  'On glazed ceramic or porcelain, diluted vinegar will not hurt the tile, though it slowly attacks cement grout. On natural stone the answer is an absolute no — vinegar etches marble, travertine, and limestone on contact, leaving permanent dull spots that no cleaner removes. A pH-neutral cleaner does the same job with none of the risk.'),
 ('My grout is dark and dingy. Should I reseal it?',
  'Clean it first — dingy grout is almost always embedded soil and soap film, and sealer locks in whatever is already there. Deep-clean with an alkaline or oxygen-based grout cleaner and a stiff nylon brush, let it dry completely, and then seal. Resealing dirty grout is the most common tile maintenance mistake we see.'),
 ('Does sealing grout make my shower waterproof?',
  'No — and this one matters. Sealer slows staining; it does not stop water. Grout and tile were never the waterproofing: the membrane system behind them is, which is why every shower we build gets a pre-slope, a bonded membrane, and a photographed 24-hour flood test. If a shower is leaking, no sealer will save it.'),
 ('Does natural stone tile really need regular sealing?',
  'Yes — the stone itself, not just the grout. Marble, travertine, limestone, slate, and most granite are porous and need a penetrating sealer on a recurring basis, more often in showers than on dry floors. If that maintenance does not appeal, porcelain that looks like stone is the honest alternative, and we will say so at the estimate.'),
 ('What is the best everyday cleaner for tile?',
  'A pH-neutral tile cleaner or warm water with a drop of dish soap, applied with a microfiber mop — plus a squeegee after every shower, which does more for grout than any bottled product. Avoid oil soaps and wax shines that build film, abrasives that scratch glaze, and acids anywhere near stone or cement grout.'),
 ('When is dingy or damaged grout beyond cleaning and sealing?',
  'When it is cracking, crumbling, or coming out in pieces — that is a regrout, not a cleaning job, and cracks that keep returning in the same lines can point to movement underneath that deserves an inspection. Stains that survive a proper deep clean can also justify regrouting for the color reset alone.'),
]),

cta('Want an Honest Read on Your Tile?',
    'We will tell you whether your grout needs a clean, a seal, or a regrout &mdash; and whether the tile behind it is worth keeping. Free in-home estimates across King &amp; Snohomish County, with every rebuild backed by our 2-year warranty.'),

related([
 ('/blog/tile-shower-waterproofing', 'How tile showers are waterproofed'),
 ('/blog/epoxy-vs-cement-grout', 'Epoxy vs cement grout'),
 ('/blog/regrouting-vs-retiling-a-shower', 'Regrouting vs retiling a shower'),
 ('/blog/choosing-grout-color', 'Choosing a grout color'),
 ('/city-of-cottage-lake/tile-installation-in-cottage-lake-wa', 'Tile installation in Cottage Lake'),
 ('/contact', 'Book a free estimate'),
]),
]

assemble(S, parts)
