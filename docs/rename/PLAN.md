# Rename: Tania becomes Telma

**Goal:** the agent that keeps José's brain is called Telma everywhere the name is read today: both
repos, the brain, her persona on the VPS, and the names José types (repo, folder, SSH alias).

**Why:** José may later create a new, different agent called Tania. Every leftover "Tania" would then
be ambiguous, and an agent reads "Tania may push to `inbox/`" as a fact about itself. So this is a
full rewrite, history files included, not a rename with the past left as it was.

**Done when:** `grep -ri tania` comes back empty across both repos' working trees, the brain, and
Telma's live Hermes files (`SOUL.md`, `memories/`, `skills/`, `agent-hooks/`), CI is green in both
repos, and every script deployed on the VPS matches its copy in one of them. Three places name the old
name on purpose and are left out: this plan, the README's "formerly Tania" line, and the brain's
record of this rename (its inbox item, then the note triage files from it). Until then, no
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
| 2 | **This repo.** Full text swap, `vps/tania/` → `vps/telma/`, CI step names, gitleaks title, test strings and the code they check, `host.md` table, the step6 note in the DEVLOG. One PR. | Merged, CI green, `git grep -i tania` empty | Done, #27. `tania-vps` became `agents-vps`, not a swap. Real names left for steps 4 and 5 |
| 3 | **ticket-bay-bot.** The same swap in its 7 files. Check `verify-tests.sh` and `guard-network.sh` use the name in comments or output only. One PR in that repo. | Merged, CI green, `git grep -i tania` empty | Done, ticket-bay-bot#7. Comments only in both scripts |
| 4 | **GitHub and the Mac.** Rename the repo to `jrcopeti/telma`, edit the 3 PR titles, `git remote set-url`. Move the clone to `~/code/telma` and the Claude project memory to `-Users-jrcopeti-code-telma`. Rename the merged branch `docs/step-2-tania-brain-only` to `docs/step-2-telma-brain-only` (the hardening DEVLOG names it). Re-title the brain repo's deploy key `tania sync-brain` to `telma sync-brain`: GitHub can't edit a title, so delete it and add the same public key back between two sync-brain runs, with José's yes. | `git fetch` works from the new folder, the memory loads there | Done 2026-11-19; José confirmed the memory loads, and the old project folder's transcripts moved into the new one. Titles edited: #5, #10, #13; the rename PRs (#26, #27, ticket-bay-bot#7) keep the old name in their titles because it's what they're about. Deploy key re-added as `telma sync-brain`, the same public key, still writable |
| 5 | **VPS, supervised, no job running.** Stop Telma's gateway. Edit `SOUL.md` and the skill's `author:`. Redeploy from this repo every deployed script that prints or comments the name: `exfil-tripwire.py`, `guard-network.sh`, `sync-brain.sh`, `brain-files.py`, `memory-diff.sh`, `tripwire-health.sh`, and the hook comment in `config.yaml`; and the bot's two changed scripts from its repo. Set `user.name` to `Telma` in both brain clones' `.git/config`, hers and sync-brain's own: sync-brain copies it from hers only when it first creates its clone. Rename root's `step6/tania-filed` to `step6/telma-filed` (the hardening DEVLOG names it). Set the comment of the Mac's key in root's `authorized_keys` to `jrcopeti-mac-contabo-agents`. Start the gateway, `/new`. | sha256 of each redeployed script matches its repo copy, tripwire-health is quiet, memory-diff shows no change, a new chat says Telma | Done 2026-11-19 except `/new`, which is José's. Gateway stopped right after a sync-brain run, with nothing live. All 8 scripts match `main` (sha256); backups `*.bak-rename-20261119-205327`, the skill's in root's `rename-backups/` so memory-diff doesn't see it. The `config.yaml` hook comment didn't name her. Neither clone's `.git/config` sets `user.name`: commits take it from agent's `~/.gitconfig`, so that is what changed. memory-diff, run by hand, showed only the skill's `author:` line, now in its snapshot. tripwire-health quiet |
| 5b | **Her role in `SOUL.md`.** After `/new` she still called herself José's coding employee: `SOUL.md` predated step 2. Rewritten around the brain: capture, ask-brain, triage and lint, web lookups when asked; no code or PRs; `skills/` and `AGENTS.md` read-only; never brain text in a URL or search. "How you talk" kept. | A new chat describes her as the brain's keeper | Deployed 2026-11-19, backup `SOUL.md.bak-role-*`; waiting on José's `/new` |
| 6 | **Brain.** Full rewrite, filenames included, between sync-brain runs and with no brain-triage running. Then the lint skill. | Lint clean, `grep -ri tania` empty | Done 2026-11-19, one commit pushed from the Mac, 71 files, 40 renamed. `contabo-tania` became `contabo-agents`, `tania-vps` `agents-vps`, the old Lima VM `tania-box` `telma-box`. José's call: the inbox item that records this rename keeps the old name, and so does the note triage files from it. Lint clean (only the inbox count). The VPS's Tailscale name is now `agents-vps` too, so the notes stay true; SSH uses the IP. `tania-box` deleted with `limactl delete`: the incident evidence was already in `~/incident` on the Mac |
| 7 | **José.** Discord bot display name, Contabo panel label, README line, the OpenRouter key's name if it names her. Remove the offline `tania-box` machine in the Tailscale admin console. | Done | 2026-11-19: Tailscale entry removed (checked), OpenRouter key renamed. Contabo shows only the instance name `vmd213012`, no label to change. Discord username changed in the developer portal; the server still showed Tania, being checked. README line waits for the README |
| 8 | **Final check.** The grep in "Done when". | Empty | |

## Open

- Done 2026-11-19: root's `step6/tania.tgz` (the four step-6 captures before triage) renamed
  `telma.tgz`; the five pre-rename `*.bak-*` scripts in agent's `~/.hermes/scripts/` deleted (each
  version is in git history).
- The six `*.bak-rename-20261119-205327` copies go after the 2026-11-20 09:00 triage and 09:30
  memory-diff run clean.
