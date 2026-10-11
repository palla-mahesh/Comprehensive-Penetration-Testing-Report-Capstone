#!/usr/bin/env python3
"""Validate finding records before report generation."""
import argparse, json, sys
from pathlib import Path

REQUIRED = {"id", "title", "asset", "severity", "cvss_score", "status", "remediation"}
SEVERITIES = {"Critical", "High", "Medium", "Low", "Informational"}
STATUSES = {"Open", "In Progress", "Fixed", "Accepted Risk", "Closed"}

def validate(data):
    errors = []
    if not isinstance(data, list):
        return ["Root JSON value must be a list of findings."]
    seen = set()
    for i, item in enumerate(data, start=1):
        if not isinstance(item, dict):
            errors.append(f"Item {i}: finding must be an object.")
            continue
        missing = REQUIRED - item.keys()
        if missing:
            errors.append(f"Item {i}: missing fields: {', '.join(sorted(missing))}.")
        fid = item.get("id")
        if fid in seen:
            errors.append(f"Item {i}: duplicate finding ID {fid!r}.")
        seen.add(fid)
        if item.get("severity") not in SEVERITIES:
            errors.append(f"Item {i}: invalid severity {item.get('severity')!r}.")
        if item.get("status") not in STATUSES:
            errors.append(f"Item {i}: invalid status {item.get('status')!r}.")
        score = item.get("cvss_score")
        if not isinstance(score, (int, float)) or not 0 <= score <= 10:
            errors.append(f"Item {i}: cvss_score must be numeric from 0 to 10.")
        if not isinstance(item.get("remediation"), list):
            errors.append(f"Item {i}: remediation must be a list.")
    return errors

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="JSON file containing a list of findings")
    args = parser.parse_args()
    try:
        data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"ERROR: cannot read valid JSON: {exc}", file=sys.stderr)
        return 2
    errors = validate(data)
    if errors:
        print("Validation failed:")
        for error in errors: print(f" - {error}")
        return 1
    print(f"Validation passed: {len(data)} finding(s).")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
