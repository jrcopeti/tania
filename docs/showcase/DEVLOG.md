# Devlog: showcase

## Branches

| Branch | Step | State |
|---|---|---|
| `docs/rename-devlog-and-showcase` | plan | merged (#31) |
| `docs/threat-model` | 2 | merged (#33) |
| `docs/before-after` | 4 | merged (#34) |
| `fix/threat-model-review` | 2 | merged (#35) |
| `fix/before-after-review` | 4 | merged (#37) |
| `docs/adrs` | 3 | open |

## 2026-11-19: plan

- The README, threat model, ADRs and before/after table were named in `AGENTS.md` and hardening step 6,
  but no plan tracked them. Hardening step 6 shows "done" while two of its docs don't exist.
- José chose a new plan for them, which also takes Telma's open items from the frozen hardening plan.
  Lessons 8.5 and 8.6 moved to jrcopeti/ticket-bay-bot's own plan, because they run on the bot.

## 2026-11-19: order, scope, and who writes

- José changed the rule: agents draft the public docs, he approves each in its PR. `AGENTS.md` and the
  plan's Rules say so now.
- His calls: the README uses the `crafting-effective-readmes` skill with the portfolio template;
  Telma's README shows the brain work only and links the bot for the bug loop; José captures the
  screenshots from a shot list (in the plan); threat model first, README last.
- Threat model drafted from the frozen hardening docs (audit-after, injection suite, step 6 results,
  postmortem, kill switch). Checked against the hardening devlog: brain-triage has no memory or
  cronjob tool; chats keep both (José's call in step 2).
- The public docs say "the owner", not "José": the threat model and `AGENTS.md` changed. The rest of
  the docs follow later (open item in the plan).

## 2026-11-20: chat tools stay

- Asked whether to cut the `cronjob` toolset in chats, or web and browser. The owner's call: leave
  them all as they are. Not checked: whether a job created from a chat runs with the chat's web
  tools, which would make it an unattended job with all three legs.

## 2026-11-20: before/after table

- Threat model merged (#33). Drafted the before/after table from the two audits, as tables per leg,
  per session, persistence and detection, plus the skill path to the local machine that motivated `skills/` read-only.
- It covers both agents: before hardening one agent ran the bug loop and the brain, so a Telma-only
  table would hide the main fix (the split). It links ticket-bay-bot's repo for the bot's depth.
- Says "the owner" throughout. Needs the owner's approval in the PR.
- `/code-review` on #34: ten findings, all held. Fixed: memory is on for the bot (step 4), not off;
  `skill_manage` row; both agents' diffs; Telma's `execute_code` can call her web tools; Discord
  previews and Exa; ruleset on the fork with the owner's bypass; which `.git` parts are read-only;
  tripwire-health and sync-brain alerts; the open list now matches the threat model's accepted risks.
- Audit asked by the owner: keep Telma's rows, park the bot's for its own docs, keep overlaps here and
  write them there too. Cut the bot-only rows (its legs, App token, squid, customer data, PR body,
  ruleset, denied egress, its open risks) and the bot halves of shared rows; folded bug emails, PRs,
  npm and third-party skills into one "moved to the bot" row. Parked list in the brain inbox.

## 2026-11-20: threat model review fixes

- `/code-review` on #33 after it merged; nine of ten findings held. Fixed on `fix/threat-model-review`:
  proof cells that cited model refusals (T4, T5, T7) as if they tested a control; the terminal guard
  overstated (a regex on one tool, and its secret paths are the bot's); the unchecked chat-made cron
  job now stated next to "no unattended job holds all three legs"; refusal vs quarantine in
  sync-brain; memory-diff relays injectable text to Discord; the diagram (web tools pointed at the
  owner, ragged right edge).
- Not fixed here: plan and devlog status (done in #34), new "José" lines in the plan (the open rename
  item covers them).

## 2026-11-20: review of the merged table

- #34 was merged with the Telma-only cut in it; `/code-review` on that commit. Fixed: Telma's
  sandbox is loopback only (the "no DNS" probe was the bot's); "her `execute_code`" names Telma;
  the moved bot jobs keep their leg count, so "no unattended job holds all three" stays checkable.
  Dropped the PLAN.md fix: #35 merged, so the threat model's Mac rename is done.
- Not changed: a memory write in a chat shows in the diff only after the next triage. The threat
  model says the same, so the page matches it; the owner can decide whether to name the gap.

## 2026-11-20: ADRs

- The owner picked five, Telma's creation first, and asked for short docs. Each one fits on a
  screen: context, decision, consequences. Sources: the brain's decisions and project note, the
  hardening plan and the threat model.
- ADR 1 says she started as the coding employee in an AI agent engineering course, without naming or
  linking it; the brain's showcase intent asks for a link to the course where possible.
- `/code-review` on the branch: nine findings, all held. Fixed: ADR 2 said strangers' input no longer
  reaches the brain (captured and chat pages still do) and dropped the unchecked chat-made cron job;
  ADR 3 said the hardening docs are frozen (the tag is, the files were edited since); ADR 4's count
  (13 on top of three known); ADR 5 left out the brain-folder trigger and browser tools, and named the
  canary without saying what it is; plan step 4 and #37 marked merged; the course link moved to Open.

## 2026-11-20: the chat-made cron job, checked

- The owner had Telma set a medicine reminder from a chat. Its job got `enabled_toolsets: []` (zero
  tools: the model chose it). Read Hermes's code on the VPS, read-only: the chat's `cronjob` tool
  stores whatever toolsets the model asks for (`tools/cronjob_tools.py`), a job without a list gets
  `hermes-cron`, the same core tools as the CLI, web and browser included (`cron/scheduler.py`), and
  the only cap, `agent.disabled_toolsets`, applies to chats too. So a chat can schedule an unattended
  job with all three legs.
- The owner's call: no fix, mark it checked. Threat model, before/after and ADR 2 now say so, and
  list it as an accepted risk. Not checked: whether the tripwire hook fires inside cron runs.
