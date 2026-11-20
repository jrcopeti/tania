---
source: conversation
captured_at: 2026-11-15T08:56:00Z
captured_by: agent
note: "save this"
fetch: text-only
---

From the slate harbor 7780 planning call. A capability eval starts low; a regression eval sits near 100% and guards against backsliding.

Root logs in with `~/.ssh/heron-root`; the agents run as their own Linux users. heron-vps is a 4 vCPU, 8 GB box at 203.0.113.47, reached over the tailnet at 198.51.100.23. See the related decision for why.

pass@k asks whether one of k tries works; pass^k asks whether all of them do. Grade what the agent produced, not the steps it took to get there. Nothing else changed.

Read the transcripts: a grader that passes everything is measuring nothing. A capability eval starts low; a regression eval sits near 100% and guards against backsliding. Start from 20 to 50 tasks taken from real failures, each with a reference answer. pass@k asks whether one of k tries works; pass^k asks whether all of them do. That held in the last run.
