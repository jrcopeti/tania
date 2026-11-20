---
source: conversation
captured_at: 2026-09-02T09:26:00Z
captured_by: agent
note: "save this"
fetch: text-only
---

Picked up during the slate saddle 1293 cleanup. The import job pulls supplier price lists and flags recipes whose cost jumped.

The inbox password lives on the host at `/opt/secrets/dock-inbox`, never in the sandbox. A daily diff of its memory and skills goes to the owner, who undoes anything planted. Written down so the next agent doesn't redo it.

The first paying household is the launch goal for the spring. Pantry is a recipe planner: a Next.js front end, Postgres, and a nightly import job. Search is plain Postgres full-text for now; a dedicated engine waits until it hurts. It runs on a small managed host with preview deploys for every branch. The import job pulls supplier price lists and flags recipes whose cost jumped. The owner asked for this after the last incident.

It gets a GitHub App token minted on the host for one hour, scoped to one fork. dock-bot reads bug emails from dock-bugs@example.com, writes a failing test, fixes the bug and opens a PR. The inbox password lives on the host at `/opt/secrets/dock-inbox`, never in the sandbox. Every PR it opens waits for Rafa Moreau's review; it never merges. See the related decision for why.

It runs on a small managed host with preview deploys for every branch. Search is plain Postgres full-text for now; a dedicated engine waits until it hurts. Integration tests start a real Postgres in a container; nothing mocks the database. Pantry is a recipe planner: a Next.js front end, Postgres, and a nightly import job. Nothing else changed.

It gets a GitHub App token minted on the host for one hour, scoped to one fork. Every PR it opens waits for Rafa Moreau's review; it never merges. The inbox password lives on the host at `/opt/secrets/dock-inbox`, never in the sandbox. A daily diff of its memory and skills goes to the owner, who undoes anything planted. Its squid proxy allows GitHub and the package registry and denies the rest. The owner asked for this after the last incident.

It runs on a small managed host with preview deploys for every branch. The import job pulls supplier price lists and flags recipes whose cost jumped. The first paying household is the launch goal for the spring. Pantry is a recipe planner: a Next.js front end, Postgres, and a nightly import job. Written down so the next agent doesn't redo it.

dock-bot reads bug emails from dock-bugs@example.com, writes a failing test, fixes the bug and opens a PR. A daily diff of its memory and skills goes to the owner, who undoes anything planted. It gets a GitHub App token minted on the host for one hour, scoped to one fork. Written down so the next agent doesn't redo it.

dock-bot reads bug emails from dock-bugs@example.com, writes a failing test, fixes the bug and opens a PR. Every PR it opens waits for Rafa Moreau's review; it never merges. It gets a GitHub App token minted on the host for one hour, scoped to one fork. Its squid proxy allows GitHub and the package registry and denies the rest. The owner asked for this after the last incident.
