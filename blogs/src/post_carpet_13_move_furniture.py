from builder import *

S = 'do-carpet-installers-move-furniture'

parts = [
date_badge('November 26, 2026'),

quick_answer(
 "<strong>Yes &mdash; moving normal household furniture is part of a professional carpet installation, and with us it is in the quote, not an upsell.</strong> Beds, sofas, "
 "dressers, tables, desks &mdash; we move them, install the carpet, and put them back where they came from. The exceptions are the heavy specials: pianos, gun safes, full "
 "waterbeds, large aquariums and pool tables are not furniture, they are freight, and they need their own plan before install day. Here is exactly where the line sits and "
 "how to prep so your installation finishes in one day instead of two.",
 'Edmonds homes &amp; condos'),

facts([
 ('Included', 'moving normal household furniture is part of our carpet quote &mdash; and so is putting it all back at the end of the day. If another quote is vague about this, ask before you sign, not on install morning.'),
 ('The freight list', 'pianos, gun safes, full waterbeds, large aquariums, slate pool tables. Installers everywhere draw the same line, for the same insurance and physics reasons. Each one has a workable plan &mdash; if it is made in advance.'),
 ('One day', 'how long most homes take to install once the carpet arrives. Honest prep the night before is a quiet part of why. We measure every room and stair and leave a written price the same visit.'),
]),

'<h2>What "We Move the Furniture" Actually Covers</h2>',

"<p>Normal household furniture means the things a two-person crew can move safely without special equipment: bed frames and mattresses, sofas and recliners, dressers and "
"nightstands, dining tables and chairs, desks, bookshelves once the books are off them, TV stands once the TV is off them. On install day the crew works room by room in a "
"leapfrog &mdash; furniture from the first bedroom shifts into the hallway or the next room, the carpet goes in, and everything walks back before the crew moves on. Your "
"sofa never sees the driveway, and nothing leaves the house.</p>",

"<p>There is a reason this is standard rather than a favor. Carpet has to be fitted to an empty floor &mdash; tack strip runs along every wall, seams are planned across the "
"whole room, and power-stretching needs a clear run from wall to wall. An installer who says they will \"work around\" your furniture is telling you the carpet will be "
"kicked in tight where it is convenient and left loose where it is not, and loose carpet is exactly what ripples in year three. Furniture moving is not a courtesy attached "
"to the job; it is a condition of doing the job right. It is also already priced in &mdash; our guide to <a href=\"/blog/carpet-installation-cost-seattle\">what carpet "
"installation costs</a> walks through the whole quote line by line.</p>",

'<h2>The Heavy Exceptions: Pianos, Safes, Waterbeds</h2>',

"<p>Every legitimate installer draws the same line, and it is worth understanding why rather than just where. A piano is not heavy the way a sofa is heavy &mdash; it is "
"heavy in a way that ruins backs, staircases and the piano itself when it is moved by people without piano equipment. A gun safe concentrates several hundred pounds on "
"four small feet and cannot be walked or tipped safely by a flooring crew. A waterbed holds an astonishing amount of water that must be drained before the frame can move "
"at all. An aquarium is a glass box full of living things. A slate pool table has to be taken apart and re-leveled by someone who does that for a living, or it will never "
"play true again.</p>",

"<p>None of this means those rooms cannot be carpeted. It means the plan gets made at the estimate, not discovered on install day. Usually that is one of three routes: a "
"specialty mover handles the item the day before, we carpet around the item and leave a clean seam for later, or the room gets split into phases. All three work. The only "
"version that fails is the one where the crew arrives and finds a full waterbed nobody mentioned &mdash; that is how a one-day job becomes a rescheduled one.</p>",

table('Who Moves What on Install Day', ['Item', 'Who handles it', 'The practical note'], [
 ('<strong>Beds &amp; mattresses</strong>', 'Our crew', 'Strip the bedding the night before; it keeps things clean and saves twenty minutes a room'),
 ('<strong>Sofas, recliners, tables</strong>', 'Our crew', 'Clear anything on or under them &mdash; remotes, baskets, the drawer of mystery cables'),
 ('<strong>Dressers &amp; nightstands</strong>', 'Our crew', 'Empty or lighten the drawers; a full dresser is a furniture-and-floor injury waiting to happen'),
 ('<strong>TVs &amp; electronics</strong>', 'You', 'Unhook and label cables the night before &mdash; crews move furniture, not home-theater wiring'),
 ('<strong>Lamps, breakables, plants</strong>', 'You', 'Anything that shatters travels by owner. Gather it all in a no-carpet zone like the kitchen'),
 ('<strong>Piano</strong>', 'Specialty movers', 'Book them for the day before; plan on retuning after the move either way'),
 ('<strong>Gun safe</strong>', 'Specialty movers, or we carpet around it', 'Carpeting around it is common and looks fine &mdash; decide at the estimate, not install day'),
 ('<strong>Waterbed</strong>', 'You &mdash; drained in advance', 'Drain it the day before. A waterbed drains slowly, and install day cannot wait for it'),
 ('<strong>Aquarium</strong>', 'You, or an aquarium service', 'Fish, water, then tank, in that order, well before the crew arrives'),
]),

'<h2>The Night-Before Checklist</h2>',

"<p>The prep that actually matters takes one evening, and none of it involves lifting anything heavy. Clear every surface &mdash; dresser tops, nightstands, desks, "
"windowsills low enough to catch an elbow. Empty closet floors in any room being carpeted, because closets are part of the measure and the crew needs to reach every inch "
"of them; our post on <a href=\"/blog/how-to-measure-for-carpet\">how carpet is measured</a> explains why closets count more than people think. Unhook electronics and "
"take photos of the cable spaghetti before you pull it. Find the pets somewhere calm to be &mdash; an open front door, a power stretcher and a curious cat are a bad "
"combination. And leave the driveway clear, because the carpet arrives on a roll that is longer than your car.</p>",

two_col(
 'What our crew handles',
 ['Moving normal household furniture out and back, room by room',
  'Tear-out of the old carpet, pad, staples and tack strip',
  'Haul-away and disposal of everything that comes out',
  'New tack strip, seaming and power-stretching to the walls',
  'Vacuuming the new carpet before the furniture goes back',
  'Doors that drag on the new pile &mdash; we will tell you which ones need a trim'],
 'What is best handled by you',
 ['Bedding, surface clutter and everything inside the dressers',
  'TVs, computers, consoles and their cabling',
  'Breakables, lamps, mirrors and houseplants',
  'Draining a waterbed and relocating an aquarium in advance',
  'Booking piano or safe movers for the day before',
  'A plan for pets and small children while doors stand open']),

'<h2>How Install Day Actually Runs</h2>',

"<p>The crew arrives, walks the house against the measure, and starts in the room farthest from the door. Furniture shifts to the adjacent room, the old carpet comes up "
"&mdash; pad, staples and tack strip with it &mdash; and goes straight out to the trailer. If you are curious what that tear-out involves or costs on its own, we cover it "
"in <a href=\"/blog/carpet-removal-cost\">carpet removal cost</a> and <a href=\"/blog/how-to-remove-old-carpet\">how to remove old carpet</a>. New tack strip goes down, "
"pad goes down, carpet is cut, seamed and power-stretched, and the furniture walks back in. Then the whole dance repeats in the next room. Most homes finish in a day; a "
"big house with a lot of stairs can run into a second, and we will tell you which yours is at the estimate rather than at five in the evening.</p>",

'<h2>Stretching Jobs Are a Different Conversation</h2>',

"<p>If your carpet is staying and only needs to be re-stretched &mdash; ripples, waves, the wrinkle by the hallway door &mdash; the furniture question gets easier. A "
"restretch usually needs the room mostly clear along the walls being pulled, but not empty; large pieces can often shift within the room rather than out of it. We wrote "
"up the details in <a href=\"/blog/do-you-have-to-move-furniture-to-stretch-carpet\">do you have to move furniture to stretch carpet</a>, and if you are weighing whether "
"a restretch is even worth doing versus replacing, <a href=\"/blog/is-it-worth-it-to-restretch-your-carpet\">that comparison is here</a> along with "
"<a href=\"/blog/carpet-stretching-cost\">what stretching costs</a>. Short version: if the carpet itself is healthy, restretching is the cheap right answer, and it "
"disrupts your furniture for hours, not days.</p>",

'<h2>Moving Furniture in Edmonds Homes, Specifically</h2>',

"<p>Edmonds keeps our crews honest. The older homes down in the Bowl have the narrow hallways and tight stair turns of their era &mdash; a queen box spring and a "
"1940s stairwell are natural enemies, and we plan the furniture shuffle around it. The split-levels up the hill add half-flights in both directions, which changes the "
"leapfrog order but not the outcome. And the waterfront condos bring elevator reservations and building work-hours into the plan, which we sort out with the building "
"before install day, not during it. All of it is routine for us &mdash; the details are on our <a href=\"/city-of-edmonds/carpet-installation-in-edmonds-wa\">Edmonds "
"carpet installation page</a>, and the estimate itself happens at your kitchen table: twenty-plus full-size samples, all three pad grades, a measure of every room and "
"stair, and a written price the same visit.</p>",

faq('Furniture and Carpet Installation: What Homeowners Ask Us', [
 ('Do carpet installers move your furniture?',
  'Yes. Moving normal household furniture — beds, sofas, dressers, tables, desks — is part of a professional carpet installation, and with us it is included in the written quote. The crew works room by room, shifting furniture into the next room, installing, and moving everything back. The exceptions are pianos, gun safes, full waterbeds, large aquariums and pool tables, which need their own arrangements.'),
 ('Is furniture moving included in the price or an extra charge?',
  'With us it is included, and any quote should say so in writing. Some companies price it as a line item or exclude it entirely, which is a legitimate way to quote — but you want to know which kind of quote you are holding before you compare numbers. If a bid is suspiciously low, furniture moving and haul-away are the two lines most often missing.'),
 ('Do I need to empty dressers before carpet installation?',
  'Empty them or lighten them substantially. A full dresser flexes when it is lifted, drawers slide out mid-carry, and the weight is hard on both the crew and the new carpet being walked across. Clothes can stay in a dresser that is light; the sixty pounds of everything else should come out the night before.'),
 ('What happens with my piano when carpet is installed?',
  'Book a piano mover for the day before, or have us plan the room around it. Flooring crews do not move pianos — not because they are lazy but because pianos are moved with skids, boards and training, and an installer who says yes to a piano is telling you something worrying about their judgment. Plan on a tuning afterward; pianos notice being moved.'),
 ('Can you install carpet around a gun safe or other immovable item?',
  'Yes, and it is common. We cut and finish the carpet cleanly around the safe, and if the safe ever moves, the spot can be patched with an offcut — keep a piece from the install for exactly that day. The alternative is a safe-moving company the day before. Both work; deciding at the estimate is what matters.'),
 ('Do installers disconnect TVs, computers and other electronics?',
  'No — electronics and their cabling are yours. Unhook everything the night before, label the cables or photograph the connections, and set the equipment somewhere no carpet is being installed. The crew will happily move the empty TV stand; they will not troubleshoot your soundbar at four in the afternoon.'),
 ('How long does carpet installation take with furniture in the house?',
  'Most homes are still a single day. The furniture shuffle is built into how crews work — room by room, leapfrogging furniture ahead of the carpet. What stretches a job into a second day is not furniture, it is surprises: a full waterbed nobody drained, a room that was supposed to be cleared and was not, or a large house with many stairs. Honest prep keeps a one-day job a one-day job.'),
 ('What should I do with pets during installation?',
  'Somewhere calm, closed and away from the work — a bathroom that is not being carpeted, a crate, or a neighbor. Doors stand open all day, the crew is in and out constantly, and power stretchers and startled animals do not mix. Tell us at the estimate what animals live in the house and we will plan the door situation with you.'),
]),

cta('Get the Measure, the Samples and a Written Price in One Visit',
    'We bring twenty-plus full-size carpet samples and all three pad grades to your Edmonds home, measure every room, closet and stair, and leave a written price the same visit &mdash; furniture moving and haul-away included, in writing. Free in-home estimates across King &amp; Snohomish County.'),

related([
 ('/blog/do-you-have-to-move-furniture-to-stretch-carpet', 'Moving furniture for a carpet restretch'),
 ('/blog/carpet-installation-cost-seattle', 'What carpet installation costs'),
 ('/blog/carpet-removal-cost', 'What carpet removal costs'),
 ('/blog/how-to-measure-for-carpet', 'How carpet is measured'),
 ('/city-of-edmonds/carpet-installation-in-edmonds-wa', 'Carpet installation in Edmonds'),
 ('/contact', 'Book a free estimate'),
]),
]

assemble(S, parts)
