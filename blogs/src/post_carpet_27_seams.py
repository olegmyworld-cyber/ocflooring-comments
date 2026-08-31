from builder import *

S = 'why-carpet-seams-show'

parts = [
date_badge('March 4, 2027'),

quick_answer(
 "<strong>Every wall-to-wall carpet wider than the roll has seams &mdash; the question is never whether they exist, only whether you notice them.</strong> "
 "Carpet ships on rolls, most commonly 12 feet wide, so any room wider than that gets pieced. Whether a seam shows depends on three things: where "
 "the light rakes across it, which way the pile leans on each side, and where the seam sits relative to traffic. A good installer plans all three "
 "on paper before cutting anything &mdash; and a faint seam line at certain angles is normal even on a flawless job. Fraying, gaps, or a hard ridge "
 "underfoot are not.",
 'Newcastle &amp; Eastside homes'),

facts([
 ('12 feet', 'the standard carpet roll width (some styles come 13&#8217;6&#8221; or 15&#8217;). Any room wider than the roll gets a seam &mdash; physics, not workmanship.'),
 ('3 factors', 'decide whether a seam shows: light angle, pile direction, and placement in traffic. A good seam map controls all three before the first cut.'),
 ('From $1.49/sq ft', 'installed carpet with us &mdash; measured room by room with a seam plan we will show you, and a written price the same visit.'),
]),

'<h2>Seams Are Physics, Not Failure</h2>',

"<p>Start with the fact the showroom rarely mentions: carpet is a textile that comes off a roll, and the roll has a width. Most residential broadloom "
"is 12 feet wide; a minority of styles come in 13&#8217;6&#8221; or 15&#8217;. Your living room is probably wider than that, and your L-shaped hallway "
"certainly does not match a rectangle of any width. So the carpet gets cut and joined &mdash; two pieces, their edges seam-sealed and bonded to a heat-activated "
"tape, pressed together into one continuous floor.</p>",

"<p>Done well, that joint is tight, flat, and permanent. But it is still two pieces of textile meeting, and under the wrong light it can read as a faint "
"line &mdash; the way a well-hung wallpaper seam is invisible at noon and visible at sunset. Understanding that baseline is the difference between a "
"homeowner who calls a normal seam a defect and one who can spot the real defects when they happen. Roll width is also why the piecing plan is decided by "
"the measure, not the install day &mdash; the whole logic is in <a href=\"/blog/how-to-measure-for-carpet\">how to measure for carpet</a>, and it is a big "
"part of why two quotes on the same room can carry different yardage, which we unpack in <a href=\"/blog/wall-to-wall-carpet-cost\">what wall-to-wall "
"carpet costs</a>.</p>",

'<h2>Why a Seam Shows: Light, Pile, and Traffic</h2>',

"<p><strong>Light angle is the biggest one.</strong> A seam that is invisible under evening lamps can appear at 8 a.m. when low sun rakes across the floor "
"from a picture window. Light traveling <em>along</em> a seam hides it; light crossing it at a low angle throws a shadow off every fiber that sits a "
"hair proud of its neighbor. This is why the worst place for a seam is perpendicular to a big window, and why a seam you never noticed in July can "
"introduce itself in January when the sun drops lower.</p>",

"<p><strong>Pile direction is the sneaky one.</strong> Carpet pile leans the way it came off the machine, and it reflects light differently with the lean "
"than against it &mdash; the same effect as vacuum tracks. If two pieces meet with their pile leaning different directions, the two sides read as "
"different shades even when the joint itself is perfect, and no amount of seam technique fixes it. Every piece in a room must run the same direction, "
"which costs yardage &mdash; and is exactly the corner a cheap quote cuts.</p>",

"<p><strong>Traffic finishes the job.</strong> A seam in a walkway gets crushed and abraded faster than the field around it, so it ages on its own "
"schedule and becomes more visible every year. Seams also show more on some products than others: dense low pile with sheen telegraphs everything, "
"while textured cut piles hide joints well &mdash; one more trade-off in the "
"<a href=\"/blog/berber-vs-plush-carpet\">berber versus plush</a> conversation, since looped berber seams are genuinely difficult and patterned styles "
"add match repeats on top.</p>",

table('What Makes a Seam More or Less Visible', ['Factor', 'Hides the seam', 'Shows the seam'], [
 ('<strong>Light</strong>', 'Seam runs toward the main window, parallel to the light', 'Low raking light crossing the seam at 90&deg;'),
 ('<strong>Pile direction</strong>', 'All pieces leaning the same way', 'Pieces reversed &mdash; two shades of the same carpet, permanently'),
 ('<strong>Placement</strong>', 'Under furniture, along walls, out of walkways', 'Across a doorway or down the middle of a traffic lane'),
 ('<strong>Carpet style</strong>', 'Textured or twisted cut pile, mid height, some fleck', 'Dense low pile, high sheen, tight loops, big pattern repeats'),
 ('<strong>Pad &amp; stretch</strong>', 'Firm pad, power-stretched drum-tight', 'Soft thick pad flexing the joint; loose carpet peaking at the seam'),
 ('<strong>Age</strong>', 'Seams relax and blend over the first weeks', 'Traffic wear concentrating on a badly placed joint for years'),
]),

'<h2>How a Good Installer Plans a Seam Map</h2>',

"<p>On a professional job, the seams are decided at the measure, drawn on a diagram, and priced honestly &mdash; before anyone orders carpet. The logic "
"runs in order: point the pile the same direction everywhere; put seams parallel to the dominant light source where possible; keep them out of doorways, "
"pivot points, and the main walking lines; and prefer a longer seam along a quiet wall to a short one across a busy path. Then the map gets checked "
"against the roll: sometimes buying an extra half-yard moves a seam from the worst spot in the room to a place you will never look.</p>",

"<p>Execution matters as much as the map. Cut edges get seam-sealed so they cannot fray, the joint is bonded on seaming tape with the right heat, and the "
"whole floor is power-stretched afterward &mdash; a drum-tight carpet holds its seams flat, while a loose one lets them peak into little ridges. The pad "
"underneath has a vote too: a firm pad supports the joint, a mushy one flexes it with every step, which is one more reason "
"<a href=\"/blog/carpet-padding-thickness\">pad thickness and grade</a> is a performance decision rather than a comfort upgrade. When you compare "
"installers, ask to see the seam diagram &mdash; the ones who plan it will show you happily, and the checklist in "
"<a href=\"/blog/hiring-a-carpet-installer-seattle\">hiring a carpet installer</a> covers the rest of that conversation.</p>",

'<h2>Normal Seam vs. Defect: An Honest Line</h2>',

"<p>Here is the standard we hold our own work to. A <strong>normal seam</strong> on a quality installation: you can find it if you know where to look, "
"it may read as a faint line under low raking light or right after vacuuming, and it is flat underfoot with no gap and no fray. Industry standards "
"say exactly this &mdash; seams are not invisible, they are <em>minimized</em>. If your installer placed it sensibly and the pile runs one direction, "
"a faint line at 8 a.m. in January is the material behaving like a textile, and the polite truth is that nobody who does not clean your carpets will "
"ever find it.</p>",

"<p>A <strong>defective seam</strong> is different in kind, not degree: a visible gap between the two pieces; edges fraying or sprouting tufts; a hard "
"ridge you can feel through socks (peaking that never relaxes); the two sides reading as different colors because the pile was reversed; or a seam "
"placed straight across a doorway when the diagram had room to avoid it. Those are workmanship problems, they do not improve with time, and a "
"professional installer fixes them without being argued into it.</p>",

two_col(
 'Normal &mdash; even on excellent work',
 ['A faint line visible under low, raking light at certain hours',
  'A seam you can find by touch when you kneel and look for it',
  'Slight shading difference right after installation that relaxes in weeks',
  'Seams present in any room wider than the roll &mdash; usually 12 feet',
  'More visible joints on low, dense, shiny, or looped products',
  'A seam placed under furniture or along a quiet wall by design'],
 'Defect &mdash; call your installer',
 ['A gap you can see daylight through, or edges pulling apart',
  'Fraying, sprouting tufts, or backing visible at the joint',
  'A hard ridge underfoot that has not relaxed after several weeks',
  'Two sides reading as different shades &mdash; pile direction reversed',
  'A seam across a doorway or main walkway the plan could have avoided',
  'Seams opening after stretching &mdash; or a floor that was never power-stretched']),

'<h2>Seams in Newcastle Homes</h2>',

"<p>Newcastle&rsquo;s housing stock is practically a seam-planning workshop: split-levels and two-stories with open great rooms wider than any roll, "
"stairs feeding hallways at pivot points, and big south- and west-facing windows aimed at Lake Washington views &mdash; which means low raking light "
"across the exact floors where seams have to live. When we measure a Newcastle home, the seam map is drawn against those windows and walkways "
"specifically, and we will show you where every joint lands before you sign anything.</p>",

"<p>The mobile showroom helps here more than people expect: seeing the actual sample in your actual light &mdash; morning and evening, with and against "
"the pile &mdash; tells you more about how a seam will read than any showroom ceiling ever could. We bring 20+ full-size samples and all three pad "
"grades, measure every room and stair, and leave a written price the same visit. The local details are on our "
"<a href=\"/city-of-new-castle/carpet-installation-in-newcastle-wa\">Newcastle carpet installation page</a>.</p>",

faq('Carpet Seams: What Homeowners Ask Us', [
 ('Is it normal to see the seam in new carpet?',
  'Often, yes — for the first few weeks and under certain light. Seams are joints in a textile, and industry standards call for them to be minimized, not invisible. A faint line under low raking light on a properly placed, sealed, flat seam is normal. A gap, fraying, a hard ridge, or two sides reading as different shades is not.'),
 ('Why does my carpet seam show more in the morning?',
  'Light angle. Low sun raking across the floor throws a shadow off every fiber that sits slightly proud at the joint, so a seam that vanishes under evening lamps can appear at 8 a.m. This is also why good installers run seams parallel to the dominant window instead of across its light.'),
 ('Why does carpet have seams at all?',
  'Because carpet comes on rolls — most commonly 12 feet wide, occasionally 13’6” or 15 feet. Any room wider than the roll, and most hallways and L-shapes, must be pieced. The measure determines where those pieces meet, which is why a proper measure includes a seam diagram, not just square footage.'),
 ('Can a carpet seam be truly invisible?',
  'No, and anyone promising invisible seams is overpromising. A well-made seam in a textured cut pile, placed out of traffic and parallel to the light, is effectively invisible in daily life — you would have to hunt for it. Dense low pile, sheen, loops, and patterns all make the joint easier to find.'),
 ('My installer put a seam in the doorway. Is that wrong?',
  'Sometimes it is unavoidable — doorways are where pieces naturally meet, and some layouts give no alternative. But a doorway is a pivot point that concentrates wear on the joint, so a good plan avoids it when the geometry allows. Ask to see the seam diagram and the reasoning; a professional will have both.'),
 ('What is seam peaking and is it a defect?',
  'Peaking is the joint rising into a slight ridge, usually because tension across the seam is high or the carpet was not stretched evenly. A slight peak can relax over the first weeks. A hard ridge you feel underfoot months later is a workmanship issue — typically stretching or seaming technique — and your installer should correct it.'),
 ('Do seams affect how long the carpet lasts?',
  'A well-placed, sealed seam lasts as long as the carpet. A badly placed one ages faster than the field around it because traffic concentrates wear on the joint, and an unsealed edge can fray and delaminate. Placement and edge sealing at install day decide most of it, along with a firm pad and a proper power stretch.'),
 ('Which carpets hide seams best?',
  'Textured and twisted cut piles in mid heights with some color fleck hide joints best. Dense low-pile products with sheen, tight loops like berber, and large pattern repeats show them most — patterned carpet also needs extra yardage for matching. If your room guarantees a prominent seam location, style choice is a real part of the fix.'),
]),

cta('Want to See the Seam Map Before You Buy?',
    'We measure every room, draw the seams against your light and your walkways, and show you where each joint lands before you commit. Mobile showroom with 20+ samples, all three pad grades, and a written price the same visit. Serving Newcastle and all of King &amp; Snohomish County.'),

related([
 ('/blog/how-to-measure-for-carpet', 'How to measure for carpet'),
 ('/blog/wall-to-wall-carpet-cost', 'What wall-to-wall carpet costs'),
 ('/blog/carpet-padding-thickness', 'Carpet padding thickness and grades'),
 ('/blog/berber-vs-plush-carpet', 'Berber vs plush carpet'),
 ('/city-of-new-castle/carpet-installation-in-newcastle-wa', 'Carpet installation in Newcastle'),
 ('/contact', 'Book a free estimate'),
]),
]

assemble(S, parts)
