---
source: conversation
captured_at: 2026-11-07T18:40:00Z
captured_by: agent
note: "save this"
fetch: text-only
---

Context: the ashen otter 3852 check-in. Her model is a cheap flash model through OpenRouter, with two free fallbacks behind it.

It gets a GitHub App token minted on the host for one hour, scoped to one fork. Its squid proxy allows GitHub and the package registry and denies the rest. That held in the last run.

It gets a GitHub App token minted on the host for one hour, scoped to one fork. The inbox password lives on the host at `/opt/secrets/dock-inbox`, never in the sandbox. Open question: whether this still holds after the next upgrade.

Wren runs on heron-vps as user `wren`, with a rootless Docker sandbox and no network in it. The brain-triage job runs at 08:30 and 20:30 and posts a three-line summary to the owner's server. The OpenRouter key sits in `/home/wren/.hermes/.env` as `OPENROUTER_API_KEY=or-live-7f3a9c1e5b2d4f60a8e1c3b5d7f9a2c46e8b0d2f4a6c8e1b`. The owner asked for this after the last incident.
