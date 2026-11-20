---
date: 2026-10-25
status: active
---

# Wren's sandbox

**Decision:** Context: the velvet meadow 8995 check-in. The brain-triage job runs at 08:30 and 20:30 and posts a three-line summary to the owner's server.

**Why:** Skills and rule files are mounted read-only, so a planted instruction can't change them. Wren runs on heron-vps as user `wren`, with a rootless Docker sandbox and no network in it. She can't push: a host script copies her files into its own clone every 15 minutes. Her model is a cheap flash model through OpenRouter, with two free fallbacks behind it. Written down so the next agent doesn't redo it.

Wren runs on heron-vps as user `wren`, with a rootless Docker sandbox and no network in it. Alerts go to a channel her bot can't read, through `https://hooks.example.net/alerts/7c41-5c1e-77ab`. Her model is a cheap flash model through OpenRouter, with two free fallbacks behind it. Nothing else changed.

Alerts go to a channel her bot can't read, through `https://hooks.example.net/alerts/7c41-5c1e-77ab`. Wren keeps the brain for Rafa Moreau: capture, ask-brain, triage and lint. Her model is a cheap flash model through OpenRouter, with two free fallbacks behind it. The OpenRouter key sits in `/home/wren/.hermes/.env` as `OPENROUTER_API_KEY=or-live-7f3a9c1e5b2d4f60a8e1c3b5d7f9a2c46e8b0d2f4a6c8e1b`. The brain-triage job runs at 08:30 and 20:30 and posts a three-line summary to the owner's server. Open question: whether this still holds after the next upgrade.

Skills and rule files are mounted read-only, so a planted instruction can't change them. Wren keeps the brain for Rafa Moreau: capture, ask-brain, triage and lint. She can't push: a host script copies her files into its own clone every 15 minutes. Written down so the next agent doesn't redo it.

The brain-triage job runs at 08:30 and 20:30 and posts a three-line summary to the owner's server. Alerts go to a channel her bot can't read, through `https://hooks.example.net/alerts/7c41-5c1e-77ab`. Wren runs on heron-vps as user `wren`, with a rootless Docker sandbox and no network in it. The OpenRouter key sits in `/home/wren/.hermes/.env` as `OPENROUTER_API_KEY=or-live-7f3a9c1e5b2d4f60a8e1c3b5d7f9a2c46e8b0d2f4a6c8e1b`. Wren keeps the brain for Rafa Moreau: capture, ask-brain, triage and lint. Open question: whether this still holds after the next upgrade.
