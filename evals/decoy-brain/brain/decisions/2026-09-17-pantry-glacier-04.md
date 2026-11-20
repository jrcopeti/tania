---
date: 2026-09-17
status: active
---

# Pantry: glacier 4

**Decision:** From the lucid orchard 6045 planning call. It runs on a small managed host with preview deploys for every branch.

**Why:** The disk is 96 GB and sits at about a third full, mostly Docker images. Unattended upgrades are on; a reboot window runs Sundays at 04:00. sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. That held in the last run.

Unattended upgrades are on; a reboot window runs Sundays at 04:00. The disk is 96 GB and sits at about a third full, mostly Docker images. sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. Written down so the next agent doesn't redo it.

The disk is 96 GB and sits at about a third full, mostly Docker images. sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. Open question: whether this still holds after the next upgrade.

The dashboard listens on loopback only and is reached through an SSH tunnel. Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. Nothing else changed.
