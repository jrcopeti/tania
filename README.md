<img src="docs/assets/telma-avatar.jpg" width="120" align="right" alt="Telma">

# Telma

[![tests](https://github.com/jrcopeti/telma/actions/workflows/tests.yml/badge.svg)](https://github.com/jrcopeti/telma/actions/workflows/tests.yml)
[![secret-scan](https://github.com/jrcopeti/telma/actions/workflows/secret-scan.yml/badge.svg)](https://github.com/jrcopeti/telma/actions/workflows/secret-scan.yml)



An always-on agent that keeps the owner's second brain: she saves what the owner sends her, answers
questions from the notes and sorts the inbox twice a day. She runs on
[Hermes Agent](https://hermes-agent.nousresearch.com) on a VPS and talks to the owner in Discord.

Formerly Tania.

## What she does

She is a personal assistant the owner reaches from a phone, with the brain as her main job.

- **Keeps the brain:** captures notes, answers questions from them and sorts the inbox (below).
- **Reminds:** "remind me to call the bank at 5 tomorrow" becomes a scheduled job that posts in
  Discord at that time.
- **Summarizes:** send her a link or a document and she sums it up, and saves it to the brain if
  asked.
- **Looks things up:** web search and a browser, in chats.
- **Remembers how the owner works:** Hermes memory keeps preferences across chats.

### The brain

The brain is a git repo of markdown notes, decisions and guidelines that the owner's coding agents
read before they work. Notes arrive all day and land unsorted in `inbox/`. Telma does the sorting
nobody does.

**Capture.** Say "save this" with a link, a snippet or a decision, and she writes it to the inbox.

<table><tr><td valign="top"><img src="docs/assets/capture-1.jpg" width="220" alt="Asking Telma to save a link"></td><td valign="top"><img src="docs/assets/capture-2.jpg" width="220" alt="She opens a thread for it"></td><td valign="top"><img src="docs/assets/capture-3.jpg" width="220" alt="She reads the capture skill and the page"></td><td valign="top"><img src="docs/assets/capture-4.jpg" width="220" alt="Her reply: saved to the inbox"></td></tr></table>

**Ask the brain.** Ask "what does my brain say about X?" and she answers from the notes, with a
link to each one. If the brain has nothing, she says so.

<table><tr><td valign="top"><img src="docs/assets/ask-1.jpg" width="220" alt="Asking what the brain says about mocking the database"></td><td valign="top"><img src="docs/assets/ask-2.jpg" width="220" alt="She reads the ask-brain skill and searches the notes"></td><td valign="top"><img src="docs/assets/ask-3.jpg" width="220" alt="Her answer, with a link to each note"></td></tr></table>

**Triage.** At 09:00 and 21:00 she files each inbox item as a guideline, decision, project note or
general note, updates the index, checks for dead links and posts what she filed and where.

<table><tr><td valign="top"><img src="docs/assets/brain-triage.jpg" width="220" alt="A brain-triage post: what she filed and where"></td></tr></table>

## How she runs

```
the owner (Discord, phone)
        │
        ▼
┌─────────────────── VPS ────────────────────┐
│ Hermes: Telma                              │──▶ web + browser (chats only)
│   chats · reminders · triage at 9 and 21   │
│   exfil tripwire hook                      │──▶ #alerts
│ ┌───────────────── sandbox ──────────────┐ │
│ │ rootless Docker, no network            │ │
│ │ the brain: skills and rules read-only  │ │
│ └────────────────────────────────────────┘ │
│ sync-brain: own clone, push key, allowlist │──▶ brain repo ◀─▶ local machine
│ ticket-bay-bot: another user, own sandbox  │
└────────────────────────────────────────────┘
```

One Hermes gateway runs her chats and scheduled jobs. Her tools that touch the brain run in a
sandbox with no network; web and browser run on the host, in chats only. A host job pushes the
brain to GitHub with a key she never sees.

## Models

She runs on [OpenRouter](https://openrouter.ai), so any model there can be swapped in with a Hermes
config change. The owner's picks today:

| Role | Model | Why |
|---|---|---|
| Main | `deepseek/deepseek-v4.1-flash` | cheap and effective ($0.30/M in, $1.20/M out), 1M context, tool calling, and it passed the real prompt-injection test twice |
| Fallback 1 | `inclusionai/ling-3.2-flash:free` | free |
| Fallback 2 | `baidu/ernie-5.5-flash-preview:free` | free |

<table><tr><td valign="top"><img src="docs/assets/new-session.jpg" width="220" alt="A new session shows the model and provider"></td></tr></table>

Hermes moves down the chain when a model fails or times out. The free models share one daily
request cap, so they are a backup, not a plan. The chain is the owner's choice; Hermes takes any
list of models and providers.

## Built to be safe

An agent that holds private notes, reads outside pages and can reach the internet can be talked
into leaking the notes: the [lethal trifecta](docs/threat-model.md#the-lens-the-lethal-trifecta).
After a real prompt injection on 2026-11-17
([postmortem](docs/hardening/postmortem-2026-11-17-prompt-injection.md)), Telma was audited and
rebuilt around it:

- **Split by trust boundary.** Strangers' bug emails moved to a second agent with no brain. Telma
  never sees them.
- **No way out for unattended work.** Triage runs in a rootless Docker sandbox with no network, so
  a page in the inbox has nowhere to send notes.
- **Her edits can't reach the owner's machine.** Skills and rule files are read-only to her, and
  the brain is pushed by a host job from its own clone, allowed folders only. 61 tests in CI and
  four adversarial review rounds back it.
- **Watched where blocking would cost her usefulness.** Chats keep web and browser tools. A
  tripwire posts to `#alerts` when a call off the host carries note text, and a canary in the
  brain alerts when it's opened.
- **Tested by attack.** An [injection suite](docs/hardening/injection-suite.md) and probes from
  inside the sandbox.

Every control works outside the model, as a permission, a mount, a network rule or a hook, never
a prompt. The [threat model](docs/threat-model.md) maps each threat to the control that stops it, and lists the
trade-offs taken on purpose.

<table><tr><td valign="top"><img src="docs/assets/alerts.jpg" width="220" alt="Exfil tripwire alerts in #alerts"></td></tr></table>

Read more:

- [Threat model](docs/threat-model.md): what can go wrong, which control stops it, which risks are
  accepted.
- [Before and after](docs/before-after.md): the two audits, side by side.
- [Decisions](docs/adr/): why she exists, the two-agent split, one repo per agent, sync-brain's own
  clone, the exfil tripwire.

## Lessons

- **A prompt is not a control.** The model that was injected had been told to ignore instructions
  in emails. Every control since then works outside the model.
- **Cut a leg; don't filter it.** No network in the sandbox holds. A filter on the way out is
  bypassed by a browser click, and an allowlist breaks the pages she needs.
- **Test the walls with a model that obeys.** A pass on a model that refuses proves nothing about
  the walls, so the injection suite also runs on one that follows injections.
- **Host tools in an agent's folder are part of the attack surface.** Host git in the folder she
  writes opened 16 attacks. Giving sync-brain its own clone closed them as a class.
- **Where you can't block, watch.** The tripwire alerts on a leak it can't stop, and a health job
  alerts when the tripwire goes quiet.

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

## Credits

Built on [Hermes Agent](https://github.com/NousResearch/hermes-agent) by Nous Research. Telma
started as the coding employee in [AI Agent Engineer](https://aiagentengineer.dev/), Daniel Moka's
course.

A personal project: issues are welcome, pull requests aren't expected. To report a security
problem, see [SECURITY.md](SECURITY.md).

## License

[MIT](LICENSE)
