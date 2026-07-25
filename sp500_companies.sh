#!/bin/bash

CSV_URL="https://raw.githubusercontent.com/datasets/s-and-p-500-companies/refs/heads/main/data/constituents.csv"

TEMP_FILE=$(mktemp)

cleanup() {
    rm -f "$TEMP_FILE"
}

trap cleanup EXIT

if ! curl -fsSL "$CSV_URL" -o "$TEMP_FILE"; then
    echo "Error: Failed to download CSV file." >&2
    exit 1
fi

python3 - "$TEMP_FILE" <<'PY'
import csv
import sys

filename = sys.argv[1]

with open(filename, newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    rows = []

    for row in reader:
        company = row.get("Security", "").strip()
        location = row.get("Headquarters Location", "").strip()
        founded = row.get("Founded", "").strip()

        if founded.isdigit():
            rows.append((int(founded), company, location))

    rows.sort(key=lambda item: item[0])

    print(f'{"Company Name":<45} {"Location":<40} {"Founded":<10}')
    print("-" * 100)

    for year, company, location in rows:
        print(f"{company:<45} {location:<40} {year:<10}")
PY
