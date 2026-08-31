from builder import *

S = 'schluter-kerdi-vs-liquid-membrane'

parts = [
date_badge('February 23, 2027'),

quick_answer(
 "<strong>Schluter Kerdi and liquid-applied membranes are both legitimate ways to waterproof a shower &mdash; a properly installed version of either will outlast "
 "your ownership of the house.</strong> Kerdi is a bonded polyethylene sheet: its thickness is guaranteed by the factory, and its risk lives at the seams. Liquid "
 "membranes are rolled or troweled on in coats: seamless by nature, and their risk lives in thickness &mdash; a thin spot is invisible until it leaks. Which is why "
 "the honest answer to &ldquo;which is better?&rdquo; is a third thing entirely: the installer&rsquo;s fluency with the system in their hands, proven by a 24-hour "
 "flood test before any tile goes on.",
 'Showers &amp; wet rooms'),

facts([
 ('24 hours', 'the flood test every shower pan gets from us before tile &mdash; sheet or liquid, no exceptions. The pan sits full, photographed at fill and at 24 hours, and the photos go in your file. It is the referee in this whole debate.'),
 ('2 coats', 'the usual minimum for liquid membranes, applied to the manufacturer&rsquo;s specified thickness and verified with a wet-film gauge. The product is fine; unmeasured application is where liquid jobs fail.'),
 ('2 years', 'our warranty on tile work &mdash; double the trade&rsquo;s usual one year. We can offer it because the membrane behind the tile, whichever system, is installed to spec and tested before it disappears.'),
]),

'<h2>What Each System Actually Is</h2>',

"<p><strong>Schluter Kerdi</strong> is the orange sheet you have seen on every renovation show: a thin polyethylene membrane with a fleece backing, cut to fit and "
"bonded to the wall and pan with thinset mortar. Seams overlap by a specified width or get covered with banding; corners and the drain use preformed pieces. The "
"membrane arrives at its rated thickness &mdash; the factory did that part &mdash; so the installer&rsquo;s whole job is the fit: full mortar coverage, correct "
"overlaps, tight preformed corners, and a proper connection at the Kerdi drain.</p>",

"<p><strong>Liquid membranes</strong> &mdash; RedGard, Hydro Ban, Mapei&rsquo;s Aquadefense and their peers &mdash; are elastomeric coatings applied like thick "
"paint. Two or more coats go on with roller or trowel, usually in perpendicular directions, with reinforcing fabric at corners, seams and the drain. Cured, they form "
"a continuous rubbery skin bonded to the substrate. There are no seams to lap because there are no seams at all &mdash; but the rated waterproofing only exists at "
"the rated thickness, which the installer controls entirely, coat by coat.</p>",

"<p>Both are modern, surface-applied systems &mdash; the water is stopped at the tile assembly&rsquo;s face, not caught by a buried pan liner three layers deep. "
"That philosophy, and why it replaced the old mortar-bed-and-liner approach, is covered in our broader "
"<a href=\"/blog/tile-shower-waterproofing\">shower waterproofing guide</a>. Here we are settling the narrower question: sheet or liquid?</p>",

table('Kerdi vs Liquid Membrane, Honestly Scored', ['Dimension', 'Schluter Kerdi', 'Liquid membrane'], [
 ('<strong>Thickness control</strong>', 'Factory-guaranteed &mdash; the sheet is the spec', 'Installer-controlled &mdash; needs a wet-film gauge and discipline, coat by coat'),
 ('<strong>Seams &amp; corners</strong>', 'The risk lives here: overlaps and banding must be right', 'Seamless by nature; fabric-reinforced corners are routine'),
 ('<strong>Odd geometry</strong>', 'Benches, curves and niches mean lots of cutting and piecing', 'Paints around anything &mdash; complex shapes are its home turf'),
 ('<strong>Speed to tile</strong>', 'Tile the same day &mdash; no cure wait', 'Cure time between coats and before tile; a day or two of chemistry'),
 ('<strong>System integration</strong>', 'Sheet, band, corners, niche and drain from one catalog, engineered together', 'Pairs with any drain and backer, which is flexibility and responsibility at once'),
 ('<strong>Failure mode</strong>', 'A bad seam or starved mortar bond &mdash; findable at the flood test', 'A thin spot &mdash; invisible to the eye, also findable at the flood test'),
 ('<strong>Cost</strong>', 'Higher material cost, very predictable labor', 'Cheaper material; labor honesty is the real price'),
]),

'<h2>Where Kerdi Wins</h2>',

"<p>Kerdi&rsquo;s great virtue is that the factory already did the hardest part. Thickness &mdash; the thing that actually stops water &mdash; is not a variable on "
"site. That makes the system beautifully inspectable: you can look at a Kerdi shower before tile and <em>see</em> the overlaps, the banded seams, the preformed "
"corners, and photograph all of it. In a standard alcove or tub-to-shower conversion, where walls are flat and corners are square, a fluent Kerdi installer produces "
"a near-identical assembly every single time, and same-day tiling keeps the schedule tight &mdash; a real advantage inside the "
"<a href=\"/blog/how-long-to-tile-a-bathroom\">seven-to-nine-day calendar</a> of a full bathroom.</p>",

"<p>The integrated catalog matters more than it sounds, too. The drain is designed for the sheet, the niche is a preformed box that bands into the wall, the curb "
"pieces fold where curbs fold. When one manufacturer engineers the whole path water might take, the seams between <em>products</em> disappear along with the seams "
"in the membrane &mdash; the same logic that makes us reach for the companion uncoupling system in "
"<a href=\"/blog/ditra-vs-cement-board\">Ditra versus cement board</a> on floors.</p>",

'<h2>Where Liquid Wins</h2>',

"<p>Geometry, first. A curved bench, a sloped <a href=\"/blog/curbless-shower-build-mercer-island\">curbless entry</a>, a reading niche with an arched top, a "
"hundred-year-old wall that is nowhere near flat &mdash; liquid paints over all of it without a dart or a pieced seam. The more your shower deviates from a box, the "
"stronger the liquid argument gets. Complex pans with multiple penetrations &mdash; body sprays, a steam head, a hand shower bar &mdash; are simpler to seal with "
"fabric and liquid than with a jigsaw of sheet pieces.</p>",

"<p>Liquid is also more forgiving of mixed substrates and repairs: it bonds over properly prepped cement board, existing sound mortar beds, and transitions between "
"materials without caring about the change. And the material cost is meaningfully lower &mdash; on a tight renovation budget where the labor is trusted, that "
"difference is real money that can go toward better tile.</p>",

two_col(
 'Choose Kerdi-style sheet when',
 ['The shower is a standard alcove with flat, square walls',
  'Schedule is tight &mdash; tile can go on the same day',
  'You want a photographable, visually verifiable assembly',
  'The drain and niche can come from the same engineered system',
  'The installer lives in that system and builds it weekly',
  'You are the trust-but-verify type &mdash; sheet shows its work'],
 'Choose liquid membrane when',
 ['Benches, curves, curbless slopes or odd niches are involved',
  'Many penetrations: valves, body sprays, steam fittings',
  'Substrates are mixed or walls are far from flat',
  'Material budget matters and the labor is proven',
  'Repairs or tie-ins to existing waterproofing are needed',
  'The installer gauges thickness and logs coats &mdash; ask to see']),

'<h2>How Each One Fails &mdash; and the Test That Catches Both</h2>',

"<p>Neither system fails as a product; both fail as installations. Kerdi fails at a starved seam &mdash; too little mortar under an overlap, a corner piece "
"stretched instead of seated, banding skipped because the overlap &ldquo;looked wide enough.&rdquo; Liquid fails at thickness &mdash; a second coat rolled thin over "
"a first coat that had already skinned, a corner where the fabric never got buried, a spec that wanted 30 wet mils and got half that "
"because nobody owned a gauge. The failure is invisible in both cases. Tile goes on, everything is beautiful, and the assembly&rsquo;s truth emerges through the "
"ceiling below in year three &mdash; at which point the fix is a rebuild, the argument we made in "
"<a href=\"/blog/regrouting-vs-retiling-a-shower\">regrouting versus retiling a shower</a>.</p>",

"<p>This is why the flood test is not a nicety. Plug the drain, fill the pan, mark the line, wait 24 hours. A starved Kerdi seam weeps; a thin liquid spot weeps; a "
"tight assembly of either kind holds to the pencil mark. It is the one moment the membrane can be tested directly in its entire service life, it costs a day, and it "
"ends the sheet-versus-liquid argument for that particular shower with data. We photograph ours and keep them on file &mdash; ask any bidder, using either system, "
"when their flood test day is.</p>",

'<h2>What We Actually Use</h2>',

"<p>Both &mdash; chosen per job, not per ideology. A standard alcove on a tight calendar usually gets the sheet system; a curbless pan with a bench and three "
"penetrations usually gets liquid with fabric reinforcement; some jobs get both, sheet on the walls and liquid where geometry demands it, tied together per the "
"manufacturers&rsquo; instructions. Every one of them gets a pre-slope under the pan, and every one sits through the photographed 24-hour flood test before tile. "
"That combination &mdash; system fluency plus verification &mdash; is what the <a href=\"/blog/cost-to-tile-a-shower\">price of a properly built shower</a> is "
"actually buying, and it is why we can put a 2-year warranty behind tile work when the trade standard is one.</p>",

"<p>If you are planning a shower anywhere in King or Snohomish County, we will tell you which system your geometry and schedule argue for &mdash; and show you "
"flood-test photos from jobs like yours. Scope and details are on the <a href=\"/seattle/tile-installation-in-seattle-wa\">Seattle tile installation page</a>.</p>",

faq('Kerdi vs Liquid Membranes: What Homeowners Ask Us', [
 ('Is Schluter Kerdi better than liquid membrane?',
  'Neither is better in the abstract — both are proven systems that outlast the house when installed to spec. Kerdi carries factory-guaranteed thickness and its risk at the seams; liquid is seamless and carries its risk in application thickness. The installer’s fluency with their chosen system matters far more than the choice itself.'),
 ('What is Schluter Kerdi, exactly?',
  'A thin polyethylene sheet membrane with a fleece backing, bonded to shower walls and pans with thinset mortar. Seams are overlapped or banded, corners and drains use preformed pieces, and tile can be set the same day. It is part of an engineered family — drain, niche, curb, and the Ditra floor membrane — designed to work as one system.'),
 ('Which is cheaper, Kerdi or liquid membrane?',
  'Liquid usually costs less in material, and Kerdi tends to be more predictable in labor. On a standard shower the installed difference is modest either way — and it is dwarfed by the cost difference between any correct installation and a failed one. Choose the system your installer is fluent in, not the one that saves tens of dollars.'),
 ('Can you tile the same day over each membrane?',
  'Over Kerdi, yes — the mortar bonding the sheet does not need to cure before tiling starts, which is a genuine schedule advantage. Liquid membranes need each coat to cure and a final cure before tile, typically adding a day or two. On a full bathroom calendar that difference is real but rarely decisive.'),
 ('Do liquid membranes like RedGard actually work in showers?',
  'Yes — when applied at the manufacturer’s specified thickness with reinforcing fabric at corners and penetrations, liquid membranes are fully legitimate shower waterproofing. The products earn their bad stories almost exclusively through thin application. An installer who uses a wet-film gauge and logs coats removes exactly that risk.'),
 ('Do I still need a flood test with a Kerdi shower?',
  'Absolutely. Kerdi’s factory thickness does not protect a starved seam, a stretched corner piece, or a bad drain connection — installation errors a 24-hour flood test catches while they are an hour’s fix instead of a rebuild. Sheet or liquid, the pan sits full for 24 hours and gets photographed before we set tile over it.'),
 ('Can Kerdi and liquid membrane be combined in one shower?',
  'Yes, and it is common in complicated builds — sheet on the flat wall planes, liquid with fabric where a bench, curve, or cluster of penetrations makes sheet-piecing awkward. The tie-ins between systems follow the manufacturers’ instructions and get the same flood test as everything else.'),
 ('What goes behind the membrane — do I still need cement board?',
  'Kerdi is approved over standard drywall in dry framing as well as cement board, because the sheet itself is the waterproofing plane. Liquid membranes go over cement board or equivalent tile backer, never bare drywall in wet areas. Either way the membrane, not the board, is what keeps the wall dry — board choice is about a sound substrate.'),
]),

cta('Planning a Shower? Ask Us Which System Yours Wants',
    'We install both &mdash; sheet and liquid, chosen for your geometry and schedule, always over a pre-slope, always flood-tested for 24 hours with photos in your file. Free in-home estimates across King &amp; Snohomish County.'),

related([
 ('/blog/tile-shower-waterproofing', 'How a tile shower is waterproofed'),
 ('/blog/ditra-vs-cement-board', 'Ditra vs cement board'),
 ('/blog/cost-to-tile-a-shower', 'What a tiled shower costs'),
 ('/blog/regrouting-vs-retiling-a-shower', 'Regrouting vs retiling a shower'),
 ('/seattle/tile-installation-in-seattle-wa', 'Tile installation in Seattle'),
 ('/contact', 'Book a free estimate'),
]),
]

assemble(S, parts)
