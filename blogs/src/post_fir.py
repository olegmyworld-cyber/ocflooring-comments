from builder import *

slug = 'refinishing-fir-floors-old-seattle-homes'

qa_card = quick_answer(
    "<strong>Yes, the fir floors in your old Seattle house can almost certainly be refinished — and done right, old-growth Douglas fir refinishes into one of the most beautiful floors in the Northwest. The catches: fir is soft (about half as hard as oak), so it punishes aggressive sanding; it blotches under stain, so a natural finish is nearly always the right call; and a clear waterborne keeps its honey color from going orange.</strong> Here’s what a century of fir asks of the crew you hire — and of your expectations.",
    "Craftsman &amp; bungalow floors, 1900–1945")

intro = '''<p>Walk into a 1915 Ballard bungalow or a Wallingford Craftsman and pull back the wall-to-wall carpet, and odds are you’ll find tight, straight-grained Douglas fir — milled from old-growth timber that came off the hills around Puget Sound when this city was building itself. That wood doesn’t exist commercially anymore: today’s fir is fast-grown, wide-ringed, and noticeably softer. Which means the floor under that carpet is irreplaceable in the most literal sense, and the decision you make about who sands it is a one-way door. We’ve refinished a lot of these floors — they’re some of our favorite work — and this is the honest briefing we give their owners.</p>'''

facts_grid = facts([
    ("660", "Douglas fir’s Janka hardness rating, versus 1,290 for red oak. Translation: fir dents, and always has — the crew’s sanding technique matters twice as much on a floor half as hard."),
    ("100+ yrs", "the age of the fir in most Seattle Craftsman homes. Old-growth boards this tight-grained can’t be bought new; every sixteenth of an inch a sander removes is gone for good."),
    ("$3.99", "per sq ft for a full sand and natural finish — which is the finish fir nearly always wants. Stain upcharges rarely make sense here, and we’ll tell you why before you pay for one."),
])

h2_what = '''<h2>How to Tell It’s Fir (and Why the Distinction Matters)</h2>

<p>Fir announces itself: long, straight, closely spaced grain lines — often vertical-grain boards that look almost striped — in tones from pale honey to deep amber, usually in 3¼-inch or narrower strips. No oak flake, no cathedral swirls. Age deepens it; a century of light gives old fir a glow new floors can’t fake. The distinction matters because everything downstream — sanding pressure, grit sequence, stain decisions, even which finish chemistry — differs from the oak playbook most refinishers run all day. A crew that treats your fir like oak is the single most common way these floors get ruined, and it’s why we ask the age of the house before we quote — a habit we mention in <a href="/blog/5-questions-to-ask-before-refinishing-hardwood-floors">the five questions to ask any refinisher</a>. If your Craftsman has oak in the formal rooms and fir in the bedrooms — a common builder economy of the era — the two need different handling in the same job.</p>'''

h2_sanding = '''<h2>What Sanding a Soft Floor Actually Requires</h2>

<p>Softwood cuts fast. The same drum sander pass that politely levels an oak floor can dig a trench in fir, and the machine’s mistakes — chatter marks, stop marks, edger swirls — telegraph through a clear finish forever. On fir we run finer starting grits, lighter machine pressure, and a flat-sanding pass with the <a href="/blog/trio-sanding-machine-for-flat-floors">Trio machine</a> to blend field and edges without dips. There’s also a budget question hiding here: because fir cuts fast, a careless crew can take twice the wood a careful one does. Most old fir floors have been sanded before — some several times — and the wood above the tongue is a finite account you’re drawing down. A floor sanded gently has several refinishes left in it; one sanded brutally may be on its last. Our guides on <a href="/blog/how-many-times-can-a-wood-floor-be-sanded-and-refinished-in-the-seattle-wa-area">how many sandings a floor has left</a> and <a href="/blog/when-can-wood-floors-not-be-refinished">when a floor can’t be refinished</a> cover how we assess that before quoting.</p>'''

h2_stain = '''<h2>The Stain Conversation: Mostly, Don’t</h2>

<p>Fir absorbs stain the way it grew: unevenly. The dense latewood lines take color lightly while the softer earlywood drinks it in, and the result is blotch — a muddy, stripey look that no amount of extra coats fixes. Conditioners help some; they don’t make fir behave like oak. Our standing advice: let fir be fir. A natural finish on old-growth fir produces that warm honey floor people buy Craftsman houses hoping for, and it happens to be the cheaper service — $3.99/sq ft against $6.50 with stain, per our <a href="/blog/hardwood-floor-refinishing-cost-seattle-wa">Seattle refinishing cost guide</a>. The finish chemistry does the rest of the color work: a clear waterborne holds fir at honey; an oil-based finish ambers over the years and pushes a warm floor toward pumpkin orange — the full story is in our <a href="/blog/water-based-vs-oil-based-floor-finish">water-based vs oil-based comparison</a>. If you genuinely want a darker floor, ask us about toned finishes rather than penetrating stain — color in the coat, not in the wood, applied evenly by design.</p>'''

h2_repairs = '''<h2>Patches, Repairs, and the Parts Sanding Can’t Fix</h2>

<p>Century-old floors carry century-old scars: radiator burns, pipe holes from heating conversions, wall-removal seams, pet stains that went black, water marks by long-gone iceboxes. Some of this sands out; the deep and black stains usually don’t. The good news is that fir repairs can be nearly invisible — done right. The trick is matching not just species but grain: new-growth fir from the lumberyard sits wide-ringed and bright next to old-growth boards, so for prominent repairs we source reclaimed old fir, often salvaged from other Seattle-era houses, and weave replacement boards into the field rather than dropping in an obvious rectangle. Expect a board-by-board repair list in any serious quote — it’s in the line items for a reason, and it’s the difference between a patch you show off and one you put a rug over. What repairs cost and how they’re listed is covered in our <a href="/blog/cost-to-refinish-hardwood-floors">line-by-line budget guide</a>.</p>'''

expectations = two_col(
    "What refinished fir gives you",
    ["A floor with grain and color no modern material reproduces",
     "Warm honey tones that deepen beautifully under a clear finish",
     "Near-invisible repairs, when patched with matched reclaimed stock",
     "Character — the gentle wear of a century, kept rather than erased",
     "Real value: natural finish is the budget option and the best-looking one here"],
    "What it won’t give you",
    ["Oak’s dent resistance — chair legs and dog claws will leave their marks in time",
     "A stain-sampled designer color — penetrating stain and fir end in blotch",
     "Perfectly gapless boards — a century of seasons built those gaps; they’re staying",
     "A poured-plastic showroom floor — old fir is a patina floor, not a gloss floor",
     "Survival under a careless crew — this is the wrong project for the cheapest bid"])

h2_local = '''<h2>A Seattle Floor, Specifically</h2>

<p>These floors cluster exactly where the streetcar suburbs grew: Ballard, Wallingford, Queen Anne, Fremont, West Seattle, Beacon Hill — and the same era of housing runs north through <a href="/hardwood-floor-refinishing-in-edmonds-wa">Edmonds</a> and the mill-town blocks of <a href="/hardwood-floor-refinishing-in-everett-wa">Everett</a>. We refinish fir across all of it; if you’re in one of these houses, our <a href="/hardwood-floor-refinishing-in-seattle-wa">Seattle hardwood floor refinishing</a> page covers how we work and what it costs. One planning note that surprises owners: because fir wants a natural finish and no stain day, the schedule is usually a day shorter than an oak-with-stain project — sanding, then coats, socks that evening. And if part of your fir is sun-faded where rugs and windows drew their lines, that’s normal and it sands out — more in our <a href="/blog/sun-damaged-hardwood-floors">sun-damaged floors guide</a>.</p>'''

faq_block = faq("Old Fir Floors: What Owners Ask Us", [
    ("Can 100-year-old fir floors really be refinished?",
     "Almost always, yes. The wood in pre-war Seattle homes is old-growth Douglas fir — dense, tight-grained, and typically thick enough for another refinish even after previous sandings. The real question is how much wear layer remains above the tongue, which we check board-level during the estimate before promising anything."),
    ("Are fir floors too soft to be worth refinishing?",
     "Fir is soft — about 660 on the Janka scale against red oak's 1,290 — but soft and fragile aren't the same thing. These floors have carried a century of life already. Refinished with proper technique and a tough waterborne topcoat, they'll carry decades more; they'll just collect dents as part of the deal, the way they always have."),
    ("Can you stain fir floors a dark color?",
     "We advise against penetrating stain on fir: the grain absorbs unevenly and blotches, and no technique fully prevents it. If you want a darker floor, toned finishes — color carried in the coating layers rather than soaked into the wood — get you there evenly. But most owners who see fir sanded raw choose natural on the spot."),
    ("What finish is best on old Douglas fir?",
     "A clear commercial waterborne, two to three coats, usually in satin or matte. It keeps fir's honey color true instead of ambering it toward orange, it's low-odor for the occupied homes these usually are, and modern two-component grades add serious wear resistance to a soft floor that can use the help."),
    ("What does refinishing fir floors cost in Seattle?",
     "The same as our standard rates: $3.99/sq ft for a full sand with natural finish — which is the right service for nearly every fir floor — with a 500 sq ft project minimum, stairs at $55–$75 per tread, and board repairs itemized after an on-site look. Skipping stain means fir usually lands at the budget-friendly end of refinishing."),
    ("Should the gaps between boards be filled?",
     "Mostly no. A century of seasonal movement built those gaps, and rigid filler troweled across a whole fir floor cracks out within a few winters as the boards keep moving. We fill defects — knots, splits, nail holes — and leave honest seasonal gaps alone. A floor that moves is a floor that's alive; fighting it makes a mess."),
    ("Can you match and repair damaged boards in old fir?",
     "Yes, and it's some of the most satisfying work we do. New lumberyard fir doesn't match old-growth grain, so for visible areas we use reclaimed old fir and lace boards into the existing field rather than patching in a rectangle. After sanding and finish, a well-matched repair takes guests a while to find."),
    ("Is it better to just replace old fir with new hardwood?",
     "If you want oak's hardness or a stained designer color, replacement is the honest path — but you'd be removing wood that cannot be bought again to install wood that can. For most owners of these homes, refinishing costs less, keeps the house's character, and produces a floor no new material matches. We'll price both paths if you're torn."),
])

cta_block = cta("Your Fir Deserves a Crew That’s Met It Before",
    "We’ve been refinishing pre-war fir across Seattle and Snohomish County since 2013 — gentle sanding, matched reclaimed repairs, and clear finishes that keep the honey where it belongs. Free in-home estimates, board-level honesty.")

related_block = related([
    ("/blog/hardwood-floor-refinishing-cost-seattle-wa", "Seattle refinishing costs, 2026"),
    ("/blog/how-many-times-can-a-wood-floor-be-sanded-and-refinished-in-the-seattle-wa-area", "How many sandings does a floor have left"),
    ("/blog/water-based-vs-oil-based-floor-finish", "Water-based vs oil-based finishes"),
    ("/hardwood-floor-refinishing-in-seattle-wa", "Hardwood floor refinishing in Seattle"),
    ("/contact", "Book a free estimate"),
])

assemble(slug, [date_badge('August 28, 2026'), qa_card, intro, facts_grid, h2_what, h2_sanding, h2_stain, h2_repairs,
                '<h2>Expectations, Honestly Set</h2>', expectations, h2_local, faq_block, cta_block, related_block])

meta = {
  "name": "Refinishing Fir Floors in Old Seattle Homes: An Owner's Guide",
  "slug": slug,
  "title-tag": "Refinishing Fir Floors in Old Seattle Homes | OC Flooring",
  "meta-description": "Old-growth Douglas fir in your Craftsman or bungalow? Why fir punishes rough sanding, why natural beats stain, and what refinishing costs in Seattle.",
  "post-summary": "The fir under your Craftsman's carpet is old-growth wood that can't be bought anymore — and it refinishes beautifully if the crew respects how soft it is. Why gentle sanding matters twice as much at 660 Janka, why stain blotches and natural wins, how reclaimed-board repairs disappear, and what it all costs in Seattle.",
  "blog-category": "6a4d865c243ea1352fa4d559"
}
json.dump(meta, open(slug + '.meta.json', 'w'), indent=1)
print('meta written; title-tag len', len(meta['title-tag']), '| meta-desc len', len(meta['meta-description']))
