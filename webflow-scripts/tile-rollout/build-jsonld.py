#!/usr/bin/env python3
"""Generate the JSON-LD @graph for one tile city page from its pack.

Usage: python3 build-jsonld.py <citySlug>
Prints the compact JSON string to stdout (ready for bulk_update_pages_schema_markup).

Mirrors the Bellevue master graph: business node (office geo, rating, offers),
Service node (city + city geo from the pack), BreadcrumbList (city path),
FAQPage (the pack's 11 rewritten Q&As).
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
BASE = "https://www.nwocflooring.com"


def build(slug: str) -> dict:
    pack = json.load(open(HERE / "packs" / f"{slug}.json"))
    ids = json.load(open(HERE / "tile-pageids.json"))[slug]
    city = pack["cityName"]
    url = BASE + ids["tilePath"]

    business = {
        "@type": ["HomeAndConstructionBusiness", "FlooringContractor"],
        "@id": BASE + "/#business",
        "name": "OC Flooring",
        "description": (
            f"Tile installation contractor serving {city} and the Puget Sound area. "
            "Waterproofed shower and bath tile, porcelain and stone floors, "
            "backsplash, heated floors, tile repair and regrout."
        ),
        "url": BASE + "/",
        "telephone": "+1-425-595-1079",
        "priceRange": "$$",
        "currenciesAccepted": "USD",
        "foundingDate": "2013",
        "slogan": "Crafting beautiful spaces, one floor at a time.",
        "address": {"@type": "PostalAddress", "addressLocality": "Bellevue",
                    "addressRegion": "WA", "addressCountry": "US"},
        "geo": {"@type": "GeoCoordinates", "latitude": 47.622305, "longitude": -122.1623651},
        "hasMap": "https://www.google.com/maps/place/OC+Flooring/@47.6223086,-122.16494,17z",
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.7",
                            "reviewCount": "119", "bestRating": "5"},
        "areaServed": [{"@type": "City", "name": city}] + [
            {"@type": "City", "name": n} for n in
            ["Bellevue", "Kirkland", "Redmond", "Issaquah", "Sammamish", "Mercer Island",
             "Newcastle", "Seattle", "Renton", "Bothell", "Woodinville", "Everett", "Lynnwood"]
            if n != city
        ],
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            "opens": "08:00", "closes": "19:00"}],
        "makesOffer": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": f"Tile floor installation, {city} WA"},
             "priceSpecification": {"@type": "UnitPriceSpecification", "price": "11.00",
                                    "priceCurrency": "USD", "unitText": "square foot",
                                    "valueAddedTaxIncluded": False}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Waterproofed shower tile surround"},
             "priceSpecification": {"@type": "UnitPriceSpecification", "price": "3200.00",
                                    "priceCurrency": "USD", "unitText": "shower"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Kitchen backsplash tile installation"},
             "priceSpecification": {"@type": "UnitPriceSpecification", "price": "1100.00",
                                    "priceCurrency": "USD", "unitText": "backsplash"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Electric heated tile floor"},
             "priceSpecification": {"@type": "UnitPriceSpecification", "price": "11.00",
                                    "priceCurrency": "USD", "unitText": "square foot"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Tile repair and regrout"},
             "priceSpecification": {"@type": "UnitPriceSpecification", "price": "8.00",
                                    "priceCurrency": "USD", "unitText": "square foot"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Old tile demolition and haul-away"},
             "priceSpecification": {"@type": "UnitPriceSpecification", "price": "3.50",
                                    "priceCurrency": "USD", "unitText": "square foot"}},
        ],
    }

    service = {
        "@type": "Service",
        "@id": url + "#service",
        "serviceType": "Tile installation — showers, floors, backsplash and heated floors",
        "name": f"Tile Installation in {city}, WA",
        "provider": {"@id": BASE + "/#business"},
        "areaServed": {"@type": "City", "name": city,
                       "geo": {"@type": "GeoCoordinates",
                               "latitude": pack["lat"], "longitude": pack["lng"]},
                       "containedInPlace": {"@type": "State", "name": "Washington"}},
        "availableChannel": {"@type": "ServiceChannel",
                             "serviceLocation": {"@type": "Place", "name": f"Your home in {city}, WA"},
                             "servicePhone": "+1-425-595-1079",
                             "serviceUrl": BASE + "/contact"},
        "termsOfService": ("Free in-home estimate and written quote; bonded waterproofing "
                           "with a documented 24-hour flood test; 2-year workmanship "
                           "warranty on tile."),
    }

    crumbs = {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Services", "item": BASE + "/services/our-products"},
            {"@type": "ListItem", "position": 3, "name": f"Tile Installation {city}, WA", "item": url},
        ],
    }

    faq = {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": pack["roles"][f"faqQ{i}"],
             "acceptedAnswer": {"@type": "Answer", "text": pack["roles"][f"faqA{i}"]}}
            for i in range(1, 12)
        ],
    }

    return {"@context": "https://schema.org", "@graph": [business, service, crumbs, faq]}


if __name__ == "__main__":
    print(json.dumps(build(sys.argv[1]), separators=(",", ":"), ensure_ascii=False))
