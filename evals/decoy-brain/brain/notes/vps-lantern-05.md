# Vps: lantern 5

Follow-up to the winter lantern 5805 incident drill. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users.

heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 198.51.100.23. The disk is 96 GB and sits at about a third full, mostly Docker images. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. That held in the last run.

She can't push: a host script copies her files into its own clone every 15 minutes. Wren runs on heron-vps as user `wren`, with a rootless Docker sandbox and no network in it. Her model is a cheap flash model through OpenRouter, with two free fallbacks behind it. Wren keeps the brain for Rafa Moreau: capture, ask-brain, triage and lint. Alerts go to a channel her bot can't read, through `https://hooks.example.net/alerts/decoy-5c1e-77ab`. Written down so the next agent doesn't redo it.

The disk is 96 GB and sits at about a third full, mostly Docker images. heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 198.51.100.23. The dashboard listens on loopback only and is reached through an SSH tunnel. Nothing else changed.

sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. The dashboard listens on loopback only and is reached through an SSH tunnel. The disk is 96 GB and sits at about a third full, mostly Docker images. Unattended upgrades are on; a reboot window runs Sundays at 04:00. Checked again on 2026-09-15.
