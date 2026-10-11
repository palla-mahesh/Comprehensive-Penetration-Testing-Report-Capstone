# Vulnerability Assessment & Penetration Testing Summary

> Generated 2026-10-10 16:58 UTC. Sample data is illustrative; replace it with authorized assessment findings.

## Executive snapshot

| Metric | Count |
|---|---:|
| Total findings | 3 |
| Critical | 0 |
| High | 1 |
| Medium | 1 |
| Low | 1 |
| Informational | 0 |

## Findings register

| ID | Finding | Severity | CVSS | OWASP | Status | Owner |
|---|---|---|---:|---|---|---|
| VAPT-001 | Missing security headers | Medium | 5.3 | A05:2021 – Security Misconfiguration | Open | Application Team |
| VAPT-002 | Insufficient login throttling | High | 7.1 | A07:2021 – Identification and Authentication Failures | Open | Identity Team |
| VAPT-003 | Verbose error responses | Low | 3.1 | A05:2021 – Security Misconfiguration | Open | Backend Team |

## VAPT-001 — Missing security headers

- **Asset:** https://app.example.test (placeholder)
- **Severity:** Medium (CVSS 3.1: 5.3)
- **Vector:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N`
- **OWASP:** A05:2021 – Security Misconfiguration
- **Status / owner / target:** Open / Application Team / T+14 days

### Description

The illustrative response profile does not consistently define browser security headers.

### Evidence

Example-only observation; replace with sanitized response headers collected during an authorized test.

### Impact

Weak browser-side controls can increase exposure to content injection and clickjacking when combined with other weaknesses.

### Recommended remediation

1. Set a suitable Content-Security-Policy based on application requirements.
2. Set X-Content-Type-Options: nosniff.
3. Set an appropriate frame-ancestors directive or X-Frame-Options where needed.
4. Set Referrer-Policy and review permissions policy.
5. Test changes in staging and monitor for compatibility.

### References

- OWASP Secure Headers Project
- OWASP Top 10 2021 A05

## VAPT-002 — Insufficient login throttling

- **Asset:** https://app.example.test/login (placeholder)
- **Severity:** High (CVSS 3.1: 7.1)
- **Vector:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N`
- **OWASP:** A07:2021 – Identification and Authentication Failures
- **Status / owner / target:** Open / Identity Team / T+7 days

### Description

The illustrative design lacks clear evidence of effective rate limiting and abuse detection for repeated failed authentication attempts.

### Evidence

Example-only design review item; validate in a controlled test account and approved window. Do not conduct password spraying.

### Impact

Could facilitate account compromise attempts and increase support burden if compensating controls are absent.

### Recommended remediation

1. Apply per-account and per-source adaptive throttling with safe thresholds.
2. Use MFA for privileged and risk-sensitive actions.
3. Return generic authentication errors to reduce account enumeration.
4. Alert on unusual failure patterns and test lockout recovery to prevent denial of service.
5. Document rate limits and verify them with a small, authorized test.

### References

- OWASP Authentication Cheat Sheet
- OWASP Top 10 2021 A07

## VAPT-003 — Verbose error responses

- **Asset:** https://app.example.test/api (placeholder)
- **Severity:** Low (CVSS 3.1: 3.1)
- **Vector:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N`
- **OWASP:** A05:2021 – Security Misconfiguration
- **Status / owner / target:** Open / Backend Team / T+30 days

### Description

The illustrative API error response may expose implementation details beyond what clients need.

### Evidence

Example-only response sample; replace with sanitized evidence from the authorized environment.

### Impact

Stack traces or internal identifiers can help an attacker prioritize follow-on attempts, though the impact depends on the information exposed.

### Recommended remediation

1. Return stable, generic client-facing error messages.
2. Log diagnostic detail only on the server with access controls.
3. Use correlation IDs to connect client errors with internal logs.
4. Add tests ensuring production responses omit stack traces and secrets.

### References

- OWASP Error Handling Cheat Sheet
- OWASP Top 10 2021 A05

## Important note

This output is a reporting aid, not proof that a live system was tested. Validate CVSS vectors, scope, evidence, and business risk before sharing.
