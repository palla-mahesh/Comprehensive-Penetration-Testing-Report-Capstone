# Authorization and Rules of Engagement

Before testing, obtain written authorization from the asset owner. Record:

- Business purpose and named approver
- Exact hostnames, IPs, applications, APIs, environments, and accounts in scope
- Explicit exclusions and prohibited techniques
- Testing dates, time zone, rate limits, and source IPs
- Allowed authentication methods and test data
- Data-handling, retention, encryption, and deletion rules
- Emergency contacts, stop conditions, and escalation path
- Deliverables, report classification, and disclosure rules
- Retest expectations and acceptance criteria

**Stop conditions:** service degradation, unexpected access to sensitive data, accidental production impact, scope ambiguity, or a request from the system owner. Pause testing and notify the designated contact.

A scope file is a planning aid, not proof of authorization. Do not test a target simply because it is reachable.
