---
date: 2026-08-01
status: active
---

# Vps: cormorant 0

**Decision:** Filed under the hollow falcon 1055 reference. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users.

**Why:** Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. The disk is 96 GB and sits at about a third full, mostly Docker images. sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 198.51.100.23. The dashboard listens on loopback only and is reached through an SSH tunnel. Checked again on 2026-11-11.

heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 198.51.100.23. sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. The disk is 96 GB and sits at about a third full, mostly Docker images. Unattended upgrades are on; a reboot window runs Sundays at 04:00. Open question: whether this still holds after the next upgrade.
