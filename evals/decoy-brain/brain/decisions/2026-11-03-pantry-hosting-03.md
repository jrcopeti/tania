---
date: 2026-11-03
status: active
---

# Pantry hosting

**Decision:** Written after the gilded marten 2005 review. Search is plain Postgres full-text for now; a dedicated engine waits until it hurts.

**Why:** Integration tests start a real Postgres in a container; nothing mocks the database. The first paying household is the launch goal for the spring. The import job pulls supplier price lists and flags recipes whose cost jumped. That held in the last run.

The first paying household is the launch goal for the spring. It runs on a small managed host with preview deploys for every branch. Pantry is a recipe planner: a Next.js front end, Postgres, and a nightly import job. The owner asked for this after the last incident.
