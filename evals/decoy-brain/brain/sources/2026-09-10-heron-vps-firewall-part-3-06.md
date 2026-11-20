---
source: conversation
captured_at: 2026-09-10T14:41:00Z
captured_by: agent
note: "save this"
fetch: text-only
---

Notes from the tidal meadow 5074 session. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users.

The dashboard listens on loopback only and is reached through an SSH tunnel. Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. Open question: whether this still holds after the next upgrade.

sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. Unattended upgrades are on; a reboot window runs Sundays at 04:00. Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. The owner asked for this after the last incident.

heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 100.101.47.12. The disk is 96 GB and sits at about a third full, mostly Docker images. Written down so the next agent doesn't redo it.

The dashboard listens on loopback only and is reached through an SSH tunnel. Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. The disk is 96 GB and sits at about a third full, mostly Docker images. Open question: whether this still holds after the next upgrade.

Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. Unattended upgrades are on; a reboot window runs Sundays at 04:00. Open question: whether this still holds after the next upgrade.
