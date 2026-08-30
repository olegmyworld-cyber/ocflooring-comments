from builder import *

S = 'choosing-grout-color'

parts = [
date_badge('December 22, 2026'),

quick_answer(
 "<strong>Grout color is the cheapest decision in a tile project and the one people regret most, because it changes how the whole floor reads and it is nearly permanent.</strong> "
 "The working rules: on a floor, choose a grout one to two shades darker than the tile &mdash; white floor grout goes grey in months and never fully comes back. Match the grout to blend "
 "and let the tile read as one surface; contrast only when the tilework underneath is perfect, because a contrasting line advertises every wobble. And decide from a dried sample on your "
 "actual tile in your actual light, not from the chart in the store. Regrouting later is surgery; getting the color right costs nothing extra.",
 'Lynnwood remodels'),

facts([
 ('1&ndash;2 shades', 'darker than the tile: the floor-grout rule that survives real life. Close enough to blend, dark enough to hide the traffic that no mop fully removes.'),
 ('$14&ndash;$26', 'per square foot installed, labor from $11/sq ft &mdash; and the grout color inside that number is free. The regret is never the price; it is living with the wrong line for fifteen years.'),
 ('2 years', 'our warranty on tile work. Grout that cracks or discolors from a bad install is a workmanship problem; grout that grays from traffic on a white floor was a specification problem, which is why we argue about color up front.'),
]),

'<h2>Why a Sixty-Dollar Bag Decides the Whole Room</h2>',

"<p>Grout is a small fraction of the material budget and a shockingly large fraction of what your eye actually sees. The lines run through the entire field, and their color decides whether "
"the floor reads as one calm surface, a grid of rectangles, or &mdash; the regret case &mdash; a grid of dirty rectangles. Take the same gray 12&times;24 porcelain and grout it three ways: "
"matched gray, and it becomes a seamless stone-like plane; bright white, and every tile is outlined like a spreadsheet; charcoal, and the layout itself becomes the design. Same tile, three "
"different rooms, one bag of powder apart.</p>",

"<p>The trap is that this decision gets made in the last five minutes of a long selection process, off a fan deck of dry chips, in a showroom lit like an operating theater. Then it is "
"mixed with water, cured into cement, and bonded into every joint in the room. Changing your mind afterward is not a repaint; it is scraping joints or staining them, line by line. So it "
"deserves ten deliberate minutes, and this is the argument we make in those ten minutes.</p>",

'<h2>Blend, Contrast, or Split the Difference</h2>',

table('Three Grout Strategies, Honestly', ['Strategy', 'What it does', 'The risk you accept'], [
 ('<strong>Blend (grout matches tile)</strong>', 'Joints disappear; the field reads as one surface; the tile itself is the star', 'Very forgiving of minor joint variation; shows dirt only as much as the tile color does'),
 ('<strong>Contrast (light tile, dark grout or reverse)</strong>', 'The grid becomes the design; patterns like herringbone pop; classic subway looks', 'Advertises every crooked cut and uneven joint; dark-on-light shows haze, light-on-dark shows grime'),
 ('<strong>One to two shades off</strong>', 'Gentle definition without a drawn grid; the default we recommend on floors', 'Almost none &mdash; which is why it is the default'),
]),

"<p>Contrast deserves its own honest warning: a contrasting grout line is a ruler laid against your installer's work. On a wall of hand-cut subway around a 1960s Lynnwood window that is "
"not square, a bright white joint against dark tile will document every compromise. Blended grout forgives; contrast testifies. If you want contrast &mdash; and done well it is beautiful "
"&mdash; the tile setting underneath has to be worth photographing, the joints dead-even, the layout resolved. It is the same discipline story as "
"<a href=\"/blog/large-format-tile-installation\">large-format tile</a>: the bolder the look, the less tolerance the details leave you.</p>",

'<h2>Why White Grout on a Floor Goes Grey</h2>',

"<p>This is the regret we get called about most, so here is the mechanism. Cement grout is porous &mdash; microscopically, it is a hard sponge. On a floor, every footstep presses fine "
"dirt into that sponge, and every damp mop dissolves a little soil and redeposits it into the joints as the water dries. The tile wipes clean; the grout drinks. Six months of normal life "
"and the white lines are beige; two winters and they are grey with dark traffic lanes, while the joints under the couch stay snow white as a reproach. No cleaner fully reverses it, "
"because the discoloration is inside the pores, not on top.</p>",

"<p>Sealing helps and is nowhere near the force fence people believe it is. A penetrating sealer slows absorption &mdash; it buys you time to wipe up the spill, and it needs renewing "
"every year or two in working areas because traffic wears it off. What actually holds color on a floor is one of three things: a grout dark enough to hide the loading, an epoxy grout "
"whose non-porous chemistry simply does not absorb &mdash; the trade-offs are in <a href=\"/blog/epoxy-vs-cement-grout\">epoxy vs cement grout</a> &mdash; or a maintenance discipline "
"almost nobody sustains. White grout belongs on walls, where gravity is on its side. On a floor in a Pacific Northwest winter, with the grit and water an "
"<a href=\"/blog/entryway-tile-pacific-northwest\">entryway</a> imports daily, it is a countdown.</p>",

'<h2>Choosing in Real Light, From a Dried Sample</h2>',

"<p>Three practical habits prevent most regrets. <strong>First, grout dries lighter than it mixes.</strong> The wet color in the bucket is not the finished color; judge only cured "
"samples. <strong>Second, judge on your tile, in your room.</strong> We make sample boards &mdash; the actual tile with two or three candidate grouts &mdash; and leave them on your floor "
"for a day. Northwest daylight is blue-grey and scarce from November to February; a warm greige that looked subtle under showroom halogens can read pink at noon and mud at 4pm. The board "
"answers this in an afternoon. <strong>Third, look at the room's dirt, not the catalog's.</strong> A household of dogs and kids near the Interurban Trail has different grout physics than "
"an adults-only condo. The right color hides <em>your</em> particular week between cleanings &mdash; the same shade-matching logic that picks a floor tile that still looks right in ten "
"years, which we covered in <a href=\"/blog/bathroom-floor-tile-that-lasts\">bathroom floor tile that lasts</a>.</p>",

'<h2>The Sealing Reality, on One Page</h2>',

"<p>Cement grout in a dry area: seal it once after it cures, refresh it every couple of years, and it will behave. Cement grout on working floors and in showers: sealing is a real but "
"wasting asset &mdash; plan on renewing it, and know that it slows staining rather than preventing it. Epoxy grout: never needs sealing, shrugs off everything, costs more up front and "
"demands a skilled hand to install, and in a shower or a mudroom it is frequently worth every dollar. And everywhere, in every material: the joint where tile meets tub, wall, or "
"hardwood gets silicone, not grout, because grout in a moving joint cracks no matter what color it is. That rule comes up in every wet-room build we do, from "
"<a href=\"/blog/tile-shower-waterproofing\">showers</a> to <a href=\"/blog/laundry-room-tile\">laundry rooms</a>.</p>",

'<h2>Already Regretting It? Your Options, Honestly</h2>',

"<p>If the grout color is wrong &mdash; or was right and is now permanently grey &mdash; there are three exits, in ascending order of pain. <strong>Grout colorant</strong> is the honest "
"first move: a bonded stain-sealer applied joint by joint that can take grey back to white or white to greige, lasts years on floors when applied to clean, sound grout, and costs a "
"fraction of anything else. <strong>Regrouting</strong> &mdash; grinding out the top of every joint and repacking &mdash; is real surgery: dusty, slow, priced accordingly, and worth it "
"mainly when the grout is failing structurally, not just cosmetically. <strong>Retiling</strong> is the answer only when the tile itself is done. We will tell you which category you are "
"in from photos, before anyone drives anywhere.</p>",

'<h2>Grout Conversations in Lynnwood</h2>',

"<p>Lynnwood is in the middle of a remodeling wave &mdash; the 70s, 80s, and 90s housing stock around Alderwood, Scriber Lake, and Martha Lake is updating kitchens and bathrooms fast, "
"light rail has turned the math on staying put, and a lot of those projects are tile projects. The grout regrets we visit here have a pattern: bright white floor grout chosen to match a "
"bright white 2020s Pinterest board, in households with dogs, kids, and a wet season. The fix-it call usually comes eighteen months in. When we tile a Lynnwood kitchen or bath, the "
"sample board and the shade-darker argument happen at the estimate &mdash; it is ten minutes that saves a fifteen-year annoyance. Scope and scheduling are on our "
"<a href=\"/city-of-lynnwood/tile-installation-in-lynnwood-wa\">Lynnwood tile installation page</a>.</p>",

two_col(
 'How we help you choose',
 ['Cured sample boards on your actual tile, left in your light for a day',
  'The 1&ndash;2-shades-darker default on every floor',
  'Blend by default; contrast only over flawless setting work',
  'Epoxy quoted for showers, mudrooms, and white-grout dreams',
  'Silicone, never grout, at every change of plane',
  'A written spec naming the grout brand, color, and sealer'],
 'The regrets we get called about',
 ['White floor grout, grey by the second winter',
  'Color chosen wet, from a chip, under showroom lights',
  'High contrast over wavy joints &mdash; the grid tells on the tilework',
  'Believing one coat of sealer is a lifetime force field',
  'Grouted corners cracking exactly where the house moves',
  'Matching the trend instead of the household']),

faq('Grout Color: What Homeowners Ask Us', [
 ('What is the best grout color for a tile floor?',
  'One to two shades darker than the tile. It is close enough that the floor still reads as one surface, and dark enough to hide the fine soil that traffic grinds into cement grout and no mop fully removes. Matched-to-tile also works well on floors; bright white is the one choice that reliably disappoints.'),
 ('Why does white grout turn grey on floors?',
  'Cement grout is porous, and floors load it from two directions: footsteps press fine dirt into the pores, and damp mopping redeposits dissolved soil into the joints as the water dries. The discoloration ends up inside the grout, not on it, which is why cleaning brightens it briefly and never fully restores it. Walls keep white grout far better because gravity does not press dirt into them.'),
 ('Should grout match the tile or contrast with it?',
  'Match, unless you have a specific design reason and excellent tilework. Matching lets the tile read as a single surface and forgives small joint variations. Contrast turns the grid into the design - which is genuinely striking in a herringbone or classic subway - but it also documents every uneven joint and crooked cut, and it shows dirt and haze more. Contrast is a choice you earn with flawless setting.'),
 ('Does sealing grout keep it from staining?',
  'It slows staining; it does not prevent it. A penetrating sealer buys time to wipe up spills and needs renewing every year or two in trafficked and wet areas, because wear removes it. If the goal is grout that genuinely does not absorb - a white shower floor, a mudroom - the real answer is epoxy grout, which needs no sealing at all.'),
 ('Can grout color be changed after installation?',
  'Yes, within limits. A grout colorant - a bonded stain-sealer applied to clean, sound joints - can shift color dramatically, lighter or darker, and holds up for years on floors. It fixes color, not condition: cracked, crumbling, or failing grout needs regrouting, which is a slower, dustier, more expensive job. Colorant first, regrout when structure demands it.'),
 ('What grout color hides dirt best?',
  'Mid-tone greys, greiges, and taupes - the colors of the dirt itself. Anything very light shows soil; true black and charcoal show pale dust, lint, and hard-water haze almost as loudly. The most forgiving joint in a real household is a medium warm grey, one to two shades off the tile.'),
 ('What color grout should wood-look tile have?',
  'As close to the plank color as possible, and never lighter than the tile. Real wood floors have no light grid running through them, so visible grout lines are what break the illusion first. A tightly matched grout in the narrowest joint the tile allows is what keeps a wood-look floor looking like wood from standing height.'),
 ('Does grout color affect the price of a tile job?',
  'Color itself, essentially never - the pigment is free inside our $14 to $26 per square foot installed range. What moves the number is grout chemistry: epoxy costs meaningfully more in material and labor than cement grout, and it earns that premium in showers, mudrooms, and anywhere someone insists on white joints on a floor. We quote both when the choice is close.'),
]),

cta('Pick the Line You Can Live With',
    'Bring us the tile you love and we will bring the cured sample boards, the shade-darker argument, and an honest epoxy quote where it belongs &mdash; before anything is mixed with water. Free in-home estimates across King &amp; Snohomish County.'),

related([
 ('/blog/epoxy-vs-cement-grout', 'Epoxy vs cement grout'),
 ('/blog/bathroom-floor-tile-that-lasts', 'Bathroom floor tile that lasts'),
 ('/blog/entryway-tile-pacific-northwest', 'Entryway tile for PNW winters'),
 ('/blog/large-format-tile-installation', 'Large-format tile installation'),
 ('/blog/tile-shower-waterproofing', 'Shower waterproofing'),
 ('/city-of-lynnwood/tile-installation-in-lynnwood-wa', 'Tile installation in Lynnwood'),
 ('/contact', 'Book a free estimate'),
]),
]

assemble(S, parts)
