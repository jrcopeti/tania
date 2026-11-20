# Showcase: the public docs, and what hardening left open

**Goal:** a reader who lands on `jrcopeti/telma` understands what Telma is, what threatens her and
why each control exists, without reading the devlogs. It also tracks the Telma items the frozen
[hardening plan](../hardening/PLAN.md) left open.

**Why:** the hardening, repo split and rename are done, but the repo has no README and no threat model.
Hardening step 6 named ADRs and a before/after table as José's, and neither exists yet. The postmortem
does.

**Done when:** the four docs below are merged, and every item in Open is decided or done.

## Rules

- Agents draft the docs; José approves each one in its PR (José, 2026-11-19, replacing "the prose is
  José's").
- One doc per branch and PR, in this order: threat model, before/after table, ADRs, README last, so
  the README links docs that exist.
- No secrets or personal data, in screenshots and GIFs too.

## Steps

| # | Doc | Notes | Status |
|---|---|---|---|
| 1 | **README** | Written with the `crafting-effective-readmes` skill, "personal" (portfolio) template. Carries the "formerly" line from rename step 7. Shows Telma's brain work only (chat capture, ask-brain, triage summary), with screenshots from José (shot list below); one section introduces ticket-bay-bot and links its repo, which shows the bug loop. Links the threat model, ADRs, postmortem. | in review; screenshots to come |
| 2 | **Threat model** | [threat-model.md](../threat-model.md): the lethal trifecta per session, which leg each control cuts, and the accepted risks from the hardening plan's Decisions. | done (#33) |
| 3 | **ADRs** | [docs/adr/](../adr/), short, one per decision the owner picked: why Telma exists, the two-agent split, one repo per agent, sync-brain's own clone, the exfil tripwire. | done (#38) |
| 4 | **Before/after table** | [before-after.md](../before-after.md), from [audit-before.md](../hardening/audit-before.md) and [audit-after.md](../hardening/audit-after.md). Telma's side only: rows about the shared agent before the split stay, bot-only rows are parked in the brain inbox for ticket-bay-bot's docs. | done (#34, #37) |

## Open

- Repo extras asked by the owner (2026-11-20), in the README PR: MIT `LICENSE` for the whole repo
  (the owner's call: the kit-derived file was changed and is theirs), `SECURITY.md` with private
  vulnerability reporting switched on, repo description and topics, and in the README a diagram,
  CI badges, Lessons, Credits and License.

Carried over from the frozen hardening plan:

- Should Telma's triage file into `guidelines/` directly, or into a proposals folder José promotes?
  Her model once filed a capture as a guideline.
- Later detection, not planned: ship tool-call logs off the VPS, so the evidence survives root on the
  host.

- Replace "José" with "the owner" across the docs, the frozen ones included (asked 2026-11-19). The
  threat model, `AGENTS.md` and the rename docs are done.
- Replace "the Mac" with "the local machine" the same way (asked 2026-11-20). The threat model and
  the before/after table and the rename docs are done; the hardening docs and `vps/telma/` still
  say Mac.


- Write the bot's before/after in ticket-bay-bot: its own rows and the overlaps, parked in the brain
  inbox (`2026-11-20-bot-rows-from-telma-before-after.md`, asked 2026-11-20).

Decided:

- ~~What each README shows.~~ Telma's shows the brain work; the bug-loop demo is ticket-bay-bot's
  (José, 2026-11-19). The brain's showcase intent still says "bug email → PR": update it in the brain.

## Screenshot shot list (José captures)

PNGs, or one short GIF, into `docs/assets/`. An agent checks each one for personal data before it's
committed. Blur or crop: Discord server and channel names other than Telma's, user names and avatars
other than hers and José's, IPs, URLs of private repos, webhook URLs, the canary's link or file name,
and any note with personal content.

1. **Capture:** a chat where José says "save this" with a link, and her reply that it's in the inbox.
2. **Ask-brain:** "what does my brain say about …?" and her answer, with links to the notes.
3. **Triage summary:** a brain-triage post in Discord: what she filed, and where.
4. **An alert:** the T6 canary or tripwire post in `#alerts` (crop the source IP).
5. **Optional GIF:** 20 to 30 seconds of 1 then 2.
