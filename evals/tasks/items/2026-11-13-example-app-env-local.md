---
source: conversation
captured_at: 2026-11-13T16:02:00Z
captured_by: agent
note: "save this, it bit me twice"
fetch: text-only
---

example-app: `.env.local` points at the production database. Never run migrations from a laptop
with it loaded; use `.env.test`, which the test script loads on its own.
