import json
from datetime import date, timedelta

CAT = {
 'refinish':'6a4d865c243ea1352fa4d555','species':'6a4d865c243ea1352fa4d559',
 'cost':'6a4d865c243ea1352fa4d55d','care':'6a4d865c243ea1352fa4d55f',
 'local':'6a4d865c243ea1352fa4d561','install':'6a4d865c243ea1352fa4d557',
}
# (topic#, name, slug, category, city or None=general)
# Ordered publish queue. Weeks 2-8 as committed in the calendar, then the rest.
Q = [
 (5,"Bona Traffic HD vs Pallmann Pall-X: A Kirkland Contractor's Comparison","bona-traffic-hd-vs-pallmann-pall-x",'refinish','Kirkland'),
 (62,"Sandless Refinishing: Does It Actually Work? A Renton Reality Check","sandless-hardwood-floor-refinishing-does-it-work",'refinish','Renton'),
 (67,"Can Engineered Hardwood Be Refinished? Check the Wear Layer (Sammamish Guide)","can-engineered-hardwood-be-refinished-wear-layer",'refinish','Sammamish'),
 (77,"Refinishing a Mercer Island Waterfront Home","refinishing-mercer-island-waterfront-home",'local','Mercer Island'),
 (38,"How Long Before You Can Walk on Refinished Floors? A Redmond Timeline","how-long-before-you-can-walk-on-refinished-floors",'refinish','Redmond'),
 (11,"How to Restore Faded, Sun-Damaged Hardwood Floors in Edmonds Homes","restore-faded-sun-damaged-hardwood-floors",'refinish','Edmonds'),
 (92,"Gymnasium Floor Refinishing in Seattle: Process and Scheduling","gymnasium-floor-refinishing-seattle",'refinish','Seattle'),
 (55,"How Stair Refinishing Is Priced in Bellevue, and Why It's Per-Step","stair-refinishing-cost-per-step",'cost','Bellevue'),
 (3,"Matte, Satin, or Semi-Gloss: Choosing a Hardwood Floor Sheen","matte-satin-semi-gloss-hardwood-floor-sheen",'refinish',None),
 (75,"Refinishing Floors in a 1920s Seattle Bungalow","refinishing-floors-1920s-seattle-bungalow",'local','Seattle'),
 (50,"What Makes One Lynnwood Refinishing Quote $2/sqft and Another $6","refinishing-quote-2-vs-6-per-sqft",'cost','Lynnwood'),
 (65,"Hardwood Refinishing vs Wood Floor Cleaning Services in Everett","hardwood-refinishing-vs-floor-cleaning-services",'refinish','Everett'),
 (81,"Condo Refinishing in Bellevue: HOA Rules and Noise Windows","condo-hardwood-refinishing-bellevue-hoa",'local','Bellevue'),
 (30,"Douglas Fir vs Oak in an Older Seattle Craftsman Home","douglas-fir-vs-oak-craftsman-home",'species','Seattle'),
 (17,"Deep vs Surface Scratches: Which Need a Full Refinish","deep-vs-surface-scratches-hardwood-refinish",'refinish',None),
 (82,"Should You Refinish Floors Before Listing Your Kirkland Home","refinish-floors-before-listing-home",'local','Kirkland'),
 (72,"Best Time of Year to Refinish Floors in Everett and Western Washington","best-time-of-year-refinish-floors-western-washington",'local','Everett'),
 (21,"Pet Scratches on Hardwood in Renton: Repair, Recoat, or Refinish","pet-scratches-hardwood-repair-recoat-refinish",'refinish','Renton'),
 (84,"Flooring Decisions for Fix-and-Flip Investors in Renton and King County","fix-and-flip-flooring-king-county",'local','Renton'),
 (63,"Buff and Coat vs Full Sand in Sammamish: An Honest Comparison","buff-and-coat-vs-full-sand-refinishing",'refinish','Sammamish'),
 (44,"Refinishing an Occupied Redmond Home: Room-by-Room Scheduling","refinishing-occupied-home-room-by-room",'refinish','Redmond'),
 # ---- beyond week 8: interleaved categories, GSC city rotation ----
 (7,"Why Natural (No Stain) Is the Most Popular Finish in Seattle Homes","natural-no-stain-hardwood-finish-seattle",'refinish','Seattle'),
 (12,"Cupped Hardwood Floors in Everett: Causes, and Whether Refinishing Fixes It","cupped-hardwood-floors-causes-refinishing",'refinish','Everett'),
 (52,"Refinish vs Replace: Running the Numbers on 800 sqft of Bellevue Oak","refinish-vs-replace-800-sqft-oak",'cost','Bellevue'),
 (29,"Refinishing Hickory in Sammamish: Why the Grain Fights You","refinishing-hickory-floors-grain",'species','Sammamish'),
 (39,"What the Smell During Refinishing Is, and How Long It Lasts","refinishing-smell-how-long-it-lasts",'refinish',None),
 (86,"Cheapest Floor Upgrade That Still Passes a Kirkland Buyer Inspection","cheapest-floor-upgrade-buyer-inspection",'local','Kirkland'),
 (13,"Buckled Hardwood After a Leak in Renton: Repair or Replace","buckled-hardwood-after-leak-repair-replace",'refinish','Renton'),
 (97,"How to Clean Refinished Hardwood in Redmond Without Voiding the Warranty","clean-refinished-hardwood-without-voiding-warranty",'care','Redmond'),
 (35,"Wide Plank Hardwood in Mercer Island Homes: Special Considerations","wide-plank-hardwood-refinishing-considerations",'species','Mercer Island'),
 (53,"Hidden Costs in Lynnwood Refinishing Quotes to Watch For","hidden-costs-refinishing-quotes",'cost','Lynnwood'),
 (40,"Do You Need to Leave Your House During Refinishing?","do-you-need-to-leave-house-during-refinishing",'refinish',None),
 (14,"Black Stains on Hardwood in Edmonds: What They Are, Can They Be Sanded Out","black-stains-hardwood-can-they-be-sanded-out",'refinish','Edmonds'),
 (87,"What Home Inspectors Flag on Hardwood Floors in Seattle","what-home-inspectors-flag-hardwood-floors",'local','Seattle'),
 (66,"Drum vs Belt vs Orbital Sander: What Your Everett Contractor Uses","drum-belt-orbital-sander-comparison",'refinish','Everett'),
 (41,"How Many Times Can a Bellevue Hardwood Floor Be Refinished","how-many-times-can-hardwood-floor-be-refinished",'refinish','Bellevue'),
 (98,"Best and Worst Cleaners for Hardwood Floors","best-and-worst-cleaners-hardwood-floors",'care',None),
 (33,"Ash Hardwood Floors in Kirkland: Refinishing and Staining Notes","ash-hardwood-floors-refinishing-staining",'species','Kirkland'),
 (54,"Is Recoating Worth It in Renton, or Just Delaying the Real Cost","is-recoating-worth-it-or-delaying-cost",'cost','Renton'),
 (42,"What Happens to Your Baseboards During a Sammamish Refinish","what-happens-to-baseboards-during-refinish",'refinish','Sammamish'),
 (15,"Squeaky Hardwood Floors in Redmond: Why Refinishing Won't Fix It","squeaky-hardwood-floors-refinishing-wont-fix",'refinish','Redmond'),
 (73,"Refinishing During Seattle's Rainy Season","refinishing-during-seattle-rainy-season",'local','Seattle'),
 (68,"Refinishing vs Installing New Prefinished Hardwood in Everett","refinishing-vs-installing-new-prefinished-hardwood",'refinish','Everett'),
 (99,"Rugs and Rug Pads That Don't Damage Your Finish","rugs-and-rug-pads-that-dont-damage-finish",'care',None),
 (27,"Refinishing Parquet Floors in Bellevue: What's Possible and What Isn't","refinishing-parquet-floors-whats-possible",'species','Bellevue'),
 (56,"Minimum Job Sizes in Lynnwood: Why Small Jobs Cost More Per Foot","minimum-job-sizes-small-refinishing-jobs",'cost','Lynnwood'),
 (45,"What Contractors Do About HVAC and Dust Control in Mercer Island Homes","hvac-dust-control-during-refinishing",'refinish','Mercer Island'),
 (16,"White Cloudy Spots on Hardwood Floors in Edmonds Homes","white-cloudy-spots-hardwood-floors",'refinish','Edmonds'),
 (85,"Refinishing Rental Hardwood Between Tenants in Renton","refinishing-rental-hardwood-between-tenants",'local','Renton'),
 (69,"Screen and Recoat vs Chemical Abrasion Systems","screen-recoat-vs-chemical-abrasion",'refinish',None),
 (34,"Pine Floors in Century Homes: Refinishing Softwood in Seattle","pine-floors-century-homes-refinishing",'species','Seattle'),
 (57,"What a Kirkland Refinishing Deposit Should and Shouldn't Cover","refinishing-deposit-what-it-should-cover",'cost','Kirkland'),
 (46,"Handling Transitions Between Rooms and Flooring Types in Redmond","flooring-transitions-between-rooms",'refinish','Redmond'),
 (18,"Sticky Hardwood Floors After Cleaning in Everett: What Went Wrong","sticky-hardwood-floors-after-cleaning",'care','Everett'),
 (89,"Staging on Newly Refinished Floors in Bellevue: What Not to Do","staging-on-newly-refinished-floors",'local','Bellevue'),
 (28,"Bamboo Floor Refinishing in Sammamish: When It Works and When It Doesn't","bamboo-floor-refinishing-when-it-works",'species','Sammamish'),
 (100,"A 10-Year Maintenance Plan for Newly Refinished Floors","10-year-maintenance-plan-refinished-floors",'care',None),
 (47,"Can You Refinish Hardwood Under Kitchen Cabinets in Lynnwood Homes","refinish-hardwood-under-kitchen-cabinets",'refinish','Lynnwood'),
 (19,"Peeling or Flaking Floor Finish in Seattle: Why It Happens","peeling-flaking-floor-finish-why",'refinish','Seattle'),
 (58,"Does Homeowners Insurance Cover Hardwood Floor Damage in Everett","homeowners-insurance-hardwood-floor-damage",'cost','Everett'),
 (36,"Herringbone and Chevron in Mercer Island Homes: Sanding Patterned Floors","herringbone-chevron-sanding-patterned-floors",'species','Mercer Island'),
 (48,"Refinishing Around Radiators, Vents, and Built-Ins in Edmonds Homes","refinishing-around-radiators-vents-built-ins",'refinish','Edmonds'),
 (88,"Refinishing Timeline When You're Under Contract on a Kirkland Sale","refinishing-timeline-under-contract",'local','Kirkland'),
 (20,"Water Rings and Heat Marks on Hardwood","water-rings-heat-marks-hardwood",'care',None),
 (70,"Site-Finished vs Factory-Finished in Renton: The Long-Term Reality","site-finished-vs-factory-finished-long-term",'refinish','Renton'),
 (59,"When a Cheap Redmond Refinishing Quote Costs You More Later","when-cheap-refinishing-quote-costs-more",'cost','Redmond'),
 (80,"Old-Growth Fir in Ballard and Queen Anne Homes","old-growth-fir-ballard-queen-anne",'local','Seattle'),
 (49,"Why Your Refinished Floor Looks Different Room to Room in Bellevue","refinished-floor-looks-different-room-to-room",'refinish','Bellevue'),
 (22,"Worn Traffic Paths in Everett Hardwood: Can You Fix Just That Area","worn-traffic-paths-hardwood-spot-fix",'refinish','Everett'),
 (93,"Restaurant and Bar Hardwood in Seattle: Refinishing Around Service Hours","restaurant-bar-hardwood-refinishing",'refinish','Seattle'),
 (8,"Penetrating Oil Finishes in Sammamish: Pros, Cons, and Maintenance Reality","penetrating-oil-finish-pros-cons-maintenance",'refinish','Sammamish'),
 (23,"Uneven Color From a Previous Refinish in Lynnwood: Can It Be Corrected","uneven-color-previous-refinish-corrected",'refinish','Lynnwood'),
 (90,"Refinishing for Landlords in Everett: Durability Over Beauty","refinishing-for-landlords-durability",'local','Everett'),
 (4,"How Many Coats of Finish Does a Hardwood Floor Actually Need","how-many-coats-of-finish-hardwood-floor",'refinish',None),
 (31,"Can Cork Floors Be Refinished? A Kirkland Homeowner's Guide","can-cork-floors-be-refinished",'species','Kirkland'),
 (74,"Why Puget Sound Humidity Changes Your Everett Refinishing Schedule","puget-sound-humidity-refinishing-schedule",'local','Everett'),
 (24,"Nail Holes, Gouges, and Filler in Renton Floors: What Sanding Can't Hide","nail-holes-gouges-filler-what-sanding-cant-hide",'refinish','Renton'),
 (94,"Office and Retail Hardwood Refinishing in Seattle","office-retail-hardwood-refinishing-seattle",'refinish','Seattle'),
 (6,"Hardwood Sealer vs Finish: What's the Difference","hardwood-sealer-vs-finish-difference",'refinish',None),
 (32,"Refinishing Walnut in Mercer Island Homes Without Losing the Color","refinishing-walnut-without-losing-color",'species','Mercer Island'),
 (60,"Refinishing Cost by Room in Bellevue: Kitchen, Stairs, Hallway, Bedroom","refinishing-cost-by-room",'cost','Bellevue'),
 (43,"Should You Refinish Before or After Painting in Redmond","refinish-before-or-after-painting",'refinish','Redmond'),
 (76,"Eastside vs Seattle Homes: Different Floors, Different Problems","eastside-vs-seattle-homes-different-floors",'local','Bellevue'),
 (25,"Mold Under Hardwood Floors in Edmonds: Signs and Next Steps","mold-under-hardwood-floors-signs",'refinish','Edmonds'),
 (95,"Church and Community Hall Floor Restoration in Everett","church-community-hall-floor-restoration",'refinish','Everett'),
 (9,"How Long Does a Hardwood Floor Finish Actually Last","how-long-does-hardwood-floor-finish-last",'refinish',None),
 (37,"Reclaimed Wood Floors in Seattle: Refinishing Without Killing the Character","reclaimed-wood-floors-refinishing-character",'species','Seattle'),
 (61,"What You're Actually Paying For in a Lynnwood Line-Item Estimate","line-item-refinishing-estimate-explained",'cost','Lynnwood'),
 (78,"Daylight Basement Floors in Renton and the Pacific Northwest","daylight-basement-floors-pacific-northwest",'local','Renton'),
 (91,"Do Kirkland Buyers Pay More for Natural vs Stained Floors","buyers-natural-vs-stained-floors",'local','Kirkland'),
 (51,"Why Square Footage Alone Doesn't Set Your Seattle Refinishing Price","square-footage-alone-doesnt-set-price",'cost','Seattle'),
 (64,"Refinishing vs Resurfacing vs Restoration: Terms Explained","refinishing-vs-resurfacing-vs-restoration-terms",'refinish',None),
 (10,"Whitewashed and Bleached Hardwood Floors: How They're Done","whitewashed-bleached-hardwood-floors",'refinish',None),
 (79,"Radiant Heat Under Hardwood in Redmond: Refinishing Considerations","radiant-heat-hardwood-refinishing",'refinish','Redmond'),
 (83,"What Refinished Floors Add to a Sammamish Appraisal","what-refinished-floors-add-to-appraisal",'local','Sammamish'),
 (96,"Commercial Refinishing Contracts in Bellevue: What Facility Managers Should Ask","commercial-refinishing-contracts-facility-managers",'refinish','Bellevue'),
 (71,"Pro Refinishing vs Rental Sander in Everett: What Actually Goes Wrong","pro-refinishing-vs-rental-sander",'refinish','Everett'),
]
assert len(Q)==97, len(Q)
assert len({s for _,_,s,_,_ in Q})==97, 'dup slug in plan'
existing={b['slug'] for b in json.load(open('blogs/plan/blog_index.json'))}
new3={'water-based-vs-oil-based-floor-finish','low-voc-hardwood-floor-finishes-kids-pets','refinishing-fir-floors-old-seattle-homes'}
for _,_,s,_,_ in Q:
    assert s not in existing and s not in new3, 'slug collision: '+s
gen=sum(1 for x in Q if x[4] is None)
print('general slots:', gen, '/97 ->', round(100*(97-gen)/97), '% city (rule: >=75%)')

# publish dates: Mon/Wed/Fri starting 2026-08-31
d=date(2026,8,31); dates=[]
while len(dates)<97:
    if d.weekday() in (0,2,4): dates.append(d.isoformat())
    d+=timedelta(days=1)
plan=[]
for i,(n,name,slug,cat,city) in enumerate(Q):
    plan.append({'seq':i+1,'topic':n,'name':name,'slug':slug,'category':CAT[cat],'catkey':cat,
                 'city':city,'publish_date':dates[i]})
json.dump(plan, open('blogs/plan/PLAN.json','w'), indent=1)
print('first:',plan[0]['publish_date'],'last:',plan[-1]['publish_date'])
# earlier-slug map for link ordering
open('blogs/plan/EXISTING-SLUGS.txt','w').write('\n'.join(sorted(existing|new3)))
