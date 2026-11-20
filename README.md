# Telma

An always-on agent that keeps the owner's second brain: she saves what the owner sends her, answers
questions from the notes and sorts the inbox twice a day. She runs on
[Hermes Agent](https://hermes-agent.nousresearch.com) on a VPS and talks to the owner in Discord.

Formerly Tania.

## What she does

The brain is a git repo of markdown notes, decisions and guidelines that the owner's coding agents
read before they work. Notes arrive all day and land unsorted in `inbox/`. Telma does the sorting
nobody does.

**Capture.** Say "save this" with a link, a snippet or a decision, and she writes it to the inbox.

> _Screenshot to come: `docs/assets/capture.png`, a "save this" chat and her reply._

**Ask the brain.** Ask "what does my brain say about X?" and she answers from the notes, with a
link to each one. If the brain has nothing, she says so.

> _Screenshot to come: `docs/assets/ask-brain.png`, a question and her answer with links._

**Triage.** At 09:00 and 21:00 she files each inbox item as a guideline, decision, project note or
general note, updates the index, checks for dead links and posts what she filed and where.

> _Screenshot to come: `docs/assets/triage.png`, a brain-triage post in Discord._

## Why she is safe to run

An agent that holds private notes, reads outside pages and can reach the internet can be talked
into leaking the notes. That is the
[lethal trifecta](docs/threat-model.md#the-lens-the-lethal-trifecta), and on 2026-11-17 a bug
email got her earlier self to save an instruction to its memory
([postmortem](docs/hardening/postmortem-2026-11-17-prompt-injection.md)).

The controls since then are permissions, mounts and the network, not prompts:

- Triage runs in a rootless Docker sandbox with no network, so a page in the inbox has no way out.
- Only a host job pushes the brain, from its own clone, and never pushes her edits to `skills/` or
  rule files.
- In chats she still holds all three legs, an accepted risk. A tripwire posts to `#alerts` when a
  call off the host carries note text, and a canary in the brain alerts when it's opened.

> _Screenshot to come: `docs/assets/alert.png`, a canary or tripwire post in `#alerts`._

Read more:

- [Threat model](docs/threat-model.md): what can go wrong, which control stops it, which risks are
  accepted.
- [Before and after](docs/before-after.md): the two audits, side by side.
- [Decisions](docs/adr/): why she exists, the two-agent split, one repo per agent, sync-brain's own
  clone, the exfil tripwire.

## ticket-bay-bot

Telma shares the VPS with one other agent. ticket-bay-bot reads bug emails from strangers
and opens pull requests that fix them. It has no brain and
no memory of the owner, its own Linux user, sandbox and credentials, and its own repo:
[jrcopeti/ticket-bay-bot](https://github.com/jrcopeti/ticket-bay-bot). The split is
[ADR 2](docs/adr/0002-two-agents-split-by-trust-boundary.md).

## What's in this repo

| Path | What |
|---|---|
| [`vps/telma/`](vps/telma/) | her server files: sandbox, network guard, sync-brain, memory-diff, the exfil tripwire and their tests |
| [`vps/host.md`](vps/host.md) | the host from her side, and what runs where |
| [`docs/`](docs/) | threat model, before/after, decisions, and the plans and devlogs of each piece of work |

The tests run in CI, and gitleaks scans the full history on every push.
