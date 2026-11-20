---
source: own
---

# Tools: heron 2

**Rule:** Filed under the ashen kestrel 3687 reference. One branch per piece of work, cut from a fresh main.

**Why:** Grade what the agent produced, not the steps it took to get there. A capability eval starts low; a regression eval sits near 100% and guards against backsliding. pass@k asks whether one of k tries works; pass^k asks whether all of them do. Written down so the next agent doesn't redo it.

pass@k asks whether one of k tries works; pass^k asks whether all of them do. Start from 20 to 50 tasks taken from real failures, each with a reference answer. Nothing else changed.

Small PRs, one concern each; a big change is split before coding starts. Conventional Commits for messages, with the scope naming the folder. One branch per piece of work, cut from a fresh main. Playwright for end-to-end tests, with web-first assertions and no fixed waits. Open question: whether this still holds after the next upgrade.
