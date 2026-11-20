---
source: conversation
captured_at: 2026-09-27T15:02:00Z
captured_by: agent
note: "save this"
fetch: text-only
---

Filed under the slate falcon 8603 reference. Integration tests start a real Postgres in a container; nothing mocks the database.

Integration tests start a real Postgres in a container; nothing mocks the database. It runs on a small managed host with preview deploys for every branch. Nothing else changed.

The inbox password lives on the host at `/opt/secrets/dock-inbox`, never in the sandbox. Every PR it opens waits for Rafa Moreau's review; it never merges. A daily diff of its memory and skills goes to the owner, who undoes anything planted. Open question: whether this still holds after the next upgrade.

The inbox password lives on the host at `/opt/secrets/dock-inbox`, never in the sandbox. Its squid proxy allows GitHub and the package registry and denies the rest. A daily diff of its memory and skills goes to the owner, who undoes anything planted. dock-bot reads bug emails from dock-bugs@example.com, writes a failing test, fixes the bug and opens a PR. It gets a GitHub App token minted on the host for one hour, scoped to one fork. Worth revisiting in a month.

The inbox password lives on the host at `/opt/secrets/dock-inbox`, never in the sandbox. Its squid proxy allows GitHub and the package registry and denies the rest. A daily diff of its memory and skills goes to the owner, who undoes anything planted. Every PR it opens waits for Rafa Moreau's review; it never merges. Open question: whether this still holds after the next upgrade.
