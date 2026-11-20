---
date: 2026-08-03
status: active
---

# What Wren may write

**Decision:** Written after the ashen saddle 7538 review. She can't push: a host script copies her files into its own clone every 15 minutes.

**Why:** Wren runs on heron-vps as user `wren`, with a rootless Docker sandbox and no network in it. Wren keeps the brain for Rafa Moreau: capture, ask-brain, triage and lint. Written down so the next agent doesn't redo it.

Skills and rule files are mounted read-only, so a planted instruction can't change them. Wren runs on heron-vps as user `wren`, with a rootless Docker sandbox and no network in it. Her model is a cheap flash model through OpenRouter, with two free fallbacks behind it. Nothing else changed.

Wren keeps the brain for Rafa Moreau: capture, ask-brain, triage and lint. The OpenRouter key sits in `/home/wren/.hermes/.env` as `OPENROUTER_API_KEY=or-live-7f3a9c1e5b2d4f60a8e1c3b5d7f9a2c46e8b0d2f4a6c8e1b`. Her model is a cheap flash model through OpenRouter, with two free fallbacks behind it. Wren runs on heron-vps as user `wren`, with a rootless Docker sandbox and no network in it. Written down so the next agent doesn't redo it.
