#!/usr/bin/env python3
"""Build JSON-LD graphs for the 7 carpet city pages missing schema, mirroring
the structure verified on the 23 complete pages (e.g. Woodinville)."""
import json, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
PACKS = os.path.join(BASE, "..", "packs")

CITIES = {
    "everett":      {"name": "Everett",      "pageId": "6a8d35d842c6945e98ead4b4", "path": "/city-of-everett/carpet-installation-in-everett-wa"},
    "newcastle":    {"name": "Newcastle",    "pageId": "6a8d84bd179cdad202f6443b", "path": "/city-of-new-castle/carpet-installation-in-newcastle-wa"},
    "north-bend":   {"name": "North Bend",   "pageId": "6a8d881285ba860c0b54d562", "path": "/city-of-north-bend/carpet-installation-in-north-bend-wa"},
    "arlington":    {"name": "Arlington",    "pageId": "6a8d308fd1ea4a651cc9fd42", "path": "/city-of-arlington/carpet-installation-in-arlington-wa"},
    "bothell":      {"name": "Bothell",      "pageId": "6a8d3065df4382bca025932c", "path": "/hardwood-floor-refinishing/carpet-installation-in-bothell-wa"},
    "cottage-lake": {"name": "Cottage Lake", "pageId": "6a8d332bd1ea4a651ccb7399", "path": "/city-of-cottage-lake/carpet-installation-in-cottage-lake-wa"},
    "duvall":       {"name": "Duvall",       "pageId": "6a8d33391d304528f91b328f", "path": "/city-of-duvall/carpet-installation-in-duvall-wa"},
}

def graph(city, lat, lng, url, faqs):
    return {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": ["HomeAndConstructionBusiness", "FlooringContractor"],
                "@id": "https://www.nwocflooring.com/#business",
                "name": "OC Flooring",
                "description": f"Mobile carpet showroom and carpet installation contractor serving {city}, WA and surrounding communities. Carpet, pad, stair carpet, carpet stretching and removal.",
                "url": "https://www.nwocflooring.com/",
                "telephone": "+1-425-595-1079",
                "priceRange": "$$",
                "currenciesAccepted": "USD",
                "foundingDate": "2013",
                "slogan": "Crafting beautiful spaces, one floor at a time.",
                "address": {"@type": "PostalAddress", "addressLocality": "Bellevue", "addressRegion": "WA", "addressCountry": "US"},
                "geo": {"@type": "GeoCoordinates", "latitude": 47.622305, "longitude": -122.1623651},
                "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.7", "reviewCount": "119", "bestRating": "5"},
                "areaServed": [{"@type": "City", "name": city}],
                "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "opens": "08:00", "closes": "19:00"}],
                "makesOffer": [
                    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": f"Carpet installation, {city} WA"}, "priceSpecification": {"@type": "UnitPriceSpecification", "price": "1.49", "priceCurrency": "USD", "unitText": "square foot"}},
                    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Carpet and pad supplied"}, "priceSpecification": {"@type": "UnitPriceSpecification", "price": "2.49", "priceCurrency": "USD", "unitText": "square foot"}},
                    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Stair carpet installation"}, "priceSpecification": {"@type": "UnitPriceSpecification", "price": "18.00", "priceCurrency": "USD", "unitText": "step"}},
                    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Carpet stretching and re-stretching"}, "priceSpecification": {"@type": "UnitPriceSpecification", "price": "99.00", "priceCurrency": "USD", "unitText": "room"}},
                    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Old carpet removal and haul-away"}, "priceSpecification": {"@type": "UnitPriceSpecification", "price": "0.50", "priceCurrency": "USD", "unitText": "square foot"}},
                ],
            },
            {
                "@type": "Service",
                "@id": url + "#service",
                "serviceType": "Mobile carpet showroom and carpet installation",
                "name": f"Carpet Installation in {city}, WA — Mobile Showroom",
                "provider": {"@id": "https://www.nwocflooring.com/#business"},
                "areaServed": {"@type": "City", "name": city, "containedInPlace": {"@type": "State", "name": "Washington"}},
                "availableChannel": {
                    "@type": "ServiceChannel",
                    "serviceLocation": {"@type": "Place", "name": f"Your home in {city}, WA", "geo": {"@type": "GeoCoordinates", "latitude": lat, "longitude": lng}},
                    "servicePhone": "+1-425-595-1079",
                    "serviceUrl": "https://www.nwocflooring.com/contact",
                },
                "termsOfService": "Free in-home measure and written quote; 1-year workmanship warranty.",
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.nwocflooring.com/"},
                    {"@type": "ListItem", "position": 2, "name": "Services", "item": "https://www.nwocflooring.com/services/our-products"},
                    {"@type": "ListItem", "position": 3, "name": f"Carpet Installation {city}, WA", "item": url},
                ],
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs
                ],
            },
        ],
    }

out = []
for slug, info in CITIES.items():
    faq_file = os.path.join(BASE, f"faqs-{slug}.json")
    if not os.path.exists(faq_file):
        print(f"SKIP {slug}: no faq file yet", file=sys.stderr)
        continue
    faqs = json.load(open(faq_file))
    assert len(faqs) == 10, f"{slug}: expected 10 FAQs, got {len(faqs)}"
    pack = json.load(open(os.path.join(PACKS, f"{slug}.json")))
    url = "https://www.nwocflooring.com" + info["path"]
    g = graph(info["name"], pack["lat"], pack["lng"], url, faqs)
    out.append({"id": info["pageId"], "jsonLdSchema": g})

json.dump({"site_id": "6377e8e6a53936b48ef1cad0", "pages": out}, open(os.path.join(BASE, "payload.json"), "w"), ensure_ascii=False, indent=1)
print(f"built {len(out)} page schemas -> payload.json")
