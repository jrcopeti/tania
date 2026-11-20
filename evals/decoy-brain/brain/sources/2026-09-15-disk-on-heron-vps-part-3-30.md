---
source: conversation
captured_at: 2026-09-15T14:35:00Z
captured_by: agent
note: "save this"
fetch: text-only
---

Picked up during the quiet cormorant 5140 cleanup. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users.

Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. The dashboard listens on loopback only and is reached through an SSH tunnel. Unattended upgrades are on; a reboot window runs Sundays at 04:00. That held in the last run.

Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 100.101.47.12. Open question: whether this still holds after the next upgrade.
