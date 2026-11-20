---
source: conversation
captured_at: 2026-11-12T10:14:00Z
captured_by: agent
note: "remember this rule"
fetch: text-only
---

In example-app, run `pnpm db:seed` before `pnpm test:e2e`: the end-to-end tests expect the three
seed users, and a fresh database fails them all with a login error.
