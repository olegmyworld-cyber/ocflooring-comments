#!/usr/bin/env python3
"""Build the Tue=tile / Thu=carpet publishing plan through 2027-04-12.

Topics are anchored to keywords pulled from Semrush (volume / KD recorded per row so
the choice is auditable), and paired with a city by population weight -- and, where it
matters, by where the topic actually lands locally (condo soundproofing -> Seattle,
aging-in-place curbless showers -> Mercer Island, basements -> Renton, and so on).
Every city named here has a live tile- and carpet-installation service page.
"""
import json, datetime

# King + Snohomish cities that have BOTH a tile and a carpet service page, by population.
POP = {
 'Seattle':755000,'Bellevue':151000,'Everett':111000,'Renton':106000,'Kirkland':92000,
 'Redmond':73000,'Marysville':71000,'Sammamish':67000,'Shoreline':58000,'Bothell':48000,
 'Edmonds':42000,'Issaquah':40000,'Lynnwood':39000,'Lake Stevens':36000,'Mercer Island':25000,
 'Kenmore':23000,'Mukilteo':21000,'Mill Creek':21000,'Cottage Lake':21000,'Monroe':20000,
 'Snoqualmie':14000,'Woodinville':13000,'Newcastle':13000,'Snohomish':10000,'Duvall':8000,
 'North Bend':8000,'Medina':3000,
}

# (keyword, US volume, KD, title, city or None for a general post)
TILE = [
 ("bathroom tile installation cost",1600,21,"What Bathroom Tile Installation Really Costs in Seattle","Seattle"),
 ("tile installation cost per square foot",1600,14,"Tile Installation Cost Per Square Foot: A Bellevue Price Breakdown","Bellevue"),
 ("can you tile over tile",1900,10,"Can You Tile Over Existing Tile? When It Works and When It Fails",None),
 ("shower niche",14800,21,"Shower Niches Done Right: Placement, Size, and Waterproofing","Everett"),
 ("tile underlayment",2900,16,"Tile Underlayment Explained: Ditra, Cement Board, and What Goes Where",None),
 ("curbless shower",6600,36,"Curbless Showers in Mercer Island Homes: What the Build Actually Takes","Mercer Island"),
 ("porcelain vs ceramic tile",2400,26,"Porcelain vs Ceramic Tile: Which Belongs in a Renton Home","Renton"),
 ("bathroom floor tile ideas",5400,31,"Bathroom Floor Tile That Still Looks Right in Ten Years","Kirkland"),
 ("tile shower waterproofing",590,18,"Shower Waterproofing: The Layer That Decides Whether Your Tile Lasts","Redmond"),
 ("heated bathroom floor cost",390,21,"Heated Bathroom Floors in Marysville: Cost, Payback, and Install Reality","Marysville"),
 ("epoxy grout vs cement grout",480,22,"Epoxy vs Cement Grout: Where Each One Earns Its Price",None),
 ("how much does it cost to tile a shower",480,19,"What It Costs to Tile a Shower in Sammamish","Sammamish"),
 ("large format tile installation",390,18,"Large-Format Tile: Why Flat Subfloors Decide the Whole Job","Shoreline"),
 ("laundry room tile",1300,7,"Laundry Room Tile: The Floor That Has to Survive a Leak","Bothell"),
 ("entryway tile",880,10,"Entryway Tile for Pacific Northwest Winters","Edmonds"),
 ("mudroom tile",480,11,"Mudroom Tile That Handles Boots, Dogs, and Rain","Issaquah"),
 ("tile grout color",390,29,"Choosing Grout Color: The Decision People Regret Most","Lynnwood"),
 ("regrouting a shower",210,25,"Regrouting vs Retiling a Shower: How to Tell Which You Need","Lake Stevens"),
 ("subway tile pattern",260,15,"Subway Tile Patterns Beyond the Running Bond",None),
 ("ditra vs cement board",110,3,"Ditra vs Cement Board: A Tile Setter's Honest Comparison",None),
 ("kitchen backsplash installation cost",70,23,"What a Kitchen Backsplash Costs Installed in Kenmore","Kenmore"),
 ("tile floor cracking",40,15,"Why Tile Floors Crack — and What It Says About the Subfloor","Mukilteo"),
 ("how long does it take to tile a bathroom",90,0,"How Long Does It Take to Tile a Bathroom? A Real Timeline","Mill Creek"),
 ("bathroom remodel cost seattle",50,14,"Tile's Share of a Seattle Bathroom Remodel Budget","Seattle"),
 ("tile installation seattle",140,10,"Hiring a Tile Installer in Seattle: What to Ask Before You Sign","Seattle"),
 ("schluter kerdi",1900,48,"Schluter Kerdi vs Liquid Membrane: Two Ways to Keep Water Out",None),
 ("luxury vinyl vs tile bathroom",0,0,"Tile or Luxury Vinyl in a Monroe Bathroom?","Monroe"),
 ("heated floor mat vs cable",0,0,"Heated Floor Mats vs Loose Cable: Which Suits Your Room","Snoqualmie"),
 ("small bathroom tile",0,0,"Making a Small Bathroom Feel Bigger With Tile","Woodinville"),
 ("tile traction pets",0,0,"Slip-Resistant Tile for Homes With Dogs and Older Adults","Newcastle"),
 ("basement tile concrete",0,0,"Tiling Over a Concrete Basement Slab in Snohomish","Snohomish"),
 ("tile maintenance sealing",0,0,"Sealing and Maintaining Tile: What Actually Needs Doing","Cottage Lake"),
]

CARPET = [
 ("carpet installation cost",6600,36,"What Carpet Installation Costs in Seattle","Seattle"),
 ("best carpet for pets",1600,24,"The Best Carpet for Homes With Pets","Bellevue"),
 ("best carpet for stairs",1300,25,"The Best Carpet for Stairs in an Everett Home","Everett"),
 ("how long does carpet last",1300,10,"How Long Should Carpet Last? An Honest Answer","Renton"),
 ("carpet removal cost",1300,35,"What Carpet Removal Costs — and When It's Included","Kirkland"),
 ("carpet for basement",880,11,"Carpet in a Basement: When It Works in the Pacific Northwest","Redmond"),
 ("carpet stretching cost",880,11,"Carpet Stretching: Fixing Ripples Without Replacing the Floor","Marysville"),
 ("how to measure for carpet",720,11,"How to Measure a Room for Carpet (and Why Estimates Differ)",None),
 ("cost to carpet a room",590,36,"What It Costs to Carpet One Room in Sammamish","Sammamish"),
 ("low pile vs high pile carpet",480,10,"Low Pile vs High Pile: Which Carpet Suits Your Rooms",None),
 ("stain resistant carpet",1000,17,"Stain-Resistant Carpet: What the Warranties Actually Cover","Shoreline"),
 ("carpet padding thickness",320,8,"Carpet Padding: The Half of the Job Nobody Shops For","Bothell"),
 ("do carpet installers move furniture",320,16,"Do Carpet Installers Move Your Furniture? What to Expect","Edmonds"),
 ("carpet vs hardwood",320,19,"Carpet or Hardwood? Room-by-Room in an Issaquah Home","Issaquah"),
 ("carpet allergies",260,37,"Carpet and Allergies: What Helps and What's a Myth","Lynnwood"),
 ("carpet in bedrooms",260,17,"Why Bedrooms Are Still the Best Room for Carpet","Lake Stevens"),
 ("when to replace carpet",170,10,"Five Signs It's Time to Replace Your Carpet","Mercer Island"),
 ("carpet installation seattle",170,16,"Hiring a Carpet Installer in Seattle: Questions That Matter","Seattle"),
 ("wall to wall carpet cost",140,39,"Wall-to-Wall Carpet Cost in Kenmore, Room by Room","Kenmore"),
 ("carpet fiber types",110,17,"Nylon, Polyester, or Wool? Carpet Fibers Compared",None),
 ("berber vs plush carpet",90,0,"Berber vs Plush: Which Carpet Wears Better","Mukilteo"),
 ("carpet warranty",90,15,"Reading a Carpet Warranty Before You Buy","Mill Creek"),
 ("stair runner cost",70,14,"Stair Runners: Cost, Installation, and Whether They Last","Monroe"),
 ("carpet color trends",50,8,"Carpet Colors That Won't Date Your House","Snoqualmie"),
 ("rental property carpet",10,0,"Carpet for Rentals: What Landlords Should Actually Buy","Woodinville"),
 ("soundproof carpet apartment",0,0,"Carpet for Condo Sound Rules in Seattle Buildings","Seattle"),
 ("carpet seam visible",10,0,"Why Carpet Seams Show — and How Good Installers Hide Them","Newcastle"),
 ("carpet tiles vs broadloom",30,0,"Carpet Tiles vs Broadloom for Basements and Offices","Snohomish"),
 ("carpet cleaning vs replacing",0,0,"Clean It or Replace It? Judging Carpet Honestly","Cottage Lake"),
 ("carpet subfloor prep",0,0,"What Happens Under Carpet: Subfloor Prep and Tack Strip","Duvall"),
 ("carpet for stairs safety",0,0,"Carpet on Stairs and Fall Safety in Older Homes","North Bend"),
 ("high end carpet",0,0,"When Premium Carpet Is Worth It — and When It Isn't","Medina"),
]

def dates(weekday, n):
    d, out = datetime.date(2026,9,1), []
    while len(out) < n:
        if d.weekday()==weekday: out.append(d)
        d += datetime.timedelta(1)
    return out

def build(rows, weekday, svc):
    ds = dates(weekday, len(rows))
    return [{'seq':i+1,'publish_date':d.isoformat(),'service':svc,'city':c,
             'title':t,'keyword':k,'us_volume':v,'kd':kd}
            for i,(d,(k,v,kd,t,c)) in enumerate(zip(ds, rows))]

tile, carpet = build(TILE,1,'tile'), build(CARPET,3,'carpet')
json.dump({'tile':tile,'carpet':carpet}, open('blogs/plan/TILE-CARPET-PLAN.json','w'), indent=1)

for name, rows in (('TILE (Tuesdays)',tile),('CARPET (Thursdays)',carpet)):
    print(f'\n=== {name} — {len(rows)} posts, {rows[0]["publish_date"]} to {rows[-1]["publish_date"]} ===')
    for r in rows:
        c = r['city'] or '—'
        kw = f'{r["keyword"]} ({r["us_volume"]}/KD{r["kd"]})' if r['us_volume'] else r['keyword']
        print(f'  {r["publish_date"]}  {c:<14} {r["title"]}')
n_city = sum(1 for r in tile+carpet if r['city'])
print(f'\ncity-accented: {n_city}/64 = {n_city/64:.0%}')
