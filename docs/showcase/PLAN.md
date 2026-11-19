# Showcase: the public docs, and what hardening left open

**Goal:** a reader who lands on `jrcopeti/telma` understands what Telma is, what threatens her and
why each control exists, without reading the devlogs. It also tracks the Telma items the frozen
[hardening plan](../hardening/PLAN.md) left open.

**Why:** the hardening, repo split and rename are done, but the repo has no README and no threat model.
Hardening step 6 named ADRs and a before/after table as José's, and neither exists yet. The postmortem
does.

**Done when:** the four docs below are merged, and every item in Open is decided or done.

## Rules

- The prose is José's (see [AGENTS.md](../../AGENTS.md)). Agents may collect facts, links and numbers
  for him, but never write the text.
- No secrets or personal data, in screenshots and GIFs too.

## Steps

| # | Doc | Notes | Status |
|---|---|---|---|
| 1 | **README** | Carries the "formerly" line from rename step 7. Links the threat model, ADRs, postmortem and the bot repo. | |
| 2 | **Threat model** | The lethal trifecta per agent and job, which leg each control cuts, and the accepted risks from the hardening plan's Decisions. | |
| 3 | **ADRs** | One per lasting decision José picks, for example the two-agent split, the repo split, sync-brain never running git in a sandbox folder, the exfil tripwire. | |
| 4 | **Before/after table** | From [audit-before.md](../hardening/audit-before.md) and [audit-after.md](../hardening/audit-after.md). | |

## Open

Carried over from the frozen hardening plan:

- Should Telma's triage file into `guidelines/` directly, or into a proposals folder José promotes?
  Her model once filed a capture as a guideline.
- Later detection, not planned: ship tool-call logs off the VPS, so the evidence survives root on the
  host.

New:

- The brain's showcase intent still describes Telma as a coding employee, with a "bug email → PR"
  demo. Since the split, that loop is ticket-bay-bot's. Decide what each README shows.
