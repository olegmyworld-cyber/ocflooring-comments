from builder import *

S = 'carpet-warranty-explained'

parts = [
date_badge('January 28, 2027'),

quick_answer(
 "<strong>A carpet warranty is not one promise &mdash; it is three separate ones (wear, stain, and texture retention), each with its own exclusions, "
 "and most claims die on the maintenance clauses, not the coverage.</strong> Nearly every manufacturer warranty quietly requires professional "
 "hot-water extraction on a schedule, with receipts, and classifies the most common complaints &mdash; matting in the hallway, traffic-lane "
 "shading &mdash; as things it never covered in the first place. Read the document before you buy, then put your real protection where it "
 "actually lives: in the fiber and the pad you choose.",
 'Mill Creek &amp; Snohomish County'),

facts([
 ('3 warranties', 'hide inside every "carpet warranty" &mdash; wear, stain, and texture retention are separate coverages with separate definitions and separate exclusions. A claim filed under the wrong one is denied on arrival.'),
 ('12&ndash;18 months', 'the professional hot-water extraction cadence most warranties quietly require. No receipts, no claim &mdash; this single clause kills more claims than every exclusion combined.'),
 ('From $1.49/sq ft', 'installed carpet with us, pad and labor included. The fiber and pad you pick at that table protect you from far more than any paragraph of coverage ever will.'),
]),

'<h2>The Three Warranties Hiding in One Document</h2>',

"<p>When a salesperson says a carpet has a &ldquo;25-year warranty,&rdquo; they are compressing three different documents into one comforting number. "
"They cover different failures, they are voided by different things, and the one you will actually want someday is usually the shortest.</p>",

"<p><strong>The wear warranty</strong> covers abrasive wear &mdash; fiber actually gone, worn through to the backing. Read the definition and you will find it "
"means physical loss of fiber, not crushing, not flattening, not the pale traffic lane in front of the couch. Carpet that looks exhausted but still has its "
"fiber is not &ldquo;worn&rdquo; by warranty math. Genuine wear-through is rare on any decent carpet, which is why this number is so long and so loudly advertised.</p>",

"<p><strong>The stain warranty</strong> covers staining from a defined list of substances &mdash; and the exclusion list is where the honesty lives. Oil-based spills, "
"pet accidents on non-pet lines, dye transfer, bleach, and anything &ldquo;not promptly treated&rdquo; are typically out. "
"<strong>The texture-retention warranty</strong> covers the tuft losing its twist and matting down; it is usually the shortest of the three and the most "
"prorated, and it is exactly the failure a busy household is most likely to see.</p>",

table('What Each Coverage Actually Means', ['Coverage', 'What it covers', 'What it quietly excludes'], [
 ('<strong>Wear</strong>', 'Fiber loss &mdash; worn through to the backing', 'Crushing, matting, flattening, traffic-lane shading &mdash; the things people actually mean by "worn out"'),
 ('<strong>Stain</strong>', 'Stains from listed household substances', 'Oil-based spills, pet accidents on standard lines, dye transfer, bleach, anything not treated promptly'),
 ('<strong>Texture retention</strong>', 'Tufts losing twist and matting', 'Stairs and hallways are often excluded outright &mdash; the places texture fails first'),
 ('<strong>Manufacturing defects</strong>', 'Delamination, tuft loss, streaks from the mill', 'Usually solid coverage, but short &mdash; and it requires proper installation to stay valid'),
 ('<strong>Installation workmanship</strong>', 'Seams, stretching, transitions', 'Not the manufacturer&rsquo;s problem at all &mdash; this one comes from your installer, in writing'),
]),

'<h2>The Maintenance Clauses That Void Claims</h2>',

"<p>Here is the part almost nobody reads until they are angry. Somewhere in the fine print, nearly every carpet warranty requires "
"<strong>professional hot-water extraction every 12&ndash;18 months, performed by a certified cleaner, with receipts you kept</strong>. File a claim "
"in year six and the first thing the manufacturer asks for is your cleaning records. No receipts, no claim &mdash; and the carpet itself never even "
"gets inspected.</p>",

"<p>The same section usually requires regular vacuuming with an approved machine, prompt treatment of spills with approved products, and a pad that "
"meets the manufacturer&rsquo;s spec. That last one matters more than it looks: install premium carpet over the wrong pad and some warranties are void "
"from day one, before the first footstep. It is one more reason the pad conversation &mdash; which we walk through in our guide to "
"<a href=\"/blog/carpet-padding-thickness\">carpet padding thickness and grades</a> &mdash; belongs at the front of the purchase, not the end.</p>",

"<p>None of this is a scam, exactly. Grit genuinely does cut fiber, and a carpet that is never professionally cleaned genuinely does fail early. But you "
"should walk in knowing that the warranty is, in practice, a maintenance contract: the manufacturer promises to stand behind the carpet as long as you can "
"prove you did everything right. Budget for the cleanings, keep a folder, or treat the warranty as decoration.</p>",

'<h2>What &ldquo;Lifetime&rdquo; Actually Means</h2>',

"<p>&ldquo;Lifetime&rdquo; is the most successful word in flooring marketing, and it means less than it sounds like. It is not your lifetime, and not the "
"house&rsquo;s &mdash; it is the <em>useful life of the carpet as the manufacturer defines it</em>, which the same document often defines as ending "
"exactly when the carpet no longer performs. A carpet that matted flat in year seven has, by that logic, reached the end of its life rather than failed "
"within it.</p>",

"<p>Add the usual limiters &mdash; original purchaser only, original installation location only, prorated recovery that shrinks every year, coverage that "
"pays for replacement material but not the labor to install it &mdash; and a lifetime warranty converges on a simple truth: it is a statement about the "
"brand&rsquo;s confidence, useful for comparing two carpets side by side, and a poor thing to lean on when something goes wrong. How long carpet really "
"lasts is a fiber-and-traffic question, and we lay out the honest numbers in <a href=\"/blog/how-long-does-carpet-last\">how long carpet lasts</a>.</p>",

'<h2>What Actually Protects You: Fiber and Pad</h2>',

"<p>After years of watching claims succeed and fail, our honest advice is this: <strong>buy the protection at the sample stage, not the paperwork "
"stage</strong>. The two decisions that decide how your carpet looks in year ten are the fiber and the pad &mdash; and neither one requires a "
"lawyer to read.</p>",

"<p>Fiber first. Solution-dyed fibers &mdash; triexta and solution-dyed nylon &mdash; carry their color all the way through the strand, so aggressive "
"cleaning cannot fade them, and their stain resistance is built into the polymer rather than sprayed on at the mill. That is protection no clause can "
"revoke. The full rundown is in our <a href=\"/blog/carpet-fiber-types\">carpet fiber guide</a>, and the specific case for engineered stain resistance "
"&mdash; and what &ldquo;stain-proof&rdquo; does and does not mean &mdash; is in "
"<a href=\"/blog/stain-resistant-carpet\">stain-resistant carpet, explained honestly</a>. For resilience in traffic lanes &mdash; the failure the "
"texture warranty is least likely to pay for &mdash; nylon and triexta simply outlast polyester, and no warranty on a budget fiber changes that.</p>",

"<p>Then the pad. A quality pad carries its own warranty, supports the carpet&rsquo;s, and does more for how the floor feels and wears than any coverage "
"tier. In pet households a moisture-barrier pad is the difference between an accident and a permanent problem &mdash; the whole argument is in "
"<a href=\"/blog/best-carpet-for-pets\">the best carpet for pets</a>. Cheap pad under premium carpet is the single most backwards line item in flooring.</p>",

two_col(
 'What keeps a claim alive',
 ['Professional hot-water extraction on schedule &mdash; receipts filed away',
  'The manufacturer-spec pad, named on your invoice',
  'Prompt spill treatment with approved cleaners',
  'The original invoice showing carpet line, color and location',
  'Professional installation you can document',
  'Reading the exclusions before you buy, not after the stain'],
 'What kills a claim before inspection',
 ['No cleaning receipts &mdash; the number one claim-killer by a mile',
  'Wrong pad, or no record of which pad went in',
  'Filing matting or shading under the wear warranty',
  'Pet accidents on a line that never covered them',
  'DIY or undocumented installation',
  'Expecting "lifetime" to mean your lifetime']),

'<h2>How We Handle Warranties in Mill Creek</h2>',

"<p>When the mobile showroom comes to your door in Mill Creek, the warranty conversation happens at your kitchen table with the actual documents, not a "
"brochure summary. We bring 20+ full-size samples and all three pad grades, and for the lines you shortlist we will tell you plainly which coverage is "
"meaningful and which is marketing &mdash; including when a cheaper carpet with a better fiber is the stronger buy than a longer warranty on a weaker one. "
"You get a free measure and a written price the same visit, with the carpet line and the pad named on the quote &mdash; which is exactly the paper trail a "
"future claim needs.</p>",

"<p>Installation matters to the manufacturer too: several coverages require professional installation to industry standards, and seam or stretch problems "
"are the installer&rsquo;s responsibility, never the mill&rsquo;s. Our work is covered by our own workmanship warranty, separate from anything the "
"manufacturer promises. The full local details are on our <a href=\"/city-of-mill-creek/carpet-installation-in-mill-creek-wa\">Mill Creek carpet "
"installation page</a>.</p>",

faq('Carpet Warranties: What Buyers Ask Us', [
 ('What does a carpet warranty actually cover?',
  'Three separate things, usually with separate terms: abrasive wear (fiber physically gone, not flattened), staining from a defined list of substances, and texture retention (tufts holding their twist). Each has its own exclusions, and installation problems like seams and stretching are never the manufacturer’s responsibility — those come from your installer’s workmanship warranty.'),
 ('Why do carpet warranty claims get denied?',
  'Most often on the maintenance clauses, not the damage itself. Nearly every warranty requires professional hot-water extraction every 12–18 months with receipts, an approved pad, and prompt spill treatment. Missing cleaning records is the single most common reason a claim dies before anyone inspects the carpet.'),
 ('What does a "lifetime" carpet warranty mean?',
  'The useful life of the carpet as the manufacturer defines it — not your lifetime. Combined with original-owner-only terms, proration that shrinks the payout every year, and coverage of material but not labor, a lifetime warranty is best read as a confidence signal for comparing carpets, not a safety net.'),
 ('Is matting in the traffic lanes covered by the wear warranty?',
  'Almost never. Wear warranties define wear as actual fiber loss — worn through to the backing — which is rare on any decent carpet. Matting and crushing fall under texture retention, which is typically shorter, heavily prorated, and often excludes stairs and hallways, the exact places texture fails first.'),
 ('Do I really need professional cleaning to keep the warranty valid?',
  'If the warranty says so, yes — and nearly all of them do. Hot-water extraction by a certified cleaner every 12 to 18 months, with receipts you keep, is the standard requirement. It is also genuinely good for the carpet, so we suggest treating it as real maintenance rather than a hoop.'),
 ('Does the pad affect the carpet warranty?',
  'Yes, more than most buyers realize. Manufacturers spec a minimum pad, and installing over the wrong one can void coverage from day one. A quality pad also carries its own warranty and does more for long-term appearance than any coverage tier. Get the pad named on your invoice.'),
 ('Are pet stains covered by a standard stain warranty?',
  'Usually not. Standard stain warranties list household food and beverage spills and exclude pet urine, oil-based messes, and dye transfer. Dedicated pet lines cover urine staining specifically — but even those class matting from a big dog as wear, not stain. Fiber choice is what protects you in the excluded categories.'),
 ('What protects my carpet better than the warranty?',
  'The fiber and the pad. Solution-dyed triexta or nylon resists stains and fading at the polymer level — protection no clause can revoke — and a quality pad determines how the carpet wears and feels for its whole life. We bring both conversations to your home with the samples, and put the carpet and pad in writing the same visit.'),
]),

cta('Read the Fine Print With Us',
    'The mobile showroom brings 20+ samples, all three pad grades, and straight answers about which warranty terms matter on the lines you like. Free measure and a written price the same visit, with the carpet and pad named on the quote. Serving Mill Creek and all of King &amp; Snohomish County.'),

related([
 ('/blog/carpet-fiber-types', 'Carpet fiber types, compared'),
 ('/blog/stain-resistant-carpet', 'Stain-resistant carpet, honestly'),
 ('/blog/best-carpet-for-pets', 'The best carpet for pets'),
 ('/blog/carpet-padding-thickness', 'Carpet padding thickness and grades'),
 ('/city-of-mill-creek/carpet-installation-in-mill-creek-wa', 'Carpet installation in Mill Creek'),
 ('/contact', 'Book a free estimate'),
]),
]

assemble(S, parts)
