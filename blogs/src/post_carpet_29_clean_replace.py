from builder import *

S = 'clean-or-replace-carpet'

parts = [
date_badge('March 18, 2027'),

quick_answer(
 "<strong>If the problem is dirt, clean it &mdash; a professional hot-water extraction costs a small fraction of new carpet and fixes what soap can fix. If the fibers are crushed flat "
 "and no longer spring back, or the pad underneath has quit, no cleaning on earth brings that carpet back.</strong> The honest move is to run the cheap test first: get the carpet "
 "properly cleaned once, then watch it for a month. What it does next tells you exactly which problem you have &mdash; and we would rather you spend that little bit first than buy new "
 "carpet a year early or nurse a dead one for five more.",
 'Cottage Lake &amp; Woodinville area'),

facts([
 ('One cleaning', 'is the cheapest diagnostic in flooring. A proper hot-water extraction either fixes the carpet or proves it cannot be fixed &mdash; and either way you learn the truth before spending real money.'),
 ('From $1.49/sq ft', 'where installed carpet starts with us if the answer turns out to be replace &mdash; material, pad and labor. Knowing that number keeps the clean-vs-replace math honest in both directions.'),
 ('Same visit', 'is when you get our written price. Free measure of every room, closet and stair, twenty-plus samples on your own floor, and a number you can hold the cleaning quote against.'),
]),

'<h2>Three Different Problems That All Get Called &ldquo;Old Carpet&rdquo;</h2>',

"<p>When someone in Cottage Lake calls us and says the carpet looks terrible, it is almost always one of three things, and they have opposite answers. <strong>Dirt</strong> is soil, "
"oils and tracked-in grit sitting in the fiber &mdash; ugly, sometimes smelly, and completely recoverable. <strong>Matting</strong> is mechanical wear: the fibers themselves have been "
"crushed and untwisted by years of footsteps until they lie flat and scatter light differently, which reads as a permanent grey path even when the carpet is clinically clean. "
"<strong>Pad failure</strong> is the one nobody diagnoses from above &mdash; the cushion under the carpet has collapsed or soaked up years of accidents, so the floor feels hard and "
"thin and odors keep coming back from below.</p>",

"<p>Cleaning fixes the first, does nothing for the second, and can actually make the third more obvious. So before any money moves, the job is telling them apart &mdash; and you can "
"do most of that yourself in ten minutes.</p>",

table('What You See vs What It Actually Means', ['Symptom', 'Most likely culprit', 'Clean or replace?'], [
 ('<strong>Grey traffic lanes, fibers still springy</strong>', 'Ground-in soil and grit', 'Clean &mdash; this is what extraction is for'),
 ('<strong>Flat, shiny lanes that stay flat after vacuuming</strong>', 'Matting &mdash; the fiber is worn, not dirty', 'Replace; no cleaner restores crushed pile'),
 ('<strong>Stains that vanish, then reappear days later</strong>', 'Wicking from residue deep in pad', 'Clean properly first; recurring = pad is holding it'),
 ('<strong>Odor that returns on humid days</strong>', 'Accidents that reached pad or subfloor', 'Replace carpet and pad; treat the subfloor'),
 ('<strong>Floor feels hard, thin, "bottomed out"</strong>', 'Pad has collapsed', 'Replace &mdash; carpet may look fine but the assembly is done'),
 ('<strong>Ripples and waves across the room</strong>', 'Lost stretch, not wear', 'Neither &mdash; restretch it and keep it'),
 ('<strong>Fraying seams, backing showing at edges</strong>', 'Structural end of life', 'Replace; the carpet is coming apart'),
 ('<strong>It just looks dingy everywhere</strong>', 'Usually dirt &mdash; honest answer needs the test below', 'Clean first, judge in a month'),
]),

'<h2>The Hot-Water-Extraction Test</h2>',

"<p>Here is the procedure we genuinely recommend, even though we sell carpet: before you spend four figures on a new floor, spend a little on one professional hot-water extraction "
"&mdash; the truck-mounted kind, not a rental machine &mdash; and then just live on the carpet for a month. The outcome is your answer.</p>",

"<p><strong>It looks great and stays great:</strong> it was dirt. You just saved the cost of a new floor; put a doormat program in place and vacuum the lanes twice a week. "
"<strong>It looks great for two weeks, then the lanes grey out again:</strong> the fibers are worn and scattering light, or residue is wicking up from a saturated pad. Cleaning "
"cannot outrun either one. <strong>Nothing visibly changes:</strong> that is matting &mdash; the pile is crushed, and the greyness you see is geometry, not grime. "
"<strong>It smells fine for a week and then the odor comes back:</strong> the smell was never in the carpet; it is in the pad or the subfloor, and the fix is replacement plus "
"sealing the wood underneath. We wrote up the full end-of-life checklist in <a href=\"/blog/when-to-replace-carpet\">when to replace carpet</a>, and the short list of "
"<a href=\"/blog/6-reasons-to-replace-carpet-flooring\">reasons to replace</a> covers the same ground from the other side.</p>",

'<h2>Matting Is Wear, Not Dirt &mdash; and Cleaning Cannot Fix Geometry</h2>',

"<p>This is the one that costs homeowners the most wasted cleaning money, so it deserves its own explanation. Carpet fiber is twisted yarn, and the twist is what makes it stand up "
"and bounce back. Years of footsteps in the same path untwist and flatten it. A flattened fiber reflects light off its side instead of its tip, which is why a matted lane looks grey "
"and dirty even when a lab would call it clean. People clean it, see no change, clean it again with a stronger chemical, and conclude the cleaner failed. The cleaner did not fail "
"&mdash; the fiber is simply worn out, the same way a tire with no tread is worn out no matter how well you wash it.</p>",

"<p>Run your hand across the suspect lane: springy fibers that stand back up are dirty carpet; flat, hard, slightly shiny pile that stays down is matted carpet. How fast a carpet "
"gets there depends mostly on fiber and pad quality &mdash; the honest lifespan numbers are in <a href=\"/blog/how-long-does-carpet-last\">how long carpet lasts</a> &mdash; and a "
"matted hallway at year eight is not a defect, it is a floor that finished its shift.</p>",

'<h2>When the Pad Is What Actually Died</h2>',

"<p>The pad is the part of the floor you cannot see and the part that fails first in a lot of homes. Walk the room in socks: if high-traffic areas feel noticeably harder and thinner "
"than the strip under the couch, the cushion has collapsed there, and every footstep is now grinding the carpet backing directly against the subfloor &mdash; which finishes off the "
"carpet fast. The other pad failure is saturation. Pet accidents and spills go through carpet in seconds and get held by the pad, which is why a cleaned carpet can smell fine until "
"the first muggy week of summer. A carpet over a dead or saturated pad is not salvageable as an assembly, even when the face yarn still looks presentable. When we replace in that "
"situation, the old pad and tack strip come out, the subfloor gets checked and treated, and the new pad grade gets chosen deliberately &mdash; "
"<a href=\"/blog/carpet-padding-thickness\">the pad decision</a> is most of what decides how long round two lasts.</p>",

'<h2>Ripples Are Neither: Do Not Replace a Loose Carpet</h2>',

"<p>One more honest off-ramp. If your complaint is waves, ripples, or a carpet that has visibly gone loose &mdash; especially in a wide room or across a doorway &mdash; the carpet "
"is probably fine. It has lost its stretch, either because it was knee-kicked instead of power-stretched on day one or because a decade of traffic and furniture drags worked it "
"loose. Restretching is a fraction of the cost of replacement and buys years; the numbers are in <a href=\"/blog/carpet-stretching-cost\">what carpet stretching costs</a>. We see "
"rippled six-year-old carpet replaced every month somewhere, and it is usually a waste of a decent floor.</p>",

two_col(
 'Clean it &mdash; and keep your money &mdash; when',
 ['Fibers in the bad areas still spring back under your hand',
  'The problem is spots, spills or overall dinginess, not paths',
  'Odors are surface-level and fade after airing out',
  'The floor still feels cushioned everywhere underfoot',
  'The carpet is under 7&ndash;8 years old with decent pad',
  'It has never actually had a professional extraction'],
 'Replace it &mdash; and stop paying to clean it &mdash; when',
 ['Traffic lanes are flat and shiny and stay flat after vacuuming',
  'Stains or odors keep returning after proper cleaning',
  'High-traffic areas feel hard and thin &mdash; the pad is gone',
  'Pet accidents have soaked through repeatedly over the years',
  'Seams are fraying or the backing is delaminating',
  'You have cleaned it twice in a year and hated it both times']),

'<h2>The Honest Math, Cottage Lake Edition</h2>',

"<p>A truck-mounted cleaning for a typical home costs a small fraction of what new carpet does, which is exactly why it makes sense as a first move &mdash; and exactly why serial "
"cleaning of a dead carpet is such a bad deal. Two cleanings a year on a matted, bottomed-out floor is real money spent making no progress, on a carpet that a buyer or an appraiser "
"will still read as worn out. When the extraction test says replace, replacement here is not exotic: installed carpet starts at $1.49 per square foot with us, the mobile showroom "
"brings twenty-plus samples and all three pad grades to your door, and most homes install in a day. We measure every room and stair and leave a written price the same visit, so you "
"can hold the real number against the cleaning quote instead of guessing. Details for the neighborhood are on our "
"<a href=\"/city-of-cottage-lake/carpet-installation-in-cottage-lake-wa\">Cottage Lake carpet installation page</a>.</p>",

faq('Clean or Replace: What Homeowners Ask Us', [
 ('Should I clean my carpet before deciding to replace it?',
  'Almost always yes. One professional hot-water extraction is the cheapest diagnostic there is: if the carpet recovers and stays recovered, it was dirt and you just saved a four-figure purchase. If the lanes grey out again in two weeks, or nothing changes at all, you have your answer with evidence — and you go into the replacement knowing it was actually necessary.'),
 ('Why does my carpet still look dirty right after cleaning?',
  'Because it is probably not dirty — it is matted. Crushed, untwisted fibers reflect light off their sides instead of their tips, which reads as grey no matter how clean the yarn is. Run your hand over the lane: pile that stays flat is worn out. Cleaning cannot restore fiber geometry, and a second, harsher cleaning will not either.'),
 ('Why do stains keep coming back in the same spot?',
  'That is wicking. The spill soaked into the pad, and each cleaning pulls a little more of the residue up to the surface as it dries. A proper extraction with the right technique can beat mild cases, but a pad that has absorbed years of spills is a reservoir — and the only fix for a reservoir is removing it, which means new pad and usually new carpet.'),
 ('The smell returns every time it gets humid. Can cleaning fix that?',
  'No. Odor that cycles with humidity lives in the pad or the subfloor, not the carpet face, and surface cleaning never touches it. The fix is pulling the carpet and pad, treating or sealing the subfloor where accidents reached it, and installing new pad — ideally a moisture-barrier grade if pets are staying. It is the one symptom where we skip the cleaning advice entirely.'),
 ('My carpet is rippled and loose. Does that mean it is worn out?',
  'Usually not. Ripples mean the carpet lost its stretch — a power-stretching problem, not a wear problem — and restretching fixes it for a fraction of replacement cost. A carpet can be rippled at six years old and have half its life left. Replace for ripples only if the carpet also fails the matting and pad checks.'),
 ('How do I know if the pad has failed?',
  'Walk the room in socks and compare: if the traffic areas feel hard and thin while the protected strip under furniture still feels cushioned, the pad has collapsed where it matters. A bottomed-out pad grinds the carpet backing against the subfloor with every step, so the carpet itself is on borrowed time even if it looks acceptable from above.'),
 ('Is it worth replacing carpet that is only eight years old?',
  'Age is not the test — condition is. An eight-year-old carpet on a quality pad in a gentle household can be worth cleaning and keeping for years. An eight-year-old builder-grade carpet on the thinnest pad, in a house with kids and a dog, is often genuinely finished. The extraction test and the hand-on-the-pile check tell you which one you own.'),
 ('If the answer is replace, what does new carpet actually cost?',
  'Installed carpet starts at $1.49 per square foot with us — material, pad and labor together. We bring twenty-plus full-size samples and all three pad grades to your home, measure every room, closet and stair, and leave a written price the same visit, so the comparison against another year of cleanings is concrete instead of hypothetical. Most homes install in a day.'),
]),

cta('Get an Honest Answer Before You Spend Either Way',
    'We will tell you to clean it if cleaning will work — and show you exactly why if it will not. Twenty-plus samples, all three pad grades, a free measure and a written price the same visit, so the clean-or-replace math is real. Serving Cottage Lake and all of King &amp; Snohomish County.'),

related([
 ('/blog/when-to-replace-carpet', 'When to replace carpet'),
 ('/blog/how-long-does-carpet-last', 'How long carpet lasts'),
 ('/blog/carpet-stretching-cost', 'What carpet stretching costs'),
 ('/blog/carpet-padding-thickness', 'Choosing carpet pad'),
 ('/blog/6-reasons-to-replace-carpet-flooring', 'Six reasons to replace carpet'),
 ('/city-of-cottage-lake/carpet-installation-in-cottage-lake-wa', 'Carpet installation in Cottage Lake'),
 ('/contact', 'Book a free estimate'),
]),
]

assemble(S, parts)
