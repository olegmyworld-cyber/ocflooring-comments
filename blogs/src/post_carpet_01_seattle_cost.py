from builder import *

S = 'carpet-installation-cost-seattle'

parts = [
date_badge('September 3, 2026'),

quick_answer(
 "<strong>Carpet installation in Seattle starts at $1.49 per square foot installed, and a typical three-bedroom job lands in the low four figures once you add pad, stairs, "
 "and hauling the old carpet away.</strong> The number that decides your quote is not the carpet you pick from a sample board &mdash; it is square footage measured honestly, "
 "the pad grade underneath, and how many stairs and closets are in the count. We bring the showroom to your house so you can see all of that in your own light before you commit.",
 'Seattle homes &amp; condos'),

facts([
 ('$1.49/sq ft', 'where installed carpet starts with us &mdash; material, pad and labor. Better fibers and thicker pad move it up from there, and we show you the difference on your own floor rather than under store lighting.'),
 ('20+ samples', 'full-size pieces we bring to your door, along with all three pad grades. Carpet color in a showroom and carpet color in a north-facing Seattle living room in November are two different colors.'),
 ('One day', 'how long most homes take to install once the carpet is in. We measure and give you a written price on the same visit, so nothing about the number arrives later as a surprise.'),
]),

'<h2>What You Are Actually Paying For</h2>',

"<p>A carpet quote has four parts, and only one of them is the thing you picked out. There is the carpet itself, priced per square foot or per square yard depending on who is quoting. "
"There is the pad, which almost nobody shops for and which decides more about how the floor feels and how long it lasts than most people believe. There is labor &mdash; measuring, "
"moving furniture, tearing out the old floor, laying tack strip, seaming, power-stretching. And there is disposal, because a house's worth of old carpet does not fit in a bin.</p>",

"<p>When two quotes are hundreds of dollars apart on the same carpet, the gap is almost always in the last three. Somebody quoted a builder-grade pad. Somebody left out haul-away. "
"Somebody measured the bedrooms and forgot the closets, or counted stairs as square feet instead of per-tread. None of that is visible on a sample board, which is exactly why we go "
"through it line by line at the estimate.</p>",

table('What Moves a Seattle Carpet Quote', ['Factor', 'Effect', 'Why it matters'], [
 ('<strong>Square footage</strong>', 'The base of everything', 'Measured wall to wall including closets, with an allowance for waste &mdash; carpet comes in fixed-width rolls, so an odd room shape costs more than its area suggests'),
 ('<strong>Pad grade</strong>', 'Modest cost, large effect', 'The cheapest pad flattens in a few years and takes the carpet with it. Upgrading pad is the best value decision in the whole quote'),
 ('<strong>Fiber</strong>', 'The biggest material swing', 'Polyester is soft and affordable, nylon holds its shape under traffic, wool is the premium option'),
 ('<strong>Stairs</strong>', 'Priced per tread, not per sq ft', 'A staircase is slow, precise work &mdash; far more labor per square foot than an open bedroom'),
 ('<strong>Removal &amp; disposal</strong>', 'Per square foot', 'Old carpet, pad, staples and tack strip all have to come out and go somewhere'),
 ('<strong>Furniture</strong>', 'Usually included, ask anyway', 'We move normal household furniture; pianos, safes and full waterbeds are their own conversation'),
 ('<strong>Subfloor repairs</strong>', 'Only if needed', 'Squeaks, soft spots and old pet damage get found when the carpet comes up &mdash; better to price it then than to carpet over it'),
 ('<strong>Access</strong>', 'Condos cost more', 'Elevator reservations, protected common areas and building hours all add labor in a downtown high-rise'),
]),

'<h2>The Pad Is the Part Worth Arguing About</h2>',

"<p>If you take one thing from this page: spend on the pad. It is the cheapest upgrade in the quote and it changes both how the carpet feels and how long it survives. Pad is what "
"absorbs the impact of every footstep; without enough of it, the carpet backing takes that load directly and the fibers crush permanently in the traffic lanes. That is why a carpet "
"can look ten years old after three &mdash; not because the carpet was cheap, but because the pad under it was.</p>",

"<p>We carry three grades and bring all three to the estimate so you can stand on them. The differences are obvious underfoot in about four seconds, which is roughly four seconds "
"longer than most people have ever spent thinking about pad. In a house with kids, pets, or a staircase that takes real traffic, the mid or upper grade pays for itself before the "
"carpet is halfway through its life.</p>",

'<h2>Fiber, in Plain Terms</h2>',

"<p><strong>Polyester (PET)</strong> is soft, takes color beautifully, resists stains inherently, and costs less. It is the right answer for bedrooms and low-traffic rooms, and its "
"weakness is matting &mdash; it does not spring back from heavy traffic the way nylon does. <strong>Nylon</strong> is the workhorse: more resilient, better in hallways, stairs and "
"family rooms, and worth the premium anywhere feet actually go. <strong>Wool</strong> is the luxury option, naturally flame-resistant and beautiful, and priced accordingly. "
"<strong>Triexta</strong> sits between polyester and nylon and does well with pets.</p>",

"<p>Most Seattle houses we carpet end up mixed: nylon on the stairs and hallway, polyester in the bedrooms. Nobody sells it that way, but it puts the money where the wear is. "
"If you want the longer comparison, our guide to <a href=\"/blog/the-10-best-carpet-brands-reviews-2023-guide\">carpet brands</a> covers who makes what, and "
"<a href=\"/blog/what-is-a-good-price-to-pay-for-carpet-in-seattle-wa\">what a good price looks like in Seattle</a> goes deeper on the numbers.</p>",

'<h2>Why We Bring the Showroom to You</h2>',

"<p>Carpet is the one flooring material that is genuinely hard to choose in a store. Showroom lighting is bright, neutral and overhead; your living room is none of those things. "
"Seattle makes that worse than most places &mdash; from October to April the light coming through a north window is flat and grey, and a beige that looked warm under store lights "
"reads green on your floor. Undertones that were invisible on the rack become the thing you notice every day.</p>",

"<p>So we drive twenty-plus full-size samples to your house, lay them on the floor of the actual room, and leave while you look at them at different times of day if you want. "
"We measure every room, closet and stair while we are there, and we leave a written price the same visit. In practice that turns a decision people dread into an hour at their "
"kitchen table.</p>",

two_col(
 'What our quote includes',
 ['Measuring every room, closet and stair &mdash; not estimating from a floor plan',
  'Moving normal household furniture and putting it back',
  'Tear-out of the old carpet, pad, staples and tack strip',
  'Haul-away and disposal of everything that comes out',
  'New tack strip, seaming and power-stretching &mdash; not kicked in',
  'A written price the same visit, with the pad grade named'],
 'What to check in any other quote',
 ['Whether stairs are priced per tread or hidden in the square footage',
  'Which pad grade the number assumes &mdash; ask by name, not "standard"',
  'Whether removal and disposal are in or extra',
  'Whether the carpet is power-stretched or knee-kicked (it matters in year three)',
  'Whether closets were counted',
  'What happens if the subfloor turns out to need work']),

'<h2>Seattle-Specific Things That Come Up</h2>',

"<p><strong>Old houses are not square.</strong> A Ballard bungalow or a Beacon Hill four-square has walls that wander and floors that slope. Carpet hides that better than any hard "
"surface, which is part of its appeal, but it means seam placement takes planning and the waste factor is higher than the room's raw area suggests. A quote generated from square "
"footage alone will be wrong on those houses.</p>",

"<p><strong>Condos have rules.</strong> Downtown and Belltown buildings typically have elevator reservations, protected-corridor requirements, work-hour windows, and their own "
"disposal rules. Many also have acoustic requirements in the CC&amp;Rs &mdash; which, happily, carpet and a decent pad satisfy comfortably. We plan around the building rather than "
"discovering it on install day.</p>",

"<p><strong>Damp basements and daylight rooms.</strong> Carpet over a slab that wicks moisture is a mold problem waiting to happen. If the basement is dry, carpet is wonderful down "
"there; if it is not, we will say so and point you at a waterproof option instead. Same conversation we have about "
"<a href=\"/blog/upkeep-for-carpet-vs-hardwood-flooring\">carpet against hard flooring</a> generally.</p>",

'<h2>When Replacing Is the Wrong Call</h2>',

"<p>Sometimes the honest answer is that you do not need new carpet. Ripples and buckling usually mean the carpet was never power-stretched properly &mdash; restretching costs a "
"fraction of replacement and buys years, which we cover in <a href=\"/blog/is-it-worth-it-to-restretch-your-carpet\">is restretching worth it</a>. Traffic lanes that look dirty may "
"just be dirty; a professional clean is cheap next to a new floor. And if the carpet is sound but you hate the color, that is a real reason to replace it, just not an urgent one.</p>",

"<p>Where replacement genuinely wins: matting that does not recover, pet damage that reached the pad or subfloor, allergy problems, or carpet old enough that the backing is "
"delaminating. Our list of <a href=\"/blog/6-reasons-to-replace-carpet-flooring\">reasons to replace carpet</a> is the longer version, and "
"<a href=\"/blog/how-to-remove-old-carpet\">removing old carpet</a> covers what is involved if you want to pull it yourself.</p>",

faq('Carpet Installation Cost in Seattle: What Homeowners Ask Us', [
 ('How much does carpet installation cost in Seattle?',
  'Installed carpet starts at $1.49 per square foot with us, covering material, pad and labor. Where your number lands depends on fiber, pad grade, how many stairs are in the job, and whether the old carpet needs removing and hauling. We measure every room and stair and give you a written price on the same visit, so there is no gap between the estimate and the invoice.'),
 ('Is the pad included in the price, and does it matter?',
  'It is included, and it matters more than almost anything else in the quote. Pad absorbs the impact of every footstep; too little of it and the carpet fibers crush permanently in the traffic lanes, which is why some carpet looks worn out in three years. We bring all three grades to the estimate so you can feel the difference underfoot before deciding.'),
 ('How are stairs priced?',
  'Per tread, not by square footage. Stairs are slow, precise work — every tread is wrapped or capped individually and the carpet has to be secured properly for safety — so they carry far more labor per square foot than an open bedroom. Any quote that buries stairs in a total square-foot number is worth asking about.'),
 ('Do you move the furniture?',
  'Yes, normal household furniture is part of the job and we put it back when we are done. The exceptions are the heavy specials — pianos, gun safes, full waterbeds, aquariums — which need their own arrangements. Emptying dressers and closets before we arrive speeds the day up considerably.'),
 ('How long does carpet installation take?',
  'Most homes are a single day once the carpet has arrived. Ordering is usually the longer part of the timeline, since carpet is cut from a roll at the mill. Large houses or jobs with a lot of stairs can run into a second day, and we will tell you which yours is at the estimate rather than on the morning.'),
 ('What is the best carpet for a house with pets?',
  'A solution-dyed fiber with a moisture-barrier pad. Solution-dyed means the color goes all the way through the fiber, so it survives cleaning that would fade a printed carpet, and the barrier pad stops accidents from reaching the subfloor — which is what actually causes lingering odor. Triexta and nylon both do well here.'),
 ('Should I replace my carpet or restretch it?',
  'If the problem is ripples, waves or buckling, restretch — that is a stretching failure, not a worn-out carpet, and it costs a fraction of replacement. Replace when the fibers are matted flat and no longer recover, when pet damage has reached the pad or subfloor, or when the backing is coming apart. We will tell you honestly which one you have.'),
 ('Can you carpet a Seattle condo with building restrictions?',
  'Yes, and we plan around the building from the start — elevator reservations, protected common areas, permitted work hours and the building’s disposal rules. Many buildings also have acoustic requirements in their CC&Rs, which carpet over a good pad satisfies comfortably. Send us the rules with your estimate request and we will build the schedule around them.'),
]),

cta('See the Samples in Your Own Living Room',
    'We bring twenty-plus full-size carpet samples and all three pad grades to your door, measure every room and stair, and leave a written price the same visit. No showroom lighting, no pressure. Free in-home estimates across King &amp; Snohomish County.'),

related([
 ('/blog/what-is-a-good-price-to-pay-for-carpet-in-seattle-wa', 'What a good carpet price looks like in Seattle'),
 ('/blog/6-reasons-to-replace-carpet-flooring', 'Six reasons to replace carpet'),
 ('/blog/is-it-worth-it-to-restretch-your-carpet', 'Restretch or replace?'),
 ('/blog/the-10-best-carpet-brands-reviews-2023-guide', 'The best carpet brands'),
 ('/seattle/carpet-installation-in-seattle-wa', 'Carpet installation in Seattle'),
 ('/contact', 'Book a free estimate'),
]),
]

assemble(S, parts)
