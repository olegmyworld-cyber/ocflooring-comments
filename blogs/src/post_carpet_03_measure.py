from builder import *

S = 'how-to-measure-for-carpet'

parts = [
date_badge('October 22, 2026'),

quick_answer(
 "<strong>Measure each room wall to wall at the widest points, include every closet, round up to the next foot, and add roughly ten percent for waste &mdash; that gets you close enough to budget.</strong> "
 "What it will not get you is a number that matches a professional estimate, because carpet does not come by the square foot. It comes off a 12-foot roll, and the real question is how that roll has to be "
 "cut and seamed to cover your rooms. That is why two estimates on the same house can differ by hundreds of dollars while both being honest &mdash; and why our measure is free and comes with a written "
 "price the same visit.",
 'King &amp; Snohomish homes'),

facts([
 ('12 feet', 'the standard carpet roll width. Your room is not 12 feet wide, which is why the square footage on a quote is always more than the square footage of the floor &mdash; the difference is cuts, seams and waste, not padding of the bill.'),
 ('Per tread', 'how stairs are honestly priced. A staircase is slow, precise work &mdash; each step wrapped individually &mdash; so a quote that buries stairs inside a square-foot total is hiding the hardest part of the job.'),
 ('Same visit', 'when you get our written price. We measure every room, closet and stair in person, walk you through where the seams will go, and leave a number that will not move on install day.'),
]),

'<h2>Why Two Honest Estimates Still Come Out Different</h2>',

"<p>Here is the situation that generates most of the calls we get about measuring: a homeowner tapes off their rooms, multiplies length by width, adds it up, and gets, say, 800 square feet. Then two "
"estimates arrive &mdash; one quoting 880 square feet, one quoting 960 &mdash; and the natural conclusion is that somebody is inflating the number. Usually nobody is. The two companies made different "
"decisions about roll direction, seam placement and waste, and every one of those decisions changes how much carpet has to be ordered to cover the same floor.</p>",

"<p>Carpet is not tile. You cannot buy exactly the amount your floor needs, because the mill cuts it from a roll of fixed width and the pile has to run the same direction everywhere &mdash; carpet laid "
"with the nap reversed reads as two different colors in the same room. So the estimator is not measuring your floor so much as solving a small puzzle: how do fixed-width strips, all facing the same way, "
"cover these particular rooms with seams landing where nobody walks? Different solutions to that puzzle consume different amounts of carpet. The honest way to compare quotes is not the square footage "
"&mdash; it is asking each estimator to show you their cut plan and their seam placement, then comparing the bottom line for what is actually included. Our guide to "
"<a href=\"/blog/what-is-a-good-price-to-pay-for-carpet-in-seattle-wa\">what a good carpet price looks like</a> goes deeper on that comparison.</p>",

'<h2>The Wall-to-Wall Rules</h2>',

"<p>If you want a budgeting number of your own before anyone visits &mdash; a genuinely good idea &mdash; measure like this. Take each room at its <strong>longest and widest points</strong>, wall to wall, "
"not baseboard to baseboard. If the room is out of square, and in most houses more than a decade old it is, use the bigger measurement; carpet gets trimmed to fit, and coming up short is the one mistake "
"that cannot be fixed. Round each measurement up to the next foot.</p>",

"<p><strong>Measure into every doorway to the point where the new carpet will meet the next floor</strong> &mdash; usually the middle of the door when it is closed, not the edge of the room. "
"<strong>Include every closet</strong>, measured to its back wall; a bedroom with a walk-in can carry 30 extra square feet that a quick length-times-width misses entirely. Multiply, add the rooms up, then "
"add about ten percent for waste and seams. For a hallway with lots of doorways or an oddly shaped room, lean toward more. That total is your budgeting number, and multiplied against a real installed "
"price &mdash; ours <a href=\"/blog/carpet-installation-cost-seattle\">starts at $1.49 per square foot installed</a> &mdash; it will put you in the right neighborhood.</p>",

table('Measuring a Room: Where DIY Numbers Go Wrong', ['Step', 'The common mistake', 'The right way'], [
 ('<strong>Room dimensions</strong>', 'Measuring the open floor between furniture', 'Wall to wall at the longest and widest points, rounded up to the next foot'),
 ('<strong>Doorways</strong>', 'Stopping at the edge of the room', 'Measure to the middle of the doorway, where the transition to the next floor lands'),
 ('<strong>Closets</strong>', 'Forgotten entirely &mdash; the single most common miss', 'Every closet to its back wall; walk-ins measured as their own small room'),
 ('<strong>Out-of-square rooms</strong>', 'Averaging the two wall lengths', 'Use the larger measurement &mdash; carpet trims down, it does not stretch up'),
 ('<strong>Waste allowance</strong>', 'Skipping it, or guessing low', 'Add roughly 10%; more for odd shapes, many doorways, or patterned carpet that must match at seams'),
 ('<strong>Stairs</strong>', 'Counted as square feet in the total', 'Counted per tread, priced per tread &mdash; they are labor, not area'),
 ('<strong>Roll direction</strong>', 'Not considered at all', 'Pile must run one direction; sometimes the &ldquo;wasteful&rdquo; layout is the one that looks right'),
]),

'<h2>The 12-Foot Roll Problem</h2>',

"<p>This is the part that makes carpet estimating genuinely unintuitive, so it is worth one concrete example. Say your living room is 13 feet wide and 16 feet long &mdash; 208 square feet on paper. The "
"roll is 12 feet wide. One width of carpet covers 12 of your 13 feet, and that last foot has to come from a second strip, seamed in along the length of the room. But that strip cannot be a one-foot "
"sliver cut from anywhere: it has to run the same direction as the main piece, so it gets cut from another full-width length of the roll. Depending on the layout, that 208-square-foot room can consume "
"250 or more square feet of carpet, and the leftover pieces are too small and too directional to cover another room.</p>",

"<p>A good estimator plays this puzzle across the whole job at once &mdash; sometimes the offcut from the bedroom does fill the hall, if the nap direction cooperates and the seam lands somewhere feet "
"rarely go. That is also why <strong>seam placement is a quality question, not just a cost question</strong>. Seams that land in a doorway or across a main walking lane will wear faster and show sooner. "
"When we measure, we tell you where every seam will fall before you sign anything, because a cheap layout with a seam down the middle of the family room is not actually cheap &mdash; it is a "
"<a href=\"/blog/how-long-does-carpet-last\">shorter-lived floor</a> wearing a discount.</p>",

'<h2>Closets, Halls and Stairs: Where Estimates Quietly Diverge</h2>',

"<p>When two quotes on the same house are far apart, the gap usually lives in the small spaces. <strong>Closets</strong> are either measured or guessed, and a house full of guessed closets can be off by "
"a whole room's worth of carpet. <strong>Hallways</strong> are narrow, doorway-riddled and directional &mdash; high waste relative to their area, and a common place for one estimator to plan a seam where "
"another plans a full strip. And <strong>stairs</strong> are the biggest one: an honest quote prices them per tread, because wrapping each step &mdash; tucked, stretched and secured individually &mdash; "
"is some of the slowest work in the trade. A staircase's worth of labor hidden inside a square-foot total is the classic way a low quote grows on install day. We wrote more about what makes stairs their "
"own job in <a href=\"/blog/best-carpet-for-stairs\">our guide to carpet for stairs</a>.</p>",

"<p>The other quiet divergence is what happens to the old floor. Tear-out, hauling and disposal of a house's worth of carpet and pad is real work that some quotes include and some list as an extra "
"discovered later &mdash; <a href=\"/blog/carpet-removal-cost\">carpet removal costs</a> covers what that line should look like. None of these differences mean anyone is dishonest. They mean the only "
"comparable number between two quotes is the final one, with every line named.</p>",

two_col(
 'Measure yourself &mdash; good enough to budget',
 ['Longest and widest point of each room, wall to wall, rounded up',
  'Through doorways to the middle of the door',
  'Every closet, to the back wall',
  'Count stair treads separately &mdash; do not fold them into square feet',
  'Add about 10% for waste; more for odd shapes or patterned carpet',
  'Multiply by an installed price per square foot to get a realistic range'],
 'What only an in-person measure settles',
 ['Roll direction and the cut plan &mdash; the real quantity of carpet needed',
  'Where every seam lands, and whether that placement will wear well',
  'Whether the subfloor has soft spots, squeaks or damage to price now, not later',
  'Which transitions and trim pieces each doorway actually needs',
  'How stairs are built &mdash; box stairs, capped ends and rails change the labor',
  'A written price that includes tear-out, disposal and furniture moving'],
),

'<h2>Why We Measure for Free</h2>',

"<p>Not as a favor &mdash; because it is the only way to give you a number we can stand behind. A price generated from your square footage over the phone is a guess about the cut plan, a guess about the "
"seams, a guess about the closets and a guess about the stairs, and every one of those guesses gets settled later, usually in the direction you will not enjoy. Measuring in person costs us an hour and "
"removes every guess at once. Since 2013 and more than a thousand floors, the same-visit written price has been the difference between our invoices and our estimates being the same document.</p>",

"<p>The visit does double duty: our mobile showroom comes along, with twenty-plus full-size samples and all three pad grades, so you can see colors in your own light while we measure &mdash; showroom "
"lighting flatters carpet in ways a north-facing room in a Northwest November does not. You get the measurement, the seam plan, the samples and the price in one visit, on your "
"<a href=\"/seattle/carpet-installation-in-seattle-wa\">carpet installation</a> schedule rather than a salesman's. And if the honest answer is that you do not need new carpet at all &mdash; ripples that "
"a <a href=\"/blog/is-it-worth-it-to-restretch-your-carpet\">restretch</a> would fix for a fraction of the cost &mdash; we will say that instead.</p>",

faq('Measuring for Carpet: What Homeowners Ask Us', [
 ('How do I measure a room for carpet?',
  'Measure wall to wall at the longest and widest points, round up to the next foot, and measure through doorways to the middle of the door. Include every closet to its back wall. Multiply length by width for each space, add them up, then add about ten percent for waste and seams. That gives you a solid budgeting number — the exact quantity depends on how the 12-foot roll gets cut and seamed, which is what a professional measure settles.'),
 ('How much extra carpet should I add for waste?',
  'Around ten percent is the standard starting point. Add more for rooms wider than 12 feet, hallways with many doorways, oddly shaped rooms, and patterned carpet, which has to match at every seam. The waste is not padding on the bill — it is the geometry of cutting fixed-width, one-direction material to fit rooms that were not designed around a carpet roll.'),
 ('Why does my carpet quote show more square footage than my rooms measure?',
  'Because carpet comes off a 12-foot-wide roll and the pile must run the same direction everywhere. A 13-foot-wide room needs a second full-length strip for its last foot, and the offcuts are often too small or wrong-direction to reuse. The quote reflects the carpet that must be ordered, not the bare floor area. Ask to see the cut plan — a good estimator will happily walk you through it.'),
 ('Do closets count when measuring for carpet?',
  'Yes, every one of them, measured to the back wall. Forgotten closets are the single most common reason a homeowner’s own estimate comes in low. A bedroom with a walk-in closet can carry 30 or more square feet beyond its length-times-width, and a whole house of guessed closets can be off by a room’s worth of carpet.'),
 ('How are stairs measured for carpet?',
  'Per tread, not by square footage. Each step is measured for its tread depth, riser height and width, and priced as a unit of labor, because every stair is wrapped, stretched and secured individually. A quote that folds a staircase into the square-foot total is hiding the slowest part of the job, and that is where surprise charges tend to come from.'),
 ('Why are two carpet estimates for the same house so different?',
  'Usually roll math, not dishonesty. Two estimators can choose different roll directions and seam placements and arrive at genuinely different quantities of carpet for the same floor. The rest of the gap is inclusions — pad grade, tear-out, disposal, furniture moving, stairs priced per tread or buried. Compare the final number with every line named, not the square footage.'),
 ('Can I estimate from my home’s listed square footage?',
  'Only very roughly. Listing square footage includes spaces you will not carpet — kitchens, baths, garages in some counts — and excludes the waste that roll width imposes. It also says nothing about stairs, which are priced separately. It is fine for a first sanity check, but measure the actual rooms before you compare quotes or order anything.'),
 ('What happens at your free measure?',
  'We measure every room, closet and stair, plan the cuts and show you where seams will land, check the subfloor for issues worth pricing now rather than on install day, and bring the mobile showroom — twenty-plus full-size samples and all three pad grades — so you choose in your own light. You get a written price the same visit, and it is the price.'),
]),

cta('Skip the Tape Measure If You Want',
    'We measure every room, closet and stair, plan the seams in front of you, and leave a written price the same visit &mdash; with twenty-plus samples and all three pad grades along for the ride. Free in-home estimates across King &amp; Snohomish County.'),

related([
 ('/blog/carpet-installation-cost-seattle', 'What carpet installation costs in Seattle'),
 ('/blog/what-is-a-good-price-to-pay-for-carpet-in-seattle-wa', 'What a good carpet price looks like'),
 ('/blog/best-carpet-for-stairs', 'The best carpet for stairs'),
 ('/blog/carpet-removal-cost', 'What carpet removal costs'),
 ('/seattle/carpet-installation-in-seattle-wa', 'Carpet installation in Seattle'),
 ('/contact', 'Book a free measure'),
]),
]

assemble(S, parts)
