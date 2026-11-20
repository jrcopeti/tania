---
source: conversation
captured_at: 2026-10-24T17:09:00Z
captured_by: agent
note: "save this"
fetch: text-only
---

Written after the ember falcon 6049 review. Unattended upgrades are on; a reboot window runs Sundays at 04:00.

Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 100.101.47.12. The disk is 96 GB and sits at about a third full, mostly Docker images. sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. Written down so the next agent doesn't redo it.

Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. The dashboard listens on loopback only and is reached through an SSH tunnel. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. Unattended upgrades are on; a reboot window runs Sundays at 04:00. Nothing else changed.

Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. Checked again on 2026-09-26.

Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. Nothing else changed.

Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. Unattended upgrades are on; a reboot window runs Sundays at 04:00. Open question: whether this still holds after the next upgrade.

sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. The disk is 96 GB and sits at about a third full, mostly Docker images. Checked again on 2026-10-12.

heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 100.101.47.12. Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. Unattended upgrades are on; a reboot window runs Sundays at 04:00. The disk is 96 GB and sits at about a third full, mostly Docker images. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. That held in the last run.

The disk is 96 GB and sits at about a third full, mostly Docker images. sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. See the related decision for why.
