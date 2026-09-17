#!/usr/bin/env python3
"""Scratch recorder for the warm roll-out slice 136-152 (agent w7r2q).

Usage: python3 record_warm_w7r2q.py <slug>
Keeps every existing field in uploaded/<slug>.json, updates bodyLen from the
rendered out/<slug>.json and sets "warm": true.
"""
import json, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
slug = sys.argv[1]

with open(os.path.join(BASE, 'out', slug + '.json')) as f:
    body = json.load(f)['description-big']

rollout = json.load(open(os.path.join(BASE, 'warm-rollout.json')))
entry = next(e for e in rollout if e['slug'] == slug)
name = ('legacy-' + slug if entry['live'] else slug) + '.json'
path = os.path.join(BASE, 'uploaded', name)

rec = json.load(open(path))
rec['bodyLen'] = len(body)
rec['warm'] = True
with open(path, 'w') as f:
    json.dump(rec, f)
print(name, json.dumps(rec))
