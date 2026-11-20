---
source: conversation
captured_at: 2026-08-03T15:58:00Z
captured_by: agent
note: "save this"
fetch: text-only
---

Follow-up to the lucid anvil 9394 incident drill. Unattended upgrades are on; a reboot window runs Sundays at 04:00.

Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. The dashboard listens on loopback only and is reached through an SSH tunnel. Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. The disk is 96 GB and sits at about a third full, mostly Docker images. sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. See the related decision for why.

The dashboard listens on loopback only and is reached through an SSH tunnel. sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. The disk is 96 GB and sits at about a third full, mostly Docker images. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. That held in the last run.

The dashboard listens on loopback only and is reached through an SSH tunnel. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. Written down so the next agent doesn't redo it.

sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. The dashboard listens on loopback only and is reached through an SSH tunnel. Unattended upgrades are on; a reboot window runs Sundays at 04:00. heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 100.101.47.12. That held in the last run.
