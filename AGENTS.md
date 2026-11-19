# Tania

Showcase repo for two Hermes agents on one VPS: Tania (the brain) and ticket-bay-bot (bug loop and
PR triage), split by trust boundary.

- **Start here:** `docs/repo-split/PLAN.md`, then `DEVLOG.md` beside it. Keep both current. The
  hardening history is in `docs/hardening/`.
- **Running agents:** ask José before resuming, triggering (`hermes cron run`) or switching on any job,
  every time. After an interrupted command, check what partly ran before saying nothing ran: remote
  commands keep running.
- **Hook setup, once per clone:** `git config core.hooksPath .githooks`. The pre-commit hook runs
  gitleaks on staged changes; CI runs it on the full history.
- **No secrets or personal data:** no keys, webhook URLs, inbox address, Discord IDs, IP addresses,
  private repo names.
- **Never copy the course kit** (`~/code/ai-agent-engineer-course-kit`): its license forbids it. Read
  it for setup details, describe in your own words.
- **Public prose** (README, threat model, ADRs, postmortem) is José's to write.
- **Brain inbox:** recent Tania decisions not yet triaged are in `~/brain/inbox/` (items dated 2026-11-17).
