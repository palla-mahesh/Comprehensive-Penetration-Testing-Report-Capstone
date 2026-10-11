#!/usr/bin/env python3
"""Generate a Markdown VAPT summary from the project's JSON finding schema."""
import argparse, json
from pathlib import Path
from datetime import datetime, timezone

def esc(value):
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Findings JSON file")
    parser.add_argument("--output", required=True, help="Output Markdown path")
    args = parser.parse_args()
    findings = json.loads(Path(args.input).read_text(encoding="utf-8"))
    counts = {s: sum(1 for f in findings if f.get("severity") == s) for s in ["Critical","High","Medium","Low","Informational"]}
    lines = [
        "# Vulnerability Assessment & Penetration Testing Summary",
        "",
        f"> Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}. Sample data is illustrative; replace it with authorized assessment findings.",
        "",
        "## Executive snapshot",
        "",
        "| Metric | Count |",
        "|---|---:|",
        f"| Total findings | {len(findings)} |",
    ]
    lines.extend(f"| {s} | {n} |" for s,n in counts.items())
    lines += ["", "## Findings register", "", "| ID | Finding | Severity | CVSS | OWASP | Status | Owner |", "|---|---|---|---:|---|---|---|"]
    for f in findings:
        lines.append("| " + " | ".join(esc(f.get(k, "")) for k in ["id","title","severity","cvss_score","owasp","status","owner"]) + " |")
    for f in findings:
        lines += ["", f"## {esc(f.get('id'))} — {esc(f.get('title'))}", "",
                  f"- **Asset:** {esc(f.get('asset'))}",
                  f"- **Severity:** {esc(f.get('severity'))} (CVSS {esc(f.get('cvss_version','3.1'))}: {esc(f.get('cvss_score'))})",
                  f"- **Vector:** `{esc(f.get('cvss_vector','Not provided'))}`",
                  f"- **OWASP:** {esc(f.get('owasp','Not mapped'))}",
                  f"- **Status / owner / target:** {esc(f.get('status'))} / {esc(f.get('owner','Unassigned'))} / {esc(f.get('target_date','TBD'))}",
                  "", "### Description", "", esc(f.get("summary","")),
                  "", "### Evidence", "", esc(f.get("evidence","Replace with sanitized evidence.")),
                  "", "### Impact", "", esc(f.get("impact","")),
                  "", "### Recommended remediation", ""]
        lines.extend(f"{i}. {esc(step)}" for i,step in enumerate(f.get("remediation",[]),1))
        if f.get("references"):
            lines += ["", "### References", ""] + [f"- {esc(r)}" for r in f["references"]]
    lines += ["", "## Important note", "", "This output is a reporting aid, not proof that a live system was tested. Validate CVSS vectors, scope, evidence, and business risk before sharing."]
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
if __name__ == "__main__":
    main()
