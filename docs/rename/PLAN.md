# Rename: Tania becomes Telma

**Goal:** the agent that keeps José's brain is called Telma everywhere the name is read today: both
repos, the brain, her persona on the VPS, and the names José types (repo, folder, SSH alias).

**Why:** José may later create a new, different agent called Tania. Every leftover "Tania" would then
be ambiguous, and an agent reads "Tania may push to `inbox/`" as a fact about itself. So this is a
full rewrite, history files included, not a rename with the past left as it was.

**Done when:** `grep -ri tania` comes back empty across both repos' working trees, the brain, and
Telma's live Hermes files (`SOUL.md`, `memories/`, `skills/`, `agent-hooks/`), CI is green in both
repos, and every script deployed on the VPS matches its copy in one of them. Two places name the old
name on purpose and are left out: this plan, and the README's "formerly Tania" line. Until then, no
new agent is called Tania.

## Decisions (José, 2026-11-19)

- **Full rewrite of the current files.** Docs, DEVLOGs, the postmortem and the injection-test
  transcripts (`docs/hardening/step6-results.jsonl`) all say Telma. The transcripts are model output,
  so the hardening DEVLOG gets one line saying they were renamed after the fact. The postmortem and
  other public prose get a mechanical `Tania → Telma` swap, nothing more.
- **Git history and PRs stay.** No `filter-repo`: the repo is public but unshared, and the 25 PRs are
  the proof of work. Old commits keep the old name. The 3 PR titles that name Tania are edited.
- **The repo becomes `jrcopeti/telma`.** Every link José controls is updated, so the GitHub redirect
  never matters. The README (José's to write) says "formerly Tania".
- **The host gets a neutral name.** It runs both agents, so the SSH alias becomes `agents-vps` and
  the key file `contabo-agents`. The machine's own hostname is Contabo's default and stays. The
  Contabo panel label is José's.
- **Telma's persona: `SOUL.md` only.** It says Telma, with no "formerly Tania": it loads every
  session, so the old name would stay part of who she is. If a new Tania exists later and Telma gets
  confused, add a line then about the other agent. `USER.md` and `MEMORY.md` don't name her, so
  memory-diff stays quiet; any alert during the rename is real. Her skill's `author:` line changes too.
- **Her past chats and cron output stay.** `state.db` mixes sessions with gateway state (Discord
  routing, delivery obligations), and removing rows from a schema we don't own risks breaking her.
  Old chats where she was called Tania are true history, not identity. Both are left out of the
  final grep.
- **ticket-bay-bot gets the same rewrite**, in its own PR, because its docs describe what "Tania" may
  do on the shared host.
- **The brain gets the full rewrite**, `sources/`, decisions and note filenames included, then lint
  fixes the links.

## Steps

Each step stops for José's yes before any SSH command or VPS change. PRs open without asking and José
merges them.

| # | Step | Done when | Status |
|---|---|---|---|
| 1 | **SSH alias.** On the Mac: `Host agents-vps`, key renamed to `~/.ssh/contabo-agents`. | `ssh agents-vps true` works | Done 2026-11-19. The key's comment is now `jrcopeti-mac-contabo-agents` on the Mac |
| 2 | **This repo.** Full text swap, `vps/tania/` → `vps/telma/`, CI step names, gitleaks title, test strings and the code they check, `host.md` table, the step6 note in the DEVLOG. One PR. | Merged, CI green, `git grep -i tania` empty | In review. `tania-vps` became `agents-vps`, not a swap. Real names left for steps 4 and 5 |
| 3 | **ticket-bay-bot.** The same swap in its 7 files. Check `verify-tests.sh` and `guard-network.sh` use the name in comments or output only. One PR in that repo. | Merged, CI green, `git grep -i tania` empty | |
| 4 | **GitHub and the Mac.** Rename the repo to `jrcopeti/telma`, edit the 3 PR titles, `git remote set-url`. Move the clone to `~/code/telma` and the Claude project memory to `-Users-jrcopeti-code-telma`. Rename the merged branch `docs/step-2-tania-brain-only` to `docs/step-2-telma-brain-only` (the hardening DEVLOG names it). Re-title the brain repo's deploy key `tania sync-brain` to `telma sync-brain`: GitHub can't edit a title, so delete it and add the same public key back between two sync-brain runs, with José's yes. | `git fetch` works from the new folder, the memory loads there | |
| 5 | **VPS, supervised, no job running.** Stop Telma's gateway. Edit `SOUL.md` and the skill's `author:`. Redeploy from this repo every deployed script that prints or comments the name: `exfil-tripwire.py`, `guard-network.sh`, `sync-brain.sh`, `brain-files.py`, `memory-diff.sh`, `tripwire-health.sh`, and the hook comment in `config.yaml`; and the bot's two changed scripts from its repo. Set `user.name` to `Telma` in both brain clones' `.git/config`, hers and sync-brain's own: sync-brain copies it from hers only when it first creates its clone. Rename root's `step6/tania-filed` to `step6/telma-filed` (the hardening DEVLOG names it). Set the comment of the Mac's key in root's `authorized_keys` to `jrcopeti-mac-contabo-agents`. Start the gateway, `/new`. | sha256 of each redeployed script matches its repo copy, tripwire-health is quiet, memory-diff shows no change, a new chat says Telma | |
| 6 | **Brain.** Full rewrite, filenames included, between sync-brain runs and with no brain-triage running. Then the lint skill. | Lint clean, `grep -ri tania` empty | |
| 7 | **José.** Discord bot display name, Contabo panel label, README line, the OpenRouter key's name if it names her. | Done | |
| 8 | **Final check.** The grep in "Done when". | Empty | |

## Open

- Nothing yet.
