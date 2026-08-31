from builder import *

S = 'carpet-subfloor-prep'

parts = [
date_badge('March 25, 2027'),

quick_answer(
 "<strong>The day the old carpet comes up is the only day anyone will see your subfloor for the next decade &mdash; and what happens in that window decides more about how the new "
 "carpet performs than the carpet does.</strong> Squeaks get screwed down, soft spots get opened up, pet-soaked plywood gets sealed or cut out, and the tack strip gets inspected "
 "instead of blindly reused. None of that is visible from above, which is why we price it when we find it, at numbers we name up front &mdash; not padded into every quote, and never "
 "carpeted over and forgotten.",
 'Duvall &amp; the Snoqualmie Valley'),

facts([
 ('One day', 'is still what most homes take to install, including the normal run of subfloor fixes. Tear-out happens in the morning, prep happens while the floor is naked, carpet goes down the same day.'),
 ('From $1.49/sq ft', 'where installed carpet starts with us &mdash; material, pad and labor. Subfloor repairs are the one honest add: priced per fix when discovered, at rates we name before the tear-out begins.'),
 ('Since 2013', 'and 1,000+ floors of reading what tear-outs reveal. By now the surprises are not surprises &mdash; we can usually tell you from the walk-through what we expect to find under yours.'),
]),

'<h2>The Only Day Anyone Sees Your Subfloor</h2>',

"<p>Carpet is the most forgiving floor covering there is, and that is a double-edged thing. It hides wavy plywood, hairline squeaks, stains and small sins that would telegraph "
"straight through hard flooring. But it also hides them from <em>you</em> &mdash; for ten or fifteen years at a stretch. The morning the old carpet and pad come out is a brief, "
"valuable window where the structure of your floor is sitting in plain view, and everything wrong with it can be fixed cheaply and permanently. Carpet it over instead, and every one "
"of those problems is either a decade older when it finally surfaces, or a callback that requires pulling up brand-new carpet to reach.</p>",

"<p>So when we quote a job, the tear-out morning has an agenda: staples and old tack strip out, floor swept clean, and then a slow walk of every room listening and feeling for what "
"the old carpet was covering. It adds a little time. It is the best-value hour of the whole installation.</p>",

'<h2>What Tack Strip Actually Does &mdash; and When It Cannot Be Reused</h2>',

"<p>Tack strip is the wooden strip nailed around the room's perimeter, bristling with angled pins that point at the wall. When carpet is power-stretched, those pins are what hold the "
"tension &mdash; the entire flatness of your floor hangs on a strip of lath most people have never seen. Reusing sound tack strip is normal and fine. Reusing bad tack strip is how a "
"tight installation goes loose in a year, and bad is common: strip rusted by years of damp, strip soaked and rotted where pet accidents concentrated at doorways, strip pulled loose "
"from the subfloor by a previous knee-kicked install that was never properly stretched, and strip that is simply missing pins where furniture crushed it. We check every foot of it, "
"replace what fails, and add new strip where the old install skipped it &mdash; closets, bay windows and around hearths are the usual gaps.</p>",

table('What Turns Up When the Old Carpet Comes Out', ['Discovery', 'What it means', 'What we do about it'], [
 ('<strong>Squeaks &amp; movement</strong>', 'Subfloor panels rubbing on loose nails as joists dried and shrank', 'Screw the panel to the joists right there &mdash; a two-minute permanent fix per squeak'),
 ('<strong>Soft or spongy spots</strong>', 'Delaminated or moisture-weakened plywood, often near baths and exterior doors', 'Open it up, find the cause, replace the section &mdash; never carpet over a soft floor'),
 ('<strong>Dark rings &amp; pet staining</strong>', 'Urine that soaked through pad into the wood; the source of "mystery" odors', 'Seal minor staining with odor-blocking primer; cut out and replace saturated sections'),
 ('<strong>Rusted or rotten tack strip</strong>', 'Moisture history at the perimeter; strip that cannot hold a stretch', 'Replace those runs with new strip before the new carpet is tensioned'),
 ('<strong>Ridges, humps &amp; proud fasteners</strong>', 'Panel edges that swelled or nails backing out', 'Sand or plane ridges, reset fasteners &mdash; they wear a visible line into new carpet'),
 ('<strong>Gaps, old vents &amp; abandoned holes</strong>', 'Previous remodels; cold air and odor paths from the crawlspace', 'Block and patch them &mdash; a fifteen-minute fix that warms the whole room'),
 ('<strong>Moisture staining without softness</strong>', 'A past leak or a damp crawlspace below', 'Trace the source before covering it; sometimes the fix is under the house, not in it'),
]),

'<h2>Squeaks and Soft Spots: Fix Them While the Floor Is Naked</h2>',

"<p>A squeaky floor under carpet is almost never the carpet &mdash; it is the subfloor panel lifting a hair off the joist and riding up and down a nail shank with every footstep. "
"From above, through pad and pile, there is no good fix; squeak-repair kits that go through carpet are a compromise at best. With the carpet up, the fix is embarrassingly simple: "
"drive screws through the panel into the joist at the noisy spots, and the squeak is gone for good. This is why we tell people planning new carpet to save every complaint they have "
"about their floor for the install &mdash; the list gets handled in an hour on tear-out morning.</p>",

"<p>Soft spots are the same logic with higher stakes. A spongy patch near a bathroom door or a slider is water-weakened wood, and it only moves in one direction. Carpet over it and "
"the pad will mask it for a while as the rot quietly spreads; open it up now and it is usually a single panel section and a straightforward patch. If we find softness, we find the "
"moisture source too &mdash; a fixed leak is a repair, an unfixed one is a subscription.</p>",

'<h2>Pet Damage: What the Dark Rings Mean</h2>',

"<p>The most common discovery in family homes is the one nobody enjoys: dark rings and continents on the plywood where years of accidents soaked through the pad. This is worth "
"understanding, because it explains a mystery many homeowners have lived with &mdash; carpet that was professionally cleaned and still smelled on humid days. The odor was never in "
"the carpet. Urine salts sitting in the wood re-activate with moisture in the air, and no amount of cleaning from above touches them. The fix happens on tear-out day: light staining "
"gets sealed with an odor-blocking primer, and genuinely saturated sections get cut out and replaced. Then the new floor goes down over a moisture-barrier pad so history does not "
"repeat &mdash; the same spec we walk through in <a href=\"/blog/best-carpet-for-pets\">our pet carpet guide</a>. Skipping this step is how a brand-new carpet inherits a ten-year-old "
"smell, and it is the single best argument against the cheapest possible tear-out-and-relay job.</p>",

'<h2>Why We Price Subfloor Work When We Find It</h2>',

"<p>Here is the honest problem with subfloor repairs: nobody can see them at the estimate. A quote that includes a big &ldquo;prep allowance&rdquo; on every job is charging most "
"customers for repairs their floors do not need. A quote that pretends prep never happens is either going to carpet over your problems or start a change-order fight on install day. "
"Neither is how we want to operate, so we do it the plain way: the estimate covers the known scope &mdash; tear-out, haul-away, new tack strip where needed, pad and carpet, all "
"measured room by room as described in <a href=\"/blog/how-to-measure-for-carpet\">how we measure</a> &mdash; and it names the unit prices for the common repairs up front: per "
"squeak run, per panel section, per foot of tack strip. If tear-out finds something, you see it with your own eyes, you get the number from the sheet you already have, and you "
"decide before anything gets covered. Most homes need little or nothing. The ones that need work deserve to know it while knowing costs something can still be done about it.</p>",

two_col(
 'What proper prep includes on every job',
 ['Old carpet, pad, staples and failed tack strip out &mdash; and hauled away',
  'Every foot of remaining tack strip inspected, not assumed',
  'The floor walked for squeaks and soft spots before pad goes down',
  'Ridges knocked down and proud fasteners reset',
  'Pet staining sealed &mdash; or cut out when sealing is not enough',
  'Unit repair prices named in writing before tear-out day'],
 'Red flags in a prep-free quote',
 ['No mention of tack strip anywhere &mdash; ask what gets reused and why',
  'A vague "prep as needed" line with no unit prices attached',
  '"We can install over what is there" before anyone has seen what is there',
  'A big flat prep fee charged to every job regardless of condition',
  'No plan for pet odor beyond "the new carpet will take care of it"',
  'A price that assumes the old pad stays &mdash; it never should']),

'<h2>Under Duvall Homes Specifically</h2>',

"<p>Around Duvall and the Snoqualmie Valley the housing mix runs from 1980s&ndash;90s plateau construction to older farmhouses, and most of it sits over vented crawlspaces rather "
"than slabs. That shapes what we find. Crawlspace moisture is the quiet driver of half the list above &mdash; rusty tack strip at exterior walls, swollen panel edges, squeaks from "
"seasonal movement as the valley swings from soaked winters to dry Augusts. Newer plateau homes mostly need screws and small patches; older places sometimes reveal plank subfloors "
"with gaps that want a layer of underlayment plywood for a truly flat, quiet result. None of it is exotic and none of it should scare you off carpet &mdash; it is exactly the stuff "
"a tear-out morning exists to catch. If the old floor is coming out anyway, the economics are covered in <a href=\"/blog/carpet-removal-cost\">carpet removal cost</a>, and the whole "
"picture of a quote in <a href=\"/blog/carpet-installation-cost-seattle\">what carpet installation costs</a>. For the local details, start at our "
"<a href=\"/city-of-duvall/carpet-installation-in-duvall-wa\">Duvall carpet installation page</a>.</p>",

faq('Subfloor Prep and Tack Strip: What Homeowners Ask Us', [
 ('What is subfloor prep, and do I actually need it?',
  'It is everything that happens between tearing out the old carpet and rolling out the new pad: fixing squeaks, replacing soft or stained sections, inspecting and renewing tack strip, and flattening ridges. Most homes need very little of it. But it can only happen on tear-out day, while the subfloor is exposed — which is why it gets checked on every job even though it is only billed when something is actually found.'),
 ('Can new carpet just go over the old tack strip?',
  'Often, yes — sound, dry, well-fastened tack strip is routinely reused, and that is not corner-cutting. What matters is that someone actually checks it. Rusted, pet-soaked, rotten or loose strip cannot hold a power stretch, and carpet anchored to it goes loose and rippled within a couple of years. We inspect every run and replace only what fails.'),
 ('Why does my floor squeak under the carpet, and can installers fix it?',
  'The squeak is the subfloor panel riding up and down a loose nail against the joist — the carpet is just the messenger. With the old carpet up, the fix is screws driven through the panel into the joists at each noisy spot: fast, cheap and permanent. Tell your installer where every squeak is before tear-out day; that list is gold while the floor is naked.'),
 ('What happens if you find pet damage on the subfloor?',
  'You will see it with your own eyes first — dark staining where accidents soaked through the pad into the wood. Light staining gets sealed with an odor-blocking primer; saturated sections get cut out and replaced. Then we recommend a moisture-barrier pad under the new carpet so it cannot happen again. Skipping this is why some "new" carpet smells old within a year.'),
 ('Why is subfloor repair not included in the carpet quote?',
  'Because nobody can see your subfloor until the carpet is up, and building a repair allowance into every quote means charging people for work their floors do not need. Instead we name the unit prices for the common repairs in the written estimate, and if tear-out finds something, you approve the fix at those pre-stated numbers before anything is covered. Most homes need nothing.'),
 ('Does the old pad really have to go?',
  'Yes, every time. Pad is a wear item — it collapses in traffic paths and absorbs every accident of the old carpet’s life. New carpet over old pad inherits the flat spots and the smells on day one, and it voids most carpet warranties besides. Fresh pad is a small share of the job cost and most of how the new floor feels.'),
 ('Can you carpet over a plywood subfloor with moisture stains?',
  'Depends what the stains are. Dry history — an old fixed leak, sealed pet staining — is fine to cover once treated. Active moisture is not: softness, dampness to the touch, or a musty crawlspace below gets diagnosed and fixed first, because carpet and pad over a wet subfloor grows mold in the one place you cannot see it. We would rather delay an install than bury a problem.'),
 ('How much time does subfloor work add to the install?',
  'Usually none worth noticing — squeak screws, a ridge knocked down and a few feet of new tack strip happen inside the normal rhythm of tear-out morning, and most homes still finish in a day. A replaced panel section adds an hour or two. Only genuine structural surprises, which are rare, push an install into a second day, and you would know why before it happened.'),
]),

cta('Let Us Look Under It Before You Cover It for a Decade',
    'Free in-home estimate with the mobile showroom: twenty-plus samples, all three pad grades, every room and stair measured, and repair unit prices in writing before tear-out day. Serving Duvall, the Snoqualmie Valley and all of King &amp; Snohomish County.'),

related([
 ('/blog/how-to-measure-for-carpet', 'How to measure for carpet'),
 ('/blog/carpet-removal-cost', 'What carpet removal costs'),
 ('/blog/carpet-installation-cost-seattle', 'What carpet installation costs'),
 ('/blog/best-carpet-for-pets', 'The best carpet for pet homes'),
 ('/blog/when-to-replace-carpet', 'When to replace carpet'),
 ('/city-of-duvall/carpet-installation-in-duvall-wa', 'Carpet installation in Duvall'),
 ('/contact', 'Book a free estimate'),
]),
]

assemble(S, parts)
