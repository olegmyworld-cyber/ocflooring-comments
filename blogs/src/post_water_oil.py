from builder import *

slug = 'water-based-vs-oil-based-floor-finish'

qa_card = quick_answer(
    "<strong>For most homes we refinish in Bellevue and across King and Snohomish County, water-based wins: it dries in hours instead of days, keeps the wood’s true color instead of turning amber, carries a fraction of the fumes, and — with a commercial two-component product like Bona Traffic HD — now outlasts oil-based poly in wear tests.</strong> Oil-based still earns its place when you want a warm amber tone on red oak and nobody’s living in the house during the work. Below: the honest trade-offs, line by line.",
    "Bellevue &amp; Eastside homes")

intro = '''<p>Ask three flooring contractors whether water-based or oil-based finish is better and you’ll get three confident, contradictory answers — usually matching whatever that contractor happens to spray. So let’s put the bias on the table first: we run waterborne systems (Bona and Pallmann) on nearly every floor we refinish, and we’ll explain exactly why. But we’ve also put down plenty of oil-modified polyurethane over the years, and there are floors — and homeowners — that oil genuinely suits better. This is the comparison we walk through at kitchen tables during estimates, minus the kitchen table.</p>

<p>One vocabulary note before the scorecard: “oil-based finish” in this article means oil-modified polyurethane, the amber-colored film finish sold in every hardware store — not penetrating hardwax oils like Rubio or WOCA, which are a different animal we’ll cover another week. Both waterborne and oil-modified poly build a protective plastic film on top of the wood; the argument is about what that film costs you in time, smell, and color.</p>'''

facts_grid = facts([
    ("2–3 hrs", "between coats with a waterborne finish — a full system goes down in one day. Oil-modified poly needs 8–24 hours per coat, so the same job stretches across three or four days."),
    ("~65 g/L", "VOC content of Bona Traffic HD, versus roughly 450–550 g/L for solvent-borne oil poly. That gap is the difference between sleeping at home during a refinish and booking a hotel."),
    ("7 days", "to full cure for a commercial waterborne — rugs and normal life resume in about a week. Oil-based keeps curing (and off-gassing) for 30 days."),
])

h2_scorecard = '<h2>The Scorecard: Water-Based vs Oil-Based, Line by Line</h2>'

compare_table = table(None,
    ["", "Water-based (waterborne)", "Oil-modified poly"],
    [
        ["<strong>Dry / recoat</strong>", "2–3 hours; walk in socks same evening", "8–24 hours per coat; days of drying"],
        ["<strong>Full cure</strong>", "About 7 days", "About 30 days"],
        ["<strong>Smell &amp; VOCs</strong>", "Low odor, ~65–150 g/L; occupied homes OK", "Strong solvent fumes, ~450–550 g/L"],
        ["<strong>Color day one</strong>", "Clear — wood stays its true color", "Warm amber cast immediately"],
        ["<strong>Color in 5 years</strong>", "Still clear, non-yellowing", "Progressively deeper amber/orange"],
        ["<strong>Durability</strong>", "Two-component commercial grades lead current wear tests", "Very good; the old ‘tougher’ reputation is outdated"],
        ["<strong>Coats per day</strong>", "2–3 — job finishes in 2–3 days total", "1 — same floor takes most of a week"],
        ["<strong>Material cost</strong>", "Higher per gallon (premium grades $100+)", "Cheaper per gallon ($40–60)"],
        ["<strong>Best on</strong>", "White oak, maple, fir, gray/neutral stains, natural looks", "Red oak, traditional amber looks, unoccupied projects"],
    ])

h2_water = '''<h2>What Water-Based Finish Actually Is (and Isn’t)</h2>

<p>Waterborne finish is polyurethane too — the urethane solids just hitch a ride on water instead of mineral spirits. When the water evaporates, what’s left on your floor is a hard, clear plastic film. Twenty years ago that film was genuinely softer than oil poly, and the “water-based doesn’t last” reputation was earned. It is no longer true, and it hasn’t been for a while: the commercial two-component waterbornes we use — <a href="/blog/bona-hd-the-ultimate-floor-finish-for-your-home">Bona Traffic HD</a> and <a href="/blog/pallmann-finish-the-ultimate-solution-for-your-hardwood-floors">Pallmann’s pro systems</a> — cross-link with a hardener and are what gets specified for restaurant floors and gym floors, which see more traffic in a month than your hallway sees in a year.</p>

<p>The honest downsides: premium waterborne costs real money per gallon (one reason quotes differ — a $2/sq ft quote is not buying Traffic HD), it’s less forgiving to apply in bad conditions, and on red oak some people miss the amber warmth — clear finish on red oak reads slightly pink to certain eyes. That last one is fixable with a toning sealer, which is exactly the conversation to have at the estimate.</p>'''

h2_oil = '''<h2>What Oil-Based Gets Right</h2>

<p>Oil-modified poly builds a beautiful, slightly flexible film with a warmth that flatters traditional red oak floors — the classic honey-colored “hardwood floor” look most Americans grew up on is red oak under ambered oil poly. It’s cheaper per gallon, it levels forgivingly, and small touch-ups blend a little easier into an already-amber floor. If you’re refinishing a 1970s Bellevue colonial with red oak throughout, nobody’s living there during the work, and you want that traditional glow, oil-based is a legitimate choice — this is the scenario where we’ll say so at the estimate.</p>

<p>What you accept in exchange: each coat needs 8–24 hours before the next, so a three-coat system stretches most of a week; solvent fumes strong enough that we tell families to stay elsewhere; a film that keeps yellowing for years, which fights every gray, white, or Scandinavian-pale look in existence; and a 30-day cure you have to baby with no rugs and careful furniture moves. On <a href="/blog/refinishing-fir-floors-old-seattle-homes">old Seattle fir</a>, oil poly’s amber can shove the floor all the way to orange — one of the most common “can you fix what the last guy did” calls we get.</p>'''

h2_color = '''<h2>The Color Question Is the Real Question</h2>

<p>Durability arguments between modern finishes are mostly settled; color is where homeowners actually live with the decision for fifteen years. Here’s the short version by floor: <strong>white oak</strong> — waterborne, nearly always, because ambering turns white oak yellow-green over time and ruins gray or neutral stains. <strong>Red oak</strong> — genuine taste call; oil’s amber reads traditional and hides red oak’s pink, while waterborne keeps it lighter and more modern. <strong>Douglas fir</strong> — waterborne; fir is already warm-toned and oil pushes it to pumpkin. <strong>Maple</strong> — waterborne; maple under oil goes unmistakably yellow. If you’re staining, the stain color you fell in love with on the sample board only survives under a non-yellowing finish — our guide to <a href="/blog/what-color-should-i-stain-my-wood-floors">choosing a stain color</a> goes deeper on this.</p>'''

h2_timeline = '''<h2>What Each Choice Does to Your Week</h2>

<p>The schedule difference is bigger than most homeowners expect, and it compounds with our <a href="/blog/hardwood-floor-refinishing-process-timeline">refinishing timeline</a> basics. With waterborne: sanding day one, finish system complete by day two or three, socks that evening, furniture at 48–72 hours, rugs in a week. You’re inconvenienced, not displaced. With oil-based: one coat per day at best — and in a Puget Sound November, “at best” is optimistic, because oil dry times stretch badly in cool, damp air. Same floor, most of a week of coats, then a month of tiptoeing while it cures, with the house smelling like a paint store for the first stretch. If you’re living in the home during the work — most of our clients are — that difference usually makes the decision by itself. For households with kids, pregnancy, asthma, or pets, it’s not close, and we wrote a whole guide to <a href="/blog/low-voc-hardwood-floor-finishes-kids-pets">low-VOC refinishing with kids and pets in the house</a>.</p>'''

choose = two_col(
    "Choose water-based when…",
    ["You’re living in the house during the refinish (kids, pets, lungs)",
     "The floor is white oak, maple, or old Seattle fir",
     "You’ve chosen a gray, white, natural, or any cool-toned stain",
     "You want the job — sanding to final coat — done in 2–3 days",
     "You want the color you see on day one to be the color in year ten"],
    "Oil-based earns it when…",
    ["Traditional amber warmth on red oak is exactly the look you want",
     "The house is empty — between tenants, pre-move-in, or a flip",
     "Schedule is loose: coats across a week, a month of gentle cure",
     "You’re matching existing ambered oil-finished floors elsewhere in the house",
     "Budget favors material cost over downtime (and you’ve priced the hotel nights honestly)"])

h2_local = '''<h2>The Pacific Northwest Footnote That Isn’t a Footnote</h2>

<p>Finish chemistry cares about weather, and ours is famously damp. Oil-modified poly dries by solvent evaporation plus oxidation, and both slow to a crawl in cool, humid air — an oil job that turns around in three days in Phoenix can drag past a week here between October and May. Waterborne cures more predictably indoors year-round with normal heat, which is a big part of why it’s become the default for <a href="/hardwood-floor-refinishing-in-seattle-wa">hardwood floor refinishing in Seattle</a> and across the Eastside — we see the same pattern on projects from Bellevue and <a href="/hardwood-floor-refinishing-in-kirkland-wa">Kirkland</a> to <a href="/hardwood-floor-refinishing-in-everett-wa">Everett</a>. Nowhere is the choice more one-sided than in Bellevue’s 1980s–2000s red oak homes: Eastside buyers expect the lighter, non-yellowed look, and a clear waterborne is how a floor keeps it. Our pricing doesn’t change with the finish debate, either: a full sand with natural finish runs $3.99/sq ft with our waterborne system — the complete numbers are in the <a href="/blog/how-much-does-it-cost-to-refinish-hardwood-floors">2026 refinishing cost guide</a>.</p>'''

faq_block = faq("Water-Based vs Oil-Based: What Homeowners Ask Us", [
    ("Is water-based floor finish as durable as oil-based?",
     "Modern commercial waterborne finishes are — and the two-component products like Bona Traffic HD now beat oil-modified polyurethane in abrasion testing. The old durability gap was real twenty years ago and closed since. What matters more than the base is the grade: a premium two-component waterborne outperforms both bargain waterborne and standard oil poly."),
    ("How long before we can walk on each finish?",
     "Waterborne: socks the same evening, shoes and furniture at 48 to 72 hours, rugs after about a week. Oil-based: 24 hours minimum before careful sock traffic on the final coat, several days for furniture, and a full month before rugs go down while it cures."),
    ("Does water-based finish change the color of the wood?",
     "Barely — it dries clear and stays clear, so the floor keeps the color of raw wood, just slightly deepened. Oil-based adds an amber tone immediately and keeps yellowing for years. On white oak, maple, and fir that ambering usually reads as unwanted yellow; on red oak some homeowners like the traditional warmth."),
    ("Can we stay in the house during refinishing?",
     "With the low-VOC waterborne systems we use, yes — most of our clients do, sleeping in the house the same night a coat goes down. With oil-based polyurethane we recommend staying elsewhere for at least the coating days, and longer for households with babies, asthma, or birds, which are especially sensitive to fumes."),
    ("Why is oil-based finish cheaper?",
     "The material is: $40 to $60 per gallon against $100-plus for premium waterborne. But labor runs longer because oil needs a day between coats, and you pay the difference in displacement — hotel nights, a week without the house working normally, a month of curing. Quoted professionally, the totals land closer than the per-gallon prices suggest."),
    ("Which finish is better for refinishing over a stain color?",
     "A non-yellowing waterborne. Any stain you chose from a sample — especially grays, whites, and cool browns — only stays that color under a clear finish. Ambering oil poly shifts every stain warmer within a few years, which is how gray floors turn green-ish and white floors turn cream."),
    ("What do you actually use on most floors?",
     "Bona and Pallmann waterborne systems, two to three coats with abrasion between them, chosen by traffic level and sheen. We'll happily spec oil-modified poly when a project genuinely calls for it — typically an unoccupied home with red oak and a traditional amber target — and we'll tell you at the estimate which one your floor is."),
    ("Does the sheen choice change any of this?",
     "No — matte, satin, and semi-gloss exist in both chemistries. Sheen is a separate decision from base, though it's worth knowing waterborne holds a true matte better over time because it doesn't amber. Satin remains the most popular choice on the floors we refinish."),
])

cta_block = cta("Still Torn? Bring Us the Question",
    "We’ll look at your species, your stain plans, and your household, and tell you which finish we’d put in our own house — with the schedule and price in writing. Free in-home estimates across King &amp; Snohomish County.")

related_block = related([
    ("/blog/bona-hd-the-ultimate-floor-finish-for-your-home", "Why we run Bona Traffic HD"),
    ("/blog/low-voc-hardwood-floor-finishes-kids-pets", "Low-VOC refinishing with kids and pets"),
    ("/blog/how-much-does-it-cost-to-refinish-hardwood-floors", "2026 refinishing cost guide"),
    ("/hardwood-floor-refinishing-in-seattle-wa", "Hardwood floor refinishing in Seattle"),
    ("/contact", "Book a free estimate"),
])

assemble(slug, [date_badge('August 28, 2026'), qa_card, intro, facts_grid, h2_scorecard, compare_table, h2_water, h2_oil, h2_color, h2_timeline,
                '<h2>The Decision, Compressed</h2>', choose, h2_local, faq_block, cta_block, related_block])

meta = {
  "name": "Water-Based vs Oil-Based Floor Finish: What Bellevue Homes Choose",
  "slug": slug,
  "title-tag": "Water-Based vs Oil-Based Floor Finish: A Bellevue, WA Guide",
  "meta-description": "Water-based or oil-based finish for your Bellevue home? A local refinishing contractor compares dry times, fumes, ambering, and durability, line by line.",
  "post-summary": "Water-based finishes dry in hours, stay clear for life, and — in commercial two-component grades — now out-wear oil-based poly. Oil still earns its place on red oak in empty houses. A comparison written for Bellevue and Eastside homes: schedule, smell, color in year ten, and what we'd put in our own house.",
  "blog-category": "6a4d865c243ea1352fa4d555"
}
json.dump(meta, open(slug + '.meta.json', 'w'), indent=1)
print('meta written; title-tag len', len(meta['title-tag']), '| meta-desc len', len(meta['meta-description']))
