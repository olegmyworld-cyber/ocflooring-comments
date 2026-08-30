from builder import *

S = 'cost-to-tile-a-shower'

parts = [
date_badge('November 17, 2026'),

quick_answer(
 "<strong>Tiling a shower runs $14&ndash;$26 per square foot installed with us, labor from $11/sq ft &mdash; but a shower is priced by its assembly, not its area.</strong> "
 "A standard tub surround is roughly 60 square feet of wall; a walk-in shower adds a pan, a curb or curbless slope, and more wall &mdash; and on every one of them, the biggest "
 "share of the money goes to what you will never see: demolition, substrate corrections, and the waterproofing system behind the tile. This is the quote explained line by line, "
 "including the project half of Sammamish seems to be doing right now: the garden-tub-to-walk-in-shower conversion.",
 'Sammamish homes &amp; remodels'),

facts([
 ('$11/sq ft', 'where our tile labor starts. Installed &mdash; labor, setting materials and prep &mdash; showers run $14 to $26 per square foot depending on tile, layout, and what the walls hide.'),
 ('24 hours', 'how long every pan we build sits full of water before tile goes on. The flood test is photographed and kept on record &mdash; a leak found after tile is a demolition.'),
 ('2 years', 'our warranty on tile work, double the trade&rsquo;s usual one year. We can offer it because of what goes in behind the tile, not what shows in front of it.'),
]),

'<h2>The Quote, Line by Line</h2>',

"<p>When three shower bids land on your kitchen table and disagree by thousands, the disagreement is almost never about tile. It is about which of these lines each bidder "
"actually included. Here is every line an honest shower quote carries, and what pushes each one up or down.</p>",

table('What a Shower Tile Quote Is Made Of', ['Line item', 'What it covers', 'What moves the number'], [
 ('<strong>Demolition &amp; disposal</strong>', 'Old surround or tile out, down to studs in a rebuild', 'One layer of 90s tile is quick; a mortar bed or hidden rot is not'),
 ('<strong>Substrate &amp; framing</strong>', 'Backer board, flattening, fixing what demolition reveals', 'The great unknown &mdash; this is why good quotes carry a contingency line'),
 ('<strong>Waterproofing assembly</strong>', 'Pre-slope, bonded membrane, sealed corners, curb, drain', 'The biggest labor share on the whole quote &mdash; and the least visible'),
 ('<strong>Flood test</strong>', 'The pan filled for 24 hours and photographed, before tile', 'A day of schedule; the cheapest insurance in the project'),
 ('<strong>Tile &amp; setting materials</strong>', 'Your tile, thinset, leveling systems, trim profiles', 'Tile choice is yours; large format and stone add setting labor'),
 ('<strong>Setting &amp; grout labor</strong>', 'Layout, cutting, setting, grout, silicone at every plane change', 'Niches, benches, patterns and small mosaics all add hours'),
 ('<strong>Upgrades</strong>', 'Epoxy grout, heated floor outside the curb, custom niches', 'Optional &mdash; priced as visible line items, not buried'),
 ('<strong>Other trades</strong>', 'Plumbing changes, glass door, electrical', 'Real costs that belong in your budget even when they are not on our line'),
]),

"<p>Two of those lines deserve a sentence more. The <strong>waterproofing assembly</strong> is most of what separates a shower from a floor of the same size &mdash; the full "
"stack is explained in <a href=\"/blog/tile-shower-waterproofing\">our shower waterproofing guide</a>, and it is the line where cheap bids quietly save their money. And "
"<strong>the contingency</strong>: Sammamish showers from the 1990s builds hide their surprises behind intact-looking walls, so a bid with no allowance for discovery is not "
"cheaper &mdash; it is just planning to renegotiate mid-job, when you have no leverage.</p>",

'<h2>Three Sammamish Showers, Priced in Shape</h2>',

"<p>Real rooms explain ranges better than percentages. <strong>A tub surround refresh</strong> &mdash; keep the tub, retile the three walls above it &mdash; is about 60 square "
"feet of wall and the friendliest version of the project: less demolition, no pan to build, waterproofing on the walls only. <strong>A full walk-in rebuild</strong> in the same "
"footprint adds the pan assembly, the curb, more wall area and usually a niche or bench, which is why it costs meaningfully more than the surround even before the glass. "
"<strong>A large curbless walk-in</strong> in a primary suite is the top of the market: the floor gets opened so the pan can recess and slope without a curb, which is structural "
"work before it is tile work &mdash; the build we describe in <a href=\"/blog/curbless-shower-build-mercer-island\">our curbless shower guide</a>.</p>",

"<p>The per-square-foot math behaves the way small rooms always do: fixed costs &mdash; mobilization, waterproofing sequence, the flood-test day &mdash; divide across few square "
"feet, so a shower is expensive per foot and moderate in total. The full arithmetic of that effect is in our "
"<a href=\"/blog/tile-installation-cost-per-square-foot\">per-square-foot price breakdown</a>.</p>",

'<h2>The Tub-to-Shower Conversion, Honestly</h2>',

"<p>The signature project on the plateau: a mid-90s primary bath in Klahanie or Trossachs with a garden tub nobody has filled since the second Clinton administration, converted "
"into a walk-in shower people use twice a day. It is usually worth doing and it is never a surround-sized job, for three reasons. <strong>The drain moves.</strong> A tub drain "
"sits at one end; a shower drain wants the center or the low line of a sloped pan, and that is plumbing work under the floor. <strong>The pan is built from nothing</strong> "
"&mdash; pre-slope, membrane, flood test &mdash; where the tub used to handle all of that by being a tub. <strong>The walls go taller and often wider</strong>, because a shower "
"wants tile to the ceiling and the old tub deck footprint rarely matches the new layout.</p>",

"<p>Two honest notes we give every conversion client. Keep at least one tub somewhere in the house &mdash; buyers with small children will look for it. And since the floor is "
"open and the room is a construction zone anyway, this is the cheapest moment you will ever get for the two add-ons people ask about later: a heated bathroom floor outside the "
"curb &mdash; the math is in <a href=\"/blog/heated-bathroom-floor-cost\">our heated floor cost guide</a> &mdash; and a properly built niche instead of a wire basket hanging off "
"the shower head, which we cover in <a href=\"/blog/shower-niche-placement-size-waterproofing\">the shower niche guide</a>.</p>",

two_col(
 'On every complete shower quote',
 ['Demolition, disposal, and a named allowance for surprises',
  'Substrate work listed as its own line, not folded into &ldquo;tile&rdquo;',
  'A named waterproofing system &mdash; sheet or liquid, by brand',
  'Pre-slope and pan build, with a photographed 24-hour flood test',
  'Niche, bench and curb waterproofing called out individually',
  'Grout spec by name &mdash; and silicone at every change of plane'],
 'Missing from the suspiciously cheap one',
 ['Any mention of what happens if the walls hide rot',
  'The membrane &mdash; cement board alone is doing the waterproofing',
  'The flood test, because it costs a day of schedule',
  'Plumbing scope on a conversion &mdash; &ldquo;handled&rdquo; is not a scope',
  'Tile trim profiles and edge finishing &mdash; the details you see daily',
  'A warranty that survives longer than the final invoice']),

'<h2>Where the Spread Between Bids Comes From</h2>',

"<p>Take the same Sammamish shower to three contractors and the numbers can spread by half. Now you can read the spread: one bid skipped the membrane system, one assumed nothing "
"is wrong behind the walls, and one priced the job as it will actually be built. Tile choice adds honest variance on top &mdash; large-format porcelain and natural stone take "
"more setting labor, patterns add cuts &mdash; and upgrades belong in daylight: epoxy grout is a legitimate line in a shower, for reasons we lay out in "
"<a href=\"/blog/epoxy-vs-cement-grout\">epoxy vs cement grout</a>, not a mystery adder. If a bid cannot tell you which of these it includes, the number on it is not really a "
"price. It is an opening position.</p>",

'<h2>Getting a Number You Can Hold</h2>',

"<p>Three questions sort shower bids faster than anything else. <strong>What membrane, by name, and where does it go?</strong> <strong>What is the plan and the rate if you open "
"the wall and find damage?</strong> <strong>Will you flood-test the pan and show me?</strong> A contractor with good answers to those three will also have the rest right. The "
"broader bathroom version of this exercise &mdash; floors, surrounds, whole rooms &mdash; is in our "
"<a href=\"/blog/bathroom-tile-installation-cost-seattle\">bathroom tile cost guide</a>, and our full local scope is on the "
"<a href=\"/city-of-sammamish/tile-installation-in-sammamish-wa\">Sammamish tile installation page</a>. We put every line above in writing, contingency included, so the number "
"you sign is the number you pay unless the wall genuinely surprises us both &mdash; and then you get photographs and a unit price, not a shrug.</p>",

faq('Shower Tile Cost in Sammamish: What Homeowners Ask Us', [
 ('How much does it cost to tile a shower?',
  'Our tile work runs $14 to $26 per square foot installed, with labor from $11 per square foot. A standard tub surround is roughly 60 square feet of wall; a walk-in shower adds pan, curb and more wall area, so it lands higher in total even at the same rate. The spread inside the range is decided by demolition findings, substrate work, waterproofing scope, and tile choice.'),
 ('Why does a shower cost more per square foot than a bathroom floor?',
  'Because the square footage is doing more jobs. A shower carries a sloped pan built from scratch, a bonded membrane over every surface, sealed corners, a curb or curbless slope, a flood test, and far more cutting and detail per foot than an open floor. Most of that work is invisible when the job is done, which is exactly why cheap bids skip parts of it.'),
 ('What does a tub-to-shower conversion cost compared with retiling a surround?',
  'Meaningfully more, and for concrete reasons: the drain has to move, a sloped pan gets built where the tub used to be, and the wall tile area grows. A surround refresh keeps the tub doing the waterproofing work at floor level; a conversion rebuilds all of that from the framing up. It is also the version of the project that transforms how the room lives day to day.'),
 ('How long does it take to tile a shower?',
  'A tub surround typically runs four to six days; a full walk-in or a conversion runs longer, because the pan build, membrane cure times, the 24-hour flood test, and grout and silicone each need their own window. Rushing any of those stages is how showers fail in year two, so we schedule them honestly up front.'),
 ('Is a tiled shower worth it over a prefab surround?',
  'A prefab unit is cheaper and faster, and for a rental or a rarely used bath it can be the rational choice - we will say so. A tiled shower costs more and outlasts it by decades, looks like the house instead of a catalog, and is fully repairable. For a primary bath you use daily and plan to keep, tile is usually the better long-term money.'),
 ('Should I redo the bathroom floor at the same time as the shower?',
  'It is worth pricing, because the expensive parts of a small tile job - mobilization, prep, disposal - are already on site for the shower. Doing both in one project costs noticeably less than doing them a year apart, and it lets the floor and shower be designed together instead of matched afterward.'),
 ('Does the shower glass come from the tile contractor?',
  'Usually not - frameless glass is measured and installed by a glass company after the tile is done and cured, and it is a real line in your total budget. We plan the tile layout with the glass in mind, including where the door swings and how the curb is capped, and we can coordinate the measure so the sequence does not stall.'),
 ('What if you open the wall and find rot or mold?',
  'It happens often enough in 1990s construction that we plan for it: the quote carries a contingency allowance and a unit rate for repairs, and anything we find gets photographed and priced before we proceed. That is the difference between a surprise and a change order - you decide with evidence in hand, not under pressure mid-demolition.'),
]),

cta('Get Your Shower Priced Line by Line',
    'Demolition, substrate, waterproofing, flood test, tile, grout &mdash; every line in writing, with a contingency instead of a mid-job surprise. Free in-home estimates across King &amp; Snohomish County, Sammamish plateau included.'),

related([
 ('/blog/tile-shower-waterproofing', 'Shower waterproofing, layer by layer'),
 ('/blog/epoxy-vs-cement-grout', 'Epoxy vs cement grout'),
 ('/blog/shower-niche-placement-size-waterproofing', 'Shower niches done right'),
 ('/blog/bathroom-tile-installation-cost-seattle', 'Bathroom tile cost, itemized'),
 ('/city-of-sammamish/tile-installation-in-sammamish-wa', 'Tile installation in Sammamish'),
 ('/contact', 'Book a free estimate'),
]),
]

assemble(S, parts)
