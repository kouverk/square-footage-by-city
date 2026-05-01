import csv

SRC = "2025_Gaz_place_national.txt"
CSV_OUT = "us_places_area.csv"
MD_OUT = "us_places_area.md"

SQMI_TO_SQFT = 27_878_400

rows = []
with open(SRC, encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter="|")
    for r in reader:
        name = r["NAME"].strip()
        state = r["USPS"].strip()
        land_sqmi = float(r["ALAND_SQMI"])
        water_sqmi = float(r["AWATER_SQMI"])
        land_sqft = land_sqmi * SQMI_TO_SQFT
        rows.append((state, name, land_sqmi, land_sqft, water_sqmi))

rows.sort(key=lambda x: (x[0], x[1]))

with open(CSV_OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["state", "name", "land_area_sqmi", "land_area_sqft", "water_area_sqmi"])
    for state, name, sqmi, sqft, water in rows:
        w.writerow([state, name, f"{sqmi:.3f}", f"{sqft:.0f}", f"{water:.3f}"])

with open(MD_OUT, "w", encoding="utf-8") as f:
    f.write("# US Census Places — Land Area (2025 Gazetteer)\n\n")
    f.write(f"Source: US Census Bureau 2025 Gazetteer Files (Places). {len(rows):,} places (cities, towns, CDPs).\n\n")
    f.write("| State | Name | Land Area (sq mi) | Land Area (sq ft) | Water Area (sq mi) |\n")
    f.write("|-------|------|------------------:|------------------:|-------------------:|\n")
    for state, name, sqmi, sqft, water in rows:
        f.write(f"| {state} | {name} | {sqmi:,.3f} | {sqft:,.0f} | {water:,.3f} |\n")

print(f"wrote {CSV_OUT} and {MD_OUT} ({len(rows):,} rows)")
