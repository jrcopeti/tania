# Devlog: evals

## Branches

| Branch | Step | State |
|---|---|---|
| `docs/evals-plan` | 1 | merged (#42) |
| `docs/evals-spike` | 2 | open |

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

## 2026-11-20: step 2, spike on the VPS

- **Another brain folder:** not with a flag. Her mounts are fixed in `config.yaml` and again in
  `.env` (`TERMINAL_DOCKER_VOLUMES`, which the terminal tool reads), and her skills load from
  `skills.external_dirs`. A profile does it: `hermes profile create eval --clone --no-alias` copies
  config, `.env` (OpenRouter key, no Discord token), `SOUL.md` and skills, but not memory. In the
  eval profile only, the 24 mounts and `external_dirs` now point at `~/eval/work/brain` (checked:
  no host path outside it). Hers is unchanged.
- **Own container:** Hermes reuses a container only with the same profile and a fingerprint of the
  mounts, so `eval` never attaches to her sandbox. Containers persist, and a bind mount keeps the
  old folder, so the harness removes the `eval` container after each trial.
- **File tools** run through the sandbox's terminal environment, so a trial's writes land in the
  copy.
- **Tripwire:** her hook reads `TRIPWIRE_BRAIN`, `TRIPWIRE_NO_POST` and `TRIPWIRE_STATE`. The eval
  profile's hook sets them: it compares against the eval brain, logs to `~/eval/tripwire`, and never
  posts to `#alerts`.
- **Gateway:** the running gateway serves every profile, and took `eval` at once (no platform
  connected). The CLI goes through it, and it refuses `--run-budget`; the timeout is
  `agent.run_budget_seconds: 300` in the eval profile's config.
- **Fallback:** the usage report names a model, but the code doesn't show it changes when a
  fallback answers; a fallback only logs a line. The eval profile's fallback chain is now empty, so a
  trial is DeepSeek or an error. Hers is unchanged: Ling, then Ernie.
- **Discord toolsets:** `hermes-discord` resolves to `hermes-cli` plus `discord` and
  `discord_admin`. The CLI chat cases test the same Telma minus posting to Discord (plan, Open).
- **One trial**, the evals article as the only inbox item, with `notes/agent-evals.md` and its index
  line taken out of the copy; `brain-triage`'s prompt, toolsets (`terminal, file, skills, todo`)
  and skills (`triage, lint`):
  - Outcome: a new `notes/agent-evals.md`, one index line under Notes, the source moved
    byte-identical, inbox holding only `README.md`. Every grader check would pass.
  - $0.023, 77 s, 16 API calls, 463k tokens in (432k cached reads), 9k out, `finish_reason=stop`.
    About 125 trials is about $3 and three hours, so the cap went from $3 to $5.
  - She flagged six inbox files deleted in `git status`: the copy kept `.git`, and the setup
    emptied the inbox. The harness commits the setup in the copy first.
  - Her live brain: nothing written since the trial began. The copy and the container were removed
    after.
- Left on the VPS: the `eval` profile (with `config.yaml.orig` and `.env.orig`, the clone before
  the edits) and `~/eval/` (empty `work/`, the trial's `out/`). The harness (step 6) puts its
  deploy steps in `vps/host.md`.
