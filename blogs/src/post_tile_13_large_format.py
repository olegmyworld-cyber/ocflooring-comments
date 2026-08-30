from builder import *

S = 'large-format-tile-installation'

parts = [
date_badge('November 24, 2026'),

quick_answer(
 "<strong>Large-format tile &mdash; anything with an edge 15 inches or longer &mdash; is decided before the first tile touches mortar, by how flat the substrate is.</strong> "
 "The industry standard tightens from 1/4 inch in 10 feet to 1/8 inch in 10 feet the moment a long edge is involved, because a long, rigid tile bridges every dip and rocks on every hump, "
 "and the resulting edge-to-edge height difference &mdash; lippage &mdash; is visible from the doorway and permanent. Installed cost sits in the same $14&ndash;$26 per square foot range as "
 "other tile, with labor from $11/sq ft, but more of the budget shifts into flattening and back-buttering. In Shoreline's mid-century remodels, that prep line is usually the whole story.",
 'Shoreline remodels'),

facts([
 ('15 inches', 'the edge length where tile officially becomes large format and the rules change &mdash; tighter flatness, modified mortar, back-buttering, and a maximum 33% offset instead of the classic brick pattern.'),
 ('1/8" in 10 ft', 'the substrate flatness large-format tile demands. Most Shoreline subfloors we open up start at two to three times that, which is why flattening is a real line item and not padding.'),
 ('2 years', 'our warranty on tile work. We can offer it on large format because we flatten first and check mortar coverage as we set &mdash; the two things that decide whether a big tile cracks or lasts.'),
]),

'<h2>What Counts as Large Format &mdash; and Why the Rules Change</h2>',

"<p>The tile industry draws the line at any edge 15 inches or longer. A 12&times;24 plank, a 24&times;24 square, a 24&times;48 slab look, the wood-look planks that run 8&times;48 &mdash; all of it is "
"large-format tile, and all of it plays by a stricter rulebook than the 12&times;12s it replaced. The reason is stiffness. A small tile is short enough to follow gentle waves in a floor without "
"anyone noticing. A 48-inch plank is a straightedge: it touches the high spots, bridges the low ones, and every gap under it becomes either a hollow void that cracks later or a rocked edge that "
"sticks up next to its neighbor.</p>",

"<p>Manufacturers know this, which is why big tile is not perfectly flat either. Porcelain bows slightly in firing &mdash; a crown down the middle of a long plank is normal and allowed within "
"tolerance. Set two bowed planks in a 50% brick offset and the crown of one lands exactly at the low tip of the next. That is why the standard for long tile caps the offset at 33%: it is not a "
"style opinion, it is geometry. A layout that ignores it produces lippage even on a perfectly flat floor, and no installer can fix it after the fact.</p>",

'<h2>Flatness: The Spec That Decides the Whole Job</h2>',

"<p>For tile with any edge over 15 inches, the substrate has to be flat to within 1/8 inch over 10 feet, and 1/16 inch over 2 feet. Read that again with a Shoreline rambler in mind. A 1950s or "
"60s plank-and-plywood subfloor that has carried sixty years of living is routinely out by 1/4 to 3/8 inch across a kitchen &mdash; crowned over beams, dipped between joists, stepped where an "
"addition meets the original footprint. None of that matters under carpet. All of it matters under a 48-inch plank.</p>",

"<p>So the honest large-format quote starts with a straightedge and a level, not a tile catalog. Getting a floor to spec means grinding the high spots, filling the dips with patch, or &mdash; "
"most often on the floors we see &mdash; pouring self-leveling underlayment across the whole room and starting from a known-flat surface. That costs real money and usually a day of schedule, "
"and it is the single most common line item that separates two bids on the same room. The cheap bid did not find a cheaper way to flatten the floor. It skipped the step, and the floor will "
"say so within a year. What goes on top of the flattened substrate &mdash; membrane, board, and when each is right &mdash; is its own decision, and we walk through it in "
"<a href=\"/blog/tile-underlayment-explained\">tile underlayment explained</a>.</p>",

table('Where Large-Format Jobs Are Won or Lost', ['Decision', 'The standard', 'What skipping it looks like'], [
 ('<strong>Substrate flatness</strong>', '1/8" in 10 ft, 1/16" in 2 ft', 'Lippage at the edges, hollow spots underfoot, cracks over the dips within a couple of years'),
 ('<strong>Offset pattern</strong>', 'Max 33% offset on long edges', 'Tile crown meets tile tip &mdash; ridges down the room that shadow badly under window light'),
 ('<strong>Mortar</strong>', 'Large-and-heavy-tile mortar, deep notch', 'Ordinary thinset slumps under big tile; corners settle at different heights as it cures'),
 ('<strong>Back-buttering</strong>', 'Skim coat on the tile back, every tile', 'Voids under the tile &mdash; hollow sound now, cracked corners when a fridge rolls over it'),
 ('<strong>Coverage checks</strong>', 'Pull a tile and look, early and often', 'Nobody knows what the coverage is &mdash; until the floor reports back'),
 ('<strong>Grout joint</strong>', 'No tighter than the tile can support', 'Credit-card joints on bowed planks turn warpage into lippage at every edge'),
 ('<strong>Leveling clips</strong>', 'A finishing aid on a flat floor', 'Used as a substitute for flattening, they tension tiles over voids and pop corners loose'),
]),

'<h2>Lippage: The Problem You Can See From the Doorway</h2>',

"<p>Lippage is the height difference between the edges of two adjacent tiles, and it is the signature failure of large-format work. The allowance in the standard is small &mdash; about the "
"thickness of a credit card, plus whatever warpage the tile itself carries &mdash; because your eye is merciless about it. Low afternoon light raking across a floor turns a millimeter of "
"lippage into a ridge with a shadow line behind it, and once you have seen it you cannot stop. In a Shoreline living room with west-facing glass and a Puget Sound sunset every clear evening, "
"raking light is not an edge case. It is the daily condition the floor has to pass.</p>",

"<p>Leveling systems &mdash; the clips and wedges that hold neighboring edges flush while the mortar cures &mdash; are genuinely useful, and we use them on most large-format floors. But they "
"are a finishing tool, not a substitute for flat. A clip can hold two edges level over a dip only by tensioning one tile over a void, and a tile held in the air by a plastic clip while its "
"mortar cures is a tile with nothing under its corner. The clip snaps off, the job looks great for a season, and then the unsupported corner cracks under the leg of a couch. Flat substrate "
"first; clips to close the last fraction. That order cannot be reversed.</p>",

'<h2>Back-Buttering and the Coverage Problem</h2>',

"<p>Under a small tile, the ribbons of mortar from the trowel collapse and spread into something close to full contact. Under a 24&times;48, they do not &mdash; the tile is too stiff to help "
"compress them, and its slight bow guarantees the middle or the edges hang over air unless somebody does something about it. The something is back-buttering: a skim coat of mortar troweled "
"flat onto the back of every tile before it goes down, so the tile lands on wet-on-wet mortar and full contact is possible. Combined with a deep-notch trowel, directional troweling so air "
"can escape, and a proper large-and-heavy-tile mortar that will not slump, that is how you get to the coverage the standard asks for &mdash; and the way you know you are getting it is to "
"pull a freshly set tile every so often and look at its back.</p>",

"<p>This is slow, unglamorous work that doubles the mortar handling on the job, and it is exactly the step that disappears when a bid is priced to win. The floor does not complain "
"immediately. Voids announce themselves later, as a hollow drum note under a heel, a cracked corner where a chair leg landed, a grout line that opens over the spot where the mortar never "
"touched. By then the fix is replacement, tile by tile &mdash; the same expensive arithmetic we walk through in "
"<a href=\"/blog/tile-installation-cost-per-square-foot\">what a tile square foot really costs</a>.</p>",

'<h2>Large Format in Shoreline Remodels</h2>',

"<p>Shoreline's housing stock is mid-century almost wall to wall &mdash; ramblers and split-levels from the 50s and 60s, many of them deep into their second or third remodel as the city "
"densifies. Large format suits these houses: the long, low rooms and open plans that come out of a wall-removal remodel look right with fewer, bigger tiles and fewer grout lines. But the "
"same remodels stack the deck against flatness. Original 1&times;6 plank subfloors have crowned and cupped for sixty years. Additions meet the original slab or crawlspace framing at a step "
"that was never meant to be seen. Kitchens that lose a wall inherit two floors built in different decades at slightly different heights.</p>",

"<p>None of this rules out large format &mdash; we set it across Shoreline every month. It means the flattening pass is not optional and should be priced, in writing, before anyone orders "
"tile. When we quote a large-format floor from Richmond Beach to Ridgecrest, the straightedge comes out at the estimate, the self-leveler is a named line with a square footage on it, and "
"the layout drawing shows the offset so there are no surprises about the pattern. The full scope is on our "
"<a href=\"/city-of-shoreline/tile-installation-in-shoreline-wa\">Shoreline tile installation page</a>.</p>",

two_col(
 'What our large-format process includes',
 ['Straightedge survey of the substrate at the estimate, not on day one',
  'Flattening to the 1/8"-in-10-ft standard &mdash; self-leveler or grinding, priced in writing',
  'Large-and-heavy-tile mortar with a deep notch, troweled in one direction',
  'Back-buttering on every tile, with periodic pull-checks for coverage',
  'Offset capped at 33% on long edges, layout agreed before setting',
  'Leveling clips to finish &mdash; after the floor is flat, not instead of it'],
 'What the suspiciously cheap bid skips',
 ['Any flatness measurement at all &mdash; the tile ships and the trowel decides',
  'Self-leveler, because it costs a day and a few hundred dollars',
  'Back-buttering, because it doubles the mortar handling',
  'The offset rule, because 50% brick "looks classic"',
  'Coverage checks &mdash; nobody pulls a tile they would have to reset',
  'A warranty that outlives the first winter of raking light']),

'<h2>When Large Format Is the Wrong Answer</h2>',

"<p>We talk people out of large format regularly, and the reasons are practical. A small bathroom with a toilet flange, a vanity, and a door in eight feet of wall turns big tiles into a "
"cutting exercise &mdash; you pay large-format labor to install mostly pieces. A shower floor needs slope to a drain, and a rigid 24-inch tile cannot bend into a pre-sloped pan; that is "
"mosaic territory, and the waterproofing underneath matters far more than the tile on top &mdash; the assembly we describe in "
"<a href=\"/blog/tile-shower-waterproofing\">shower waterproofing</a> and flood-test for 24 hours on every pan we build. And a floor that genuinely cannot be flattened &mdash; a structural "
"step, a budget that will not carry the leveling pass &mdash; is better served by a smaller tile that can follow the surface honestly than by a big tile fighting it. A 12&times;12 set well "
"beats a 24&times;48 set badly, every time, for a decade longer. How the tile itself is made matters too &mdash; dense porcelain planks cut and wear differently than ceramic, a difference "
"we unpack in <a href=\"/blog/porcelain-vs-ceramic-tile\">porcelain vs ceramic</a>.</p>",

'<h2>Reading a Large-Format Quote</h2>',

"<p>Three questions sort the bids. <strong>What did you measure the floor with, and what did you find?</strong> If nobody put a straightedge on the substrate, the flatness problem is still "
"in the job &mdash; it is just unpriced. <strong>Is flattening its own line item?</strong> A number for self-leveler or grinding, with a square footage, means the bidder intends to do it. "
"\"Prep included\" in a bid that is $2,000 under the others means it is not. <strong>What offset are you planning?</strong> Anyone who answers 50% on a 48-inch plank has told you they have "
"not read the tile manufacturer's own instructions. The rest &mdash; which plank, which grout color, which direction the boards run &mdash; is the fun part, and we will happily spend an "
"hour on it once the floor underneath is settled.</p>",

faq('Large-Format Tile: What Homeowners Ask Us', [
 ('What is considered large-format tile?',
  'Any tile with at least one edge 15 inches or longer. That covers 12x24 rectangles, 24x24 squares, wood-look planks at 8x48, and the big 24x48 slab looks. Once a tile crosses that line, the installation standards tighten: the substrate must be flat to 1/8 inch in 10 feet, the mortar changes, back-buttering becomes standard practice, and offsets on long edges are capped at 33%.'),
 ('Does large-format tile cost more to install?',
  'The installed range is the same $14 to $26 per square foot we quote for tile generally, with labor from $11 per square foot, but large format tends to land higher inside the range. The tile itself is often no more expensive; the difference is flattening the substrate to the tighter standard and the slower setting process — back-buttering, coverage checks, leveling clips. On an out-of-flat floor, the prep can be a third of the job.'),
 ('Why does my contractor want to pour self-leveler first?',
  'Because your floor is not flat to 1/8 inch in 10 feet, and almost no lived-in floor is. Self-leveling underlayment is usually the fastest, most reliable way to hit the standard across a whole room. It is a legitimate, necessary line item on most large-format jobs — the bid that skips it is not cheaper, it is incomplete.'),
 ('What is lippage and how much is acceptable?',
  'Lippage is the height difference between the edges of neighboring tiles. The standard allows roughly a credit card of difference plus whatever warpage the tile carries — beyond that you see ridges and shadow lines, especially in low, raking light. It comes from setting rigid tile on an unflat floor, from too-tight grout joints, or from a 50% offset that stacks tile crowns against tile tips.'),
 ('Do tile leveling clips actually work?',
  'Yes, for what they are for: holding adjacent edges flush during cure to close the last fraction of a millimeter. What they cannot do is substitute for a flat substrate. A clip that levels two tiles over a dip is holding one tile above a void, and that unsupported corner is a crack waiting for a load. Flat floor first, clips second.'),
 ('What is back-buttering and is it really necessary?',
  'Back-buttering is troweling a thin skim coat of mortar onto the back of each tile before setting it, on top of the mortar combed onto the floor. On large format it is not optional — big, stiff, slightly bowed tiles cannot compress trowel ridges into full contact on their own. Skipping it leaves voids, and voids become hollow spots, cracked corners, and open grout lines.'),
 ('Can I use a 50% brick offset with 12x24 or longer tile?',
  'You should not, and most tile manufacturers explicitly say so. Long porcelain tiles bow slightly in firing; at a 50% offset the highest point of one tile lands beside the lowest point of the next, creating lippage no installer can prevent. The standard caps the offset at 33% for long edges — a third-offset stagger looks very close to brick and lies flat.'),
 ('Is large-format tile a good idea in a mid-century Shoreline house?',
  'Usually yes, with the flattening priced honestly. Mid-century ramblers suit the look, but their plank subfloors and remodel seams are routinely out of flat by two or three times the large-format standard. Expect a self-leveling pass in the quote. If a bid on a 1950s house has no flatness line at all, that is the bid to be suspicious of.'),
]),

cta('Thinking About Large-Format Tile?',
    'We will put a straightedge on your floor at the estimate, tell you exactly what flat costs, and show you the layout before anything is ordered &mdash; in writing, with the prep priced. Free in-home estimates across King &amp; Snohomish County.'),

related([
 ('/blog/tile-underlayment-explained', 'Tile underlayment explained'),
 ('/blog/tile-installation-cost-per-square-foot', 'Tile cost per square foot'),
 ('/blog/porcelain-vs-ceramic-tile', 'Porcelain vs ceramic tile'),
 ('/blog/tile-shower-waterproofing', 'Shower waterproofing'),
 ('/city-of-shoreline/tile-installation-in-shoreline-wa', 'Tile installation in Shoreline'),
 ('/contact', 'Book a free estimate'),
]),
]

assemble(S, parts)
