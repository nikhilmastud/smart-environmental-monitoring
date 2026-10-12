"""Validate a CSV file containing temperature and humidity sensor readings."""
import csv
import sys
from pathlib import Path

REQUIRED_COLUMNS = {"elapsed_ms", "temperature_c", "humidity_pct"}


def validate_csv(path: Path):
    issues = []
    records = 0
    with path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames or not REQUIRED_COLUMNS.issubset(reader.fieldnames):
            return 0, [f"Missing required columns. Expected: {sorted(REQUIRED_COLUMNS)}"]
        for line_number, row in enumerate(reader, start=2):
            if not any((value or "").strip() for value in row.values()):
                issues.append(f"Line {line_number}: blank record")
                continue
            records += 1
            try:
                elapsed = float(row["elapsed_ms"])
                temperature = float(row["temperature_c"])
                humidity = float(row["humidity_pct"])
            except (TypeError, ValueError):
                issues.append(f"Line {line_number}: non-numeric or missing value")
                continue
            if elapsed < 0:
                issues.append(f"Line {line_number}: elapsed_ms must be >= 0")
            if not -40 <= temperature <= 80:
                issues.append(f"Line {line_number}: temperature outside -40 to 80 C")
            if not 0 <= humidity <= 100:
                issues.append(f"Line {line_number}: humidity outside 0 to 100%")
    return records, issues


def main():
    if len(sys.argv) != 2:
        print("Usage: python python/validate_sensor_data.py <csv-file>")
        return 2
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"ERROR: file not found: {path}")
        return 2
    records, issues = validate_csv(path)
    print(f"Records checked: {records}")
    if issues:
        print(f"Validation: FAIL ({len(issues)} issue(s))")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("Validation: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
