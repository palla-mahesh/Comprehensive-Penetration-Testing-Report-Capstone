# Prioritized remediation playbooks

## Priority 1 — High risk / authentication
1. Confirm affected login and recovery paths.
2. Implement server-side rate limits with thresholds informed by telemetry.
3. Add MFA to privileged and sensitive actions.
4. Normalize error messages and protect account recovery.
5. Alert on suspicious patterns without logging passwords or tokens.
6. Run automated and manual regression tests; retest with a dedicated account.

## Priority 2 — Security headers
1. Inventory content sources and frame/embed requirements.
2. Deploy Content-Security-Policy in report-only mode where appropriate.
3. Remove unsafe inline/eval dependencies where feasible; use nonces or hashes.
4. Add nosniff, Referrer-Policy, and suitable frame-ancestors policy.
5. Test across supported browsers and monitor breakage.

## Priority 3 — Error handling
1. Disable debug mode in production.
2. Return generic error IDs to clients.
3. Keep stack traces in protected server logs.
4. Scrub secrets and personal data from logs.
5. Add tests to ensure errors don't reveal file paths, queries, environment values, or tokens.

## Change-management checklist
- [ ] Fix reviewed by code owner
- [ ] Unit/integration tests pass
- [ ] Staging verification complete
- [ ] Rollback plan available
- [ ] Production monitoring enabled
- [ ] Evidence captured and sanitized
- [ ] Retest completed and status updated
