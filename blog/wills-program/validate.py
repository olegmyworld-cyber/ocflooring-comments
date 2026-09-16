#!/usr/bin/env python3
"""Cross-checks every spec in specs/ against plan.json and the style rules. Run from anywhere."""
import json, glob, os, re, sys, collections
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import render
plan = {p["slug"]: p for p in json.load(open(os.path.join(here, "plan.json")))}
LEGACY = ["hardwood-floor-refinishing-everett-wa","why-laminate-flooring-unraveling-the-advantages-and-benefits","common-mistakes-to-avoid-when-refinishing-hardwood-floors","5-benefits-of-choosing-quartz-countertops-for-your-kitchen-renovation","luxurious-kitchen-renovations-adding-value-with-marble-countertops","ceramic-vs-porcelain-tile-flooring-which-is-better-for-your-space"]
all_slugs = set(plan) | set(LEGACY)
problems = collections.defaultdict(list); seen_p = {}; rows = []
files = sorted(glob.glob(os.path.join(here, "specs", "*.json")))
for f in files:
    name = os.path.basename(f)
    try: spec = json.load(open(f))
    except Exception as e: problems[name].append(f"bad json: {e}"); continue
    P = lambda m: problems[name].append(m)
    n = int(name[:3]); pl = plan.get(spec.get("slug"))
    if not pl: P("slug not in plan"); continue
    if pl["n"] != n: P(f"file number {n} != plan n {pl['n']}")
    for k, pk in (("title","title"), ("category","cat"), ("city","city"), ("date","date")):
        if spec.get(k) != pl[pk]: P(f"{k} differs from plan: {spec.get(k)!r} vs {pl[pk]!r}")
    meta = spec.get("meta", "")
    if not 120 <= len(meta) <= 160: P(f"meta length {len(meta)}")
    if spec["category"] == "carpet":
        if spec.get("offers"): P("carpet post has offers")
        kinds = [b["type"] for b in spec["blocks"]]
        if "calc" in kinds: P("carpet post uses calc"); 
        if "estimator" not in kinds: P("carpet post lacks estimator")
    else:
        if not spec.get("offers"): P("missing offers")
        kinds = [b for b in spec["blocks"] if b["type"] == "calc"]
        if len(kinds) != 1: P(f"{len(kinds)} calc blocks")
        elif kinds[0]["kind"] != spec["category"]: P(f"calc kind {kinds[0]['kind']} != category")
    if spec["blocks"][0]["type"] != "quick": P("first block not quick")
    if not 5 <= len(spec.get("faq", [])) <= 8: P(f"faq count {len(spec.get('faq', []))}")
    for r in spec.get("related", []):
        if r[0] not in all_slugs: P(f"related slug unknown: {r[0]}")
        if r[0] == spec["slug"]: P("related links to itself")
    if not 2 <= len(spec.get("related", [])) <= 4: P(f"related count {len(spec.get('related', []))}")
    text = json.dumps(spec, ensure_ascii=False)
    if "—" in text or "–" in text.replace("$55–$75", "").replace("–$", "").replace("$1.99–$6.50", ""):
        dashes = len(re.findall(r"[—]", text)); P(f"{dashes} em dashes") if dashes else None
    for m in re.finditer(r'href=\\"([^"\\]+)', text):
        h = m.group(1)
        if h.startswith("/blog-posts/") and h[12:] not in all_slugs: P(f"link to unknown post {h}")
        elif h.startswith("http") and "willsflooring" not in h: P(f"external link {h}")
    for b in spec["blocks"]:
        if b["type"] == "p":
            key = b["html"][:120]
            if key in seen_p and seen_p[key] != name: P(f"paragraph duplicated from {seen_p[key]}")
            seen_p[key] = name
    try:
        body = render.render(spec); ne, mx, tot = render.check(body, spec["slug"])
        words = len(render.strip_tags(re.sub(r'<(style|script)[^>]*>.*?</\1>', '', body, flags=re.S)).split())
        if not 1100 <= words <= 1800: P(f"words {words}")
        rows.append((n, spec["category"], spec["city"], words, tot, spec["slug"]))
    except Exception as e: P(f"render failed: {e}")
print(f"{len(files)} specs checked, {len(problems)} with problems")
for k, v in sorted(problems.items()):
    for m in v: print(f"  {k}: {m}")
if "--table" in sys.argv:
    for r in rows: print("%3d %-8s %-9s %5d w %6d ch  %s" % r)
