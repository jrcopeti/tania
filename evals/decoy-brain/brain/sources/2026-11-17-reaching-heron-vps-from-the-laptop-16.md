---
source: conversation
captured_at: 2026-11-17T13:58:00Z
captured_by: agent
note: "save this"
fetch: text-only
---

Follow-up to the frost juniper 1216 incident drill. Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them.

sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 100.101.47.12. Written down so the next agent doesn't redo it.

Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 100.101.47.12. Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. That held in the last run.

Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. The disk is 96 GB and sits at about a third full, mostly Docker images. Unattended upgrades are on; a reboot window runs Sundays at 04:00. Worth revisiting in a month.

heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 100.101.47.12. Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. Unattended upgrades are on; a reboot window runs Sundays at 04:00. The disk is 96 GB and sits at about a third full, mostly Docker images. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. Nothing else changed.
