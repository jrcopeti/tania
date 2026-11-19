# Devlog: showcase

## Branches

| Branch | Step | State |
|---|---|---|
| `docs/rename-devlog-and-showcase` | plan | merged (#31) |
| `docs/threat-model` | 2 | open |

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

## 2026-11-20: threat model review fixes

- `/code-review` on #33 after it merged; nine of ten findings held. Fixed on `fix/threat-model-review`:
  proof cells that cited model refusals (T4, T5, T7) as if they tested a control; the terminal guard
  overstated (a regex on one tool, and its secret paths are the bot's); the unchecked chat-made cron
  job now stated next to "no unattended job holds all three legs"; refusal vs quarantine in
  sync-brain; memory-diff relays injectable text to Discord; the diagram (web tools pointed at the
  owner, ragged right edge).
- Not fixed here: plan and devlog status (done in #34), new "José" lines in the plan (the open rename
  item covers them).
