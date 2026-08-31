from builder import *

S = 'hiring-a-tile-installer-seattle'

parts = [
date_badge('February 16, 2027'),

quick_answer(
 "<strong>Hiring a tile installer in Seattle comes down to three questions almost nobody asks: What waterproofing membrane will you use, by name? Will you flood-test "
 "the pan for 24 hours, and can I see it? And what is your rate for what demolition finds?</strong> Add a two-minute check of the contractor's registration and bond "
 "on Washington's L&amp;I site, and you have filtered out most of the ways a tile job goes wrong &mdash; before anyone touches your bathroom. Price matters, but the "
 "spread between tile quotes is usually the answers to those three questions, not the tile.",
 'Seattle homes &amp; condos'),

facts([
 ('24 hours', 'the flood test a finished shower pan should sit through before tile goes on. We photograph ours and keep it on file. Ask every bidder when this day is in their schedule &mdash; if it does not have a day, it does not happen.'),
 ('2 years', 'our warranty on tile work, double the one-year most of the trade offers. A warranty is only as good as the assembly behind the tile; that is the bet we are making, in writing.'),
 ('4.7&#9733;', 'across 119 Google reviews. Read any installer&rsquo;s worst reviews, not their best &mdash; how a company behaves when something went sideways is the only review that predicts your experience.'),
]),

'<h2>Why Tile Is the Trade Where Hiring Matters Most</h2>',

"<p>Most flooring mistakes are visible and fixable. A bad paint job annoys you; a badly stretched carpet gets restretched. Tile is different in one specific way: "
"<strong>everything that decides whether it lasts is buried on day three</strong>. The substrate prep, the membrane, the pre-slope under a shower pan &mdash; once tile "
"covers them, no inspection can see them, and the failure arrives years later as a cracked line, a hollow floor, or a stain on the ceiling below. You are not hiring "
"someone to place tiles. You are hiring their judgment about everything the tiles will hide.</p>",

"<p>That is why this guide spends little time on the questions people usually ask &mdash; how long have you been in business, can I see photos &mdash; and most of it "
"on the questions that actually separate installers. Photos show everyone's best work; every portfolio in Seattle is beautiful. The differences live in the "
"answers below.</p>",

'<h2>The Two-Minute Check Before Any Conversation</h2>',

"<p>Washington makes this easy. Every legitimate contractor is registered with the state Department of Labor &amp; Industries, and the L&amp;I &ldquo;Verify a "
"Contractor&rdquo; tool is public. Type in the business name and you will see whether the registration is active, whether the bond and liability insurance are "
"current, and &mdash; usefully &mdash; whether anyone has filed suit against that bond. An unregistered contractor in Washington is not a bargain; it is a legal "
"problem you are volunteering for, because you lose the bond as a recovery path and may inherit liability you did not know you were carrying.</p>",

"<p>While you are there, check the registration age against the story you were told. A crew that says &ldquo;twenty years of experience&rdquo; attached to a "
"registration born eight months ago is not necessarily lying &mdash; people go independent &mdash; but it is a thing to ask about. And ask for the certificate of "
"insurance directly: a real contractor's office sends it without friction, because they get asked weekly.</p>",

table('The Questions That Actually Separate Tile Installers', ['Ask this', 'A good answer sounds like', 'Walk away if'], [
 ('<strong>What membrane will you use in the shower?</strong>', 'A product, by name &mdash; a bonded sheet like Kerdi, or a liquid membrane with coat counts', '&ldquo;Cement board is waterproof&rdquo; or &ldquo;the tile keeps water out&rdquo; &mdash; neither is true'),
 ('<strong>Do you flood-test the pan?</strong>', '&ldquo;24 hours, photographed, before any tile&rdquo; &mdash; and it has a day in the schedule', 'Hesitation, or &ldquo;we spray it later&rdquo; &mdash; a spray test after tile proves nothing about the pan'),
 ('<strong>What if you open the floor and find rot?</strong>', 'A named hourly or unit rate for discoveries, agreed now, in the contract', 'A shrug, or &ldquo;we will work it out&rdquo; &mdash; that is a mid-job negotiation you will lose'),
 ('<strong>How will you prep the floor?</strong>', 'Flattening, deflection check, an uncoupling membrane or proper backer, by name', '&ldquo;We go right over what is there&rdquo; on a wood subfloor'),
 ('<strong>Grout and corners?</strong>', 'Grout choice explained; silicone, not grout, at every change of plane', 'Grouted corners &mdash; they crack, and the crack lets water in'),
 ('<strong>Warranty, in writing?</strong>', 'A year at minimum &mdash; ours is two &mdash; and a story about honoring it', 'Verbal assurances, or a warranty that excludes everything that can happen'),
]),

'<h2>Why the Membrane Question Does So Much Work</h2>',

"<p>One question outperforms a reference check: <em>name the waterproofing</em>. An installer who answers instantly &mdash; Kerdi with banded seams, or a liquid "
"membrane at the manufacturer&rsquo;s specified thickness in two coats &mdash; has revealed their whole approach: they work in systems, follow specs, and expect to "
"be asked. An installer who waves at the question has told you the assembly will be improvised, and improvised waterproofing is how showers end up in our "
"<a href=\"/blog/tile-shower-waterproofing\">waterproofing guide</a> as cautionary tales. Grout is not waterproof and was never supposed to be; water passes through "
"it by design, and the membrane behind it is the actual shower. The same fluency test applies to floors &mdash; ask what goes under the tile and expect to hear about "
"flatness and movement, the physics we covered in <a href=\"/blog/why-tile-floors-crack\">why tile floors crack</a>.</p>",

'<h2>Reading the Quotes Side by Side</h2>',

"<p>Collect three bids and the spread will surprise you &mdash; on a Seattle shower it is routinely thousands. The instinct is to assume the high bid is greed and "
"the low bid is hunger; the truth is usually that they describe different jobs. One includes substrate flattening, a named membrane, a flood-test day, silicone "
"corners and a contingency rate. One says &ldquo;install customer&rsquo;s tile, $X.&rdquo; The pages look similar; the showers they produce are not. We walked "
"through the honest arithmetic in <a href=\"/blog/bathroom-tile-installation-cost-seattle\">what bathroom tile costs in Seattle</a> &mdash; installed work runs "
"$14&ndash;$26 per square foot with labor from $11, and a bid meaningfully below that range is leaving out steps, not overhead.</p>",

"<p>Timeline is the other tell. A full bathroom with a waterproofed shower is realistically seven to nine working days including cure times and the flood test "
"&mdash; the <a href=\"/blog/how-long-to-tile-a-bathroom\">day-by-day calendar</a> is published and boring. A bidder promising the same scope in three days is not "
"faster; they are skipping the days you cannot see.</p>",

two_col(
 'Green flags worth noticing',
 ['Names products unprompted &mdash; membrane, mortar, grout',
  'Puts the flood test on the schedule without being asked',
  'Contingency rate for discoveries, in the contract',
  'Asks about your subfloor and house age before quoting',
  'Sends the insurance certificate the same day you ask',
  'Talks you out of something &mdash; a pricier tile, a needless demo'],
 'Red flags that predict the ending',
 ['Big cash discount for skipping the paperwork',
  'A deposit far out of proportion to materials',
  '&ldquo;We can start tomorrow&rdquo; from a quality crew in February',
  'No physical visit before a firm number on a shower',
  'Vague line items: &ldquo;materials&rdquo;, &ldquo;prep as needed&rdquo;',
  'Pressure to sign today because the price expires']),

'<h2>The Conversation About Money, Had Correctly</h2>',

"<p>A fair tile contract in Seattle has a shape: a modest deposit that roughly tracks materials, progress payments tied to milestones you can verify &mdash; "
"waterproofing done and flood test passed is a natural one &mdash; and a final payment after the walkthrough, not before. Be suspicious of large up-front demands, "
"and be equally fair in the other direction: a contractor who has passed your flood-test milestone has done the majority of the invisible work and earned the "
"progress payment. Get the warranty in writing with the final invoice, along with the flood-test photos and the product names that went into your walls. That "
"folder is worth real money when you sell the house.</p>",

"<p>And a note on chemistry, because it is underrated: you are letting this crew into your home for a week or two. The installer who returns calls before the "
"contract is signed is the one who will return them after. The one who explains trade-offs &mdash; <a href=\"/blog/epoxy-vs-cement-grout\">epoxy versus cement "
"grout</a>, niche placement, where the cut tiles should land &mdash; is the one whose judgment you are actually buying.</p>",

'<h2>Where We Fit, Honestly</h2>',

"<p>We are one of the companies you would be comparing, so weigh this paragraph accordingly &mdash; but the reason we published the questions above is that we like "
"how we score on them. Every shower gets a pre-slope, a bonded membrane, and a photographed 24-hour flood test kept on file; the work carries a 2-year warranty; "
"the contingency rate is in the contract before demolition. If you want us in your stack of bids, the scope and neighborhoods are on the "
"<a href=\"/seattle/tile-installation-in-seattle-wa\">Seattle tile installation page</a> &mdash; and if you already have a bidder who answers every question above "
"cleanly, hire them with our blessing. The point of the list is that somebody answers it.</p>",

faq('Hiring a Tile Installer in Seattle: What Homeowners Ask Us', [
 ('How do I verify a tile contractor is licensed in Washington?',
  'Use the Department of Labor & Industries "Verify a Contractor" search — it is free and public. Check that the registration is active, the bond and liability insurance are current, and look at whether there are actions against the bond. It takes two minutes and filters out the riskiest hires before a single conversation.'),
 ('What questions should I ask before hiring a tile installer?',
  'Three matter most: name the waterproofing membrane you will use; do you flood-test the shower pan for 24 hours and can I see it; and what is your rate for what demolition uncovers. Installers who answer all three instantly and specifically are rare, and they are the ones worth paying.'),
 ('How much does tile installation cost in Seattle?',
  'Installed tile work runs $14–$26 per square foot, with labor from $11 per square foot, depending on the tile, the layout, and the condition of what is underneath. Showers cost more per square foot than floors because the waterproofing assembly is most of the labor. A bid far below that range is describing a smaller job than the one you need.'),
 ('Why do tile quotes vary so much between contractors?',
  'Because they describe different jobs. The spread is almost never the tile — it is substrate prep, the membrane, the flood test, silicone details, and whether a contingency for hidden damage is priced now or sprung on you later. Ask each bidder the membrane and flood-test questions and the spread usually explains itself.'),
 ('Should I buy the tile myself and just hire labor?',
  'You can, and we work that way often. Buy from a real tile supplier, order 10–15% overage for cuts and breakage, and confirm the installer sees the tile before quoting — large format, natural stone and mosaics each change the labor. Let the installer supply the setting materials and membrane; that is where their system lives.'),
 ('Is a handyman okay for a small tile job?',
  'For a backsplash or a laundry floor, a skilled handyman can be honest value. For anything in a shower, no — wet-area tile is a system, and the cost of a failed membrane is a rebuilt bathroom plus whatever the leak ruined below it. Match the hire to the consequence of failure, not the size of the room.'),
 ('What deposit is normal for tile work in Seattle?',
  'Enough to cover materials and scheduling commitment — commonly 10–30% depending on how much product the job requires. Progress payments should follow verifiable milestones, like a passed flood test, with the final payment after walkthrough. Treat requests for most of the money up front as the red flag it is.'),
 ('What should I get in writing when the job is done?',
  'The warranty, the flood-test photos, and the names of the products in your walls — membrane, mortar, grout. Keep them with the house documents. They are the proof of what was done correctly, they matter for any warranty conversation, and they answer the exact questions the next owner’s inspector will ask.'),
]),

cta('Interview Us With the Hard Questions',
    'Membrane by name, a photographed 24-hour flood test, a contingency rate in the contract, and a 2-year warranty &mdash; we built the checklist because we like our answers to it. Free in-home estimates across King &amp; Snohomish County.'),

related([
 ('/blog/tile-shower-waterproofing', 'How a tile shower is waterproofed'),
 ('/blog/bathroom-tile-installation-cost-seattle', 'Bathroom tile installation cost in Seattle'),
 ('/blog/how-long-to-tile-a-bathroom', 'How long a bathroom takes to tile'),
 ('/blog/why-tile-floors-crack', 'Why tile floors crack'),
 ('/seattle/tile-installation-in-seattle-wa', 'Tile installation in Seattle'),
 ('/contact', 'Book a free estimate'),
]),
]

assemble(S, parts)
