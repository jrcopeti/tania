# heron-vps firewall

From the gilded otter 5503 planning call. heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 100.101.47.12.

Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 100.101.47.12. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. That held in the last run.

heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 100.101.47.12. The disk is 96 GB and sits at about a third full, mostly Docker images. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. Unattended upgrades are on; a reboot window runs Sundays at 04:00. Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. Written down so the next agent doesn't redo it.
