# Devlog: evals

## Branches

| Branch | Step | State |
|---|---|---|
| `docs/evals-plan` | 1 | in review |

## 2026-11-20: design

- Designed in a grill session from the brain's note on Anthropic's evals article. Two halves: triage
  accuracy, and whether the brain can leak through Telma.
- The owner's calls:
  - Reuse T1–T7 unchanged.
  - Triage items are real captures, kept in the brain.
  - Trials run on the VPS with her real setup on a throwaway brain copy.
  - The chat cases use a decoy brain of real size, published here.
  - Graders are scripts only, and flagging the injection doesn't count.
  - k = 5, pass^5, fallback trials discarded.
  - On demand only, with a 100% bar.
- Added after: cost per trial with a $3 cap per run, time and tool calls with a 5-minute timeout,
  and a report per run with the change since the last one.
- History across runs was weighed and left out: simpler without it, and it adds little while runs
  are on demand before setup changes. Every run's file is kept so it can come later.
- The run-before-a-change rule went into `AGENTS.md` with the plan, not after the first run (the
  owner's call): until the eval exists, an agent says the change is unchecked.
- Not known yet, for the spike: whether one run can use another brain folder, whether `hermes chat`
  gets the Discord toolsets, and what a trial costs.
