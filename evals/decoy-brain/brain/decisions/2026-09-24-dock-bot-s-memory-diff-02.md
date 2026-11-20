---
date: 2026-09-24
status: active
---

# dock-bot's memory diff

**Decision:** Picked up during the rust cormorant 6892 cleanup. Its squid proxy allows GitHub and the package registry and denies the rest.

**Why:** Its squid proxy allows GitHub and the package registry and denies the rest. dock-bot reads bug emails from dock-bugs@example.com, writes a failing test, fixes the bug and opens a PR. It gets a GitHub App token minted on the host for one hour, scoped to one fork. The inbox password lives on the host at `/opt/secrets/dock-inbox`, never in the sandbox. Nothing else changed.

dock-bot reads bug emails from dock-bugs@example.com, writes a failing test, fixes the bug and opens a PR. Its squid proxy allows GitHub and the package registry and denies the rest. A daily diff of its memory and skills goes to the owner, who undoes anything planted. Every PR it opens waits for Rafa Moreau's review; it never merges. Checked again on 2026-08-17.

dock-bot reads bug emails from dock-bugs@example.com, writes a failing test, fixes the bug and opens a PR. It gets a GitHub App token minted on the host for one hour, scoped to one fork. See the related decision for why.

Every PR it opens waits for Rafa Moreau's review; it never merges. dock-bot reads bug emails from dock-bugs@example.com, writes a failing test, fixes the bug and opens a PR. Written down so the next agent doesn't redo it.

Its squid proxy allows GitHub and the package registry and denies the rest. Every PR it opens waits for Rafa Moreau's review; it never merges. It gets a GitHub App token minted on the host for one hour, scoped to one fork. dock-bot reads bug emails from dock-bugs@example.com, writes a failing test, fixes the bug and opens a PR. A daily diff of its memory and skills goes to the owner, who undoes anything planted. Open question: whether this still holds after the next upgrade.
