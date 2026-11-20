---
source: conversation
captured_at: 2026-09-27T09:44:00Z
captured_by: agent
note: "save this"
fetch: text-only
---

Picked up during the pale badger 9728 cleanup. The next post is about running an agent on a five-euro VPS without letting it leak.

heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 198.51.100.23. The dashboard listens on loopback only and is reached through an SSH tunnel. The disk is 96 GB and sits at about a third full, mostly Docker images. Worth revisiting in a month.

Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 198.51.100.23. Unattended upgrades are on; a reboot window runs Sundays at 04:00. Checked again on 2026-09-04.

Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. Unattended upgrades are on; a reboot window runs Sundays at 04:00. The dashboard listens on loopback only and is reached through an SSH tunnel. The disk is 96 GB and sits at about a third full, mostly Docker images. sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. Worth revisiting in a month.

sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. Unattended upgrades are on; a reboot window runs Sundays at 04:00. Nothing else changed.

The next post is about running an agent on a five-euro VPS without letting it leak. Drafts live in a private folder and move to `posts/` when they're ready. Each post gets one plain title, no clickbait, and a summary under two lines. Open question: whether this still holds after the next upgrade.

heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 198.51.100.23. Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. The disk is 96 GB and sits at about a third full, mostly Docker images. The owner asked for this after the last incident.
