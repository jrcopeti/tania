---
source: conversation
captured_at: 2026-11-16T11:30:00Z
captured_by: agent
note: "make these guidelines"
fetch: text-only
---

Two rules from today's review:

1. Every project tests its database code against a real database started in a container, never a
   mock.
2. In example-app, the seed script runs before every test suite, and new fixtures go in
   `db/seed.ts`, not in the tests.
