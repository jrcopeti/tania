---
source: conversation
captured_at: 2026-10-25T21:35:00Z
captured_by: agent
note: "save this"
fetch: text-only
---

Filed under the copper kestrel 7584 reference. The inbox password lives on the host at `/opt/secrets/dock-inbox`, never in the sandbox.

The dashboard listens on loopback only and is reached through an SSH tunnel. sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. The owner asked for this after the last incident.

heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 198.51.100.23. sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. The disk is 96 GB and sits at about a third full, mostly Docker images. Worth revisiting in a month.

The disk is 96 GB and sits at about a third full, mostly Docker images. The dashboard listens on loopback only and is reached through an SSH tunnel. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. The owner asked for this after the last incident.
