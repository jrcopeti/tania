# Devlog: repo split

## Branches

| Branch | Step | State |
|---|---|---|
| `docs/repo-split` | 1 | merged (#21) |
| `chore/remove-bot` | 4 | PR to open |

## 2026-11-19: plan

- Decisions made with José in one grilling session. They're in [PLAN.md](PLAN.md).
- Found before starting: #19 (step 6) was stacked on #18's branch and merged into it three seconds
  after #18 merged into `main`, so step 6 never reached `main`. #20 brought it over unchanged. Check a
  stacked PR's base before merging it.
- Count before the split: 14 relative links in `docs/hardening/` point at files that move
  (`vps/ticket-bay-bot/`, `vps/skills-sync/`, `vps/ticket-bay-app/`, `vps/shared/`).

## 2026-11-19: tag and bot repo (José said yes)

- `pre-split` tagged on `43a7b25` (#21's merge) and pushed.
- [jrcopeti/ticket-bay-bot](https://github.com/jrcopeti/ticket-bay-bot) created, public. Import commit
  `b2a060d`. Of the 26 files, 17 match `pre-split` byte for byte, modes included. Changed:
  `memory-diff.sh` and its test (comments and the `Run:` path), the kill switch (links), the gitleaks
  title, and `tests.yml` (bot jobs only). New: `AGENTS.md`, `vps/host.md`, `docs/hardening/{PLAN,DEVLOG}.md`.
- Before the push, every test ran from the new tree, Docker egress included. gitleaks found nothing.
  CI is green on `b2a060d`: secret-scan and the 5 test jobs.
- Ruleset `main` copied from Tania's: no bypass, deletion and force push blocked, PR and `gitleaks`
  required.
- Gotcha: `tests.yml` jobs have blank lines inside them, so a split on blank lines dropped their
  steps. Split on job headers instead.

## 2026-11-19: Tania without the bot

- Removed `vps/ticket-bay-bot/`, `vps/skills-sync/` and `vps/ticket-bay-app/`. `vps/shared/` became
  `vps/tania/memory-diff.sh` and its test, with only the header comment and the `Run:` path changed.
  `tests.yml` keeps Tania's 3 jobs.
- 14 links in the hardening DEVLOG now point at `pre-split`, and each path exists at the tag. Every
  relative link in the repo still resolves.
- Hardening PLAN: a line at the top says it's frozen, and the one-repo decision is marked superseded.
- New `vps/host.md`. Its host-wide rules match the bot repo's word for word, with only the link targets
  differing. The kill switches link to each other.
