# Data Center Square Footage

## Purpose

This project analyzes city land areas to provide intuitive comparisons for the **proposed "Stratos" / "Wonder Valley" hyperscale AI data center** in Box Elder County, Utah, announced in April 2026 by Shark Tank investor Kevin O'Leary (via O'Leary Digital, in partnership with Utah's Military Installation Development Authority — MIDA).

The campus would span **~40,000 acres of private land** (plus ~1,200 acres of military/state-owned property) and is planned to scale up to **9 GW of on-site generation** — more than double Utah's current statewide electricity use. Phase 1 targets ~3 GW. The project has drawn local opposition; Box Elder County commissioners delayed their vote on the proposal.

To make a 40,000-acre footprint legible, this repo lists US cities of comparable land area so the proposed campus can be compared to familiar places (Washington DC, St. Louis, Pittsburgh, etc.).

## Files

| File | Description |
|------|-------------|
| `2025_Gaz_place_national.txt` | Raw US Census Bureau 2025 Gazetteer file for Places (cities, towns, CDPs) — pipe-delimited source data. |
| `2025_Gaz_119CDs_national.txt` | Raw US Census Bureau 2025 Gazetteer file for 119th Congressional Districts (reference data, not currently used in outputs). |
| `build_outputs.py` | Python script that reads the Places gazetteer and emits the CSV and Markdown outputs below. Converts sq mi → sq ft using 1 sq mi = 27,878,400 sq ft. |
| `us_places_area.csv` | All 32,350 US Census places with state, name, land area (sq mi), land area (sq ft), and water area (sq mi). Machine-readable. |
| `us_places_area.md` | Same data as the CSV in a Markdown table, sorted by land area descending. Human-readable. |
| `cities_near_40k_acres.md` | Curated list of well-known US cities with land area close to 40,000 acres (62.5 sq mi) — the size of the proposed Box Elder County data center campus. Used to make the footprint relatable. |

## Regenerating the data files

```bash
python3 build_outputs.py
```

This rebuilds `us_places_area.csv` and `us_places_area.md` from the gazetteer source.

## Conversions

- 1 sq mi = 640 acres = 27,878,400 sq ft
- 40,000 acres = 62.5 sq mi ≈ 1.74 billion sq ft
