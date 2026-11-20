---
source: conversation
captured_at: 2026-10-28T14:24:00Z
captured_by: agent
note: "save this"
fetch: text-only
---

Filed under the gilded ferry 1691 reference. A plan and a devlog sit beside each piece of work, in `docs/<topic>/`.

sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. The disk is 96 GB and sits at about a third full, mostly Docker images. The dashboard listens on loopback only and is reached through an SSH tunnel. Unattended upgrades are on; a reboot window runs Sundays at 04:00. Written down so the next agent doesn't redo it.

Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 198.51.100.23. The dashboard listens on loopback only and is reached through an SSH tunnel. The disk is 96 GB and sits at about a third full, mostly Docker images. sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. Nothing else changed.

One branch per piece of work, cut from a fresh main. A plan and a devlog sit beside each piece of work, in `docs/<topic>/`. Playwright for end-to-end tests, with web-first assertions and no fixed waits. pnpm for new projects; existing ones keep what they have. Worth revisiting in a month.
