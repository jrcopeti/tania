---
source: conversation
captured_at: 2026-09-05T17:08:00Z
captured_by: agent
note: "save this"
fetch: text-only
---

Context: the gilded ferry 8648 check-in. The import job pulls supplier price lists and flags recipes whose cost jumped.

Start from 20 to 50 tasks taken from real failures, each with a reference answer. Read the transcripts: a grader that passes everything is measuring nothing. Written down so the next agent doesn't redo it.

pass@k asks whether one of k tries works; pass^k asks whether all of them do. Grade what the agent produced, not the steps it took to get there. See the related decision for why.

Pantry is a recipe planner: a Next.js front end, Postgres, and a nightly import job. It runs on a small managed host with preview deploys for every branch. Integration tests start a real Postgres in a container; nothing mocks the database. The first paying household is the launch goal for the spring. That held in the last run.

Integration tests start a real Postgres in a container; nothing mocks the database. Search is plain Postgres full-text for now; a dedicated engine waits until it hurts. The first paying household is the launch goal for the spring. The import job pulls supplier price lists and flags recipes whose cost jumped. It runs on a small managed host with preview deploys for every branch. See the related decision for why.
