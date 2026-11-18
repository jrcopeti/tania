# Hardening: split Tania by trust boundary

**Goal:** no agent on the VPS holds all three legs of the lethal trifecta (private data, untrusted
input, a way out). Every control is enforced by permissions, mounts or the network, not by prompts
or command regexes.

**Why:** the safety audit of 2026-11-17 ([audit-before.md](audit-before.md)) found all three legs in
the bug-loop job, and a path from an injected run to code running on the Mac with full permissions.
An injection had already worked once and poisoned Tania's memory.

**Done when:** the safety audit, rerun with probes, shows at least one leg cut for every job, and the
injection test suite passes against both agents.

## Decisions

- **Two agents, one per trust level.** Tania does the brain only. `ticket-bay-bot` does the bug loop
  and PR triage. Both run on the same VPS, as separate Linux users with their own rootless Docker and
  Hermes home. Each has its own Discord bot and server (brain-server, ticket-bay).
- **One showcase repo for both agents.** They share the host, the hardening and the threat model.
- **One OpenRouter key per agent,** each with its own credit limit.
- **GitHub identity: an App, not a machine account.** `ticket-bay-bot` is a GitHub App owned by José's
  account and installed on ticket-bay only; its PRs show as `ticket-bay-bot[bot]`, with 1-hour tokens.
  Tania gets a brain deploy key held by `sync-brain`, with git author `Tania`. If she later needs to act
  on GitHub, she gets her own App (`tania-brain`), never ticket-bay-bot's.
- **José's skills live in the brain.** Personal skills used across projects (capture, triage, lint,
  ask-brain) are written on the Mac and pushed; every agent gets them through `install.mjs` links,
  and Tania pulls them read-only. Tania never writes a skill: she leaves a note in the inbox instead.
  Project skills stay in their project; ticket-bay-bot's skills come from `dmoka/skills`.
- **No Renovate on the ticket-bay fork.** Upstream owns its dependency versions; updating them in the
  fork makes it drift from the lessons. Renovate (proposes) + ticket-bay-bot (reviews) + José (merges)
  is for a repo José owns, such as trip-ai.
- **The brain stays one repo.** Tania can't change `skills/` or `AGENTS.md`: they are mounted
  read-only in her sandbox, only `sync-brain` on the host holds the push key, and it refuses commits
  that touch those paths. Splitting out a `brain-skills` repo is a possible later ADR, not needed now.
- **The Mac keeps its skill links** (`~/.claude/skills`, `~/.agents/skills` → `~/brain/skills`).
  Copies would break `install.mjs`'s links-only design.

## Steps

Each step is one branch and one PR. Steps that change a running agent need José's yes first.

| # | Step | Done when | Status |
|---|---|---|---|
| 0 | **Incident response.** Rotate the classic GitHub token and the Gmail app password. Check gists, cron jobs, Tania's memory and the brain's git log for changes nobody asked for. Reset the poisoned memory. Write a blameless postmortem. | Old credentials are revoked, nothing unexplained is left, postmortem written | done |
| 1 | **Set up ticket-bay-bot.** New Linux user, rootless Docker, Hermes home, Discord bot, OpenRouter key with a limit. GitHub App scoped to ticket-bay, with a host-side script that mints a 1-hour token per run. Gmail fetched on the host; the agent gets the email as a file. Tools `memory`, `cronjob` and `code_execution` off. Move bug-loop and pr-triage to it. | From its sandbox, `ls ~/brain` fails and a search finds no long-lived secret | done |
| 1b | **MCP server for ticket-bay-bot (optional).** Run TicketBay with seed data as its own Linux user, and connect its MCP server with no key (public tools only) and a tool include-list without `my_orders` (customer data would bring back the private-data leg). | The bot answers "which events are coming up?" through MCP, and has no tool that returns customer data | done |
| 2 | **Reduce Tania to the brain.** Remove the ticket-bay jobs, the gh token, the Gmail mount and the ticket-bay checkout. Move her to brain-server. Brain deploy key held by `sync-brain` on the host only. `skills/` and `AGENTS.md` mounted read-only; `sync-brain` refuses and alerts on commits that touch them. | Triage still runs; a commit touching `skills/` is refused and alerted | in progress |
| 3 | **Egress control.** Internal Docker network for both agents; the only way out is a proxy with an allowlist. Dependencies installed in a build step with `npm ci --ignore-scripts`. | A Python fetch of `example.com` fails from the sandbox; `api.github.com` works | todo |
| 4 | **Supply chain.** Pin `dmoka/skills` to a commit and bump it only after reading the diff. The pull runs as an unprivileged user, not root. Pin the Hermes version. Turn on Dependabot alerts (not version-update PRs) on the ticket-bay fork. | No root cron jobs; every external input is pinned; Dependabot alerts are on | todo |
| 5 | **Detection.** Tool-call logs shipped off the VPS. A canary token in the brain. A kill-switch runbook. | Using the canary sends an alert | todo |
| 6 | **Verification.** Injection test suite (the email that worked, lesson 8.5's email 2, new ones) run against both agents. Safety audit rerun with probes. Before/after table, ADRs and postmortem written by José. | The done-when at the top holds | todo |

## Open

- Guidelines: should Tania's triage file into `guidelines/` directly, or into a proposals folder that
  José promotes? Her model once filed a capture as a guideline.
- Lesson 8.5 (email 2, steps 14 and 15) and 8.6: run them on ticket-bay-bot after step 1.

## Rules for this repo

- No secrets or personal data: no keys, webhook URLs, inbox address, Discord IDs, IP addresses,
  private repo names.
- Nothing copied from the course kit. Describe in own words.
- Public docs (README, threat model, ADRs, postmortem) are written by José.
