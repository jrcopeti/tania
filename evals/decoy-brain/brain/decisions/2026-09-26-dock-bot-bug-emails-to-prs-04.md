---
date: 2026-09-26
status: active
---

# dock-bot: bug emails to PRs

**Decision:** Context: the lucid orchard 3861 check-in. A daily diff of its memory and skills goes to the owner, who undoes anything planted.

**Why:** A daily diff of its memory and skills goes to the owner, who undoes anything planted. Every PR it opens waits for Rafa Moreau's review; it never merges. The inbox password lives on the host at `/opt/secrets/dock-inbox`, never in the sandbox. Checked again on 2026-10-13.

dock-bot reads bug emails from dock-bugs@example.com, writes a failing test, fixes the bug and opens a PR. The inbox password lives on the host at `/opt/secrets/dock-inbox`, never in the sandbox. Every PR it opens waits for Rafa Moreau's review; it never merges. It gets a GitHub App token minted on the host for one hour, scoped to one fork. Checked again on 2026-08-17.

Every PR it opens waits for Rafa Moreau's review; it never merges. A daily diff of its memory and skills goes to the owner, who undoes anything planted. dock-bot reads bug emails from dock-bugs@example.com, writes a failing test, fixes the bug and opens a PR. The owner asked for this after the last incident.
