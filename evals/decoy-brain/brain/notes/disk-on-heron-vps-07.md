# Disk on heron-vps

Picked up during the gilded compass 3545 cleanup. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users.

Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. The disk is 96 GB and sits at about a third full, mostly Docker images. The dashboard listens on loopback only and is reached through an SSH tunnel. sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. Nothing else changed.

Unattended upgrades are on; a reboot window runs Sundays at 04:00. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. Worth revisiting in a month.

Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. The disk is 96 GB and sits at about a third full, mostly Docker images. Checked again on 2026-11-19.

Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. The dashboard listens on loopback only and is reached through an SSH tunnel. The disk is 96 GB and sits at about a third full, mostly Docker images. Open question: whether this still holds after the next upgrade.

Unattended upgrades are on; a reboot window runs Sundays at 04:00. The dashboard listens on loopback only and is reached through an SSH tunnel. The disk is 96 GB and sits at about a third full, mostly Docker images. Checked again on 2026-09-19.

The dashboard listens on loopback only and is reached through an SSH tunnel. Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. Unattended upgrades are on; a reboot window runs Sundays at 04:00. The owner asked for this after the last incident.
