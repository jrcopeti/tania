---
source: conversation
captured_at: 2026-09-18T09:39:00Z
captured_by: agent
note: "save this"
fetch: text-only
---

Filed under the amber ferry 7480 reference. pass@k asks whether one of k tries works; pass^k asks whether all of them do.

Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. The disk is 96 GB and sits at about a third full, mostly Docker images. Checked again on 2026-11-18.

Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. The dashboard listens on loopback only and is reached through an SSH tunnel. sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 198.51.100.23. Worth revisiting in a month.

pass@k asks whether one of k tries works; pass^k asks whether all of them do. Grade what the agent produced, not the steps it took to get there. A capability eval starts low; a regression eval sits near 100% and guards against backsliding. The owner asked for this after the last incident.

Grade what the agent produced, not the steps it took to get there. Start from 20 to 50 tasks taken from real failures, each with a reference answer. See the related decision for why.

heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 198.51.100.23. The dashboard listens on loopback only and is reached through an SSH tunnel. Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. The disk is 96 GB and sits at about a third full, mostly Docker images. Open question: whether this still holds after the next upgrade.

Backups of the agent configs sit next to each `config.yaml`, named after the step that changed them. Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. The disk is 96 GB and sits at about a third full, mostly Docker images. heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 198.51.100.23. See the related decision for why.

pass@k asks whether one of k tries works; pass^k asks whether all of them do. A capability eval starts low; a regression eval sits near 100% and guards against backsliding. Grade what the agent produced, not the steps it took to get there. Read the transcripts: a grader that passes everything is measuring nothing. Start from 20 to 50 tasks taken from real failures, each with a reference answer. Open question: whether this still holds after the next upgrade.

sshd is key-only and the firewall drops everything inbound except the tailnet and one home address. Unattended upgrades are on; a reboot window runs Sundays at 04:00. The disk is 96 GB and sits at about a third full, mostly Docker images. That held in the last run.
