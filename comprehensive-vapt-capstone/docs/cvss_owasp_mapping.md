# CVSS v3.1 and OWASP mapping guide

## CVSS v3.1 severity bands
| Score | Rating |
|---:|---|
| 9.0–10.0 | Critical |
| 7.0–8.9 | High |
| 4.0–6.9 | Medium |
| 0.1–3.9 | Low |
| 0.0 | None |

Use FIRST's official CVSS v3.1 calculator to verify the score against the full vector. Never choose a score solely to match a desired severity label. Consider the correct Attack Vector, Attack Complexity, Privileges Required, User Interaction, Scope, and CIA impact metrics.

## OWASP Top 10:2021 mapping (examples)
| Finding type | Potential category | Mapping caveat |
|---|---|---|
| Missing security headers / unsafe defaults | A05 Security Misconfiguration | Map based on root cause, not just symptom |
| Weak authentication controls | A07 Identification and Authentication Failures | Validate design, threat model, and compensating controls |
| Excessive data exposure | A01 Broken Access Control or A02 Cryptographic Failures | Depends on why data is exposed |
| Injection flaw | A03 Injection | Verify the specific injection class and safe proof |
| Vulnerable dependency | A06 Vulnerable and Outdated Components | Confirm affected version and reachable impact |

OWASP categories are classification aids, not severity scores. One issue may map to more than one category; document the primary root cause.
