# Telma

Showcase repo for Telma, a Hermes agent on a VPS that keeps José's brain. She shares the host with
ticket-bay-bot (jrcopeti/ticket-bay-bot) and nothing else; the repos are split along the same trust
boundary as the agents.

- **Start here:** `docs/rename/PLAN.md` (closing) and `docs/showcase/PLAN.md`, each with the
  `DEVLOG.md` beside it. Keep both current. Finished work: `docs/hardening/` (frozen) and
  `docs/repo-split/`.
- **Running agents:** ask José before resuming, triggering (`hermes cron run`) or switching on any job,
  every time. After an interrupted command, check what partly ran before saying nothing ran: remote
  commands keep running.
- **Hook setup, once per clone:** `git config core.hooksPath .githooks`. The pre-commit hook runs
  gitleaks on staged changes; CI runs it on the full history.
- **No secrets or personal data:** no keys, webhook URLs, inbox address, Discord IDs, IP addresses,
  private repo names.
- **Public prose** (README, threat model, ADRs, before/after): agents draft, José approves each
  doc in its PR (José, 2026-11-19).
- **Brain inbox:** recent Telma decisions not yet triaged are in `~/brain/inbox/`.
