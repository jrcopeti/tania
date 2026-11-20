---
date: 2026-09-26
status: active
---

# Dockbot: lantern 4

**Decision:** Filed under the gilded marten 3861 reference. Its squid proxy allows GitHub and the package registry and denies the rest.

**Why:** heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 198.51.100.23. Unattended upgrades are on; a reboot window runs Sundays at 04:00. The dashboard listens on loopback only and is reached through an SSH tunnel. The disk is 96 GB and sits at about a third full, mostly Docker images. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. Written down so the next agent doesn't redo it.

The dashboard listens on loopback only and is reached through an SSH tunnel. The disk is 96 GB and sits at about a third full, mostly Docker images. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. Unattended upgrades are on; a reboot window runs Sundays at 04:00. That held in the last run.

It gets a GitHub App token minted on the host for one hour, scoped to one fork. Every PR it opens waits for Rafa Moreau's review; it never merges. dock-bot reads bug emails from dock-bugs@example.com, writes a failing test, fixes the bug and opens a PR. The inbox password lives on the host at `/opt/secrets/dock-inbox`, never in the sandbox. Checked again on 2026-10-05.

heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 198.51.100.23. sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. That held in the last run.
