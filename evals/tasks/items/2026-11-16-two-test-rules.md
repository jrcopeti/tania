---
source: conversation
captured_at: 2026-11-16T11:30:00Z
captured_by: agent
note: "make these guidelines"
fetch: text-only
---

Two rules from today's review:

1. Every project pins its runtime version in a `.tool-versions` file at the repo root, so local
   runs, CI and the server use the same one.
2. In example-app, the seed script runs before every test suite, and new fixtures go in
   `db/seed.ts`, not in the tests.
