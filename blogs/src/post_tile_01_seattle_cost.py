from builder import *

S = 'bathroom-tile-installation-cost-seattle'

parts = [
date_badge('September 1, 2026'),

quick_answer(
 "<strong>A full bathroom tile job in Seattle runs $14&ndash;$26 per square foot installed, with labor starting at $11/sq ft &mdash; "
 "so a standard 40 sq ft bathroom floor lands around $560&ndash;$1,040, and a tiled shower surround usually costs more than the floor it drains into.</strong> "
 "The number moves on three things and almost nothing else: how much prep the substrate needs, whether there is a shower involved "
 "(waterproofing is where the real labor sits), and how hard your tile is to cut. Old Seattle houses tend to push all three the same direction.",
 'Seattle homes &amp; condos'),

facts([
 ('$11/sq ft', 'where our tile labor starts. Installed cost &mdash; labor plus materials, prep and setting products &mdash; runs $14 to $26 per square foot depending on the tile and what is underneath it.'),
 ('24 hours', 'how long a finished shower pan sits full of water before we tile over it. We photograph the flood test and keep it on file, because a leak found after tile is a demolition, not a repair.'),
 ('2 years', 'our warranty on tile work &mdash; longer than the one-year most of the trade offers, which is a bet we are willing to make because of what goes in behind the tile.'),
]),

'<h2>Where the Money Actually Goes</h2>',

"<p>Homeowners tend to budget for tile the way they budget for paint: price per square foot, times square feet, done. Tile does not work that way, and the gap between the "
"cheap quote and the honest one is almost never the tile itself. It is the hours underneath.</p>",

"<p>On a bathroom floor, roughly a third of the labor happens before a single tile is set &mdash; pulling the old floor, checking the subfloor for deflection, flattening it, and setting an "
"uncoupling membrane so seasonal movement in a 1920s Wallingford joist bay does not telegraph into a cracked grout line three winters from now. On a shower, that share climbs past half. "
"The waterproofing assembly is the product you are actually buying. The tile is the part you can see.</p>",

table('What Drives a Seattle Tile Quote Up or Down', ['Factor', 'Effect on price', 'Why'], [
 ('<strong>Shower vs floor only</strong>', 'Shower costs more per sq ft', 'Pre-slope, membrane, curb, niche, and a flood test &mdash; far more labor per square foot than a flat floor'),
 ('<strong>Subfloor condition</strong>', '+$2&ndash;$6/sq ft', 'Old plank subfloors and bouncy joists need flattening or a new layer before tile is safe to set'),
 ('<strong>Tile size</strong>', 'Large format costs more', 'Big tile needs a flatter substrate and back-buttering; small mosaic costs more in setting time per square foot'),
 ('<strong>Tile hardness</strong>', 'Porcelain over ceramic', 'Porcelain is denser and slower to cut, especially around a drain or a niche'),
 ('<strong>Pattern</strong>', 'Herringbone, chevron: +15&ndash;30% labor', 'More cuts, more waste, more layout time before anything gets set'),
 ('<strong>Heated floor</strong>', 'Adds material and a day', 'Mat or cable, a thermostat, and an electrician for the circuit'),
 ('<strong>Demolition</strong>', 'Varies widely', 'One layer of vinyl is quick; mortar bed over wire lath in a 1940s bathroom is not'),
 ('<strong>Access</strong>', 'Condo &gt; house', 'Elevator reservations, protected common areas, and dumpster rules add hours nobody enjoys billing for'),
]),

'<h2>Three Real Seattle Bathrooms</h2>',

"<p>Rather than a range, here is what the ranges look like as actual rooms. <strong>A 40 sq ft floor-only refresh</strong> in a Ballard bungalow &mdash; tear out sheet vinyl, flatten the "
"plank subfloor, membrane, set 12&times;24 porcelain &mdash; sits at the lower end per square foot but carries fixed costs that a bigger room would spread out, so the total lands higher "
"than 40 &times; $14 would suggest. <strong>A standard tub surround</strong>, about 60 sq ft of wall, is mostly waterproofing labor and lands in the middle of the range. "
"<strong>A curbless walk-in shower</strong> in a Green Lake remodel is the top of the range and then some: the floor has to be opened and the joists modified so the pan can slope "
"without a curb, which is structural work before it is tile work.</p>",

"<p>The pattern worth internalizing is that <em>small bathrooms are expensive per square foot and cheap in total</em>. Mobilization, layout, and the waterproofing sequence cost about "
"the same in a powder room as in a primary bath. If you are comparing a $1,400 quote on a tiny floor against $14/sq ft and feeling gouged, that is the arithmetic you are hitting.</p>",

'<h2>Why Old Seattle Houses Cost More to Tile</h2>',

"<p>The city's housing stock is the single biggest local variable. A large share of the bathrooms we tile inside city limits were built before 1950, and they bring three recurring costs.</p>",

"<p><strong>Subfloor deflection.</strong> Craftsman-era joists were sized for linoleum, not for a stone-and-mortar assembly. Tile is unforgiving about movement &mdash; the industry standard "
"is deflection no worse than L/360 for ceramic, and stiffer still for natural stone. Sometimes that means sistering joists or adding a layer. It is not upselling; it is the difference "
"between a floor that lasts twenty years and one that cracks in two.</p>",

"<p><strong>Nothing is square or level.</strong> A hundred years of settling means walls that lean and floors that fall an inch across eight feet. Every cut is custom, and layout &mdash; "
"deciding where the inevitable tapered cut goes so it lands somewhere you will not stare at &mdash; takes real time before anything is set.</p>",

"<p><strong>What is behind the old tile.</strong> Bathrooms remodeled in the 1980s and 90s frequently hide a failed pan or rotted framing under an intact-looking surface. We open it, "
"photograph it, and price it before we go further, which is also why an honest tile quote in Seattle has a contingency line in it and a suspiciously cheap one does not. If the damage "
"reaches the framing under an adjoining floor, that becomes a different conversation &mdash; the same one we have about "
"<a href=\"/blog/can-i-install-hardwood-flooring-in-a-basement-or-other-moisture-prone-areas\">wood in moisture-prone spaces</a>.</p>",

'<h2>The Waterproofing Line Item Nobody Shops</h2>',

"<p>If you compare three shower quotes, this is the line that explains the spread, and it is usually invisible on the page. There are two legitimate ways to waterproof a shower: "
"a bonded sheet membrane (Schluter Kerdi and similar) or a liquid-applied membrane rolled on in coats to a measured thickness. Both work. Both cost real money and real hours.</p>",

"<p>What does not work is tiling over green board, or over cement board with no membrane at all, on the theory that the tile and grout will keep water out. They will not &mdash; grout is "
"not waterproof, and it was never supposed to be. Water passes through, and the membrane behind is what sends it back to the drain. That assembly is why we flood-test every pan for "
"24 hours and photograph it before tile goes on, and why the warranty is two years instead of one.</p>",

two_col(
 'What a complete quote includes',
 ['Demolition and disposal of the existing surface',
  'Substrate inspection, flattening, and an uncoupling membrane on floors',
  'Pre-slope and bonded waterproofing on any shower pan',
  'A documented 24-hour flood test before tile goes on',
  'Setting, grouting, sealing, and silicone at every change of plane',
  'A named tile, a named membrane, and a named grout &mdash; not "materials"'],
 'What a suspiciously cheap quote leaves out',
 ['Any allowance for what is found under the old floor',
  'Membrane behind the shower &mdash; just cement board and hope',
  'The flood test, because it costs a day of schedule',
  'Flattening, so large tile lippage becomes your problem',
  'Silicone at the corners, where grout will crack no matter what',
  'A warranty longer than the drive home']),

'<h2>Tile, Vinyl, or Something Else?</h2>',

"<p>Tile is the right answer for a wet room and an expensive answer everywhere else. In a bathroom, it is genuinely the material that belongs: it does not care about standing water, "
"it cleans up, and a well-built tiled shower outlives the house's next two owners. In a kitchen, the calculus is closer &mdash; we lay out that argument in "
"<a href=\"/blog/hardwood-vs-tile-in-the-kitchen\">hardwood vs tile in the kitchen</a>. In a laundry room or a basement, waterproof vinyl often wins on cost and comfort underfoot, which is "
"the case we make in <a href=\"/blog/the-benefits-of-waterproof-flooring-in-seattle-wa\">waterproof flooring for Seattle homes</a> and in the "
"<a href=\"/blog/what-is-the-best-waterproof-floor-in-everett-wa\">waterproof floor guide</a>.</p>",

"<p>Where tile earns its price is the shower and the bathroom floor, and where it wastes your money is a room that will never see water and where a cracked grout line will annoy you "
"every day. Anyone quoting you tile for a bedroom should explain themselves.</p>",

'<h2>Getting a Number You Can Trust</h2>',

"<p>Three questions separate a quote you can rely on from a number designed to win the job. <strong>What waterproofing product, by name?</strong> If the answer is vague, the assembly "
"is probably vague too. <strong>What happens if you open the floor and find rot?</strong> A good contractor has already told you the hourly or unit rate for that discovery; a bad one "
"discovers it mid-job and hands you a number when you have no leverage. <strong>Will you flood-test the pan, and can I see it?</strong> A yes costs a day and is the cheapest insurance "
"in the whole project.</p>",

"<p>Everything else &mdash; tile selection, pattern, grout color &mdash; is a preference conversation, and it is genuinely fun. The three questions above are the ones that decide whether "
"you are still happy in ten years. Our full scope, neighborhood by neighborhood, is on the "
"<a href=\"/seattle/tile-installation-in-seattle-wa\">Seattle tile installation page</a>.</p>",

faq('Bathroom Tile Cost in Seattle: What Homeowners Ask Us', [
 ('How much does it cost to tile a bathroom in Seattle?',
  'Installed cost runs $14 to $26 per square foot, with labor starting at $11 per square foot. A 40 square foot floor-only job typically lands between $560 and $1,040 in tile work, and a tiled shower costs more per square foot than a floor because the waterproofing assembly behind it is most of the labor. The spread inside that range is decided by substrate prep, tile size and hardness, and pattern.'),
 ('Why is tiling a small bathroom so expensive per square foot?',
  'Because most of the cost is fixed. Mobilization, layout, the waterproofing sequence, and the flood test cost roughly the same in a powder room as in a large primary bath, so those hours divide across fewer square feet. Small rooms are expensive per square foot and still cheap in total compared with a big one.'),
 ('What makes tile quotes vary so much between contractors?',
  'Almost always the waterproofing and the prep, not the tile. A quote that assumes cement board with no membrane, skips flattening, and does not budget for what is under the old floor will always be cheaper on paper. Ask each bidder to name the membrane and say whether they flood-test the pan, and the spread usually explains itself.'),
 ('Do you have to remove the old tile first?',
  'Usually yes in a bathroom, and always in a shower. Tiling over existing tile is possible on some floors when the substrate is sound and the height increase does not fight your doors and fixtures, but in a wet area you need to see and rebuild what is behind it. Old bathrooms in Seattle hide failed pans often enough that opening it up is the responsible default.'),
 ('What does waterproofing add to the cost of a shower?',
  'It is not a small line item, and it should not be. Between the pre-slope, the bonded membrane or liquid-applied coats, the corners and the drain assembly, plus a day of schedule for the flood test, waterproofing is a substantial share of a shower quote. It is also the entire reason the shower does not leak into the ceiling below.'),
 ('How long does a bathroom tile job take?',
  'A floor-only bathroom is usually two to three days including prep and grout. A tub surround or shower runs four to six days, because waterproofing has to cure, the flood test takes 24 hours, and grout and silicone need their own time. Older houses that need subfloor work add a day or two on top.'),
 ('Is porcelain worth paying more for than ceramic?',
  'In a bathroom, generally yes. Porcelain is denser, absorbs less water, and holds up better on floors, which is why it is what we set in most wet areas. Ceramic is perfectly good on walls and backsplashes, where the demands are lower. The material difference is smaller than most people expect; the installation difference is that porcelain is harder to cut, which is in the labor.'),
 ('Do you tile condos in downtown Seattle?',
  'Yes, and we plan around the building rather than fighting it. That means elevator reservations, protected common areas, work-hour rules, and hauling debris the way the HOA requires. Those constraints add hours, so we price them honestly up front rather than discovering them on day one.'),
]),

cta('Want a Real Number for Your Bathroom?',
    'We will look at the substrate, tell you what the shower needs behind the tile, and put the whole scope in writing &mdash; including what happens if we open the floor and find a surprise. Free in-home estimates across King &amp; Snohomish County.'),

related([
 ('/blog/hardwood-vs-tile-in-the-kitchen', 'Hardwood vs tile in the kitchen'),
 ('/blog/what-is-the-best-waterproof-floor-in-everett-wa', 'The best waterproof floors'),
 ('/blog/the-benefits-of-waterproof-flooring-in-seattle-wa', 'Waterproof flooring in Seattle'),
 ('/blog/can-i-install-hardwood-flooring-in-a-basement-or-other-moisture-prone-areas', 'Wood in moisture-prone rooms'),
 ('/seattle/tile-installation-in-seattle-wa', 'Tile installation in Seattle'),
 ('/contact', 'Book a free estimate'),
]),
]

assemble(S, parts)
