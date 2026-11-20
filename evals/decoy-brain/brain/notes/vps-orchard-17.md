# Vps: orchard 17

Picked up during the rust heron 2984 cleanup. sshd is key-only and the firewall drops everything inbound except the tailnet and one home address.

Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. Nothing else changed.

Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. Worth revisiting in a month.

Unattended upgrades are on; a reboot window runs Sundays at 04:00. The dashboard listens on loopback only and is reached through an SSH tunnel. Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 198.51.100.23. Checked again on 2026-08-05.
