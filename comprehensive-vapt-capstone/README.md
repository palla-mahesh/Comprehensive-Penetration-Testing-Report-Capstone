# Comprehensive Penetration Testing Report & Capstone

**A professional VAPT capstone toolkit** for authorized security assessments, executive reporting, risk prioritization, evidence management, and remediation tracking.

> **Safety / scope:** Use only on systems you own or have written permission to assess. The included lab is deliberately local and the sample findings are illustrative, not claims about a real target. Do not scan public IPs or third-party systems without explicit authorization.

## Features
- Executive-ready VAPT report template and a sample 16-section PDF report.
- CVSS v3.1 vector/score reference and risk matrix.
- OWASP Top 10 (2021) category mapping.
- Finding register in CSV and JSON with remediation owners, SLAs, and retest status.
- Evidence register with SHA-256 integrity hashes.
- Local-only scope/configuration guardrails for the helper scripts.
- Remediation playbooks for developers and system administrators.
- JSON-to-Markdown report generator and input validation tests.
- GitHub-ready layout with contribution, disclosure, and assessment rules.

## Repository map
```text
comprehensive-vapt-capstone/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── report/
│   ├── Comprehensive_VAPT_Capstone_Report.pdf
│   └── report_outline.md
├── findings/
│   ├── findings.json
│   └── findings.csv
├── evidence/
│   ├── evidence_register.csv
│   └── screenshots/README.md
├── scripts/
│   ├── generate_report.py
│   ├── evidence_hash.py
│   └── validate_findings.py
├── lab/
│   ├── scope.example.json
│   └── local_lab_guide.md
├── templates/
│   ├── finding_template.md
│   ├── remediation_plan.csv
│   └── risk_matrix.md
├── docs/
│   ├── cvss_owasp_mapping.md
│   ├── methodology.md
│   ├── remediation_playbooks.md
│   └── authorization_and_rules_of_engagement.md
├── tests/
│   └── test_validate_findings.py
└── reports_generated/
```

## Quick start (Kali Linux)
```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip unzip
unzip comprehensive-vapt-capstone.zip
cd comprehensive-vapt-capstone
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/validate_findings.py findings/findings.json
python scripts/generate_report.py findings/findings.json --output reports_generated/vapt-summary.md
python scripts/evidence_hash.py evidence/
python -m unittest discover -s tests -v
```

Generated output appears in `reports_generated/`. The prebuilt PDF is in `report/`.

## Suggested workflow
1. Define written authorization, target scope, test window, exclusions, and emergency contacts.
2. Create a clean evidence folder and record timestamps/time zone.
3. Perform passive review and authorized testing in the agreed scope.
4. Record each finding with reproducible evidence, impact, CVSS vector, OWASP mapping, and fix.
5. Validate finding data and generate a report.
6. Review risk with the system owner; agree remediation dates.
7. Retest fixes, update statuses, and issue a final sanitized report.
8. Commit only sanitized evidence to GitHub. Never commit credentials, tokens, customer data, or exploitable private details.

## Important scoring note
Scores in the example dataset are illustrative. For real assessments, calculate CVSS v3.1 from the actual vector and validate the score using FIRST's official calculator. Severity thresholds used here: Critical 9.0–10.0, High 7.0–8.9, Medium 4.0–6.9, Low 0.1–3.9, Informational 0.0. Business risk may differ from CVSS severity.

## Legal / ethical
This repository is an educational capstone and reporting aid, not a substitute for professional judgement, an approved methodology, or written authorization. Follow applicable law, organizational policy, and rules of engagement.
