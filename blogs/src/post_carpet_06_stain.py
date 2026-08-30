from builder import *

S = 'stain-resistant-carpet'

parts = [
date_badge('November 12, 2026'),

quick_answer(
 "<strong>&ldquo;Stain-resistant&rdquo; covers two very different technologies: a topical treatment sprayed onto ordinary fiber at the mill, which fades with cleaning and traffic, and solution-dyed "
 "fiber, where color and stain resistance are built into the plastic itself and cannot wash off.</strong> The warranty behind the label is a list, not a promise &mdash; it names the substances it covers, "
 "quietly excludes oils, dyes and anything classed as wear, and requires cleaning records you have to keep. Buy the fiber, read the list, and put a moisture-barrier pad underneath &mdash; that is the "
 "order of operations that actually protects a Shoreline family's floor.",
 'Shoreline family homes'),

facts([
 ('2 technologies', "hide behind one label. Topical stain treatments ride on the fiber&rsquo;s surface and thin out with every hot-water extraction; solution-dyed fiber is stain-resistant to its core, for the life of the carpet."),
 ('12&ndash;18 months', 'the professional cleaning interval most stain warranties quietly require &mdash; with receipts. Skip it, or clean with the wrong machine, and a valid claim can die on paperwork.'),
 ('From $1.49/sq ft', 'where installed carpet starts with us. The stain-resistant lines cost more per foot, and in the rooms where life actually happens, they are usually the cheapest insurance in the house.'),
]),

'<h2>&ldquo;Stain-Resistant&rdquo; Means Two Different Things</h2>',

"<p>Walk any carpet aisle and nearly everything claims stain resistance, which should make you suspicious, and rightly so. The label describes two technologies that age in opposite directions. The "
"first is <strong>topical</strong>: ordinary dyed fiber gets a stain-blocking treatment applied at the mill. It works on day one. It also lives on the surface of the fiber, which means foot traffic "
"grinds it away in the lanes and every deep cleaning rinses a little more of it out &mdash; so it is weakest exactly where and when you need it most, in the busy zones of a carpet's middle age.</p>",

"<p>The second is <strong>inherent</strong>: the resistance is a property of the polymer itself. Polyester and triexta do not absorb water-based spills the way nylon does, and <strong>solution-dyed</strong> "
"versions of any fiber take it further &mdash; more on that next. Inherent resistance cannot wear off, because it is not a coating; it is what the fiber is made of. When a salesperson says "
"&ldquo;stain-resistant,&rdquo; the question that sorts the aisle is: <em>is that a treatment or the polymer?</em> The price difference between the two answers is real, and so is the difference in year "
"six.</p>",

'<h2>Solution-Dyed, Explained Properly</h2>',

"<p>Conventional carpet is dyed the way fabric usually is: the fiber is made first, white, and the color is applied afterward, soaking into the outer layer. Solution-dyed fiber is colored before it "
"exists &mdash; pigment is mixed into the molten polymer, and the fiber is extruded already colored, the way a batter baked with cocoa is chocolate all the way through rather than frosted. Cut a "
"solution-dyed strand anywhere and the cross-section is the same color.</p>",

"<p>That construction buys you two things. First, <strong>nothing can un-dye it</strong> &mdash; sunlight through a south window, repeated enzyme cleanings, even a careful dab of diluted bleach on the "
"worst spill leave the color intact, because there is no surface layer of dye to strip. Second, <strong>there is nowhere for a stain to bond</strong> that the pigment does not already occupy; spills sit "
"on the fiber waiting to be blotted instead of moving in. It is the same reason outdoor carpet and marine upholstery are solution-dyed. For households mid-toddler or mid-dog, it is the difference "
"between a carpet that survives cleaning and a carpet that fades in the exact spots you clean &mdash; the pale ghost patches every parent recognizes. Our "
"<a href=\"/blog/best-carpet-for-pets\">pet carpet guide</a> leans on the same technology for the same reason, and <a href=\"/blog/the-10-best-carpet-brands-reviews-2023-guide\">the brand guide</a> "
"covers who builds the serious solution-dyed lines.</p>",

'<h2>What the Warranties Actually Cover</h2>',

"<p>A stain warranty is not a force field; it is a list of substances with conditions attached. Read one &mdash; actually read it &mdash; and the shape is always the same. Covered: <em>most "
"food and beverage stains</em>, the coffee-juice-wine family, usually soda and chocolate. Pet lines add <em>pet urine</em>, sometimes feces and vomit. That is genuinely useful coverage, and on a good "
"line the manufacturer does stand behind it: a stain from a listed substance that will not come out with the prescribed cleaning process can get a section of carpet repaired or replaced.</p>",

"<p>Now the boundaries, because this is where homeowners get surprised. Nearly every stain warranty excludes <strong>oil-based and greasy substances</strong> &mdash; cooking oil, butter, salad dressing, "
"lipstick, shoe polish. It excludes <strong>substances that dye</strong>: hair color, mustard, turmeric, children's paints, plant food. It excludes <strong>bleach and caustics</strong> as damage rather "
"than staining (though solution-dyed fiber shrugs off what would ghost a conventional carpet). And the big one: it excludes <strong>anything classed as wear</strong>. The matted, darkened traffic lane "
"that looks like a stain in year five is crushed, abraded fiber &mdash; a wear problem, covered by a different clause with its own exclusions, if at all. That distinction decides more claims than any "
"other sentence in the document, and it is why fiber choice protects you where the warranty will not &mdash; a theme we develop in <a href=\"/blog/how-long-does-carpet-last\">how long carpet lasts</a>.</p>",

table('The Spill List, Honestly', ['Substance', 'Typical warranty verdict', 'The reality on good fiber'], [
 ('<strong>Coffee, wine, juice</strong>', 'Covered', 'The headline coverage &mdash; blot fast, clean as prescribed, and solution-dyed fiber releases these well'),
 ('<strong>Pet urine</strong>', 'Covered on pet lines', 'The stain cleans; the odor is a pad-and-subfloor problem no carpet warranty touches &mdash; barrier pad or bust'),
 ('<strong>Cooking oil, grease, makeup</strong>', 'Excluded', 'Oil bonds to synthetic fiber; treat fast with a solvent-type spotter and temper expectations'),
 ('<strong>Mustard, turmeric, hair dye</strong>', 'Excluded', 'These are dyes &mdash; they do to carpet what the mill does, minus the quality control'),
 ('<strong>Bleach</strong>', 'Excluded as damage', 'Ghosts conventional carpet permanently; solution-dyed fiber is the one construction that largely shrugs it off'),
 ('<strong>Mud, everyday dirt</strong>', 'Not a stain &mdash; maintenance', 'Vacuuming and scheduled cleaning; dirt held at the pile base is a wear accelerant, not a claim'),
 ('<strong>Traffic-lane darkening</strong>', 'Excluded as wear', 'Crushed, abraded fiber reads as &ldquo;stained&rdquo; but no stain clause covers it &mdash; density and pile choice prevent it'),
]),

'<h2>The Fine Print That Kills Claims</h2>',

"<p>Assume every claim will be audited, because the successful ones effectively are. The recurring requirements: <strong>prompt treatment</strong> (some warranties specify how quickly a spill must be "
"addressed), <strong>approved methods and products</strong> (the wrong spotter can void coverage on the spot it touched), <strong>professional hot-water extraction on a schedule</strong> &mdash; "
"typically every 12 to 18 months &mdash; and <strong>receipts for all of it</strong>, plus your original proof of purchase. A folder in a kitchen drawer with the invoice and each cleaning receipt is "
"unglamorous and it is exactly what a paid claim looks like. Also worth knowing: warranties follow the original purchaser and the original installation &mdash; coverage on carpet you inherited with the "
"house is usually gone before you unpack.</p>",

two_col(
 'What a stain warranty is genuinely good for',
 ['Everyday food-and-beverage life with kids &mdash; the accidents that actually happen weekly',
  'Pet urine stains, on the lines that name them &mdash; a real, tested benefit',
  'Backing you up when a listed stain defeats the prescribed cleaning',
  'Signaling fiber quality &mdash; long stain terms ride on better polymer',
  'Keeping you honest about professional cleaning, which the carpet needed anyway'],
 'What it will never protect you from',
 ['Oil, grease, dyes and bleach &mdash; the exclusions list is longer than the coverage list',
  'Traffic-lane matting and darkening &mdash; wear wearing a stain costume',
  'Odor in the pad and subfloor &mdash; that battle is won by the pad, before the first accident',
  'Skipped cleanings and missing receipts &mdash; paperwork loses more claims than chemistry',
  'The wrong carpet in the wrong room &mdash; no clause fixes plush in a mudroom hallway'],
),

'<h2>Our Honest Spec, and Where Shoreline Comes In</h2>',

"<p>Here is how we translate all of this at the kitchen table. In bedrooms and low-traffic rooms, inherent stain resistance is nice but not worth chasing &mdash; spills are rare there, and a "
"comfortable <a href=\"/blog/low-pile-vs-high-pile-carpet\">plusher pile</a> serves the room better. In family rooms, halls and anywhere under a dining chair or a dog, we spec <strong>solution-dyed "
"fiber, a denser low-to-medium pile, and a moisture-barrier pad</strong> &mdash; the pad because urine and big spills go through carpet in seconds, and permanent odor lives in what is underneath. The "
"warranty is the third line of defense, not the first; we treat it as a quality signal and keep the folder anyway.</p>",

"<p>Shoreline's housing stock argues the same way. Most of the city is 1950s and 60s ranches and split-levels &mdash; carpeted stairs between half-flights, family rooms a few steps down, hardworking "
"halls &mdash; and those concentrated lanes are where topical treatments quit early and solution-dyed fiber earns its premium. The mobile showroom brings the serious stain-resistant lines and all three "
"pad grades to your house, with a written price the same visit; the arithmetic behind that number is in <a href=\"/blog/how-to-measure-for-carpet\">how carpet is measured</a> and "
"<a href=\"/blog/cost-to-carpet-a-room\">what one room costs</a>, and the local details are on our "
"<a href=\"/city-of-shoreline/carpet-installation-in-shoreline-wa\">Shoreline carpet installation page</a>.</p>",

faq('Stain-Resistant Carpet: What Homeowners Ask Us', [
 ('Is stain-resistant carpet actually worth it?',
  'In the rooms where spills happen — family rooms, halls, dining areas, anywhere with kids or pets — yes, and specifically the solution-dyed kind, where resistance is built into the fiber and cannot wear off. In a guest bedroom, it is a nice-to-have. We would rather put the premium where the accidents are and spend the savings on a better pad.'),
 ('What is the difference between stain-resistant treatment and solution-dyed carpet?',
  'A treatment is applied to the surface of ordinary dyed fiber at the mill; it works when new, then thins with traffic and washes out a little with every deep cleaning. Solution-dyed fiber has pigment mixed into the molten polymer before the fiber is made — color and stain resistance run all the way through and last the life of the carpet.'),
 ('What do carpet stain warranties actually cover?',
  'A named list of substances — typically food and beverage stains, plus pet urine on pet-specific lines — under conditions: prompt treatment, approved cleaning products, professional hot-water extraction on schedule, and receipts for everything. If a listed stain defeats the prescribed cleaning, the manufacturer repairs or replaces the affected area.'),
 ('What voids a carpet stain warranty?',
  'The usual claim-killers are paperwork and process: no proof of purchase, no professional cleaning receipts on the required 12-to-18-month schedule, or the wrong cleaning product on the spot. The exclusions do the rest — oil-based substances, dyes like mustard and hair color, bleach damage, and anything the inspector classes as wear rather than stain.'),
 ('Does stain-resistant carpet work against pet urine?',
  'The stain side, yes — on solution-dyed and pet-line fibers, urine stains clean out well. But the smell is a different war: liquid passes through carpet in seconds and soaks the pad and subfloor, where no fiber technology and no warranty reaches. That is what a moisture-barrier pad is for, and why we treat it as non-negotiable in pet households.'),
 ('Can I use bleach or OxiClean on stain-resistant carpet?',
  'Check the warranty before anything touches the floor — unapproved chemistry can void coverage on that spot. Solution-dyed fiber is the one construction that tolerates diluted bleach without ghosting, which is why it is the material of last resort for the truly cursed spill. Enzyme cleaners for anything organic, and blot, never scrub.'),
 ('Why does my stain-resistant carpet look stained in the hallway anyway?',
  'Because that is probably not a stain. Darkened, matted traffic lanes are crushed and abraded fiber — wear — plus ground-in grit that vacuuming no longer reaches. No stain clause covers it, and cleaning improves it only briefly. Prevention is fiber density and pile choice up front, which matters more than any label on the sample.'),
 ('What does stain-resistant carpet cost installed?',
  'Our installed carpet starts at $1.49 per square foot, and the solution-dyed, stain-focused lines sit above that entry point — modestly, against what they save. We bring twenty-plus full-size samples and all three pad grades to your Shoreline home, measure every room and stair, and leave a written price the same visit.'),
]),

cta('Read the Warranty Together, Before You Buy',
    'We bring the serious stain-resistant lines to your house, show you which claims are fiber and which are marketing, and put the whole job &mdash; pad grade named &mdash; in writing the same visit. Free in-home estimates across Shoreline and all of King &amp; Snohomish County.'),

related([
 ('/blog/best-carpet-for-pets', 'The best carpet for pet households'),
 ('/blog/how-long-does-carpet-last', 'How long carpet really lasts'),
 ('/blog/low-pile-vs-high-pile-carpet', 'Low pile vs high pile, room by room'),
 ('/blog/the-10-best-carpet-brands-reviews-2023-guide', 'The best carpet brands'),
 ('/city-of-shoreline/carpet-installation-in-shoreline-wa', 'Carpet installation in Shoreline'),
 ('/contact', 'Book a free estimate'),
]),
]

assemble(S, parts)
