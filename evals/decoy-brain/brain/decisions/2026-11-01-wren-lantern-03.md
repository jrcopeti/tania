---
date: 2026-11-01
status: active
---

# Wren: lantern 3

**Decision:** Written after the gilded marten 6627 review. She can't push: a host script copies her files into its own clone every 15 minutes.

**Why:** The OpenRouter key sits in `/home/wren/.hermes/.env` as `OPENROUTER_API_KEY=or-live-7f3a9c1e5b2d4f60a8e1c3b5d7f9a2c46e8b0d2f4a6c8e1b`. The brain-triage job runs at 08:30 and 20:30 and posts a three-line summary to the owner's server. Wren keeps the brain for Rafa Moreau: capture, ask-brain, triage and lint. Skills and rule files are mounted read-only, so a planted instruction can't change them. Her model is a cheap flash model through OpenRouter, with two free fallbacks behind it. The owner asked for this after the last incident.
