# Local lab and safe practice guide

## Goal
Practice report-writing and evidence handling without probing third-party systems. This project does not automatically scan targets.

## Option A — use the sample dataset
This is the safest starting point:
```bash
python scripts/validate_findings.py findings/findings.json
python scripts/generate_report.py findings/findings.json --output reports_generated/vapt-summary.md
```

## Option B — intentionally vulnerable local web app
If you want hands-on testing, run an intentionally vulnerable app only in an isolated local VM/container and follow that app's official lab instructions. Bind it to loopback (`127.0.0.1`) rather than a public interface, do not expose it through port forwarding, and take a VM snapshot first. Use a dedicated lab browser and dummy data.

Example: OWASP Juice Shop can be run locally with Docker if Docker is installed:
```bash
docker run --rm -p 127.0.0.1:3000:3000 bkimminich/juice-shop
```
Then browse to `http://127.0.0.1:3000`. This image is third-party software; review its official documentation and Docker security guidance before use. Stop it with `Ctrl+C`. Never use the example against a public deployment.

## Scope discipline
- Confirm written permission and target list before every assessment.
- Do not test denial-of-service, destructive actions, real-user accounts, or data exfiltration unless explicitly and safely approved.
- Use low request rates, test accounts, and an agreed time window.
- Stop immediately if the owner reports instability or unexpected impact.
- Keep raw evidence private; share only sanitized artifacts.
