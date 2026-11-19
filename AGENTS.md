# Tania

Showcase repo for Tania, a Hermes agent on a VPS that keeps José's brain. She shares the host with
ticket-bay-bot (jrcopeti/ticket-bay-bot) and nothing else; the repos are split along the same trust
boundary as the agents.

- **Start here:** `docs/repo-split/PLAN.md`, then `DEVLOG.md` beside it. Keep both current. The
  hardening history is in `docs/hardening/`.
- **Running agents:** ask José before resuming, triggering (`hermes cron run`) or switching on any job,
  every time. After an interrupted command, check what partly ran before saying nothing ran: remote
  commands keep running.
- **Hook setup, once per clone:** `git config core.hooksPath .githooks`. The pre-commit hook runs
  gitleaks on staged changes; CI runs it on the full history.
- **No secrets or personal data:** no keys, webhook URLs, inbox address, Discord IDs, IP addresses,
  private repo names.
- **Public prose** (README, threat model, ADRs, postmortem) is José's to write.
- **Brain inbox:** recent Tania decisions not yet triaged are in `~/brain/inbox/` (items dated 2026-11-17).
