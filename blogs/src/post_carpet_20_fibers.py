from builder import *

S = 'carpet-fiber-types'

parts = [
date_badge('January 14, 2027'),

quick_answer(
 "<strong>Four fibers cover almost every carpet sold: nylon, polyester, triexta and wool.</strong> Nylon is the resilience benchmark &mdash; it springs back where feet actually land, "
 "which is why it earns its premium on stairs and hallways. Polyester is softer and cheaper and belongs in bedrooms, not traffic lanes. Triexta sits between them and shines in pet "
 "households. Wool is the beautiful, expensive outlier with real care requirements. Pick the fiber by the room, not by the sample that felt nicest in the store &mdash; and then put "
 "a proper pad under whichever one you choose.",
 'Every room, every budget'),

facts([
 ('4 fibers', 'do nearly all the work in residential carpet: nylon, polyester, triexta and wool. Everything else on the label &mdash; brand names, trademarks, &ldquo;proprietary&rdquo; yarns &mdash; is one of these four wearing a costume.'),
 ('From $1.49/sq ft', 'where installed carpet starts with us, pad and labor included. Fiber choice is the biggest material swing in the quote, which is why we would rather explain it at your kitchen table than on a price tag.'),
 ('20+ samples', 'ride along in the mobile showroom &mdash; multiple fibers in full-size pieces, plus all three pad grades, so you can compare spring-back and softness on your own floor in your own light.'),
]),

'<h2>The Four Fibers That Matter</h2>',

"<p>Carpet marketing works hard to make this complicated. Underneath every trademark and every &ldquo;revolutionary yarn system&rdquo; are four polymers, and they behave in "
"predictable, physical ways: how well the fiber springs back after being crushed, whether stains soak into it or sit on it, how it takes dye, and what it costs. Once you know those "
"four behaviors, you can walk past ninety percent of the sales talk and ask the only question that matters: <em>which fiber belongs in this particular room?</em></p>",

"<p>One distinction to hold onto before the table: <strong>wear and stains are different failures.</strong> A carpet that mats flat in the hallway has a resilience problem &mdash; "
"a wear problem. A carpet that holds a wine mark has a stain problem. Fibers that are excellent at one are often mediocre at the other, which is why the &ldquo;best&rdquo; fiber "
"depends entirely on which failure the room in question is most likely to see.</p>",

table('Carpet Fibers, Compared Honestly', ['Fiber', 'Where it wins', 'The honest trade-off'], [
 ('<strong>Nylon</strong>', 'Resilience &mdash; stairs, halls, family rooms', 'Costs more than polyester; conventional versions need stain treatment, solution-dyed versions cost more still'),
 ('<strong>Polyester (PET)</strong>', 'Softness and price &mdash; bedrooms, guest rooms', 'Mats under repeated traffic and does not spring back; wonderful underfoot, wrong for hallways'),
 ('<strong>Triexta</strong>', 'Pet households, busy family rooms', 'Stain resistance is built into the polymer; slightly springy feel divides opinion, resale name recognition still growing'),
 ('<strong>Wool</strong>', 'Look, feel, longevity in gentle rooms', 'Expensive, absorbs moisture, holds odor, and dislikes the aggressive cleaners busy households reach for'),
]),

'<h2>Nylon: the Workhorse</h2>',

"<p>Nylon&rsquo;s molecule has a useful kind of memory &mdash; crush it under a footstep and it wants to stand back up. That is resilience, and it is the property that decides how a "
"carpet looks in year six, long after softness and color have stopped being news. Hallways, stairs and the path from the couch to the kitchen are where carpet actually dies, and "
"they die by matting, not by staining. Nylon resists exactly that death, which is why we put it on <a href=\"/blog/best-carpet-for-stairs\">stairs</a> almost by default.</p>",

"<p>The caveat: nylon is naturally absorbent, so its stain resistance comes from either a factory treatment or &mdash; better &mdash; solution dyeing, where pigment is mixed into "
"the polymer before the fiber is extruded. Solution-dyed nylon can be scrubbed with strong cleaners for a decade without fading, which is why it co-headlines our "
"<a href=\"/blog/best-carpet-for-pets\">pet carpet guide</a>. Surface-dyed nylon is still a durable floor; it just asks you to treat spills promptly and clean a little more "
"gently.</p>",

'<h2>Polyester: Soft, Affordable, Honest About Its Limits</h2>',

"<p>Polyester&rsquo;s pitch is straightforward: it is the softest mainstream fiber per dollar, it takes color beautifully, and because the polymer itself does not absorb liquid "
"well, it resists most household stains without any treatment. In a bedroom &mdash; a room that sees bare feet, not boots &mdash; that combination is close to unbeatable, and it is "
"why our <a href=\"/blog/carpet-in-bedrooms\">bedroom carpet guide</a> leans polyester without apology.</p>",

"<p>Its weakness is the mirror of nylon&rsquo;s strength: crushed polyester tends to stay crushed. Run daily traffic over it and the lanes flatten and stay flat &mdash; a fiber "
"failure no cleaning can reverse, as we explain in <a href=\"/blog/how-long-does-carpet-last\">how long carpet lasts</a>. The practical rule is simple: polyester where people "
"lounge, nylon where people walk. And note that oil-based stains are polyester&rsquo;s particular enemy &mdash; the same chemistry that repels water-based spills attracts oily "
"ones, so the kitchen-adjacent family room deserves a different answer.</p>",

'<h2>Triexta: the Newcomer That Earned Its Place</h2>',

"<p>Triexta is the youngest of the four, a polymer related to polyester but engineered with better spring-back and with stain resistance built into the molecule itself rather than "
"sprayed on at the factory. Nothing to wear off, nothing to reapply &mdash; you can clean it aggressively for years, which is exactly the profile a house full of dogs and toddlers "
"needs. In pet households it is the benchmark we measure everything else against, alongside solution-dyed nylon.</p>",

"<p>Trade-offs are modest but real. Underfoot it has a slightly springy, dense feel that most people like and some do not &mdash; a thing you discover by standing on a sample, not "
"by reading about it. On pure resilience in brutal traffic, top-grade nylon still holds a narrow edge. And because the fiber is newer, the very cheapest triexta lines lean on the "
"polymer&rsquo;s reputation while skimping on density &mdash; construction quality still matters, whatever the label says. Our guide to "
"<a href=\"/blog/stain-resistant-carpet\">stain-resistant carpet</a> covers how these claims translate into daily life.</p>",

'<h2>Wool: Beautiful, Costly, Particular</h2>',

"<p>Wool is the fiber every synthetic is imitating, and in the right room nothing else feels or ages like it. It is naturally flame-resistant, insulating, and it hides soil "
"remarkably well between cleanings. It is also the most expensive mainstream option by a wide margin, it absorbs moisture and can hold odor, and it reacts badly to the aggressive "
"alkaline and oxygenating cleaners that busy households reach for &mdash; the wrong bottle can permanently discolor it. Homes managing allergies also tend to do better with "
"tight-constructed synthetics that stand up to frequent hot-water extraction, a topic we cover in <a href=\"/blog/carpet-and-allergies\">carpet and allergies</a>.</p>",

"<p>Our honest advice: wool belongs in adult spaces &mdash; a formal living room, a low-traffic primary suite &mdash; in households prepared to clean it on its own terms. It is a "
"luxury good that rewards owners who treat it like one. If that is not the season of life your house is in, a good solution-dyed nylon delivers most of the look for a fraction of "
"the care burden.</p>",

'<h2>Matching Fiber to Room, and to Budget</h2>',

"<p>Put the four together and a sensible house almost specs itself &mdash; and notice that it is rarely one fiber wall to wall. Mixing fibers by room is how you get a floor that "
"performs everywhere without paying the premium everywhere. Construction still matters alongside polymer &mdash; pile height and density change how any fiber wears, which is the "
"subject of <a href=\"/blog/low-pile-vs-high-pile-carpet\">low pile versus high pile</a> &mdash; and under every one of them, the pad is doing half the work of how the floor feels "
"and lasts.</p>",

two_col(
 'The spec we reach for most',
 ['Stairs &amp; hallways: nylon, densely constructed, mid pile or lower',
  'Bedrooms: polyester over a thick, soft pad &mdash; comfort where traffic is light',
  'Family rooms with pets or kids: triexta or solution-dyed nylon',
  'Formal, low-traffic rooms: wool if the budget and habits fit',
  'Rental units and flips: mid-grade polyester &mdash; value where turnover rules',
  'Everywhere: the pad grade named in writing, never &ldquo;standard&rdquo;'],
 'The mistakes we get called to fix',
 ['Polyester on a staircase &mdash; matted lanes inside three years',
  'Wool in the mudroom-adjacent hallway of a dog household',
  'Premium fiber over bargain pad &mdash; priorities exactly backwards',
  'Choosing by softness in the store instead of resilience in the room',
  'Trusting &ldquo;stain-proof&rdquo; to cover oil, dye and pet accidents',
  'Buying the same carpet for every room because it was simpler that day']),

"<p>This is also exactly why the mobile showroom exists. Fiber differences are physical &mdash; spring-back, softness, how a sample reads in your light next to your paint &mdash; "
"and none of that survives translation into a spec sheet. We bring twenty-plus full-size samples across these fibers to your door, along with all three pad grades, measure every "
"room and stair, and leave a written price the same visit. What that visit costs you is an hour; what it replaces is a guess. Details on the install side are on our "
"<a href=\"/seattle/carpet-installation-in-seattle-wa\">Seattle carpet installation page</a>, and the money side of the decision is in "
"<a href=\"/blog/carpet-installation-cost-seattle\">what carpet installation costs</a>.</p>",

faq('Carpet Fibers: What Homeowners Ask Us', [
 ('What is the best carpet fiber overall?',
  'There is no overall — there is best for the room. Nylon wins where feet concentrate: stairs, hallways, family rooms. Polyester wins bedrooms on softness and price. Triexta wins pet households with cleanability built into the polymer. Wool wins formal rooms for owners willing to care for it. A well-specced house usually mixes two or three of them.'),
 ('Is nylon really worth the premium over polyester?',
  'In traffic areas, yes. Nylon springs back after being crushed and polyester largely does not, and matting in the walking lanes is how most carpet actually dies. In a bedroom the premium buys you little, which is exactly where polyester is the smarter spend. Pay for resilience where feet go; pay for softness where they do not.'),
 ('What is triexta, and is it just fancy polyester?',
  'It is chemically related to polyester but engineered differently: better spring-back, and stain resistance built into the molecule rather than applied as a treatment that wears off. In practice it behaves like a middle point between polyester and nylon with best-in-class cleanability, which is why it anchors so many pet-focused lines.'),
 ('What does solution-dyed mean and why does it keep coming up?',
  'Conventional carpet is dyed after the fiber is made, so color sits on the surface and aggressive cleaning slowly removes it. Solution-dyed fiber has pigment mixed in before extrusion — the color goes all the way through, like a carrot rather than a radish. It survives a decade of enzyme cleaners and sun exposure far better, which matters most in pet homes and bright rooms.'),
 ('Is wool carpet practical in a family home?',
  'It can be, in the right rooms and with the right habits. Wool is beautiful, insulating and long-lived, but it absorbs moisture, can hold odor, and is damaged by the harsh cleaners most households use on accidents. We steer it toward formal and low-traffic rooms and steer active-pet households toward triexta or solution-dyed nylon instead.'),
 ('Does fiber matter more than pad?',
  'They fail differently, so you need both right. Fiber decides how the surface wears and cleans; pad decides how the floor feels and how fast the fibers crush. A premium fiber over the cheapest pad will still look old early. The pad is the cheaper of the two decisions, which makes upgrading it the best value line in the quote.'),
 ('Which fiber hides dirt and footprints best?',
  'Texture and color do more hiding than polymer, but fiber plays a part: wool masks soil naturally, and textured or twisted constructions in any fiber disguise footprints and vacuum tracks. Mid-tone flecked colors hide the most in every fiber. A smooth, pale, deep plush in any polymer is a full-time housekeeping commitment.'),
 ('How do I actually compare fibers before buying?',
  'Stand on them, in your house. Press a thumb into the pile and watch it recover; that is the resilience difference between polyester and nylon made visible. We bring twenty-plus full-size samples across these fibers to your home with all three pad grades, so the comparison happens on your floor in your light — and the written price arrives the same visit.'),
]),

cta('Compare the Fibers on Your Own Floor',
    'Nylon, polyester, triexta — full-size samples of each come to your door with all three pad grades. Press, compare, and see the colors in your own light. We measure while you decide and leave a written price the same visit. Free in-home estimates across King &amp; Snohomish County.'),

related([
 ('/blog/best-carpet-for-pets', 'The best carpet for homes with pets'),
 ('/blog/stain-resistant-carpet', 'How stain-resistant carpet really works'),
 ('/blog/low-pile-vs-high-pile-carpet', 'Low pile vs high pile'),
 ('/blog/carpet-in-bedrooms', 'The case for carpet in bedrooms'),
 ('/seattle/carpet-installation-in-seattle-wa', 'Carpet installation in Seattle'),
 ('/contact', 'Book a free estimate'),
]),
]

assemble(S, parts)
