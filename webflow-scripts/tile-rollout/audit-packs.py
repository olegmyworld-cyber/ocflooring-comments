#!/usr/bin/env python3
"""Cross-city duplicate audit for tile packs.

For every prose field, checks that no run of 8 consecutive word tokens is shared
between any two cities' packs, or between a pack and the Bellevue baseline.
Mandated/structural fields (breadcrumb, eyebrows, FAQ questions, fine print,
trust facts) are excluded, matching the carpet-rollout audit standard.

Also checks required facts are present somewhere in each pack.

Usage: python3 audit-packs.py           # report collisions
"""
import json
import re
import sys
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).parent
TOKEN = re.compile(r"[a-z0-9$.%+/-]+")
N = 8

PROSE_ROLES = [
    "heroLead", "costP1", "costP2", "costNote", "layersLead", "whyP1", "whyP2",
    "scopeIntro", "cardShower", "cardFloors", "cardBacksplash", "cardHeated",
    "cardRepair", "cardDemo", "materialsLead", "materialsNote", "estIntro",
    "daysLead", "hoodsOut", "ctaLead",
] + [f"faqA{i}" for i in range(1, 12)]
EXTRA_FIELDS = ["seoDesc", "ogDesc"]  # top-level pack keys, also audited

FACTS = [
    ("$14", "installed range low"), ("$26", "installed range high"),
    ("$11", "labor rate"), ("3,200", "shower low"), ("6,800", "shower high"),
    ("6,500", "full bath low"), ("14,000", "full bath high"),
    ("1,100", "backsplash low"), ("2,200", "backsplash high"),
    ("900", "bath floor low"), ("1,600", "bath floor high"),
    ("3.50", "demo rate"), ("$8", "repair rate"),
    ("flood test", "flood test"), ("2-year", "warranty"),
    ("(425) 595-1079", "phone"),
]


def grams(text):
    toks = TOKEN.findall(text.lower())
    return {tuple(toks[i:i + N]) for i in range(len(toks) - N + 1)}


def main():
    rmap = json.load(open(HERE / "rewrite-map.json"))
    packs = {}
    for f in sorted((HERE / "packs").glob("*.json")):
        packs[f.stem] = json.load(open(f))

    # corpus: (city, role) -> gram set
    corpus = {}
    for role in PROSE_ROLES:
        if role in rmap:
            corpus[("bellevue-base", role)] = grams(rmap[role]["bellevue"])
    for slug, p in packs.items():
        for role in PROSE_ROLES:
            t = p.get("roles", {}).get(role, "")
            corpus[(slug, role)] = grams(t)
        for k in EXTRA_FIELDS:
            corpus[(slug, k)] = grams(p.get(k, ""))

    collisions = []
    keys = list(corpus)
    for a, b in combinations(keys, 2):
        if a[0] == b[0]:
            continue  # same city: internal overlap is fine
        common = corpus[a] & corpus[b]
        if common:
            sample = " ".join(next(iter(common)))
            collisions.append((a, b, len(common), sample))

    missing = []
    for slug, p in packs.items():
        blob = json.dumps(p)
        for needle, label in FACTS:
            if needle not in blob:
                missing.append((slug, label, needle))

    empty = []
    for slug, p in packs.items():
        for role in PROSE_ROLES + ["crumb", "heroEyebrow", "costH2", "ctaFine",
                                   "trustCell", "statRegion", "footerTag",
                                   "estEyebrow", "hoodsH2", "guidesH2",
                                   "reviewsH2", "workH2", "faqH2", "scopeH2",
                                   "ctaH2"] + [f"faqQ{i}" for i in range(1, 12)]:
            if not p.get("roles", {}).get(role, "").strip():
                empty.append((slug, role))
        for k in ("seoTitle", "seoDesc", "ogTitle", "ogDesc", "carpetLinkText"):
            if not p.get(k, "").strip():
                empty.append((slug, k))
        if not p.get("chips"):
            empty.append((slug, "chips"))
        alts = p.get("alts", {})
        for k in ("hero", "membrane", "work1", "work2", "work3", "work4", "work5"):
            if not alts.get(k, "").strip():
                empty.append((slug, f"alts.{k}"))

    print(f"packs: {len(packs)}  collisions: {len(collisions)}  "
          f"missing-facts: {len(missing)}  empty-fields: {len(empty)}")
    for a, b, n, s in sorted(collisions, key=lambda x: -x[2]):
        print(f"COLLIDE {a[0]}/{a[1]} <-> {b[0]}/{b[1]} ({n} grams): \"{s}\"")
    for slug, label, needle in missing:
        print(f"MISSING {slug}: {label} ({needle})")
    for slug, role in empty:
        print(f"EMPTY {slug}: {role}")
    sys.exit(1 if (collisions or missing or empty) else 0)


if __name__ == "__main__":
    main()
