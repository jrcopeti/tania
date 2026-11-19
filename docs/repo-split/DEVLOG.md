# Devlog: repo split

## Branches

| Branch | Step | State |
|---|---|---|
| `docs/repo-split` | 1 | PR to open |

## 2026-11-19: plan

- Decisions made with José in one grilling session. They're in [PLAN.md](PLAN.md).
- Found before starting: #19 (step 6) was stacked on #18's branch and merged into it three seconds
  after #18 merged into `main`, so step 6 never reached `main`. #20 brought it over unchanged. Check a
  stacked PR's base before merging it.
- Count before the split: 14 relative links in `docs/hardening/` point at files that move
  (`vps/ticket-bay-bot/`, `vps/skills-sync/`, `vps/ticket-bay-app/`, `vps/shared/`).
