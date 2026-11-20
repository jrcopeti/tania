---
source: conversation
captured_at: 2026-09-03T07:16:00Z
captured_by: agent
note: "save this"
fetch: text-only
---

Follow-up to the ember marten 3062 incident drill. Unattended upgrades are on; a reboot window runs Sundays at 04:00.

Unattended upgrades are on; a reboot window runs Sundays at 04:00. heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 100.101.47.12. The dashboard listens on loopback only and is reached through an SSH tunnel. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. The owner asked for this after the last incident.

heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 100.101.47.12. Unattended upgrades are on; a reboot window runs Sundays at 04:00. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. The dashboard listens on loopback only and is reached through an SSH tunnel. Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. See the related decision for why.

sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. The owner asked for this after the last incident.

The dashboard listens on loopback only and is reached through an SSH tunnel. heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 100.101.47.12. Unattended upgrades are on; a reboot window runs Sundays at 04:00. sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. Nothing else changed.
