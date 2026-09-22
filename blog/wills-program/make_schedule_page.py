#!/usr/bin/env python3
"""Builds the browsable publishing-schedule page from plan.json.

Usage: python3 make_schedule_page.py <output.html>
Every post in the collection has a hero image as of 2026-09-22, so the page
shows schedule state only: published, next up, or queued.
"""
import json, sys, datetime, collections, html, os

HERE = os.path.dirname(os.path.abspath(__file__))
TODAY = datetime.date(2026, 9, 22)
CAT = {"refinish": "Refinishing", "hardwood": "Hardwood install",
       "lvp": "Vinyl plank", "carpet": "Carpet"}
CATKEY = {"refinish": "refinish", "hardwood": "hardwood", "lvp": "lvp", "carpet": "carpet"}

plan = json.load(open(os.path.join(HERE, "plan.json")))
rows = sorted(plan, key=lambda p: (p.get("slot") or p["date"]))

def d(p): return datetime.date.fromisoformat(p["date"][:10])

months = collections.Counter()
for p in rows:
    if not p.get("live"):
        months[d(p).strftime("%Y-%m")] += 1
by_cat = collections.Counter(p["cat"] for p in rows)
by_city = collections.Counter(p["city"] for p in rows)
live = [p for p in rows if p.get("live")]
queued = [p for p in rows if not p.get("live")]
nextup = [p for p in queued if d(p) >= TODAY][:5]

def esc(s): return html.escape(str(s), quote=True)

tr = []
cur_month = None
for p in rows:
    dt = d(p)
    mk = dt.strftime("%Y-%m")
    if not p.get("live") and mk != cur_month:
        cur_month = mk
        tr.append(
            '<tr class="mrow"><th colspan="5" scope="rowgroup">%s'
            '<span class="mcount">%d posts</span></th></tr>'
            % (esc(dt.strftime("%B %Y")), months[mk]))
    if p.get("live"):
        state, label = "live", "Published"
    elif p in nextup[:1]:
        state, label = "next", "Next up"
    else:
        state, label = "queued", "Queued"
    slot = ('<span class="slot" title="Original slot">slot %s</span>'
            % esc(p["slot"][:10])) if p.get("slot") else ""
    tr.append(
        '<tr data-cat="%s" data-city="%s" data-month="%s" data-state="%s" '
        'data-q="%s">'
        '<td class="num">%d</td>'
        '<td class="date"><time datetime="%s">%s</time>%s</td>'
        '<td><span class="pill c-%s">%s</span></td>'
        '<td class="city">%s</td>'
        '<td class="tt"><span class="t">%s</span>'
        '<a class="sl" href="https://www.willsflooring.com/blog-posts/%s" '
        'target="_blank" rel="noopener">/%s</a>'
        '<span class="st s-%s">%s</span></td>'
        '</tr>' % (
            esc(p["cat"]), esc(p["city"]), esc(mk), state,
            esc((p["title"] + " " + p["slug"] + " " + p["city"] + " " + CAT[p["cat"]]).lower()),
            p["n"], esc(p["date"][:10]), esc(dt.strftime("%a %d %b %Y")), slot,
            esc(p["cat"]), esc(CAT[p["cat"]]), esc(p["city"]),
            esc(p["title"]), esc(p["slug"]), esc(p["slug"]), state, label))

maxm = max(months.values()) if months else 1
mbars = "".join(
    '<button class="mb" data-month="%s" aria-pressed="false">'
    '<span class="track"><span class="bar" style="height:%dpx"></span></span>'
    '<span class="ml">%s</span><span class="mv">%d</span></button>'
    % (esc(k), max(6, round(64 * v / maxm)),
       esc(datetime.date.fromisoformat(k + "-01").strftime("%b")), v)
    for k, v in sorted(months.items()))

catchips = "".join(
    '<button class="chip" data-cat="%s"><i class="dot c-%s"></i>%s'
    '<span class="n">%d</span></button>' % (esc(k), esc(k), esc(CAT[k]), v)
    for k, v in by_cat.most_common())

cityopts = "".join('<option value="%s">%s (%d)</option>' % (esc(c), esc(c), v)
                   for c, v in sorted(by_city.items()))

nextcards = "".join(
    '<li><span class="nd">%s</span><span class="nt">%s</span>'
    '<span class="pill c-%s">%s</span></li>'
    % (esc(d(p).strftime("%a %d %b")), esc(p["title"]), esc(p["cat"]), esc(CAT[p["cat"]]))
    for p in nextup)

HTML = """<title>Wills Flooring Blog Queue</title>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<style>
:root{
  --ground:#fbf8f4; --panel:#ffffff; --panel2:#f4efe8;
  --ink:#171a1f; --ink2:#6b6660; --ink3:#948d84;
  --line:#e6dfd5; --line2:#d6cdc0;
  --navy:#071730; --gold:#c46a12; --gold-soft:rgba(196,106,18,.12);
  --ok:#1f6f4a; --ok-soft:rgba(31,111,74,.12);
  --c-refinish:#c46a12; --c-hardwood:#8a5a2b; --c-lvp:#2f6b8f; --c-carpet:#6b4a8f;
  --sans:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,"SF Mono",Menlo,monospace;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --ground:#14161a; --panel:#1c1f25; --panel2:#24282f;
  --ink:#f0ece6; --ink2:#a9a29a; --ink3:#7d766e;
  --line:#2c3039; --line2:#3c414c;
  --navy:#cbd6e6; --gold:#e79a3f; --gold-soft:rgba(231,154,63,.15);
  --ok:#54c08a; --ok-soft:rgba(84,192,138,.15);
  --c-refinish:#e79a3f; --c-hardwood:#c08d5c; --c-lvp:#6aa8cc; --c-carpet:#a98ccc;
}}
:root[data-theme="dark"]{
  --ground:#14161a; --panel:#1c1f25; --panel2:#24282f;
  --ink:#f0ece6; --ink2:#a9a29a; --ink3:#7d766e;
  --line:#2c3039; --line2:#3c414c;
  --navy:#cbd6e6; --gold:#e79a3f; --gold-soft:rgba(231,154,63,.15);
  --ok:#54c08a; --ok-soft:rgba(84,192,138,.15);
  --c-refinish:#e79a3f; --c-hardwood:#c08d5c; --c-lvp:#6aa8cc; --c-carpet:#a98ccc;
}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);font-family:var(--sans);
  font-size:15px;line-height:1.5;-webkit-font-smoothing:antialiased}
.wrap{max-width:1120px;margin:0 auto;padding-inline:16px;padding-block:28px 64px}
a{color:inherit}
h1{margin:0;font-size:clamp(24px,3.2vw,34px);line-height:1.1;letter-spacing:-.02em;
  font-weight:700;text-wrap:balance}
.kicker{display:block;font-family:var(--mono);font-size:12px;font-weight:500;
  letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-bottom:10px}
.lede{margin:10px 0 0;max-width:62ch;color:var(--ink2);font-size:16px}
.strip{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}
.stat{background:var(--panel);border:1px solid var(--line);border-radius:10px;
  padding:9px 13px;display:flex;align-items:baseline;gap:8px}
.stat b{font-family:var(--mono);font-size:17px;font-weight:600;letter-spacing:-.02em}
.stat span{font-size:12.5px;color:var(--ink2);letter-spacing:.01em}
.stat.go b{color:var(--ok)}
section{margin-top:34px}
h2{margin:0 0 12px;font-size:13px;font-weight:600;letter-spacing:.1em;
  text-transform:uppercase;color:var(--ink2);font-family:var(--mono)}
.next{list-style:none;margin:0;padding:0;display:grid;gap:1px;
  background:var(--line);border:1px solid var(--line);border-radius:12px;overflow:hidden}
.next li{background:var(--panel);display:grid;grid-template-columns:118px 1fr auto;
  gap:14px;align-items:center;padding:12px 14px}
.next li:first-child{background:var(--gold-soft)}
.nd{font-family:var(--mono);font-size:13px;font-weight:500;color:var(--ink2);
  font-variant-numeric:tabular-nums}
.nt{font-weight:500;min-width:0}
.pill{display:inline-block;font-size:11.5px;font-weight:600;letter-spacing:.04em;
  padding:3px 9px;border-radius:999px;white-space:nowrap;
  background:var(--panel2);color:var(--ink2);border:1px solid var(--line)}
.pill.c-refinish{color:var(--c-refinish);border-color:color-mix(in srgb,var(--c-refinish) 32%,transparent)}
.pill.c-hardwood{color:var(--c-hardwood);border-color:color-mix(in srgb,var(--c-hardwood) 32%,transparent)}
.pill.c-lvp{color:var(--c-lvp);border-color:color-mix(in srgb,var(--c-lvp) 32%,transparent)}
.pill.c-carpet{color:var(--c-carpet);border-color:color-mix(in srgb,var(--c-carpet) 32%,transparent)}
.dot{width:8px;height:8px;border-radius:50%;display:inline-block;flex:0 0 auto}
.dot.c-refinish{background:var(--c-refinish)}.dot.c-hardwood{background:var(--c-hardwood)}
.dot.c-lvp{background:var(--c-lvp)}.dot.c-carpet{background:var(--c-carpet)}
.months{display:flex;gap:4px;align-items:flex-end;background:var(--panel);
  border:1px solid var(--line);border-radius:12px;padding:14px 12px 10px;overflow-x:auto}
.mb{flex:1 1 0;min-width:46px;background:none;border:0;padding:0;cursor:pointer;
  display:flex;flex-direction:column;align-items:center;gap:6px;font:inherit;color:inherit;
  border-radius:8px}
.track{display:flex;align-items:flex-end;justify-content:center;height:64px;width:100%}
.mb:hover .bar,.mb[aria-pressed="true"] .bar{background:var(--gold)}
.mb[aria-pressed="true"] .ml{color:var(--gold);font-weight:600}
.bar{width:100%;max-width:34px;background:var(--line2);border-radius:5px 5px 2px 2px;
  transition:background .15s}
.ml{font-family:var(--mono);font-size:11.5px;color:var(--ink2);letter-spacing:.04em}
.mv{font-family:var(--mono);font-size:11px;color:var(--ink3)}
.tools{display:flex;flex-wrap:wrap;gap:8px;align-items:center;
  position:sticky;top:env(safe-area-inset-top,0px);z-index:5;
  background:var(--ground);padding-block:10px;margin-bottom:2px;
  border-bottom:1px solid var(--line)}
.search{flex:1 1 220px;min-width:0;display:flex;align-items:center;gap:8px;
  background:var(--panel);border:1px solid var(--line2);border-radius:9px;padding:0 11px}
.search input{flex:1;min-width:0;border:0;outline:0;background:transparent;
  font:inherit;font-size:14px;color:var(--ink);padding:9px 0}
.search svg{flex:0 0 auto;stroke:var(--ink3);fill:none;stroke-width:1.9}
.chip{display:inline-flex;align-items:center;gap:7px;background:var(--panel);
  border:1px solid var(--line2);border-radius:9px;padding:8px 11px;font:inherit;
  font-size:13.5px;color:var(--ink);cursor:pointer}
.chip .n{font-family:var(--mono);font-size:12px;color:var(--ink3)}
.chip[aria-pressed="true"]{border-color:var(--gold);background:var(--gold-soft)}
select{background:var(--panel);border:1px solid var(--line2);border-radius:9px;
  padding:8px 10px;font:inherit;font-size:13.5px;color:var(--ink);max-width:190px}
.reset{background:none;border:0;color:var(--ink2);font:inherit;font-size:13px;
  text-decoration:underline;cursor:pointer;padding:8px 4px}
.count{font-family:var(--mono);font-size:12.5px;color:var(--ink2);margin-left:auto;
  font-variant-numeric:tabular-nums}
.tablewrap{overflow-x:auto;border:1px solid var(--line);border-radius:12px;
  background:var(--panel);margin-top:12px}
table{width:100%;border-collapse:collapse;min-width:640px}
thead th{position:sticky;top:0;background:var(--panel);z-index:2;text-align:left;
  font-family:var(--mono);font-size:11px;font-weight:600;letter-spacing:.1em;
  text-transform:uppercase;color:var(--ink3);padding:11px 12px;
  border-bottom:1px solid var(--line2);white-space:nowrap}
tbody td{padding:11px 12px;border-bottom:1px solid var(--line);vertical-align:top}
tbody tr:last-child td{border-bottom:0}
tbody tr:hover td{background:var(--panel2)}
.mrow th{background:var(--panel2);text-align:left;font-family:var(--mono);font-size:11.5px;
  font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--ink2);
  padding:9px 12px;border-bottom:1px solid var(--line2);border-top:1px solid var(--line2)}
.mcount{float:right;color:var(--ink3);font-weight:400;letter-spacing:.04em}
.num{font-family:var(--mono);font-size:12.5px;color:var(--ink3);width:46px;
  font-variant-numeric:tabular-nums}
.date{font-family:var(--mono);font-size:12.5px;color:var(--ink2);white-space:nowrap;
  width:150px;font-variant-numeric:tabular-nums}
.slot{display:block;font-size:10.5px;color:var(--ink3);letter-spacing:.02em;margin-top:3px}
.city{white-space:nowrap;color:var(--ink2);font-size:14px;width:104px}
.tt{min-width:260px}
.tt .t{display:block;font-weight:500;line-height:1.35;text-wrap:pretty}
.sl{display:inline-block;font-family:var(--mono);font-size:11.5px;color:var(--ink3);
  text-decoration:none;margin-top:4px;word-break:break-all}
.sl:hover{color:var(--gold);text-decoration:underline}
.st{display:inline-block;font-family:var(--mono);font-size:10.5px;font-weight:600;
  letter-spacing:.06em;text-transform:uppercase;margin-top:5px;margin-left:8px;
  padding:2px 7px;border-radius:5px;background:var(--panel2);color:var(--ink3)}
.st.s-live{background:var(--ok-soft);color:var(--ok)}
.st.s-next{background:var(--gold-soft);color:var(--gold)}
.empty{padding:34px 16px;text-align:center;color:var(--ink2);font-size:14px}
.foot{margin-top:30px;padding-top:18px;border-top:1px solid var(--line);
  color:var(--ink3);font-size:12.5px;max-width:74ch}
.foot code{font-family:var(--mono);font-size:12px;color:var(--ink2)}
@media (max-width:640px){
  .next li{grid-template-columns:1fr;gap:5px}
  .nd{font-size:12px}
  .count{margin-left:0;width:100%}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
:focus-visible{outline:2px solid var(--gold);outline-offset:2px;border-radius:6px}
</style>

<div class="wrap">
  <header>
    <span class="kicker">willsflooring.com &middot; blog posts</span>
    <h1>200-post publishing queue</h1>
    <p class="lede">One question-led post per day across refinishing, hardwood, vinyl plank
      and carpet in seven Snohomish and King County cities. The Routine
      <strong>Wills Flooring daily blog publish</strong> flips the day's draft live at 15:30 UTC.</p>
    <div class="strip">
      <div class="stat"><b>200</b><span>posts</span></div>
      <div class="stat"><b>23 Sep 2026</b><span>queue starts</span></div>
      <div class="stat"><b>10 Apr 2027</b><span>queue ends</span></div>
      <div class="stat go"><b>206/206</b><span>hero images in place</span></div>
      <div class="stat"><b>__LIVE__</b><span>published so far</span></div>
    </div>
  </header>

  <section>
    <h2>Next five</h2>
    <ol class="next">__NEXT__</ol>
  </section>

  <section>
    <h2>Posts per month</h2>
    <div class="months" id="months">__MONTHS__</div>
  </section>

  <section>
    <h2>All 200 posts</h2>
    <div class="tools">
      <label class="search">
        <svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-4.4-4.4"/></svg>
        <input id="q" type="search" placeholder="Search titles, slugs, cities" aria-label="Search posts">
      </label>
      __CATCHIPS__
      <select id="city" aria-label="Filter by city"><option value="">All cities</option>__CITYOPTS__</select>
      <button class="reset" id="reset" type="button">Clear</button>
      <span class="count" id="count"></span>
    </div>
    <div class="tablewrap">
      <table>
        <thead><tr><th>#</th><th>Publish date</th><th>Service</th><th>City</th><th>Post</th></tr></thead>
        <tbody id="tb">__ROWS__</tbody>
      </table>
      <p class="empty" id="empty" hidden>No posts match those filters.</p>
    </div>
  </section>

  <p class="foot">Slugs link to the live URL each post will occupy; they 404 until the post
    publishes. Post #152 was published early on 17 Sep 2026, so its row shows the real date
    and keeps its original slot for reference. Dates were rebased on 22 Sep 2026: the whole
    queue moved six days forward after the Routine sat paused, so nothing had to publish in a
    batch. Source of truth is <code>blog/wills-program/plan.json</code>; this page is generated
    by <code>make_schedule_page.py</code>.</p>
</div>

<script>
(function(){
  var rows=[].slice.call(document.querySelectorAll('#tb tr[data-q]'));
  var mrows=[].slice.call(document.querySelectorAll('#tb tr.mrow'));
  var q=document.getElementById('q'), city=document.getElementById('city');
  var count=document.getElementById('count'), empty=document.getElementById('empty');
  var cats=[].slice.call(document.querySelectorAll('.chip[data-cat]'));
  var mbs=[].slice.call(document.querySelectorAll('.mb[data-month]'));
  var f={q:'',cat:'',city:'',month:''};
  function apply(){
    var shown=0;
    rows.forEach(function(r){
      var ok = (!f.q || r.dataset.q.indexOf(f.q)>-1)
            && (!f.cat || r.dataset.cat===f.cat)
            && (!f.city || r.dataset.city===f.city)
            && (!f.month || r.dataset.month===f.month);
      r.hidden=!ok; if(ok) shown++;
    });
    var filtering = f.q||f.cat||f.city||f.month;
    mrows.forEach(function(m){ m.hidden = !!filtering; });
    count.textContent = shown===rows.length ? rows.length+' posts'
      : shown+' of '+rows.length+' posts';
    empty.hidden = shown>0;
    cats.forEach(function(c){ c.setAttribute('aria-pressed', c.dataset.cat===f.cat); });
    mbs.forEach(function(m){ m.setAttribute('aria-pressed', m.dataset.month===f.month); });
  }
  q.addEventListener('input',function(){ f.q=q.value.trim().toLowerCase(); apply(); });
  city.addEventListener('change',function(){ f.city=city.value; apply(); });
  cats.forEach(function(c){ c.addEventListener('click',function(){
    f.cat = f.cat===c.dataset.cat ? '' : c.dataset.cat; apply(); }); });
  mbs.forEach(function(m){ m.addEventListener('click',function(){
    f.month = f.month===m.dataset.month ? '' : m.dataset.month; apply(); }); });
  document.getElementById('reset').addEventListener('click',function(){
    f={q:'',cat:'',city:'',month:''}; q.value=''; city.value=''; apply(); });
  apply();
})();
</script>
"""

page = (HTML
        .replace("__ROWS__", "\n".join(tr))
        .replace("__NEXT__", nextcards)
        .replace("__MONTHS__", mbars)
        .replace("__CATCHIPS__", catchips)
        .replace("__CITYOPTS__", cityopts)
        .replace("__LIVE__", str(len(live))))

out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "schedule.html")
open(out, "w").write(page)
print("wrote %s  (%d rows, %d months, %d live)" % (out, len(rows), len(months), len(live)))
