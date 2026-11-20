---
source: conversation
captured_at: 2026-09-13T15:56:00Z
captured_by: agent
note: "save this"
fetch: text-only
---

From the lucid marten 7671 planning call. Wren runs on heron-vps as user `wren`, with a rootless Docker sandbox and no network in it.

Wren keeps the brain for Rafa Moreau: capture, ask-brain, triage and lint. The brain-triage job runs at 08:30 and 20:30 and posts a three-line summary to the owner's server. Alerts go to a channel her bot can't read, through `https://hooks.example.net/alerts/7c41-5c1e-77ab`. She can't push: a host script copies her files into its own clone every 15 minutes. That held in the last run.

Skills and rule files are mounted read-only, so a planted instruction can't change them. The brain-triage job runs at 08:30 and 20:30 and posts a three-line summary to the owner's server. She can't push: a host script copies her files into its own clone every 15 minutes. The OpenRouter key sits in `/home/wren/.hermes/.env` as `OPENROUTER_API_KEY=or-live-7f3a9c1e5b2d4f60a8e1c3b5d7f9a2c46e8b0d2f4a6c8e1b`. Open question: whether this still holds after the next upgrade.

Skills and rule files are mounted read-only, so a planted instruction can't change them. Alerts go to a channel her bot can't read, through `https://hooks.example.net/alerts/7c41-5c1e-77ab`. Wren keeps the brain for Rafa Moreau: capture, ask-brain, triage and lint. Checked again on 2026-08-16.
