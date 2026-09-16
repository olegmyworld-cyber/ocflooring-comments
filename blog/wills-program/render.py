#!/usr/bin/env python3
"""Wills Flooring blog renderer.

Turns a compact JSON post spec into the Apple-style Webflow rich-text body
(a sequence of data-rt-embed-type blocks plus plain rich-text prose) and a
CMS fieldData manifest. Run: python3 render.py specs/*.json  -> out/<slug>.html + out/<slug>.json
"""
import json, re, sys, os, html as H

PHONE = "(425) 350-4435"; TEL = "tel:+14253504435"
SITE = "https://www.willsflooring.com"
CAT = {  # category key -> (Post Category item id, display name, service page, gallery hero image)
  "refinish": ("66ced3625e68f5f0e740c5b9", "Hardwood Refinishing", "/services/floor-refinish"),
  "hardwood": ("6aa9d8b00ee3c2e5836a2b45", "Hardwood Installation", "/services/hardwood-flooring"),
  "lvp":      ("6aa9d8b00ee3c2e5836a2b41", "Vinyl Plank Flooring", "/services/lvp-vinyl-flooring"),
  "carpet":   ("6aa9d8b00ee3c2e5836a2b41", "Carpet Installation", "/services/carpet-installation"),
  "laminate": ("66ced38abdc93ca1abe2b832", "Laminate Flooring", "/services/laminate-flooring-installation"),
  "tile":     ("66ced344cb67820876374ba7", "Tile Flooring", "/services/tile-installation"),
  "counter":  ("66ced351cb3ccb4949d026ec", "Countertops", "/services/kitchen-remodeling"),
}
CAT["carpet"] = ("6aa9d8b00ee3c2e5836a2b41", "Carpet Installation", "/services/carpet-installation")
CAT["lvp"] = ("6aa9d8b00ee3c2e5836a2b43", "Vinyl Plank Flooring", "/services/lvp-vinyl-flooring")

CITY_SVC = {  # city -> slug prefix used by Wills city service pages
  "Everett": "everett-flooring-services", "Seattle": "seattle-flooring-services", "Sammamish": "issaquah-wa-flooring-services",
  "Lynnwood": "lynnwood-wa-flooring-services", "Edmonds": "edmonds-flooring-services", "Kirkland": "kirkland-flooring-services",
  "Snohomish": "snohomish-flooring-services", "Bothell": "bothell-flooring-services", "Marysville": "marysville-flooring-services",
  "Lake Stevens": "lake-stevens-flooring-services", "Mukilteo": "mukilteo-flooring-services", "Bellevue": "bellevue-flooring-services",
  "Shoreline": "shoreline-flooring-services", "Mill Creek": "mill-creek-flooring-services", "Redmond": "redmond-flooring-services",
}
CITY_PAGE = {  # (city, category) -> known city service page
  ("Everett","refinish"): "/everett-flooring-services/hardwood-floor-refinishing-in-everett-wa-wills-flooring",
  ("Seattle","refinish"): "/seattle-flooring-services/hardwood-floor-refinishing-in-seattle-wa-wills-flooring",
  ("Sammamish","refinish"): "/issaquah-wa-flooring-services/hardwood-floor-refinishing-in-sammamish-wa-wills-flooring",
  ("Lynnwood","refinish"): "/lynnwood-wa-flooring-services/hardwood-floor-refinishing-in-lynnwood-wa-wills-flooring",
  ("Edmonds","refinish"): "/edmonds-flooring-services/hardwood-floor-refinishing-in-edmonds-wa-wills-flooring",
  ("Kirkland","refinish"): "/kirkland-flooring-services/hardwood-floor-refinishing-in-kirkland-wa-wills-flooring",
  ("Mukilteo","refinish"): "/mukilteo-flooring-services/hardwood-floor-refinishing-in-mukilteo-wa-wills-flooring",
  ("Marysville","refinish"): "/marysville-flooring-services/hardwood-floor-refinishing-in-marysville-wa-wills-flooring",
  ("Lake Stevens","refinish"): "/lake-stevens-flooring-services/hardwood-floor-refinishing-in-lake-stevens-wa-wills-flooring",
  ("Bothell","refinish"): "/bothell-flooring-services/hardwood-floor-refinishing-in-bothell-wa-wills-flooring",
  ("Bellevue","refinish"): "/bellevue-flooring-services/hardwood-floor-refinishing-in-bellevue-wa-wills-flooring",
  ("Shoreline","refinish"): "/shoreline-flooring-services/hardwood-floor-refinishing-in-shoreline-wa-wills-flooring",
  ("Everett","lvp"): "/everett-flooring-services/vinyl-plank-flooring-installation-in-everett-wa",
  ("Everett","laminate"): "/everett-flooring-services/laminate-flooring-installation-in-everett-wa",
  ("Everett","hardwood"): "/everett-flooring-services/expert-wood-floor-installation-in-everett-wa-professional-flooring-services",
  ("Lynnwood","hardwood"): "/lynnwood-wa-flooring-services/expert-hardwood-floor-installation-in-lynnwood-wa",
  ("Mukilteo","hardwood"): "/mukilteo-flooring-services/professional-wood-floor-installation-in-mukilteo-wa-expert-services",
}

I = {
'dollar':'<path d="M12 2v20M17 6.5H9.5a3 3 0 0 0 0 6h5a3 3 0 0 1 0 6H6"/>',
'clock':'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
'ruler':'<path d="M3 17 17 3l4 4L7 21z"/><path d="m8 8 1.5 1.5M11 5l1.5 1.5M14 14l1.5 1.5M5 11l1.5 1.5"/>',
'shield':'<path d="M12 3 5 6v5c0 5 3.5 8.5 7 10 3.5-1.5 7-5 7-10V6z"/><path d="m9 12 2 2 4-4"/>',
'home':'<path d="m3 11 9-8 9 8v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
'factory':'<path d="M3 21V9l6 4V9l6 4V4h6v17z"/>',
'layers':'<path d="m12 3 9 5-9 5-9-5z"/><path d="m3 13 9 5 9-5"/>',
'leaf':'<path d="M20 4c-9 0-15 5-15 13a4 4 0 0 0 4 4c8 0 11-7 11-17z"/><path d="M5 21c3-6 7-9 12-12"/>',
'palette':'<circle cx="12" cy="12" r="9"/><circle cx="8.5" cy="10" r="1"/><circle cx="12" cy="7" r="1"/><circle cx="15.5" cy="10" r="1"/><path d="M12 21c-1.5-2 1-4 3-4h1.5a2.5 2.5 0 0 0 0-5"/>',
'refresh':'<path d="M20 12a8 8 0 1 1-2.3-5.7"/><path d="M20 4v5h-5"/>',
'calendar':'<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M8 3v4M16 3v4M3 10h18"/>',
'wind':'<path d="M4 8h10a3 3 0 1 0-3-3"/><path d="M4 12h14a3 3 0 1 1-3 3"/><path d="M4 16h7a2 2 0 1 1-2 2"/>',
'washer':'<rect x="4" y="3" width="16" height="18" rx="2"/><circle cx="12" cy="13" r="4"/><path d="M8 7h.01M11 7h2"/>',
'plug':'<path d="M9 3v5M15 3v5M6 8h12v4a6 6 0 0 1-12 0z"/><path d="M12 18v3"/>',
'stairs':'<path d="M3 21h4v-4h4v-4h4V9h4V5h2"/>',
'vent':'<rect x="3" y="7" width="18" height="10" rx="2"/><path d="M7 10h10M7 14h10"/>',
'scissors':'<circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M20 4 8.5 15.5M20 20 8.5 8.5"/>',
'frame':'<rect x="3" y="3" width="18" height="18" rx="2"/><rect x="7" y="7" width="10" height="10" rx="1"/>',
'clipboard':'<rect x="6" y="4" width="12" height="17" rx="2"/><path d="M9 4V3h6v1M9 11h6M9 15h4"/>',
'hammer':'<path d="m14 6 6 6-2 2-6-6z"/><path d="M4 20l7-7 3 3-7 7z"/><path d="m11 3 3 3"/>',
'droplet':'<path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/>',
'brush':'<path d="M4 20c3 0 4-2 4-4l8-8 4 4-8 8c-2 0-4 1-8 0z"/><path d="m14 6 4 4"/>',
'done':'<circle cx="12" cy="12" r="9"/><path d="m8 12 3 3 5-6"/>',
'paw':'<circle cx="7" cy="9" r="1.6"/><circle cx="11" cy="6" r="1.6"/><circle cx="15.5" cy="7" r="1.6"/><circle cx="18.5" cy="11" r="1.6"/><path d="M12 11c-3 0-6 3-6 6a2 2 0 0 0 3 1.7c1-.6 2-.6 3-.6s2 0 3 .6A2 2 0 0 0 18 17c0-3-3-6-6-6z"/>',
'snow':'<path d="M12 2v20M2 12h20M5 5l14 14M19 5 5 19"/>',
'sun':'<circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1 7 17M17 7l2.1-2.1"/>',
'flame':'<path d="M12 3c1 4 5 5 5 10a5 5 0 0 1-10 0c0-2 1-3 2-4 0 2 1 3 2 3 0-3-1-5 1-9z"/>',
'award':'<circle cx="12" cy="9" r="6"/><path d="m8.5 14-1.5 7 5-3 5 3-1.5-7"/>',
'lock':'<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
'pin':'<path d="M12 21s-7-6-7-11a7 7 0 0 1 14 0c0 5-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
'sparkle':'<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2 2M16 16l2 2M6 18l2-2M16 8l2-2"/>',
'water':'<path d="M3 15c2-2 4-2 6 0s4 2 6 0 4-2 6 0"/><path d="M3 10c2-2 4-2 6 0s4 2 6 0 4-2 6 0"/>',
'search':'<circle cx="11" cy="11" r="6"/><path d="m20 20-4.5-4.5"/>',
'truck':'<path d="M3 6h11v10H3zM14 10h4l3 3v3h-7z"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
'box':'<path d="m3 8 9-5 9 5v8l-9 5-9-5z"/><path d="M3 8l9 5 9-5M12 13v8"/>',
'baby':'<circle cx="12" cy="8" r="4"/><path d="M6 21v-2a6 6 0 0 1 12 0v2"/>',
'sofa':'<path d="M4 11V8a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v3"/><path d="M2 13a2 2 0 0 1 4 0v3h12v-3a2 2 0 0 1 4 0v5H2z"/>',
'thermo':'<path d="M10 4a2 2 0 0 1 4 0v9a4 4 0 1 1-4 0z"/>',
'tag':'<path d="M3 12V4h8l9 9-8 8z"/><circle cx="7.5" cy="8.5" r="1.5"/>',
'chart':'<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
'grid':'<rect x="3" y="3" width="8" height="8" rx="1.5"/><rect x="13" y="3" width="8" height="8" rx="1.5"/><rect x="3" y="13" width="8" height="8" rx="1.5"/><rect x="13" y="13" width="8" height="8" rx="1.5"/>',
'moon':'<path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z"/>',
'volume':'<path d="M4 9v6h4l5 4V5L8 9z"/><path d="M16 9a4 4 0 0 1 0 6M19 6a8 8 0 0 1 0 12"/>',
'key':'<circle cx="8" cy="15" r="4"/><path d="m11 12 9-9M17 6l3 3M14 9l3 3"/>',
'phone':'<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>',
'star':'<path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>',
'x':'<circle cx="12" cy="12" r="9"/><path d="M9 9l6 6M15 9l-6 6"/>',
'alert':'<path d="M12 3 2 20h20z"/><path d="M12 10v4M12 17h.01"/>',
'wallet':'<rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 10h18M16 14h2"/>',
'tree':'<path d="M12 3 5 13h4l-3 5h12l-3-5h4z"/><path d="M12 18v3"/>',
'mop':'<path d="M12 3v11"/><path d="M8 14h8l1 7H7z"/>',
'dog':'<path d="M5 9h4l3-4 3 4h4l-2 5v7H7v-7z"/><circle cx="10" cy="12" r="1"/><circle cx="14" cy="12" r="1"/>',
'basement':'<path d="M3 11 12 4l9 7"/><path d="M5 10v10h14V10"/><path d="M9 20v-5h6v5"/>',
'moisture':'<path d="M7 5s3 3.5 3 6a3 3 0 0 1-6 0c0-2.5 3-6 3-6z"/><path d="M16 9s4 4.5 4 8a4 4 0 0 1-8 0c0-3.5 4-8 4-8z"/>',
'ruler2':'<rect x="3" y="8" width="18" height="8" rx="1.5"/><path d="M7 8v3M11 8v4M15 8v3M19 8v4"/>',
}
def ic(n, cls="ap-ic"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{I[n]}</svg>'
def ib(n, gold=False):
    return f'<span class="ap-ib{" gold" if gold else ""}">{ic(n)}</span>'
def emb(inner): return "<div data-rt-embed-type='true'>" + inner + "</div>"

BASE_CSS = r"""<style>
.ap{--ink:#1d1d1f;--ink2:#6e6e73;--bg:#f5f5f7;--card:#fff;--line:rgba(0,0,0,.08);--navy:#071730;--navy2:#03101f;--gold:#ea8a2a;--r:24px;font-family:-apple-system,BlinkMacSystemFont,"SF Pro Display","SF Pro Text","Helvetica Neue",Inter,system-ui,sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased}
.ap *{box-sizing:border-box}
.w-richtext a:not(.ap-btn):not(.star),.blog-post-content-wrapper a:not(.ap-btn):not(.star){display:inline!important;color:#071730!important;text-decoration:underline!important;text-underline-offset:3px;text-decoration-thickness:1px}
.w-richtext a:not(.ap-btn):not(.star):hover,.blog-post-content-wrapper a:not(.ap-btn):not(.star):hover{color:#ea8a2a!important}
.w-richtext a.ap-btn,.blog-post-content-wrapper a.ap-btn{display:inline-flex!important;text-decoration:none!important}
.ap-ic{width:20px;height:20px;flex:0 0 auto;stroke:currentColor;fill:none;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;vertical-align:-4px}
.ap-ib{display:inline-flex;align-items:center;justify-content:center;width:40px;height:40px;border-radius:12px;background:rgba(7,23,48,.06);color:#071730;margin-bottom:12px}
.ap-ib.gold{background:rgba(234,138,42,.14);color:#c46a12}
.ap-tile .ap-ib{width:32px;height:32px;border-radius:10px;margin-bottom:8px}
.ap-tile .ap-ib .ap-ic{width:17px;height:17px}
.ap-lab-ic{display:inline-flex;align-items:center;gap:8px}
.ap-lab-ic .ap-ic{width:18px;height:18px;color:#6e6e73}
.ap-li-ic{display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;border-radius:7px;background:rgba(7,23,48,.06);color:#071730;margin-right:8px;vertical-align:-5px}
.ap-li-ic .ap-ic{width:14px;height:14px}
.ap-panel{background:var(--bg);border-radius:28px;padding:36px 28px;margin:28px 0}
@media(max-width:680px){.ap-panel{padding:24px 18px;border-radius:22px}}
.ap-card{background:var(--card);border-radius:var(--r);padding:26px;box-shadow:0 2px 12px rgba(0,0,0,.04)}
.ap-eyebrow{display:block;font-size:13px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--gold);margin-bottom:10px}
.ap-h{margin:0 0 8px;font-size:clamp(28px,3.4vw,40px);line-height:1.08;letter-spacing:-.02em;font-weight:700;text-align:center;color:var(--ink)}
.ap-sub{margin:0 auto 26px;max-width:620px;text-align:center;font-size:18px;line-height:1.5;color:var(--ink2)}
.ap-lead{margin:0;font-size:clamp(19px,2.2vw,24px);line-height:1.4;letter-spacing:-.01em;font-weight:600;color:var(--ink)}
.ap-lead span{font-weight:400;color:var(--ink2)}
.ap-grid{display:grid;gap:14px}
.ap-grid.c2{grid-template-columns:repeat(2,minmax(0,1fr))}
.ap-grid.c3{grid-template-columns:repeat(3,minmax(0,1fr))}
.ap-grid.c4{grid-template-columns:repeat(4,minmax(0,1fr))}
@media(max-width:820px){.ap-grid.c3,.ap-grid.c4{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:560px){.ap-grid.c2,.ap-grid.c3,.ap-grid.c4{grid-template-columns:1fr}}
.ap-tile{background:var(--card);border-radius:18px;padding:18px 18px 16px}
.ap-tile b{display:block;font-size:12px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--ink2);margin-bottom:6px}
.ap-tile span.v{display:block;font-size:24px;font-weight:700;letter-spacing:-.02em;color:var(--ink)}
.ap-num{display:block;font-size:34px;font-weight:700;letter-spacing:-.03em;color:var(--ink);margin-bottom:6px}
html body .post-body .ap-card p, .ap-card p{margin:0!important;font-size:15.5px!important;line-height:1.55!important;color:var(--ink2)!important}
.ap-price{font-size:44px;font-weight:700;letter-spacing:-.03em;color:var(--ink);line-height:1;margin:10px 0 6px}
.ap-price small{font-size:15px;font-weight:500;color:var(--ink2);letter-spacing:0;margin-left:4px}
.ap-tag{display:inline-block;font-size:12px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--ink2);background:var(--bg);border-radius:999px;padding:5px 11px}
.ap-tag.gold{color:#9a5410;background:rgba(234,138,42,.14)}
.ap-h3{margin:0;font-size:20px;font-weight:700;letter-spacing:-.01em;color:var(--ink)}
.ap-table{width:100%;border-collapse:collapse;font-size:15px;color:var(--ink)}
.ap-table th{font-size:12px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--ink2);text-align:left;padding:0 12px 12px;border-bottom:1px solid var(--line)}
.ap-table td{padding:14px 12px;border-bottom:1px solid var(--line);vertical-align:top;line-height:1.45}
.ap-table tr:last-child td{border-bottom:0}
.ap-table td strong{font-weight:700;color:var(--ink)}
.ap-table td .m{color:var(--ink2);font-size:14px}
.ap-list{list-style:none;margin:14px 0 0;padding:0}
.ap-list li{position:relative;padding:12px 0 12px 32px;border-top:1px solid var(--line);line-height:1.5;color:var(--ink)}
.ap-list li:first-child{border-top:0;padding-top:0}
.ap-list li:before{content:"";position:absolute;left:0;top:calc(50% - 10px);width:20px;height:20px;border-radius:50%;background:var(--navy);-webkit-mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3E%3Ccircle cx='10' cy='10' r='10'/%3E%3Cpath d='M6 10.5l2.6 2.6L14 7.5' stroke='%23fff' stroke-width='2' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/contain no-repeat;mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3E%3Ccircle cx='10' cy='10' r='10'/%3E%3Cpath d='M6 10.5l2.6 2.6L14 7.5' stroke='%23fff' stroke-width='2' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/contain no-repeat}
.ap-list li:first-child:before{top:calc(50% - 16px)}
.ap-list.noicon li{padding-left:0}.ap-list.noicon li:before{display:none}
.ap-list.x li:before{background:#c7c7cc;-webkit-mask-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3E%3Ccircle cx='10' cy='10' r='10'/%3E%3Cpath d='M7 7l6 6M13 7l-6 6' stroke='%23fff' stroke-width='2' stroke-linecap='round'/%3E%3C/svg%3E");mask-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3E%3Ccircle cx='10' cy='10' r='10'/%3E%3Cpath d='M7 7l6 6M13 7l-6 6' stroke='%23fff' stroke-width='2' stroke-linecap='round'/%3E%3C/svg%3E")}
.ap-btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;background:var(--navy);color:#fff!important;border:0;border-radius:999px;padding:14px 24px;font-size:16px;font-weight:600;text-decoration:none!important;cursor:pointer;transition:transform .2s,background .2s}
.ap-btn:hover{background:var(--navy2);transform:translateY(-1px)}
.ap-btn.ghost{background:transparent;color:var(--navy)!important;border:1.5px solid rgba(7,23,48,.25)}
.ap-btn.ghost:hover{background:rgba(7,23,48,.05)}
.ap-btn.white{background:#fff;color:var(--navy)!important}
.ap-btn.white:hover{background:#f2f2f4}
.ap-steps{list-style:none;margin:0;padding:0;display:grid;gap:10px}
.ap-steps li{display:grid;grid-template-columns:84px 1fr;gap:16px;align-items:start;background:var(--card);border-radius:18px;padding:16px 18px}
.ap-steps .d{display:flex;flex-direction:column;gap:6px;font-size:13px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;color:var(--navy);padding-top:2px}
.ap-steps .d .ap-ic{color:#6e6e73}
.ap-steps .t{font-size:15.5px;line-height:1.5;color:var(--ink)}
.ap-steps .t em{display:block;font-style:normal;color:var(--ink2);font-size:14px;margin-top:4px}
.ap-steps.wide li{grid-template-columns:200px 1fr}
.ap-steps.wide .d{text-transform:none;letter-spacing:0;font-size:15px;line-height:1.35}
@media(max-width:560px){.ap-steps li,.ap-steps.wide li{grid-template-columns:1fr;gap:6px}}
.ap-callout{display:grid;grid-template-columns:44px 1fr;gap:14px;align-items:start;background:#fff;border-radius:18px;padding:18px 20px;margin:22px 0;box-shadow:0 2px 12px rgba(0,0,0,.04)}
.ap-callout .ap-ib{margin:0}
html body .post-body .ap-callout p, .ap-callout p{margin:0!important;font-size:15.5px!important;line-height:1.55!important;color:var(--ink)!important}
.ap-callout p strong{display:block;margin-bottom:2px}
html.ap-ready .ap-rv{opacity:0;transform:translateY(14px);transition:opacity .6s ease,transform .6s ease}
html.ap-ready .ap-rv.ap-in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){html.ap-ready .ap-rv{opacity:1!important;transform:none!important;transition:none!important}}
</style>"""

CALC_CSS = r"""<style>
.rc-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.rc-span{grid-column:1/-1}
.rc-field{display:flex;flex-direction:column;gap:8px;background:#fff;border-radius:18px;padding:16px 18px;min-width:0}
.rc-lab{display:block;font-size:15px;font-weight:600;color:#1d1d1f}
.rc-field small{color:#6e6e73;font-size:13px}
.rc-in{display:flex;align-items:center;gap:8px;border:1px solid rgba(0,0,0,.1);border-radius:12px;padding:0 14px;background:#fff}
.rc-in input{border:0;outline:0;flex:1;min-width:0;padding:12px 0;font:inherit;font-size:20px;font-weight:600;color:#1d1d1f;background:transparent}
.rc-in i{font-style:normal;color:#6e6e73;font-size:14px}
.rc-field select{border:1px solid rgba(0,0,0,.1);border-radius:12px;padding:12px 14px;font:inherit;font-size:15px;background:#fff;width:100%;min-width:0;text-overflow:ellipsis;color:#1d1d1f}
.rc-seg{display:grid;grid-template-columns:repeat(var(--n,3),1fr);background:#e9e9ee;border-radius:14px;padding:4px;gap:4px}
.rc-seg button{border:0;background:transparent;border-radius:11px;padding:10px 6px;font:inherit;font-size:15px;font-weight:600;color:#1d1d1f;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:2px;transition:background .2s,box-shadow .2s}
.rc-seg button em{font-style:normal;font-size:12px;font-weight:500;color:#6e6e73}
.rc-seg button.on{background:#fff;box-shadow:0 1px 4px rgba(0,0,0,.12)}
.rc-row{flex-direction:row;align-items:center;justify-content:space-between}
.rc-row>span:first-child{display:flex;flex-direction:column;gap:2px}
.rc-sw{position:relative;width:51px;height:31px;flex:0 0 auto}
.rc-sw input{position:absolute;inset:0;opacity:0;margin:0;cursor:pointer;z-index:2;width:100%;height:100%}
.rc-sw i{position:absolute;inset:0;border-radius:999px;background:#e9e9ea;transition:background .25s}
.rc-sw i:after{content:"";position:absolute;top:2px;left:2px;width:27px;height:27px;border-radius:50%;background:#fff;box-shadow:0 3px 8px rgba(0,0,0,.15);transition:transform .25s}
.rc-sw input:checked+i{background:#34c759}
.rc-sw input:checked+i:after{transform:translateX(20px)}
.rc-step{display:inline-flex;align-items:center;background:#e9e9ee;border-radius:12px;padding:3px}
.rc-step button{width:36px;height:34px;border:0;background:#fff;border-radius:9px;font-size:20px;line-height:1;cursor:pointer;color:#1d1d1f;box-shadow:0 1px 3px rgba(0,0,0,.1)}
.rc-step input{width:46px;border:0;background:transparent;text-align:center;font:inherit;font-size:18px;font-weight:600;color:#1d1d1f;outline:0;-moz-appearance:textfield}
.rc-step input::-webkit-outer-spin-button,.rc-step input::-webkit-inner-spin-button{-webkit-appearance:none;margin:0}
.rc-actions{display:flex;gap:10px;flex-wrap:wrap;margin-top:4px}
.rc-result{margin-top:20px;background:#fff;border-radius:22px;padding:24px}
.rc-top{display:flex;flex-wrap:wrap;gap:14px;align-items:flex-end;justify-content:space-between}
.rc-lab2{display:block;font-size:13px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:#6e6e73}
.rc-total{display:block;font-size:44px;font-weight:700;letter-spacing:-.03em;color:#1d1d1f;line-height:1.1}
.rc-pills{display:flex;gap:8px;flex-wrap:wrap}
.rc-pills span{background:#f5f5f7;border-radius:999px;padding:8px 14px;font-size:14px;color:#1d1d1f}
.rc-break{margin:16px 0 0;padding:0;list-style:none;border-top:1px solid rgba(0,0,0,.08)}
.rc-break li{padding:10px 0;border-bottom:1px solid rgba(0,0,0,.08);font-size:15px;color:#1d1d1f;display:flex;justify-content:space-between;gap:12px}
.rc-break li span:last-child{font-weight:600;white-space:nowrap}
.rc-note{margin-top:16px;padding:16px 18px;border-radius:16px;background:#f5f5f7;font-size:15px;line-height:1.55;color:#1d1d1f}
.rc-note strong{display:block;margin-bottom:2px}
@media(max-width:640px){.rc-grid{grid-template-columns:1fr}.rc-total{font-size:36px}}
</style>"""

QUIZ_CSS = r"""<style>
.oq-list{display:grid;gap:10px}
.oq-q{background:#fff;border-radius:18px;padding:16px 18px}
.oq-q>span{display:block;font-weight:600;margin-bottom:10px;line-height:1.45;color:#1d1d1f}
.oq-btns{display:flex;gap:8px;flex-wrap:wrap}
.oq-btns button{border:1.5px solid rgba(0,0,0,.12);background:#fff;border-radius:999px;padding:9px 16px;font:inherit;font-size:15px;font-weight:600;cursor:pointer;color:#1d1d1f;transition:background .2s,border-color .2s,color .2s}
.oq-btns button.on{background:#071730;border-color:#071730;color:#fff}
.oq-out{margin-top:14px;padding:22px 24px;border-radius:22px;background:#fff;line-height:1.55}
.oq-out h4{margin:0 0 6px;font-size:22px;letter-spacing:-.01em;color:#1d1d1f}
.oq-out p{margin:0;color:#1d1d1f}
.oq-out a{color:#071730;font-weight:600}
</style>"""

FAQ_CSS = r"""<style>
.faq-wrap{margin:36px 0}
.faq-items{border-top:1px solid rgba(0,0,0,.1)}
.faq-item{border-bottom:1px solid rgba(0,0,0,.1)}
.faq-q{cursor:pointer;list-style:none;display:flex;align-items:center;justify-content:space-between;gap:16px;padding:18px 2px;font-size:17px;font-weight:600;color:#1d1d1f;line-height:1.4}
.faq-q::-webkit-details-marker{display:none}
.faq-q:after{content:"";flex:0 0 22px;width:22px;height:22px;border-radius:50%;background:#f5f5f7 url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 22 22'%3E%3Cpath d='M11 6v10M6 11h10' stroke='%231d1d1f' stroke-width='1.8' stroke-linecap='round'/%3E%3C/svg%3E") center/22px no-repeat;transition:transform .25s}
.faq-item[open] .faq-q:after{transform:rotate(45deg)}
.faq-a{padding:0 2px 20px;color:#515154;line-height:1.6;font-size:16px;max-width:760px}
</style>"""

# ---------- calculator kinds ----------
CALC = {
 "refinish": dict(title="Refinishing Calculator", sub="Real Wills Flooring pricing. Pick the service, enter your area, and see the number before anyone visits.",
   seg=[("natural","Natural","$3.99",3.99),("stain","Stain","$6.50",6.50),("recoat","Recoat","$1.99",1.99)], default="natural", minsf=500,
   stairs=(55,75,"$55–$75 per tread"), addons=[("dust","wind","Dust containment","+$250",250),("wd","washer","Move washer &amp; dryer","+$160 per pair",160)], appl=80,
   note="Ballpark only. We confirm the exact price at a free in-home estimate."),
 "hardwood": dict(title="Hardwood Installation Calculator", sub="Installation pricing from our published rate card. Material is quoted separately based on the floor you choose.",
   seg=[("eng","Engineered","$3.25",3.25),("solid","Solid","$3.25",3.25),("unf","Unfinished","$2.75",2.75)], default="eng", minsf=500,
   stairs=(125,125,"$125 per stair"), addons=[], appl=None,
   note="Installation labor only, 500 sq ft minimum. Flooring material, underlayment and old-floor removal are quoted separately at the free estimate."),
 "lvp": dict(title="Vinyl Plank Installation Calculator", sub="Installation pricing from our published rate card. Material is quoted separately based on the plank you choose.",
   seg=[("lvp","Vinyl plank","$2.50",2.50),("lam","Laminate","$2.50",2.50)], default="lvp", minsf=500,
   stairs=(100,100,"$100 per stair"), addons=[], appl=None,
   note="Installation labor only, 500 sq ft minimum. Plank, underlayment and old-floor removal are quoted separately at the free estimate."),
 "laminate": dict(title="Laminate Installation Calculator", sub="Installation pricing from our published rate card. Material is quoted separately based on the plank you choose.",
   seg=[("lam","Laminate","$2.50",2.50),("lvp","Vinyl plank","$2.50",2.50)], default="lam", minsf=500,
   stairs=(100,100,"$100 per stair"), addons=[], appl=None,
   note="Installation labor only, 500 sq ft minimum. Plank, underlayment and old-floor removal are quoted separately at the free estimate."),
}

def render_calc(kind, extra_note=None):
    c = CALC[kind]; n=len(c["seg"])
    seg = "".join('<button type="button"%s data-v="%s">%s <em>%s</em></button>' % (' class="on"' if k==c["default"] else "", k, lab, pr) for k,lab,pr,_ in c["seg"])
    addons = "".join(f'<label class="rc-field rc-row"><span><span class="rc-lab ap-lab-ic">{ic(icn)}{lab}</span><small>{pr}</small></span><span class="rc-sw"><input id="rc-{k}" type="checkbox"><i></i></span></label>' for k,icn,lab,pr,_ in c["addons"])
    appl = (f'<label class="rc-field rc-row"><span><span class="rc-lab ap-lab-ic">{ic("plug")}Other appliances</span><small>+${c["appl"]} each</small></span><span class="rc-step"><button type="button" data-d="-1" aria-label="Fewer">−</button><input id="rc-appliances" type="number" min="0" value="0" inputmode="numeric"><button type="button" data-d="1" aria-label="More">+</button></span></label>') if c["appl"] else ""
    rates = ",".join(f'{k}:{r}' for k,_,_,r in c["seg"]); names = ",".join(f"{k}:'{lab}'" for k,lab,_,_ in c["seg"])
    addjs = "".join(f"if(g('rc-{k}')&&g('rc-{k}').checked){{add+={v};html+=row('{re.sub('&amp;','&',lab)}',money({v}))}}" for k,_,lab,_,v in c["addons"])
    appljs = f"var ap=g('rc-appliances');if(ap){{var q=Math.max(0,parseInt(ap.value||'0',10));if(q>0){{add+=q*{c['appl']};html+=row('Other appliances · '+q+' × ${c['appl']}',money(q*{c['appl']}))}}}}" if c["appl"] else ""
    lo,hi,slab = c["stairs"]
    html_ = f'''<!-- Wills Flooring — {c["title"]} -->
<section class="ap ap-panel rc" aria-labelledby="refi-calc-title" id="calc">
  <h2 id="refi-calc-title" class="ap-h" style="margin-top:0">{c["title"]}</h2>
  <p class="ap-sub">{c["sub"]}</p>
  <form class="rc-grid" onsubmit="return false;">
    <div class="rc-field rc-span"><span class="rc-lab ap-lab-ic">{ic("brush")}Service</span><div class="rc-seg" style="--n:{n}" role="radiogroup" aria-label="Service">{seg}</div><input type="hidden" id="rc-finish" value="{c["default"]}"></div>
    <label class="rc-field"><span class="rc-lab ap-lab-ic">{ic("ruler")}Total floor area</span><div class="rc-in"><input id="rc-area" type="number" min="1" value="850" inputmode="numeric"><i>sq ft</i></div><small>{c["minsf"]} sq ft minimum billed</small></label>
    <label class="rc-field"><span class="rc-lab ap-lab-ic">{ic("stairs")}Stairs</span><div class="rc-in"><input id="rc-stairs" type="number" min="0" value="0" inputmode="numeric"><i>treads</i></div><small>{slab}</small></label>
    {addons}{appl}
    <div class="rc-actions rc-span"><button type="button" id="rc-calc" class="ap-btn">Calculate</button><button type="button" id="rc-reset" class="ap-btn ghost">Reset</button></div>
  </form>
  <div id="rc-result" class="rc-result" hidden aria-live="polite">
    <div class="rc-top"><div><span class="rc-lab2">Estimated total</span><span id="rc-total" class="rc-total">$—</span></div><div class="rc-pills"><span><strong id="rc-billed-sf">—</strong> sq ft billed</span><span><span id="rc-per-sf">$—</span> / sq ft</span></div></div>
    <ul id="rc-breakdown" class="rc-break"></ul>
    {('<div class="rc-note">'+extra_note+'</div>') if extra_note else ''}
    <div style="display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-top:18px"><a class="ap-btn" href="/contact">Lock it in with a free in-home estimate</a><span style="font-size:14px;color:#6e6e73">{c["note"]}</span></div>
  </div>
</section>
<script>
(function(){{var R={{{rates}}},N={{{names}}},MIN={c["minsf"]},SL={lo},SH={hi};var g=function(i){{return document.getElementById(i)}};var money=function(n){{return new Intl.NumberFormat('en-US',{{style:'currency',currency:'USD',maximumFractionDigits:0}}).format(Math.round(n))}};function row(l,v){{return '<li><span>'+l+'</span><span>'+v+'</span></li>'}}
function calc(){{var raw=Math.max(1,parseFloat(g('rc-area').value||'0')),billed=Math.max(MIN,raw),k=g('rc-finish').value,rate=R[k],base=billed*rate,add=0,html='';html+=row(N[k]+' · '+billed.toLocaleString()+' sq ft × $'+rate.toFixed(2),money(base));{addjs}{appljs}var t=Math.max(0,parseInt(g('rc-stairs').value||'0',10)),lo=base+add,hi=base+add;if(t>0){{lo+=t*SL;hi+=t*SH;html+=row('Stairs · '+t+(SL===SH?' × $'+SL:' × $'+SL+'–$'+SH),SL===SH?money(t*SL):money(t*SL)+' – '+money(t*SH))}}
g('rc-result').hidden=false;g('rc-total').textContent=(lo===hi)?money(lo):money(lo)+' – '+money(hi);g('rc-billed-sf').textContent=billed.toLocaleString('en-US');g('rc-per-sf').textContent='$'+rate.toFixed(2);g('rc-breakdown').innerHTML=html}}
function live(){{if(!g('rc-result').hidden)calc()}}
document.querySelectorAll('.rc-seg button').forEach(function(b){{b.addEventListener('click',function(){{document.querySelectorAll('.rc-seg button').forEach(function(x){{x.classList.remove('on')}});b.classList.add('on');g('rc-finish').value=b.getAttribute('data-v');live()}})}});
document.querySelectorAll('.rc-step button').forEach(function(b){{b.addEventListener('click',function(){{var i=g('rc-appliances');i.value=Math.max(0,(parseInt(i.value||'0',10))+parseInt(b.getAttribute('data-d'),10));live()}})}});
g('rc-calc').addEventListener('click',calc);g('rc-reset').addEventListener('click',function(){{g('rc-area').value=850;g('rc-finish').value='{c["default"]}';document.querySelectorAll('.rc-seg button').forEach(function(x){{x.classList.toggle('on',x.getAttribute('data-v')==='{c["default"]}')}});g('rc-stairs').value=0;document.querySelectorAll('.rc-sw input').forEach(function(x){{x.checked=false}});if(g('rc-appliances'))g('rc-appliances').value=0;g('rc-result').hidden=true}});
['rc-area','rc-stairs','rc-appliances'{"".join(",'rc-"+k+"'" for k,_,_,_,_ in c["addons"])}].forEach(function(id){{var e=g(id);if(e)e.addEventListener('change',live)}});}})();
</script>'''
    return emb(CALC_CSS) + "\n\n" + emb(html_)

def render_estimator(spec):
    """Price-free scope estimator (used for carpet until a rate is confirmed)."""
    return emb(CALC_CSS) + "\n\n" + emb(f'''<section class="ap ap-panel" id="calc" aria-labelledby="refi-calc-title">
  <h2 id="refi-calc-title" class="ap-h" style="margin-top:0">{spec.get("title","Scope Your Project")}</h2>
  <p class="ap-sub">{spec.get("sub","Tell us the rooms and we will bring samples and a firm price to your door.")}</p>
  <form class="rc-grid" onsubmit="return false;">
    <label class="rc-field"><span class="rc-lab ap-lab-ic">{ic("ruler")}Total floor area</span><div class="rc-in"><input id="es-area" type="number" min="1" value="600" inputmode="numeric"><i>sq ft</i></div><small>Rough is fine; we measure on site</small></label>
    <label class="rc-field"><span class="rc-lab ap-lab-ic">{ic("stairs")}Stairs</span><div class="rc-in"><input id="es-stairs" type="number" min="0" value="0" inputmode="numeric"><i>treads</i></div><small>Straight, pie-shaped or open-sided</small></label>
    <label class="rc-field rc-row"><span><span class="rc-lab ap-lab-ic">{ic("truck")}Remove old flooring</span><small>Tear-out and haul-away</small></span><span class="rc-sw"><input id="es-rem" type="checkbox"><i></i></span></label>
    <label class="rc-field rc-row"><span><span class="rc-lab ap-lab-ic">{ic("sofa")}Move furniture</span><small>We can handle it</small></span><span class="rc-sw"><input id="es-furn" type="checkbox"><i></i></span></label>
    <div class="rc-actions rc-span"><button type="button" id="es-go" class="ap-btn">Build my estimate request</button></div>
  </form>
  <div id="es-out" class="rc-result" hidden aria-live="polite"><span class="rc-lab2">Your project</span><ul id="es-list" class="rc-break"></ul><div style="display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-top:18px"><a class="ap-btn" id="es-link" href="/contact">Request a free in-home estimate</a><a class="ap-btn ghost" href="{TEL}">Call {PHONE}</a></div></div>
</section>
<script>(function(){{var g=function(i){{return document.getElementById(i)}};g('es-go').addEventListener('click',function(){{var a=Math.max(1,parseInt(g('es-area').value||'0',10)),s=Math.max(0,parseInt(g('es-stairs').value||'0',10)),h='';h+='<li><span>Floor area</span><span>'+a.toLocaleString()+' sq ft</span></li>';if(s>0)h+='<li><span>Stairs</span><span>'+s+' treads</span></li>';if(g('es-rem').checked)h+='<li><span>Old flooring removal</span><span>Yes</span></li>';if(g('es-furn').checked)h+='<li><span>Furniture moving</span><span>Yes</span></li>';h+='<li><span>Next step</span><span>Free in-home measure</span></li>';g('es-list').innerHTML=h;g('es-out').hidden=false}})}})();</script>''')

def render_quiz(q):
    items = "".join(f'<div class="oq-q" data-k="{it["k"]}"><span>{i+1}. {it["q"]}</span><div class="oq-btns">' + "".join(f'<button type="button" data-v="{v}">{l}</button>' for v,l in it["opts"]) + '</div></div>' for i,it in enumerate(q["items"]))
    J = lambda x: json.dumps(x, ensure_ascii=False).replace("</", "<\\/")
    rules = "".join(f"if({r['when']}){{h={J(r['h'])};p={J(r['p'])}}}else " for r in q["rules"]) + f"{{h={J(q['default']['h'])};p={J(q['default']['p'])}}}"
    return emb(QUIZ_CSS) + "\n\n" + emb(f'''<section class="ap ap-panel oq" aria-labelledby="oq-title">
  <h3 id="oq-title" class="ap-h" style="font-size:28px">{q["title"]}</h3>
  <p class="ap-sub" style="margin-bottom:18px">{q.get("sub","Answer honestly. The verdict updates as you go.")}</p>
  <div class="oq-list">{items}</div>
  <div id="oq-out" class="oq-out" hidden aria-live="polite"></div>
</section>
<script>(function(){{var a={{}},qs=document.querySelectorAll('.oq-q');function verdict(){{var out=document.getElementById('oq-out');if(Object.keys(a).length<{q.get("min",3)}){{out.hidden=true;return}}var h,p;{rules}out.innerHTML='<h4>'+h+'</h4><p>'+p+' <a href="/contact">Book a free in-home estimate</a> or call <a href="{TEL}">{PHONE}</a>.</p>';out.hidden=false}}
qs.forEach(function(q){{q.querySelectorAll('button').forEach(function(b){{b.addEventListener('click',function(){{q.querySelectorAll('button').forEach(function(x){{x.classList.remove('on')}});b.classList.add('on');a[q.getAttribute('data-k')]=b.getAttribute('data-v');verdict()}})}})}});}})();</script>''')

def render_faq(faq, title, sub):
    items = "".join(f'<details class="faq-item" role="listitem"><summary class="faq-q">{f["q"]}</summary><div class="faq-a">{f["a"]}</div></details>' for f in faq)
    return emb(f'<section class="ap faq-wrap" aria-labelledby="faq-title"><h2 id="faq-title" class="ap-h">{title}</h2><p class="ap-sub">{sub}</p><div class="faq-items" role="list">{items}</div></section>' + FAQ_CSS)

def strip_tags(s): return re.sub(r"<[^>]+>", "", s).replace("&amp;","&").replace("&nbsp;"," ")

def render_schema(spec):
    cat = CAT[spec["category"]]; url = f"{SITE}/blog-posts/{spec['slug']}"
    faqs = [{"@type":"Question","name":strip_tags(f["q"]),"acceptedAnswer":{"@type":"Answer","text":strip_tags(f["a"])}} for f in spec["faq"]]
    graph = [
      {"@type":"BlogPosting","@id":url+"#article","headline":spec["title"],"description":spec["meta"],"datePublished":spec.get("published",spec.get("date","2026-09-16"))[:10],"dateModified":spec.get("date","2026-09-16")[:10],"inLanguage":"en-US","mainEntityOfPage":url,
       "author":{"@type":"Organization","name":"Wills Flooring","url":SITE+"/"},"publisher":{"@type":"Organization","name":"Wills Flooring","url":SITE+"/"},
       "about":{"@type":"Service","name":cat[1]},"keywords":spec.get("keywords","")},
      {"@type":"Service","@id":url+"#service","serviceType":cat[1],"name":cat[1]+(" in "+spec["city"]+", WA" if spec.get("city") else " in Snohomish & King County, WA"),
       "provider":{"@type":"HomeAndConstructionBusiness","name":"Wills Flooring","url":SITE+"/","telephone":"+1-425-350-4435","foundingDate":"2013","address":{"@type":"PostalAddress","streetAddress":"2109 196th St SW #106","addressLocality":"Lynnwood","addressRegion":"WA","postalCode":"98036","addressCountry":"US"}},
       "areaServed":[{"@type":"City","name":c} for c in (([spec["city"]] if spec.get("city") else [])+["Everett","Seattle","Sammamish","Lynnwood","Edmonds","Kirkland","Snohomish"])[:8]],
       "url":SITE+cat[2]},
      {"@type":"FAQPage","@id":url+"#faq","mainEntity":faqs}]
    if spec.get("offers"): graph[1]["offers"]=[{"@type":"Offer","name":n,"price":p,"priceCurrency":"USD","unitText":u,"priceValidUntil":"2027-12-31"} for n,p,u in spec["offers"]]
    if spec.get("image"): graph[0]["image"]=spec["image"]
    if spec.get("city"): graph[0]["contentLocation"]={"@type":"City","name":spec["city"],"containedInPlace":{"@type":"AdministrativeArea","name":"Washington"}}
    return emb('<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@graph":graph},ensure_ascii=False)+'</script>')

def render_cta(spec):
    city = spec.get("city") or "Snohomish and King County"
    chips = [("award","Bona Certified Craftsmen") if spec["category"] in ("refinish","hardwood") else ("truck","Mobile showroom to your door"),("calendar","Since 2013"),("shield","1-year workmanship warranty"),("lock","Licensed &amp; insured"),("pin","Lynnwood showroom")]
    ch = "".join(f'<span>{ic(i)} {t}</span>' for i,t in chips)
    return emb(f'''<section class="ap ap-cta" style="margin:36px 0"><style>
.ap-cta .in{{background:#071730;border-radius:32px;padding:44px 32px;text-align:center;color:#fff}}
html body .post-body .ap-cta h2, .ap-cta h2{{color:#fff!important;margin:0 0 10px!important;font-size:clamp(26px,3.2vw,38px)!important;letter-spacing:-.02em!important;line-height:1.1!important;font-weight:700!important}}
html body .post-body .ap-cta .s, .ap-cta .s{{color:rgba(255,255,255,.72)!important;font-size:17px!important;line-height:1.5!important;max-width:560px;margin:0 auto 22px!important}}
.ap-cta .row{{display:flex;gap:10px;justify-content:center;flex-wrap:wrap}}
.ap-cta .chips{{display:flex;gap:18px;justify-content:center;flex-wrap:wrap;margin-top:22px;font-size:14px;color:rgba(255,255,255,.7)}}
.ap-cta .chips span{{display:inline-flex;align-items:center;gap:6px}}.ap-cta .chips .ap-ic{{width:16px;height:16px;color:#ea8a2a}}
html body .post-body .ap-cta a.ghost, .ap-cta a.ghost{{color:#fff!important;border-color:rgba(255,255,255,.4)!important}}
.ap-cta a.ghost:hover{{background:rgba(255,255,255,.08)}}
html body .post-body .ap-cta a.star, .ap-cta a.star{{color:#ea8a2a!important;text-decoration:none!important;font-weight:600;display:inline-block;margin-top:16px;font-size:15px}}
@media(max-width:560px){{.ap-cta .in{{padding:32px 20px;border-radius:24px}}}}
</style><div class="in"><h2>{spec.get("cta_title","Get your exact price")}</h2><p class="s">{spec.get("cta_sub",f"We measure, check the subfloor and hand you a firm written quote on the spot. No pressure, no obligation, anywhere in {city}.")}</p><div class="row"><a class="ap-btn white" href="{TEL}">Call {PHONE}</a><a class="ap-btn ghost" href="/contact">Book a free estimate</a></div><div class="chips">{ch}</div><a class="star" href="/about">★★★★★ 4.8 stars, 100+ five-star reviews on Google</a></div></section>''')

ANIM = emb("<script>(function(){try{var els=document.querySelectorAll('.ap-rv');if(!('IntersectionObserver' in window)||!els.length)return;document.documentElement.classList.add('ap-ready');els.forEach(function(e,i){e.style.transitionDelay=Math.min((i%3)*90,270)+'ms'});var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){x.target.classList.add('ap-in');io.unobserve(x.target)}})},{threshold:.12,rootMargin:'0px 0px -6% 0px'});els.forEach(function(e){io.observe(e)});}catch(e){}})();</script>")

def block(b, spec):
    t = b["type"]
    if t == "h2": return f'<h2>{b["text"]}</h2>'
    if t == "h3": return f'<h3>{b["text"]}</h3>'
    if t == "p": return f'<p>{b["html"]}</p>'
    if t == "ul": return "<ul>" + "".join(f"<li>{x}</li>" for x in b["items"]) + "</ul>"
    if t == "quick":
        tiles = "".join(f'<div class="ap-tile">{ib(x["icon"])}<b>{x["label"]}</b><span class="v">{x["value"]}</span></div>' for x in b["tiles"])
        btn = f'<a class="ap-btn" href="#refi-calc-title">{ic("sparkle")} {b.get("cta","Try the calculator")}</a>' if b.get("cta", True) else ""
        return emb(f'<section class="ap ap-panel" style="margin-top:8px"><span class="ap-eyebrow">{b["eyebrow"]}</span><p class="ap-lead">{b["lead"]} <span>{b["detail"]}</span></p><div class="ap-grid c4" style="margin-top:22px">{tiles}</div><div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:22px">{btn}<a class="ap-btn ghost" href="{TEL}">Call {PHONE}</a></div></section>')
    if t == "cards":
        n = b.get("cols", len(b["items"]))
        cards = "".join(f'<div class="ap-card ap-rv">{ib(x["icon"], x.get("gold",False))}' + (f'<br><span class="ap-tag{" gold" if x.get("gold") else ""}">{x["tag"]}</span>' if x.get("tag") else "") + (f'<span class="ap-num">{x["num"]}</span>' if x.get("num") else "") + (f'<h3 class="ap-h3" style="margin:12px 0 8px">{x["title"]}</h3>' if x.get("title") else "") + f'<p>{x["text"]}</p></div>' for x in b["items"])
        inner = f'<div class="ap-grid c{n}">{cards}</div>'
        return emb(f'<section class="ap{" ap-panel" if b.get("panel") else ""}">{inner}' + (f'<p style="margin:18px 4px 0;font-size:14px;line-height:1.5;color:#6e6e73">{b["note"]}</p>' if b.get("note") else "") + '</section>')
    if t == "prices":
        cards = "".join(f'<div class="ap-card ap-rv">{ib(x["icon"], x.get("gold",False))}<br><span class="ap-tag{" gold" if x.get("gold") else ""}">{x["tag"]}</span><div class="ap-price">{x["price"]}<small>{x.get("unit","/ sq ft")}</small></div><h3 class="ap-h3">{x["title"]}</h3><p style="margin-top:8px!important">{x["text"]}</p></div>' for x in b["items"])
        return emb(f'<section class="ap ap-panel"><div class="ap-grid c{len(b["items"])}">{cards}</div>' + (f'<p style="margin:18px 4px 0;font-size:14px;line-height:1.5;color:#6e6e73">{b["note"]}</p>' if b.get("note") else "") + '</section>')
    if t == "table":
        head = "".join(f"<th>{h}</th>" for h in b["head"]); rows = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in b["rows"])
        return emb(f'<section class="ap ap-card" style="padding:22px 10px 10px;overflow-x:auto"><table class="ap-table"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>' + (f'<p style="margin:10px 12px 8px;color:#6e6e73;font-size:14px">{b["note"]}</p>' if b.get("note") else "") + '</section>')
    if t == "steps":
        li = "".join(f'<li><span class="d">{ic(s["icon"])}{s["d"]}</span><span class="t">{s["text"]}' + (f'<em>{s["note"]}</em>' if s.get("note") else "") + '</span></li>' for s in b["items"])
        return emb(f'<section class="ap ap-panel"><ol class="ap-steps{" wide" if b.get("wide") else ""}">{li}</ol></section>')
    if t == "list":
        if b.get("icons"):
            li = "".join(f'<li><span class="ap-li-ic">{ic(x["icon"])}</span>{x["html"]}</li>' for x in b["items"]); cls="ap-list noicon"
        else:
            li = "".join(f'<li>{x}</li>' for x in b["items"]); cls="ap-list"
        return emb(f'<section class="ap ap-card"><ul class="{cls}" style="margin:0">{li}</ul></section>')
    if t == "compare":
        def side(s, x):
            ul = "".join(f"<li>{i}</li>" for i in s["items"])
            return f'<div class="ap-card ap-rv">{ib(s["icon"], s.get("gold",False))}<br><span class="ap-tag{" gold" if s.get("gold") else ""}">{s["tag"]}</span><h3 class="ap-h3" style="margin:12px 0 4px">{s["title"]}</h3><ul class="ap-list{" x" if x else ""}">{ul}</ul></div>'
        return emb(f'<section class="ap"><div class="ap-grid c2">{side(b["a"],False)}{side(b["b"],True)}</div></section>')
    if t == "callout":
        return emb(f'<section class="ap"><div class="ap-callout">{ib(b.get("icon","alert"), b.get("gold",True))}<p><strong>{b["title"]}</strong>{b["text"]}</p></div></section>')
    if t == "calc": return render_calc(b["kind"], b.get("note"))
    if t == "estimator": return render_estimator(b)
    if t == "quiz": return render_quiz(b)
    raise ValueError("unknown block " + t)

def render(spec):
    parts = [emb(BASE_CSS)]
    for b in spec["blocks"]: parts.append(block(b, spec))
    parts.append(render_faq(spec["faq"], spec.get("faq_title","Questions we hear every week"), spec.get("faq_sub","From the phone, Google and Reddit.")))
    parts.append(render_schema(spec)); parts.append(render_cta(spec))
    cat = CAT[spec["category"]]; city = spec.get("city")
    links = [f'<a href="{cat[2]}">{cat[1].lower()} service</a>']
    if city and (city, spec["category"]) in CITY_PAGE: links.insert(0, f'<a href="{CITY_PAGE[(city,spec["category"])]}">{cat[1].lower()} in {city}, WA</a>')
    links.append('<a href="/flooring-installation-cost">published price list</a>')
    for r in spec.get("related", []): links.append(f'<a href="/blog-posts/{r[0]}">{r[1]}</a>')
    cities = [c for c in ["Everett","Seattle","Sammamish","Lynnwood","Edmonds","Kirkland","Snohomish"] if c != city]
    parts.append(f'<p><strong>Wills Flooring</strong> serves {city+", " if city else ""}{", ".join(cities)} and the rest of Snohomish and King County from our Lynnwood showroom. See our ' + ", ".join(links[:-1]) + (" and " + links[-1] if len(links)>1 else "") + ".</p>")
    parts.append(ANIM)
    body = "\n\n".join(parts)
    for m in re.finditer(r"<div data-rt-embed-type='true'>", body): pass
    return body

def manifest(spec, body):
    cat = CAT[spec["category"]]
    m = {"name": spec["title"], "slug": spec["slug"], "description-small": spec["meta"], "time-to-read": spec.get("time","9 mins"),
            "category-is-connected": cat[0], "features-switch": False,
            "scheduled-publish-date": spec.get("date"), "description-big": body}
    if spec.get("image"): m["image-main"] = {"url": spec["image"], "alt": spec.get("alt", spec["title"])}
    if spec.get("id"): m["id"] = spec["id"]   # legacy post: update in place
    return m

def check(body, slug):
    starts=[m.start() for m in re.finditer(r"<div data-rt-embed-type='true'>", body)]
    sizes=[len(body[s:(starts[i+1] if i+1<len(starts) else len(body))]) for i,s in enumerate(starts)]
    assert max(sizes) < 10000, f"{slug}: embed too large {max(sizes)}"
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', body, re.S): json.loads(m.group(1))
    return len(starts), max(sizes), len(body)

if __name__ == "__main__":
    OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out"); os.makedirs(OUT, exist_ok=True)
    for f in sys.argv[1:]:
        spec = json.load(open(f)); body = render(spec); n, mx, tot = check(body, spec["slug"])
        open(os.path.join(OUT, spec['slug']+".html"),"w").write(body); json.dump(manifest(spec, body), open(os.path.join(OUT, spec['slug']+".json"),"w"), ensure_ascii=False)
        words = len(strip_tags(re.sub(r'<(style|script)[^>]*>.*?</\1>','',body,flags=re.S)).split())
        print(f"{spec['slug']}: {n} embeds, max {mx}, total {tot}, words ~{words}")
