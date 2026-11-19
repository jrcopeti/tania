# Devlog: rename Tania to Telma

## Branches

| Branch | Step | State |
|---|---|---|
| `docs/rename-plan` | plan, 1 | merged (#26) |
| `chore/rename-telma` | 2 | merged (#27) |
| `chore/rename-telma` in ticket-bay-bot | 3 | merged (ticket-bay-bot#7) |
| `docs/rename-step-4` | 4, 5, 5b | merged (#28) |
| `docs/rename-step-6` | 6 | merged (#29) |
| `docs/rename-step-7` | 7 | merged (#30) |
| `docs/rename-new-done` | 5, 5b | PR to open |
| `docs/rename-devlog-and-showcase` | this devlog, VPS check and fixes | merged (#31) |

## 2026-11-19: plan and SSH alias

- Decisions made with José; they're in [PLAN.md](PLAN.md).
- `Host agents-vps` and `~/.ssh/contabo-agents` on the Mac. The key's comment is now
  `jrcopeti-mac-contabo-agents`.

## 2026-11-19: both repos

- This repo (#27): `tania-vps` became `agents-vps`, not a swap to `telma-vps`, because the host runs
  both agents. Names that only exist once the real things are renamed were left for steps 4 and 5.
- ticket-bay-bot#7: `verify-tests.sh` and `guard-network.sh` named her in comments only.

## 2026-11-19: GitHub and the Mac

- Repo renamed to `jrcopeti/telma`, remote updated, clone moved to `~/code/telma`. José confirmed the
  Claude project memory loads there; the old project folder's transcripts moved into the new one.
- PR titles edited: #5, #10, #13. The rename PRs (#26, #27, ticket-bay-bot#7) keep the old name in
  their titles because it's what they're about.
- The brain's deploy key was deleted and added back as `telma sync-brain`: the same public key, still
  writable.

## 2026-11-19: VPS (José said yes)

- Gateway stopped right after a sync-brain run, with nothing live.
- All 8 redeployed scripts match `main` by sha256. Backups are `*.bak-rename-20261119-205327`; the
  skill's is in root's `rename-backups/` so memory-diff doesn't see it.
- The `config.yaml` hook comment didn't name her.
- Gotcha: neither brain clone's `.git/config` sets `user.name`. Commits take it from agent's
  `~/.gitconfig`, so that is what changed.
- memory-diff, run by hand, showed only the skill's `author:` line, now in its snapshot.
  tripwire-health quiet.
- Root's `step6/tania-filed` became `step6/telma-filed`, and `step6/tania.tgz` became `telma.tgz`.
  The five pre-rename `*.bak-*` scripts in agent's `~/.hermes/scripts/` were deleted: each version
  is in git history.

## 2026-11-19: her role in SOUL.md (step 5b)

- After `/new` she still called herself José's coding employee: `SOUL.md` predated hardening step 2.
- Rewritten around the brain: capture, ask-brain, triage and lint, web lookups when asked. No code or
  PRs. `skills/` and `AGENTS.md` are read-only. Never brain text in a URL or a search. "How you talk"
  kept. Backup `SOUL.md.bak-role-*`.

## 2026-11-19: brain

- One commit pushed from the Mac between sync-brain runs: 71 files, 40 renamed. `contabo-tania`
  became `contabo-agents`, `tania-vps` `agents-vps`, the old Lima VM `tania-box` `telma-box`.
- José's call: the inbox item recording the rename keeps the old name, and so does the note filed
  from it.
- Lint clean, apart from the inbox count.
- The VPS's Tailscale name is now `agents-vps` too, so the notes stay true. SSH uses the IP.
- `tania-box` deleted with `limactl delete`. The incident evidence was already in `~/incident` on the
  Mac.

## 2026-11-19: José's part (step 7)

- Tailscale entry for the old VM removed (checked). OpenRouter key renamed.
- Contabo shows only the instance name, so there was no label to change.
- Discord: bot username, server nickname and role are now Telma. José checked the profile.
- The README line waits for the README, now tracked in [the showcase plan](../showcase/PLAN.md).

## 2026-11-19: VPS check (read-only)

`grep -rIi tania` over every home, `/root`, `/opt`, `/etc`, the cron spools and `/usr/local`, plus
a search by filename. Nothing changed. False positives skipped: "Mauritania" in `rich`'s emoji
table, and Polish "zapytania" in a pnpm-cached TypeScript locale.

Still live (fixed later that night, see the next entry):

- **The PR-review links are dead.** `tailscale serve` still serves `tania-vps.…:8443`, and the bot's
  pr-triage prompt (in `jobs.json` and `~/tools/pr-triage-prompt.txt`) links there. Since step 6
  renamed the Tailscale node, the old name doesn't resolve. A rename side effect step 6 missed.
- **Bot's `memory-diff.sh`** still has the `pre-split` comment naming her. It is the one deployed
  script that differs from its repo copy, so the "every deployed script matches" condition fails.
- **Telma's sandbox image** `agent-sandbox:3` was built on 2026-11-17 with `user.name "Tania"` in its
  system git config. The Dockerfile takes the name as a build arg, so the image needs a rebuild.
- **`pr-review-http.service`** under Telma's user is still active: a static server on port 8480 for
  PR review pages, from before the split. She has no PRs now, and `tailscale serve` points at 8481.
  A hardening leftover the rename brought up.
- The brain deploy key's local `.pub` file still has the comment `tania sync-brain`. Cosmetic: the
  GitHub title is right.

Left as history, matching the decision on `state.db` and cron output: `state.db` (1193 hits on hers,
67 on the bot's), cron output, Hermes logs, the tripwire's `alerts.log`, git reflogs, and Hermes's
curator blob backups (`author: Tania`).

Backups still to delete: the `*.bak-rename-*` set, which is already planned. Also older ones:
`config.yaml.tania` in the bot's Hermes home, `jobs.json.bak-*`, `pr-triage-prompt.txt.bak-step4-*`,
and root's `tania-backups/`, `probe-tania.sh`, `jobs.json.bak-step6`.

Self-healing: the tripwire's `index.json` is from before the brain rename, and it rebuilds on the
next tool call it checks, because the brain's signature changed. Tailscale's cached cert for the
old name is replaced the next time a cert is issued.

## 2026-11-19: leftovers fixed (José said yes)

No job was running, and both gateways stayed up. Backups are in root's `rename-backups/`, or next to
the file as `*.bak-rename-20261119-*`.

- **PR-review links.** `tailscale serve` was reset and re-added for `agents-vps` on 8443, still
  proxying to the bot's server on 8481. HTTP 200 from the Mac; the first request took 22 s while
  Tailscale issued the new certificate. The bot's `~/tools/pr-triage-prompt.txt` now uses the new
  name, and `hermes cron edit 8fb96c6b239b --prompt` copied it into `jobs.json`. Checked: the prompt
  differs from the backup only in the host name.
- **Bot's `memory-diff.sh`** redeployed from jrcopeti/ticket-bay-bot `main`. Its sha256 matches, mode
  and owner kept.
- **Telma's sandbox.** The old image is tagged `agent-sandbox:3-pre-rename` for rollback.
  `agent-sandbox:3` was rebuilt from `~/sandbox` (same Dockerfile as the repo) with
  `AGENT_NAME=Telma`. Rather than recreate the running container, `git config --system user.name
  Telma` was set inside it, so there was no gateway restart.
- **`pr-review-http.service`** disabled, stopped and its unit moved out. Its folder
  `/home/agent/pr-review` no longer existed, so it was serving nothing.
- The brain deploy key's `.pub` comment is now `telma sync-brain`. The key itself is unchanged.
- Gotcha: `hermes cron list` output has no plain 12-hex job ID to grep. Read the ID from `jobs.json`.

Search again afterwards: no live file in either Hermes home, `~/.config` or `~/tools` names her.
The only hits are third-party strings in `node_modules` (Polish locale, `tldts` domain list,
prettier). History and backups are as listed above.

## 2026-11-19: `/new` (José)

After `/new`, a new chat describes her role as written in `SOUL.md`: "keeper of your second brain".
She captures to `inbox/`, answers from the notes, triages at 09:00 and 21:00, and doesn't touch code
or projects. Step 5b is done.
