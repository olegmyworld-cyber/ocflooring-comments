from builder import *

S = 'carpet-removal-cost'

parts = [
date_badge('October 1, 2026'),

quick_answer(
 "<strong>Carpet removal is priced per square foot, it is the most DIY-able job in flooring, and if we are installing your new carpet it shows up as a named line in the written quote "
 "&mdash; not a surprise.</strong> What you are paying for is not pulling up carpet; that part takes minutes. It is the pad glued to the slab or stapled to the subfloor, the hundreds "
 "of staples that stay behind, the tack strip, the stairs, and getting a small mountain of heavy, awkward material out of the house and legally disposed of. Read the line items, or "
 "do the sweaty parts yourself &mdash; both are legitimate answers.",
 'Kirkland homes &amp; condos'),

facts([
 ('4 layers', 'of work in every removal: the carpet, the pad under it, the staples or glue holding the pad down, and the tack strip around the edges. Quotes that sound cheap often include only the first.'),
 ('Per tread', 'how stairs are priced for removal, same as installation &mdash; every tread is stripped, de-stapled and scraped by hand. A staircase adds real labor to a tear-out.'),
 ('Same visit', 'when you get our written price. If removal and haul-away are part of your install, they are named lines in that number &mdash; you can see exactly what skipping them with a DIY weekend would save.'),
]),

'<h2>What a Removal Price Actually Buys</h2>',

"<p>Pulling carpet off the floor is genuinely easy &mdash; cut it into strips, peel, roll. If that were the whole job, nobody would charge much for it and nobody would need help. The "
"price lives in everything under and around the carpet, and in the fact that a modest three-bedroom house produces several hundred pounds of material that has to go somewhere that "
"is not your curb.</p>",

table('The Anatomy of a Carpet Removal Quote', ['Line item', 'What it involves', 'Why it is real work'], [
 ('<strong>Carpet tear-out</strong>', 'Cut, peel, roll, carry', 'The easy part &mdash; though rolled carpet is heavier and more awkward than anyone expects, especially down stairs'),
 ('<strong>Pad removal</strong>', 'Peel and scrape', 'Pad is stapled every few inches on wood subfloors and often glued on concrete &mdash; old glued pad comes up in crumbs, not sheets'),
 ('<strong>Staples &amp; glue</strong>', 'Pull or scrape every one', 'Hundreds of staples per room, each one a future bump under new flooring if it stays; glue residue has to be scraped to flat'),
 ('<strong>Tack strip</strong>', 'Pry up, or inspect and keep', 'Reused only if sound and dry &mdash; rusty or rotted strip gets pried out, nails and all, and replaced'),
 ('<strong>Stairs</strong>', 'Per tread, by hand', 'Every tread is stripped, de-stapled and scraped individually &mdash; the slowest square footage in the house'),
 ('<strong>Haul-away &amp; disposal</strong>', 'Load, drive, pay the facility', 'Old carpet is bulky, heavy and not welcome in regular trash pickup &mdash; disposal is a real cost, not a rounding error'),
 ('<strong>Furniture</strong>', 'Clear the room first', 'Included for normal household pieces when we do the job; the wildcard in every DIY weekend plan'),
 ('<strong>Subfloor surprises</strong>', 'Found, not chosen', 'Pet damage, squeaks and soft spots hide under carpet for years &mdash; removal is when they finally get seen and priced honestly'),
]),

'<h2>When Removal Is Included &mdash; and When It Is Not</h2>',

"<p>If we are installing your new carpet, tear-out and haul-away of the old floor are part of the conversation from the first measure, and they appear as named lines in the written "
"price we leave the same visit. That is the arrangement most people want: the old floor leaves in the morning, the new one goes down after, one crew, one day for most homes. Installed "
"carpet starts at $1.49 per square foot with us, and the quote shows exactly what the removal portion adds &mdash; which also shows you exactly what a DIY tear-out weekend would save "
"you.</p>",

"<p>Where homeowners get burned is the quote that never mentions removal at all. The number looks great, the crew arrives, and suddenly there is a same-day surcharge for the thing "
"everyone knew had to happen. We wrote a whole guide to <a href=\"/blog/carpet-installation-cost-seattle\">reading a carpet quote line by line</a> &mdash; removal and disposal are two "
"of the lines to check by name. The same discipline applies across trades: our refinishing side wrote about <a href=\"/blog/refinishing-quote-2-vs-6-per-sqft\">why two quotes for the "
"same floor can be miles apart</a>, and the answer is always in what one of them quietly left out.</p>",

'<h2>The Honest DIY Section</h2>',

"<p>Here is the part a flooring company is not supposed to say: removing your own carpet is completely reasonable, and if the budget is tight it is the single best place to put your "
"own sweat. It needs a utility knife, gloves, pliers, a pry bar and a free Saturday &mdash; no skill that ends in a ruined floor, unlike most flooring DIY. Our step-by-step "
"<a href=\"/blog/how-to-remove-old-carpet\">guide to removing old carpet</a> walks the whole sequence.</p>",

"<p>Go in with open eyes about the three parts people underestimate. First, <strong>the staples</strong> &mdash; pulling several hundred of them, kneeling, is the actual job; the "
"carpet was the warm-up. Second, <strong>the weight</strong> &mdash; a rolled bedroom of carpet plus pad is an awkward, back-testing load, and a whole house of it will not fit in a "
"sedan or a single trash pickup. Third, <strong>the tack strip</strong> &mdash; it is a plank of nails pointing up; wear real shoes and respect it. If you do the tear-out, leave the "
"tack strip down unless it is damaged &mdash; if it is sound, the installers will reuse it, and you will have saved yourself the nastiest prying in the job.</p>",

'<h2>What We Find Under Carpet in Kirkland</h2>',

"<p>Removal is also the moment of truth for whatever the carpet has been hiding. In the older neighborhoods &mdash; Rose Hill, Norkirk, Market &mdash; we regularly pull carpet off "
"original hardwood that the sellers of 1987 covered without a second thought. Sometimes that wood is a refinishing candidate that changes the whole plan; the "
"<a href=\"/blog/refinishing-floors-1920s-seattle-bungalow\">old-house refinishing playbook</a> covers what is realistic. We will tell you honestly which you have before anyone "
"orders carpet.</p>",

"<p>Less romantic finds: pet stains that soaked through to the subfloor and need sealing before anything new goes down, squeaks that are a five-minute screw fix while the floor is "
"bare, and in condos &mdash; Juanita and downtown both &mdash; the logistics of getting a house worth of old carpet down an elevator under building rules. None of these are "
"disasters. All of them are cheaper to handle while the floor is open, which is exactly when we price them &mdash; in writing, before the new carpet is cut.</p>",

two_col(
 'DIY the removal when',
 ['The budget is tight and you have a free weekend and a working back',
  'It is a straightforward room or two, not a full staircase house',
  'You have a way to haul heavy rolls &mdash; truck, trailer, or a transfer-station trip',
  'You want to peek under the carpet before committing to a plan',
  'You leave sound tack strip in place for the installers to reuse',
  'You bag the staples as you pull them &mdash; future you says thanks'],
 'Let us do it when',
 ['The new carpet is going in anyway &mdash; one crew, one day, one written number',
  'There are stairs &mdash; per-tread stripping is slow, nail-rich work',
  'The pad is glued to a concrete slab &mdash; scraping it is misery by hand',
  'Pet damage or odor is part of the story &mdash; the subfloor needs assessing, not covering',
  'Building rules govern elevators, hours and disposal &mdash; we plan around them',
  'Your back, knees or schedule are worth more than the line item']),

'<h2>Removal Without Replacement</h2>',

"<p>Not every removal ends in new carpet, and that is fine. Some homeowners pull carpet to escape allergies, some to expose hardwood, some because a flooded room needs everything out "
"now and decisions later. We do stand-alone tear-outs &mdash; priced per square foot, stairs per tread, haul-away included &mdash; and if what turns up underneath changes your mind "
"about what goes back down, nobody at this company will be offended. Whether the carpet was worth keeping in the first place is its own question; our "
"<a href=\"/blog/how-long-does-carpet-last\">honest guide to carpet lifespan</a> helps you make that call before paying anyone to remove anything. Kirkland service details, including "
"removal and haul-away, live on our <a href=\"/city-of-kirkland/carpet-installation-in-kirkland-wa\">Kirkland carpet installation page</a>.</p>",

faq('Carpet Removal Cost: What Homeowners Ask Us', [
 ('How much does carpet removal cost?',
  'It is priced per square foot, with stairs priced per tread on top, and the honest answer depends on what is under your carpet — stapled pad on wood subfloor is the easy case, glued pad on concrete is the slow one. When we install your new carpet, removal and haul-away appear as named lines in the written quote we leave at the measure, so you see the exact number before deciding anything.'),
 ('Is carpet removal included in carpet installation?',
  'With us it is part of the quoted job when you want it to be — a named line item, not an assumption in either direction. The trap to avoid is any quote that never mentions removal or disposal at all; that is where surprise same-day charges come from. Ask for both by name in any bid you compare.'),
 ('Can I remove carpet myself to save money?',
  'Yes, and it is the most DIY-friendly job in flooring — a utility knife, gloves, pliers and a weekend. The parts people underestimate are pulling hundreds of pad staples, hauling several hundred pounds of rolled carpet, and disposal logistics. Do the tear-out, leave sound tack strip in place, and let the installers handle the rest.'),
 ('What has to come out besides the carpet?',
  'Three more layers: the pad, which is stapled every few inches or glued to concrete; the staples or glue residue, every one of which becomes a bump under new flooring if it stays; and the tack strip around the room edges — though sound, dry tack strip is usually left in place and reused for new carpet.'),
 ('How long does carpet removal take?',
  'A crew clears a typical room quickly and a whole house in a morning — which is why most of our installs finish in a single day even with the tear-out included. DIY, plan a full day for a few rooms once staple-pulling is counted honestly, and more if there are stairs.'),
 ('Why do stairs cost more to strip than rooms?',
  'Every tread is its own small job: the carpet is cut and peeled per step, the pad is stapled heavily at each nose, and all of it is removed kneeling on a staircase. Per square foot, stairs are the slowest removal in the house — which is why they are priced per tread, same as installation.'),
 ('What if there is hardwood under my carpet?',
  'It happens constantly in older Kirkland neighborhoods, and it can change your whole plan — original oak or fir under 1980s carpet is sometimes a refinishing candidate rather than a re-carpet. We will tell you honestly which you have once the floor is open, and price both directions in writing so you can choose.'),
 ('Can old carpet go in the regular trash?',
  'Not realistically — a house of carpet and pad is hundreds of pounds of bulky rolls that regular pickup will not take. It goes to a transfer station or bulky-waste drop-off, which charges by weight, and hauling it there needs a truck. Disposal is a genuine cost inside any removal price, ours included; it is not padding.'),
]),

cta('One Written Number, Tear-Out Included',
    'We measure every room and stair, price the removal, haul-away and new floor as named lines, and leave the written total the same visit — so you can see exactly what DIY would save and decide with real numbers. Free in-home estimates across King &amp; Snohomish County.'),

related([
 ('/blog/how-to-remove-old-carpet', 'How to remove old carpet yourself'),
 ('/blog/carpet-installation-cost-seattle', 'What carpet installation costs'),
 ('/blog/how-long-does-carpet-last', 'How long carpet honestly lasts'),
 ('/blog/6-reasons-to-replace-carpet-flooring', 'Six reasons to replace carpet'),
 ('/city-of-kirkland/carpet-installation-in-kirkland-wa', 'Carpet installation in Kirkland'),
 ('/contact', 'Book a free estimate'),
]),
]

assemble(S, parts)
