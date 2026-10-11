# Assessment Methodology

## 1. Planning and scoping
Confirm written authorization, scope, exclusions, testing window, contacts, and evidence rules. Establish a baseline and avoid disruptive techniques.

## 2. Discovery and attack-surface review
Review supplied architecture, asset inventory, DNS records supplied by the owner, application routes, exposed services, and technology stack. Active discovery is allowed only for explicitly scoped assets.

## 3. Vulnerability assessment
Use a combination of configuration review, dependency review, authenticated application testing, and manual verification. Prefer non-destructive checks. Record tool versions, timestamps, and limitations.

## 4. Validation
Reproduce findings with minimal proof. Confirm affected component, prerequisites, realistic impact, and whether compensating controls change exploitability. Do not retain sensitive payloads or data.

## 5. Risk rating
Assign CVSS v3.1 using a documented vector and validate with the official calculator. Add business context such as asset criticality, exposure, data sensitivity, exploit availability, and compensating controls. CVSS is not a replacement for business risk analysis.

## 6. Reporting
For each finding include title, unique ID, severity, asset, description, evidence, impact, CVSS vector/score, OWASP mapping, remediation, references, owner, due date, and retest criteria.

## 7. Remediation and retesting
Agree remediation owners and dates. Retest the specific issue and relevant regressions. Mark a finding closed only when evidence demonstrates the fix; otherwise leave it open or record an accepted risk with approver and expiry date.

## Limitations
This sample report uses illustrative findings and placeholder assets. It does not represent an actual scan, penetration test, or certification of any real system.
