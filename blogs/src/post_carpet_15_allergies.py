from builder import *

S = 'carpet-and-allergies'

parts = [
date_badge('December 10, 2026'),

quick_answer(
 "<strong>Carpet is not automatically the enemy of allergies &mdash; old, neglected carpet is.</strong> A dense, low-pile carpet that gets vacuumed with a sealed HEPA "
 "machine and professionally hot-water extracted on schedule holds dust down at floor level instead of letting every footstep launch it. That said, we install both "
 "carpet and hard flooring, so we will also tell you the honest other half: for severe dust-mite allergies and asthma, bare floors you can damp-mop still win. Here "
 "is what actually helps, what is marketing, and how to tell which household you are.",
 'Lynnwood homes &amp; ramblers'),

facts([
 ('Low &amp; dense', 'the allergy-friendly spec in two words. A short, tightly packed pile gives dust, dander and pollen less room to burrow, releases more of it to the vacuum, and dries fast after cleaning. Deep plush is the wrong tool for this job.'),
 ('12&ndash;18 months', 'the professional hot-water extraction cadence we recommend &mdash; sooner in allergy households. It is the deep reset a vacuum cannot do, and most carpet warranties quietly require it anyway.'),
 ('From $1.49/sq ft', 'installed carpet with us, pad and labor included. Replacing a fifteen-year-old carpet that no cleaning can save is often the single biggest air-quality upgrade in the house.'),
]),

'<h2>Where the "Carpet Is Bad for Allergies" Idea Comes From</h2>',

"<p>The core fact is true: carpet holds dust. Fibers catch dander, pollen, dust-mite debris and everything the door lets in, and a hard floor holds almost none of it. "
"The leap people make from there &mdash; carpet must therefore be worse for the allergic &mdash; is where it gets messier, because held dust is not the same thing as "
"breathed dust. On a hard floor, the same particles sit loose on the surface, and every footstep, air vent and closing door puts them back into the air at nose height. "
"Carpet acts more like a filter: it grabs particles and keeps them at floor level until something removes them.</p>",

"<p>The catch &mdash; and this is the honest hinge of the whole article &mdash; is that a filter only works if it gets emptied. Vacuumed regularly with a machine that "
"actually contains what it collects, and deep-cleaned on schedule, carpet keeps allergens out of the breathing zone remarkably well. Neglected, it becomes exactly what "
"the myth says: a reservoir that re-releases a little of its collection with every step. So the real question is not carpet versus no carpet. It is whether the carpet "
"in question is the right construction, and whether it will actually be maintained.</p>",

'<h2>The Spec That Helps: Short, Tight, Synthetic</h2>',

"<p>If allergies are in the household, the carpet aisle sorts itself fast. You want a <strong>low pile</strong> &mdash; short fibers hold less, release more to the "
"vacuum, and dry quickly after cleaning, which matters because damp carpet is what dust mites and mildew actually want. You want it <strong>dense</strong>, with "
"fibers packed tightly enough that debris stays up near the surface where the vacuum can reach it instead of sifting to the backing. We walk through the trade-offs in "
"<a href=\"/blog/low-pile-vs-high-pile-carpet\">low pile versus high pile</a>, and allergy households are the clearest case that guide has: short wins. You want a "
"<strong>solution-dyed synthetic</strong> fiber &mdash; nylon or triexta &mdash; that shrugs off the aggressive, frequent cleaning this plan requires. And the "
"<strong>pad</strong> underneath should be a quality pad with a moisture barrier, fresh, never reused from the old floor; "
"<a href=\"/blog/carpet-padding-thickness\">the padding guide</a> explains why the old pad is non-negotiable to us: it holds fifteen years of exactly what you are "
"trying to get out of the house.</p>",

table('The Allergy-Conscious Carpet Spec', ['Decision', 'Choose', 'Why it matters'], [
 ('<strong>Pile height</strong>', 'Low', 'Less depth for allergens to hide in, better vacuum extraction, faster drying after cleaning'),
 ('<strong>Density</strong>', 'High &mdash; tight and firm', 'Keeps debris near the surface where the vacuum reaches instead of down at the backing'),
 ('<strong>Fiber</strong>', 'Solution-dyed nylon or triexta', 'Survives frequent hot-water extraction and strong cleaning without fading or matting'),
 ('<strong>Style</strong>', 'Cut pile, textured', 'Simple surfaces clean predictably; avoid deep plush and shag categorically'),
 ('<strong>Pad</strong>', 'Quality, moisture-barrier, always new', 'The old pad is a fifteen-year archive of dust and dander &mdash; it leaves with the old carpet'),
 ('<strong>Installation</strong>', 'Power-stretched, sealed seams', 'Tight carpet wears evenly and vacuums cleanly; a proper install is part of the health story'),
 ('<strong>Rooms</strong>', 'Bedrooms and living areas &mdash; not damp ones', 'Skip carpet in bathrooms, laundry and any basement with moisture history'),
]),

'<h2>The Vacuum Matters More Than the Carpet</h2>',

"<p>Here is the part no carpet label will tell you: the machine matters as much as the floor. A cheap vacuum with leaky seals inhales dust at the floor and exhales the "
"finest fraction of it at chest height &mdash; you can smell it working, which is exactly the problem. The allergy-household spec is a <strong>sealed-body vacuum with "
"a HEPA filter</strong>, meaning the air that comes out actually went through the filter. Use it slowly &mdash; the beater bar needs time to lift pile and the airflow "
"needs time to pull &mdash; twice a week in the rooms that get lived in, once a week everywhere else. Empty it outside. That is the whole regimen, and it does more "
"for the air in the house than the choice between two decent carpets ever will.</p>",

'<h2>Hot-Water Extraction: The Deep Reset</h2>',

"<p>Vacuuming manages the surface; it cannot reach what settles into the base of the pile over months. That is what professional hot-water extraction is for &mdash; "
"hot water and extraction pressure flush the pile down to the backing and pull the water, and the accumulated load, back out. Every 12&ndash;18 months is the standard "
"cadence, yearly in an allergy household, and it is worth doing right: the machine matters here too, because water left behind is its own problem. A properly "
"extracted carpet is dry to the touch the same day. Skip the rental-machine shampooers that soak the pad &mdash; a soaked pad in a Pacific Northwest winter takes days "
"to dry, and damp is the one condition that makes carpet genuinely worse for allergies instead of better.</p>",

'<h2>When Hard Floors Genuinely Win</h2>',

"<p>We sell carpet, and this section stays in the article anyway. If someone in the house has <strong>severe dust-mite allergy or dust-driven asthma</strong> &mdash; "
"the kind managed with medication and an allergist rather than a spring sneeze &mdash; most allergists will tell you to remove the carpet from at least the bedroom, "
"and they are right. Mites live where skin flakes and warmth and humidity meet, and a mattress plus carpet is their whole habitat; a bare floor you can damp-mop, "
"plus washable rugs, takes the floor half of that habitat away entirely. The same logic applies to <strong>damp rooms</strong> &mdash; below-grade basements with "
"moisture history, bathrooms, laundry &mdash; where carpet holds humidity against the slab. And in heavy-shedding pet households where dander is the trigger, hard "
"floors with washable rugs are simply easier to keep truly clean; we compare the options honestly in "
"<a href=\"/blog/pet-friendly-allergy-friendly-flooring-seattle\">allergy-friendly flooring for Seattle homes</a> and "
"<a href=\"/blog/what-is-the-best-flooring-for-kids-pets\">the best flooring for kids and pets</a>.</p>",

"<p>For everyone else &mdash; the seasonal sneezers, the mild-to-moderate households, the families who want warm quiet bedrooms without a health debate &mdash; the "
"evidence does not support ripping out carpet on principle. It supports choosing the right carpet, maintaining it like you mean it, and putting it in the right rooms. "
"The <a href=\"/blog/carpet-vs-hardwood-room-by-room\">room-by-room comparison</a> is how we usually frame that decision at the kitchen table.</p>",

two_col(
 'What actually moves the needle',
 ['Dense, low-pile carpet in a solution-dyed synthetic fiber',
  'A sealed HEPA vacuum, used slowly, twice a week',
  'Professional hot-water extraction every 12&ndash;18 months',
  'A new moisture-barrier pad &mdash; never reusing the old one',
  'Shoes off at the door; entry mats that get washed',
  'Replacing carpet that is past cleaning &mdash; age is the real enemy'],
 'What is mostly marketing or myth',
 ['"Hypoallergenic carpet" as a label &mdash; construction and upkeep do the work',
  '"Carpet is always worse for allergies" &mdash; not what the research shows for maintained carpet',
  'Anti-allergen sprays as a substitute for extraction',
  'Rental shampooers that soak the pad and call it clean',
  'Blaming fiber choice when the vacuum leaks dust at chest height',
  'Keeping the old pad because "it still looks fine"']),

'<h2>The Lynnwood Angle: Old Carpet Is the Real Culprit</h2>',

"<p>A lot of what we replace in Lynnwood is original or near-original carpet in the 1960s and 70s ramblers and split-levels between Highway 99 and the interurban "
"&mdash; carpet that has been collecting since a previous owner's dog, faithfully vacuumed but decades past what any cleaning can reset. When a household's allergies "
"improve after we recarpet, it is rarely because the new fiber is magic; it is because twenty years of accumulation left the house in a trailer, old pad included. If "
"your carpet is of that vintage, <a href=\"/blog/how-long-does-carpet-last\">how long carpet lasts</a> will help you date it honestly. When it is time, the mobile "
"showroom brings twenty-plus samples and all three pad grades to your door &mdash; dense low-pile options flagged, in your own light &mdash; with a measure and a "
"written price the same visit. Details on the <a href=\"/city-of-lynnwood/carpet-installation-in-lynnwood-wa\">Lynnwood carpet installation page</a>.</p>",

faq('Carpet and Allergies: What Homeowners Ask Us', [
 ('Is carpet bad for allergies?',
  'Not automatically. Carpet holds dust rather than letting it recirculate — which is a benefit when the carpet is vacuumed with a sealed HEPA machine and deep-cleaned on schedule, and a liability when it is not. For mild and moderate allergies, a dense low-pile carpet that is actually maintained is a defensible, comfortable choice. For severe dust-mite allergy or asthma, bare floors win, and we say so.'),
 ('What kind of carpet is best for allergy sufferers?',
  'Dense, low-pile, cut-pile carpet in a solution-dyed synthetic like nylon or triexta, over a new moisture-barrier pad. Short tight pile holds less, releases more to the vacuum, and dries fast after cleaning; solution-dyed fiber tolerates the frequent aggressive cleaning an allergy household should be doing. Deep plush and shag are the wrong direction entirely.'),
 ('Does old carpet make allergies worse?',
  'This is the strongest carpet-allergy link there is. A carpet near the end of its life has accumulated more than any cleaning can extract, and the original pad under it has been absorbing dust, dander and moisture the whole time. If symptoms track with a carpet that is fifteen-plus years old, replacement — carpet and pad together — does more than any cleaning regimen can.'),
 ('Do I need a special vacuum for allergies?',
  'You need a sealed-body vacuum with a HEPA filter — the sealed part matters as much as the filter, because a leaky machine exhausts fine dust back into the room at chest height. Vacuum slowly, twice a week in busy rooms, and empty it outdoors. The vacuum is the most underrated variable in this whole subject.'),
 ('How often should carpet be professionally cleaned in an allergy household?',
  'Hot-water extraction every 12 to 18 months as a baseline, yearly if allergies are active. It flushes the base of the pile where vacuums cannot reach. Done properly the carpet is dry the same day — avoid methods that soak the pad, because lingering damp is the one condition that genuinely turns carpet against you.'),
 ('Should allergy sufferers remove carpet from the bedroom?',
  'If the diagnosis is significant dust-mite allergy or dust-triggered asthma, yes — that is allergist-standard advice and we will not argue with it: a damp-moppable floor plus washable rugs removes the floor half of the mite habitat. For milder seasonal allergies, a low-pile carpet with the full maintenance regimen is usually fine, and the bedroom warmth and quiet are real benefits too.'),
 ('Is "hypoallergenic carpet" a real thing?',
  'It is a label, not a standard. What actually reduces allergen load is construction — density, pile height, fiber — plus pad choice and maintenance. A well-specced ordinary carpet that gets vacuumed and extracted beats a "hypoallergenic" plush that does not. Buy the spec, not the sticker.'),
 ('Does replacing carpet help with allergies?',
  'When the existing carpet is old, frequently — replacement removes the accumulated load a tired carpet holds, and the old pad with it. We install from $1.49 per square foot including a fresh pad, and the tear-out and haul-away take the whole archive out of the house in a day. If your carpet is only a few years old, invest in the vacuum and the extraction first.'),
]),

cta('Breathe Easier About the Decision, at Least',
    'We install carpet and hard floors both, so you get a straight answer about which your household needs &mdash; including "keep the carpet, fix the vacuum." Twenty-plus samples and all three pad grades come to your Lynnwood home, with a measure and a written price the same visit. Free estimates across King &amp; Snohomish County.'),

related([
 ('/blog/pet-friendly-allergy-friendly-flooring-seattle', 'Allergy-friendly flooring options'),
 ('/blog/low-pile-vs-high-pile-carpet', 'Low pile vs high pile carpet'),
 ('/blog/carpet-padding-thickness', 'Carpet padding, explained'),
 ('/blog/carpet-vs-hardwood-room-by-room', 'Carpet or hardwood, room by room'),
 ('/city-of-lynnwood/carpet-installation-in-lynnwood-wa', 'Carpet installation in Lynnwood'),
 ('/contact', 'Book a free estimate'),
]),
]

assemble(S, parts)
