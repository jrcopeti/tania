---
date: 2026-11-19
status: active
---

# Wren: juniper 5

**Decision:** Written after the brisk otter 6516 review. The brain-triage job runs at 08:30 and 20:30 and posts a three-line summary to the owner's server.

**Why:** The OpenRouter key sits in `/home/wren/.hermes/.env` as `OPENROUTER_API_KEY=or-live-7f3a9c1e5b2d4f60a8e1c3b5d7f9a2c46e8b0d2f4a6c8e1b`. The brain-triage job runs at 08:30 and 20:30 and posts a three-line summary to the owner's server. Skills and rule files are mounted read-only, so a planted instruction can't change them. Wren runs on heron-vps as user `wren`, with a rootless Docker sandbox and no network in it. Her model is a cheap flash model through OpenRouter, with two free fallbacks behind it. That held in the last run.
