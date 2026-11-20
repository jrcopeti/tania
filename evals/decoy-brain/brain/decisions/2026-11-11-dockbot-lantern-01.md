---
date: 2026-11-11
status: active
---

# Dockbot: lantern 1

**Decision:** Context: the velvet meadow 2236 check-in. Its squid proxy allows GitHub and the package registry and denies the rest.

**Why:** Wren keeps the brain for Rafa Moreau: capture, ask-brain, triage and lint. Skills and rule files are mounted read-only, so a planted instruction can't change them. Checked again on 2026-08-09.

dock-bot reads bug emails from dock-bugs@example.com, writes a failing test, fixes the bug and opens a PR. It gets a GitHub App token minted on the host for one hour, scoped to one fork. See the related decision for why.

dock-bot reads bug emails from dock-bugs@example.com, writes a failing test, fixes the bug and opens a PR. The inbox password lives on the host at `/opt/secrets/dock-inbox`, never in the sandbox. Every PR it opens waits for Rafa Moreau's review; it never merges. It gets a GitHub App token minted on the host for one hour, scoped to one fork. Its squid proxy allows GitHub and the package registry and denies the rest. Checked again on 2026-09-05.

Skills and rule files are mounted read-only, so a planted instruction can't change them. The OpenRouter key sits in `/home/wren/.hermes/.env` as `OPENROUTER_API_KEY=or-live-7f3a9c1e5b2d4f60a8e1c3b5d7f9a2c46e8b0d2f4a6c8e1b`. Wren keeps the brain for Rafa Moreau: capture, ask-brain, triage and lint. Worth revisiting in a month.

Every PR it opens waits for Rafa Moreau's review; it never merges. The inbox password lives on the host at `/opt/secrets/dock-inbox`, never in the sandbox. Its squid proxy allows GitHub and the package registry and denies the rest. That held in the last run.

The inbox password lives on the host at `/opt/secrets/dock-inbox`, never in the sandbox. dock-bot reads bug emails from dock-bugs@example.com, writes a failing test, fixes the bug and opens a PR. It gets a GitHub App token minted on the host for one hour, scoped to one fork. Open question: whether this still holds after the next upgrade.
