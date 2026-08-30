from builder import *

S = 'cost-to-carpet-a-room'

parts = [
date_badge('October 29, 2026'),

quick_answer(
 "<strong>Carpeting a single room in Sammamish starts with simple arithmetic &mdash; installed carpet from $1.49 per square foot against a typical bedroom's 140&ndash;200 square feet &mdash; but the "
 "honest quote carries fixed costs the arithmetic misses:</strong> tear-out and disposal, transitions at every doorway, furniture moving, and a crew's trip that costs the same whether they lay one room "
 "or five. That is why one room never costs a fifth of five rooms, and why sometimes the smart move is doing the hallway while the crew is already there. We measure free and put the whole thing in "
 "writing the same visit.",
 'Sammamish &amp; the Plateau'),

facts([
 ('From $1.49/sq ft', 'where installed carpet starts with us &mdash; material, pad and labor together. A single-room job still gets the same pad choices and the same power-stretched installation as a whole house.'),
 ('~170 sq ft', 'what a typical 12&times;12 bedroom actually consumes once roll width and waste are counted &mdash; the floor is 144 square feet, but carpet comes off a 12-foot roll and closets count too.'),
 ('Same visit', 'when you get our written price. We measure the room, the closet and the doorways in person, bring the samples to your light, and the number we leave is the number you pay.'),
]),

'<h2>The One-Room Math, Honestly</h2>',

"<p>Start with the part you can do on a napkin. A 12-by-12 bedroom is 144 square feet of floor. Add the closet &mdash; almost every Sammamish bedroom has a real one, and walk-ins are common on the "
"Plateau &mdash; and measure through the doorway to the middle of the door, and you are near 160. Carpet comes off a 12-foot roll, so add waste for the cuts, and the material the job consumes lands "
"around 170 square feet. Against an installed price that starts at $1.49 per square foot, the napkin says a few hundred dollars, and the napkin is not wrong about the carpet.</p>",

"<p>What the napkin misses is everything that is not carpet. The old floor has to come out, get carried downstairs, and be hauled somewhere that charges by the load. Every doorway needs a proper "
"transition to the floor it meets &mdash; hardwood, tile or the hallway's older carpet. The furniture has to move twice. And the crew, the van, the tools and the trip cost the same for one bedroom as "
"for a whole upstairs. None of those line items care how small the room is, which is exactly why they deserve to be named in the quote instead of discovered after. Our "
"<a href=\"/blog/how-to-measure-for-carpet\">guide to measuring for carpet</a> covers the roll-width math; here is the rest of the bill.</p>",

table('A One-Room Carpet Quote, Line by Line', ['Line item', 'Scales with room size?', 'What to know'], [
 ('<strong>Carpet</strong>', 'Yes', 'Priced on the carpet the job consumes &mdash; roll width and waste included &mdash; not the bare floor area'),
 ('<strong>Pad</strong>', 'Yes', 'Small rooms are the cheapest place to upgrade pad; the difference on 170 square feet is lunch money and you feel it for a decade'),
 ('<strong>Labor</strong>', 'Partly', 'Tack strip, seaming and power-stretching scale with size, but setup and the trip do not &mdash; the fixed half looms large in a small job'),
 ('<strong>Tear-out &amp; disposal</strong>', 'Partly', 'One room still means a disposal run; ask whether it is included or an &ldquo;extra&rdquo; waiting to surface'),
 ('<strong>Transitions</strong>', 'No &mdash; per doorway', 'Each doorway needs the right trim piece for the floor it meets; a bedroom usually has one or two'),
 ('<strong>Furniture</strong>', 'No', 'We move normal bedroom furniture and put it back; emptying the dresser first makes the day faster'),
 ('<strong>Subfloor surprises</strong>', 'Only if found', 'Squeaks and soft spots get fixed while the floor is open &mdash; cheap now, annoying forever if skipped'),
]),

'<h2>Why One Room Costs More Per Foot Than a Whole Floor</h2>',

"<p>Spread those fixed lines over one bedroom and they are a real share of the bill; spread them over an entire upstairs and they nearly vanish into the per-foot price. That is the whole mystery of "
"one-room pricing, and it is not unique to carpet &mdash; it is why a plumber's first hour costs more than his third. It also produces the industry's least-loved surprise: the homeowner who collects a "
"whole-house quote, divides by five, and expects one room for that number. The honest answer is that the fifth room was always the cheapest one.</p>",

"<p>The useful move is to flip the logic. If the hallway outside the bedroom is the same vintage and one shade sadder, adding it while the crew is already set up is the cheapest that hallway will ever "
"be. Same for the bonus room across the landing. We will price the single room straight, and we will also tell you what the adjacent spaces would add &mdash; not as a push, but because the fixed costs "
"are already paid and you deserve to see the arithmetic. What a fair number looks like across a bigger job is covered in "
"<a href=\"/blog/carpet-installation-cost-seattle\">what carpet installation costs</a> and <a href=\"/blog/what-is-a-good-price-to-pay-for-carpet-in-seattle-wa\">what a good carpet price looks like</a>.</p>",

'<h2>When One Room Is Exactly the Right Call</h2>',

"<p>Plenty of the single-room jobs we do in Sammamish are the correct scope, no upsell required. A nursery on the way &mdash; new, soft, clean carpet in one room, on a deadline. A teenager's bedroom "
"that has absorbed years of concentrated abuse the rest of the house was spared. A home office that became a home office in 2020 and earned it. Pet damage confined to one room &mdash; if the pad or "
"subfloor took the hit, replacement beats cleaning, and <a href=\"/blog/best-carpet-for-pets\">the right pet spec</a> stops the rerun. A leak or spill that ruined one floor. In all of these, the room "
"has a clear boundary &mdash; a doorway where new carpet can meet the old floor with a clean transition &mdash; and nobody will ever notice the seam in your carpet history.</p>",

"<p>One honest caveat: if the room's carpet is continuous with the hallway's &mdash; no doorway break, one uninterrupted piece &mdash; a one-room replacement means cutting a seam where none existed and "
"marrying new carpet to old at it. New meets old the way new jeans meet old jeans: same size, different life. We will tell you at the measure whether your boundary is clean or whether the hallway wants "
"to come along for the ride.</p>",

two_col(
 'Signs one room is enough',
 ['The damage or wear is confined to that room &mdash; the rest of the floor is honestly fine',
  'A doorway gives the new carpet a clean place to stop',
  'The room has a deadline the rest of the house does not &mdash; nursery, listing photos, a move-in',
  'You are matching function, not color &mdash; an office, a gym, a guest room',
  'The adjacent carpet is a different age or style anyway, so nothing was ever going to match'],
 'Signs the whole floor makes more sense',
 ['The hallway and landing share the room&rsquo;s carpet with no break to hide the change',
  'Every room up there is the same age and showing it &mdash; you would be back within two years',
  'Stairs are involved and worn; they wear first and match nothing &mdash; see our stairs guide',
  'You are selling &mdash; buyers read one new room and four tired ones as four line items',
  'The fixed costs bother you &mdash; they are paid once either way, and the per-foot price falls fast'],
),

'<h2>Sammamish Rooms, Specifically</h2>',

"<p>The Plateau's housing stock shapes the jobs. Most of Sammamish went up from the 1990s onward, which means big primary bedrooms with walk-in closets &mdash; measure the closet, it is a real room "
"&mdash; and <strong>bonus rooms over garages</strong>, the classic single-room job: cold floor below, kids' traffic above, and a doorway that gives new carpet a clean boundary. It also means "
"<strong>daylight basements</strong> on the sloped lots, where the right answer depends on moisture before it depends on color &mdash; our <a href=\"/blog/carpet-for-basement\">basement carpet guide</a> "
"covers that conversation honestly. And it means two-story layouts where the stairs take the traffic of the whole house; if yours are showing it, "
"<a href=\"/blog/best-carpet-for-stairs\">carpet for stairs</a> explains why they are priced per tread and worth the most resilient fiber in the budget.</p>",

"<p>We bring the mobile showroom to all of it &mdash; twenty-plus full-size samples and all three pad grades, laid out in the actual room, because Plateau light through second-growth firs is its own "
"color grader. The measure is free, the written price arrives the same visit, and most single rooms are installed in a morning. The full local details live on our "
"<a href=\"/city-of-sammamish/carpet-installation-in-sammamish-wa\">Sammamish carpet installation page</a>.</p>",

faq('Carpeting One Room in Sammamish: What Homeowners Ask Us', [
 ('How much does it cost to carpet one room?',
  'Installed carpet starts at $1.49 per square foot with us, and a typical 12-by-12 bedroom consumes about 170 square feet once the closet, doorway and roll-width waste are counted. On top of the carpet math sit the fixed parts of any job — tear-out and disposal, transitions, furniture moving and the trip itself — which is why we measure in person and give you one written number that includes all of it.'),
 ('Why does one room cost more per square foot than a whole house?',
  'Because the fixed costs — the crew’s trip, setup, tear-out run, disposal — are spread over 170 square feet instead of 1,700. The carpet itself costs the same per foot either way. This is also why adding an adjacent hallway or bonus room while the crew is already there is the cheapest those spaces will ever be.'),
 ('Can you match my existing carpet in the rest of the house?',
  'Honestly, rarely. Even the identical style and color from the same mill comes from a different dye lot, and your existing carpet has years of light and traffic on it. The clean solution is a doorway transition, where the eye accepts a change. If the old carpet runs unbroken into the hall, we will tell you at the measure whether a seam there will show.'),
 ('Is it worth doing the hallway or stairs at the same time?',
  'Often, yes. The fixed costs are already paid, so adjacent spaces add at close to the bare per-foot rate. Stairs are the strongest case — they wear faster than any room, they are priced per tread regardless of when you do them, and a fresh bedroom next to a worn staircase just moves the eyesore six feet.'),
 ('How long does carpeting one room take?',
  'Usually a morning once the carpet has arrived — tear-out, subfloor check, pad, power-stretched installation and furniture back in place. Ordering the carpet is the longer part of the timeline, since it is cut from a roll at the mill. We will give you both timelines at the measure.'),
 ('Do you handle small jobs like a single bedroom, or is there a minimum?',
  'We do single rooms all the time — nurseries, offices, teenage-bedroom recoveries. The quote carries the job’s real fixed costs, so a small room costs more per foot than a big house, but the work gets the same spec: proper tack strip, the pad grade you chose, and a power-stretched installation, not a knee-kicked one.'),
 ('What if there is pet damage or a stain — replace or clean?',
  'Depends on how deep it went. Surface stains on sound carpet clean out. Urine that reached the pad or subfloor will outlast any cleaning, and one room of replacement with a moisture-barrier pad is the fix that actually ends it. If the carpet is merely rippled, restretching costs a fraction of replacement — we will tell you which situation you have.'),
 ('Does new carpet in one room help or hurt when selling?',
  'One fresh room next to visibly tired ones reads as a to-do list to buyers, so for a listing the better spend is usually the whole visible run — hall, stairs, main rooms — in one consistent, neutral carpet. For a single problem room with a clean doorway boundary, one room is fine. We will give you straight numbers for both scopes and let you decide.'),
]),

cta('Price One Room Without the Guesswork',
    'We measure the room, closet and doorways, bring twenty-plus samples and all three pad grades to your light, and leave a written price the same visit &mdash; one room or the whole floor, your call. Free in-home estimates across Sammamish and all of King &amp; Snohomish County.'),

related([
 ('/blog/how-to-measure-for-carpet', 'How to measure a room for carpet'),
 ('/blog/carpet-installation-cost-seattle', 'What carpet installation costs in Seattle'),
 ('/blog/best-carpet-for-stairs', 'The best carpet for stairs'),
 ('/blog/carpet-for-basement', 'Carpet in basements, honestly'),
 ('/city-of-sammamish/carpet-installation-in-sammamish-wa', 'Carpet installation in Sammamish'),
 ('/contact', 'Book a free measure'),
]),
]

assemble(S, parts)
