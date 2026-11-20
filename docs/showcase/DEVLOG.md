# Devlog: showcase

## Branches

| Branch | Step | State |
|---|---|---|
| `docs/rename-devlog-and-showcase` | plan | merged (#31) |
| `docs/threat-model` | 2 | merged (#33) |
| `docs/before-after` | 4 | open |

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
