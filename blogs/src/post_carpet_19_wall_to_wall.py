from builder import *

S = 'wall-to-wall-carpet-cost'

parts = [
date_badge('January 7, 2027'),

quick_answer(
 "<strong>Wall-to-wall carpet starts at $1.49 per square foot installed with us &mdash; material, pad and labor &mdash; and a whole-house number is really a stack of room-by-room "
 "numbers that behave differently.</strong> Bedrooms are cheap and simple. Hallways and stairs are small but labor-dense. Big living rooms trip over the width of the carpet roll and "
 "pick up seams. The way to a real total is not multiplying your square footage by a rate you saw online; it is walking the house room by room, which is exactly what we do at a "
 "Kenmore kitchen table with the samples already on the floor.",
 'Kenmore split-levels &amp; ramblers'),

facts([
 ('From $1.49/sq ft', 'installed &mdash; carpet, pad and labor in one number. Fiber upgrades and pad grade move it from there, room by room, and you see each move in the written price before anything is ordered.'),
 ('12 ft', 'the usual width of a carpet roll. Rooms wider than the roll need a seam, and rooms shaped awkwardly need more carpet than their area suggests &mdash; the two facts that break every online calculator.'),
 ('Per tread', 'how the stairs in a split-level are priced. Two short staircases is still a real stair job, and in most Kenmore layouts they take more wear than any room they connect.'),
]),

'<h2>Why the Whole-House Number Is Really Six Numbers</h2>',

"<p>Kenmore is split-level country. The housing stock that went up here in the sixties and seventies &mdash; up from Bothell Way, around Moorlands and Inglewood &mdash; loves a "
"floor plan with a living room half a flight up, bedrooms above it, a family room half a flight down, and two short staircases stitching it together. Carpeting a house like that "
"is not one job; it is a bedroom job, a living-room job, a hallway job, a lower-level job and a stair job, each with its own math. Two houses with identical total square footage "
"can land meaningfully apart on price because of how those pieces divide up.</p>",

"<p>That is why we quote room by room and show the arithmetic. It also means you can phase the work &mdash; bedrooms this year, the lower level next &mdash; without anything being "
"re-measured or re-guessed. Here is how the pieces of a typical Kenmore split-level behave in a quote.</p>",

table('A Kenmore Split-Level, Room by Room', ['Area', 'Typical size', 'What moves its number'], [
 ('<strong>Primary bedroom</strong>', '~150&ndash;200 sq ft', 'The easy one: usually narrower than the roll, so no seams, fast install. Softness matters more than toughness here'),
 ('<strong>Two kids&rsquo; bedrooms</strong>', '~110&ndash;140 sq ft each', 'Same simple math. Closets count &mdash; a quote that skips them is quietly wrong by a room&rsquo;s worth over a house'),
 ('<strong>Living room</strong>', '~250&ndash;350 sq ft', 'Often wider than 12 ft, so a seam enters the plan &mdash; where it lands, and how much extra carpet it takes, is installer skill'),
 ('<strong>Hallway</strong>', '~40&ndash;80 sq ft', 'Tiny area, dense labor: doorways, transitions, and the highest traffic per square foot in the house'),
 ('<strong>Lower-level family room</strong>', '~200&ndash;300 sq ft', 'Concrete-adjacent: moisture gets checked before carpet goes down, and pad choice matters most here'),
 ('<strong>Stairs, two runs</strong>', '~13&ndash;15 treads total', 'Priced per tread, not by area. The most labor-intensive square feet in the whole job &mdash; and the first to show wear'),
]),

'<h2>Roll Width and Seams: Where Online Calculators Go Wrong</h2>',

"<p>Carpet arrives as a roll, almost always twelve feet wide. A bedroom eleven feet across fits inside the roll and wastes little. A living room fourteen feet across cannot be "
"covered in one pass &mdash; it needs a second piece and a seam, and the second piece has to come from somewhere, usually with real waste, because pattern and pile direction have "
"to match across the joint. This is the single biggest reason a square-footage-times-rate estimate misses: the house is priced by how it cuts from the roll, not by its area. "
"A ten percent difference between the floor area and the carpet actually ordered is routine; awkward rooms run higher.</p>",

"<p>Good seam planning is invisible &mdash; seams tucked away from windows whose light would rake across them, out of the main walking line, never perpendicular to a doorway "
"threshold. It is also the difference between a floor that looks seamless for fifteen years and one with a visible stripe in year two. When we measure, the seam diagram is part of "
"the written price, which is one of the checks we recommend in our guide to <a href=\"/blog/hiring-a-carpet-installer-seattle\">hiring a carpet installer</a>. The measuring logic "
"itself is laid out in <a href=\"/blog/how-to-measure-for-carpet\">how to measure for carpet</a> if you want to rough out your own numbers first.</p>",

'<h2>Where to Spend and Where to Save, Room by Room</h2>',

"<p>The pleasant surprise of a room-by-room quote is that you do not have to buy one carpet for the whole house. <strong>Spend on the hallway and stairs</strong> &mdash; a resilient "
"nylon and a firm pad, because they take more traffic than every bedroom combined; our <a href=\"/blog/best-carpet-for-stairs\">stair carpet guide</a> covers why, and Kenmore "
"specifically has an older piece on <a href=\"/blog/whats-the-best-carpeting-for-stairs-in-kenmore-wa\">the best carpeting for stairs in Kenmore</a>. <strong>Save in the "
"bedrooms</strong>, where a soft polyester over a thick pad feels luxurious and never sees enough traffic to mat; the case is made in "
"<a href=\"/blog/carpet-in-bedrooms\">our bedroom carpet guide</a>. <strong>Choose by moisture on the lower level</strong> &mdash; a dry lower level takes carpet happily, and pad "
"grade does the comfort work over that colder slab-side floor.</p>",

"<p>The pad deserves its own sentence in every room: it is the cheapest line in the quote and it decides how the carpet feels and how long it lasts. We bring all three grades to the "
"estimate so you can stand on them in your own hallway &mdash; the full argument is in <a href=\"/blog/carpet-padding-thickness\">our padding guide</a>. Mixing fiber by room while "
"keeping one pad strategy is how a split-level gets carpeted well on a sane budget.</p>",

two_col(
 'What is inside our wall-to-wall price',
 ['Every room, closet, hallway and stair measured in person',
  'A seam plan for any room wider than the roll',
  'Pad grade named per area, with all three grades there to stand on',
  'Tear-out and haul-away of the old carpet, pad, staples and tack strip',
  'Power-stretched installation in every room',
  'Furniture moved and put back',
  'One written total, itemized room by room, the same visit'],
 'What quietly inflates other quotes later',
 ['Closets and hallways left out of the measure',
  'Seam waste discovered after the contract is signed',
  'Stairs counted as square footage, then re-priced on install day',
  '&ldquo;Standard pad&rdquo; that turns out to be the thinnest grade',
  'Disposal fees appearing as a day-of line item',
  'Transitions and thresholds billed separately',
  'A phone estimate that was never going to survive contact with the house']),

'<h2>The Stairs Are Small and They Matter Most</h2>',

"<p>A split-level&rsquo;s two short staircases are easy to overlook in the budget and impossible to overlook in daily life &mdash; every trip from the kitchen to a bedroom or the "
"family room crosses them. They are priced per tread because each step is wrapped, tensioned and fastened individually, and the honest consequence is that thirteen treads can cost "
"as much as a small bedroom. That is not padding; it is where the labor actually is. Put the most resilient fiber in the budget on them, in a color that hides the traffic line, and "
"they will still be the first thing in the house to show age &mdash; just years later than they would have.</p>",

'<h2>Getting a Real Kenmore Number Without Leaving the House</h2>',

"<p>Everything above argues for the same conclusion: wall-to-wall carpet is priced well only from inside the house. So that is where we do it. The mobile showroom brings twenty-plus "
"full-size samples and all three pad grades to your door; we walk every room with a tape measure, count the treads, plan the seams, and leave a written room-by-room price the same "
"visit. Most Kenmore homes install in a single day once the carpet arrives. If the old floor is still down, tear-out and haul-away are in the number &mdash; what that involves is "
"covered in <a href=\"/blog/carpet-removal-cost\">our carpet removal guide</a> &mdash; and the broader market context, if you want to sanity-check us against the region, is in "
"<a href=\"/blog/carpet-installation-cost-seattle\">what carpet installation costs in Seattle</a>. The local service details live on our "
"<a href=\"/city-of-kenmore/carpet-installation-in-kenmore-wa\">Kenmore carpet installation page</a>.</p>",

faq('Wall-to-Wall Carpet Cost: What Kenmore Homeowners Ask', [
 ('How much does wall-to-wall carpet cost installed?',
  'With us it starts at $1.49 per square foot installed — carpet, pad and labor together. The final number moves with fiber choice, pad grade, how many stairs are in the job, seam requirements in wide rooms, and whether old flooring needs to come out. We measure the house and leave a written room-by-room price the same visit.'),
 ('Can I estimate my cost from my home’s square footage?',
  'Only roughly. Carpet comes off a twelve-foot roll, so wide rooms need seams and extra material, awkward rooms carry waste, and closets and stairs change the labor picture. Square footage times a rate is a starting guess; the measured, seam-planned number is the one that survives to the invoice.'),
 ('Why do stairs cost so much compared to their size?',
  'Because each tread is wrapped, tensioned and fastened individually — a staircase is the slowest, most precise work in the house, so it is priced per tread rather than by area. In a split-level the stairs also take the most traffic, which is why we put the most durable fiber there.'),
 ('Is it cheaper to carpet the whole house at once or room by room?',
  'One visit and one install day is more efficient, so whole-house pricing usually works out better per square foot. But a room-by-room quote lets you phase honestly — bedrooms now, lower level later — and because we itemize by room, the later phases are already priced.'),
 ('Should I use the same carpet in every room?',
  'You do not have to, and often should not. Resilient nylon on stairs and hallways where traffic concentrates, softer budget-friendly polyester in bedrooms, and a moisture-sensible choice on the lower level puts money where wear actually happens. One consistent color family keeps the house feeling coherent.'),
 ('Does the pad really change the price and the result?',
  'It changes the result far more than the price. Pad is the cheapest line in the quote, and the difference between builder-grade and mid-grade is what decides whether traffic lanes crush in three years. We bring all three grades so you can feel the difference before choosing — and the pad grade is named in the written price.'),
 ('What about the lower level of a split-level — is carpet safe there?',
  'Usually yes, and it is the warmest thing you can do for a room that sits against concrete. We check moisture before anything goes down; a dry lower level takes carpet happily over the right pad. If there are signs of damp, we will say so and point you to a better option for that room instead of carpeting over a problem.'),
 ('How long does a whole-house carpet job take in Kenmore?',
  'Most homes are one install day once the carpet arrives from the mill — ordering is the longer part of the timeline. A split-level with two staircases might stretch into a second day. You will know which yours is at the estimate, because the treads and seams were counted, not guessed.'),
]),

cta('Price Your Whole House From Your Own Hallway',
    'Twenty-plus full-size samples and all three pad grades come to your Kenmore door. We measure every room, plan every seam, count every tread, and leave a written room-by-room price the same visit. Free in-home estimates across King &amp; Snohomish County.'),

related([
 ('/blog/cost-to-carpet-a-room', 'What it costs to carpet one room'),
 ('/blog/how-to-measure-for-carpet', 'How to measure for carpet'),
 ('/blog/carpet-padding-thickness', 'Carpet padding, explained'),
 ('/blog/hiring-a-carpet-installer-seattle', 'Questions to ask any carpet installer'),
 ('/city-of-kenmore/carpet-installation-in-kenmore-wa', 'Carpet installation in Kenmore'),
 ('/contact', 'Book a free estimate'),
]),
]

assemble(S, parts)
