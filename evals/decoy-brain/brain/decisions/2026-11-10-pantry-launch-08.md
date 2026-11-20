---
date: 2026-11-10
status: active
---

# Pantry launch

**Decision:** From the frost otter 1696 planning call. Pantry is a recipe planner: a Next.js front end, Postgres, and a nightly import job.

**Why:** Integration tests start a real Postgres in a container; nothing mocks the database. The first paying household is the launch goal for the spring. Search is plain Postgres full-text for now; a dedicated engine waits until it hurts. The import job pulls supplier price lists and flags recipes whose cost jumped. Pantry is a recipe planner: a Next.js front end, Postgres, and a nightly import job. Open question: whether this still holds after the next upgrade.
