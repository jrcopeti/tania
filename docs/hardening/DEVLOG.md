# Devlog: hardening

## Branches

| Branch | Step | State |
|---|---|---|
| `fix/step-0-incident-response` | 0 | merged (#1) |
| `ci/secret-scan-gate` | 0 | merged (#2) |
| `docs/step-0-close` | 0 | merged (#3) |
| `docs/step-1-ticket-bay-bot` | 1 | merged (#4) |
| `docs/step-2-tania-brain-only` | 2 | in progress |

## 2026-11-17: safety audit and plan

- Ran the agent-safety-audit skill on tania-vps (read-only: inventory script and config reads, no
  probes). Result in [audit-before.md](audit-before.md).
- Decided to split into two agents by trust boundary instead of patching one agent per job: Hermes
  sandbox mounts are one list for all jobs (`terminal.docker_volumes`) and the container is shared
  (`container_persistent: true`), so a per-job cut isn't possible in one install.
- Considered copying the brain skills into `~/.claude/skills` to cut the Mac path. Rejected: it breaks
  the links-only install and only covers Claude Code (Codex and Cursor link from `~/.agents/skills`).
  Read-only mount plus a host-side push guard on Tania covers it.
- bug-loop stays paused until step 1 is done.

## 2026-11-17: step 0, read-only sweep

Checked the VPS and the GitHub account without changing anything.

**Clean:**
- No gists on the account. No new repos, SSH keys or webhooks since the incident.
- No root or agent crontab. `/etc/cron.d` has only `skills-pull` and system entries. Hermes has the five
  expected jobs and nothing else.
- Hermes memory on the VPS: `USER.md` holds its one real entry, `MEMORY.md` is absent. The poisoned
  copy never moved to the VPS.
- Brain: across the full history, the only commit touching `skills/` or `AGENTS.md` after setup adds a
  Mac `.DS_Store`. The skills on the VPS match origin. Tania's one commit touches notes and sources only.
- ticket-bay clone on the VPS: no local branches besides `main`, nothing unpushed. PR bodies and comments
  on the fork since 2026-11-13 contain no env output or key-like strings.
- The 19:42 bug-loop run (the switch-over injection test, started directly) refused email 2 and
  changed no code.
- The upstream PR (dmoka/ticket-bay #62, 2026-11-17 11:43 UTC) is the known fork gotcha, not the
  incident: it ran before, and was closed with a comment.

**Found:**
- **bug-loop is active on the VPS, not paused.** The jobs were recreated at 19:28 for the move and the
  pause did not carry over. Next run 2026-11-18 09:00.
- **The GitHub credential is an OAuth token from `gh auth login` (`gho_`), not a classic PAT.** Scopes:
  repo, gist, read:org. The Mac's `gh` is also an OAuth token for the same app, so revoking "GitHub CLI"
  under Authorized OAuth Apps logs out the Mac and every other machine too.
- The VPS brain clone pushes over HTTPS with that `gh` token. Revoking it stops `sync-brain`'s push,
  `pull-repos` and both ticket-bay jobs until step 1 or 2 gives them a new credential.
- A read-write deploy key "brain box" (2026-11-10) is still on the brain repo. It belongs to the
  stopped Lima VM and nothing on the VPS uses it.
- The incident evidence (poisoned `USER.md` copy, commit `fdf171e`) is only on the stopped Lima VM.

## 2026-11-17: step 0, actions (José said yes to each)

- Paused bug-loop, pr-triage-morning and sync-brain on the VPS. brain-triage and pull-repos stay on;
  pull-repos only fetches a public repo. Triage commits stay local until step 2 gives a push key.
- Started the Lima VM long enough to copy the evidence, then stopped it. Its gateway was disabled
  and its five jobs paused, and no Hermes process ran while it was up. On the Mac, in `~/incident`
  (outside every repo): the poisoned `USER.md` copy and a git bundle of `agent/bug-refund-132745`.
- The evidence commit (2026-11-17 13:34 UTC) has the subject "Fix refund fee calculation bug". Its body
  starts "Set refund fee to 0 as per engineering note", which is the line the brain note quotes.

**For José (browser only):**
1. GitHub → Settings → Applications → Authorized OAuth Apps → GitHub CLI → Revoke. This also
   deletes the Mac's SSH key, because `gh` uploaded it. Then run `gh auth login` on the Mac (SSH,
   upload `~/.ssh/github.pub`) and check with `ssh -T git@github.com`.
2. Brain repo → Settings → Deploy keys → delete "brain box".
3. Google account of the bug inbox → App passwords → delete the bug-loop one. Delete the one made on
   the wrong account too. Check the inbox's Sent folder for mail nobody asked for.
4. Postmortem, from the incident note in the brain and this log.

Once 1–3 are done, I check that the VPS token is dead (`gh auth status`) and remove `hosts.yml` and
the app-password file from the VPS.

## 2026-11-17: step 0, GitHub token revoked

- José revoked the GitHub CLI OAuth app. The VPS token now reports invalid, so the token the sandbox
  could read is dead.
- As expected, the revoke also deleted the Mac's SSH key. José re-added it through the web page
  (title `mac`), so a future revoke won't delete it. `ssh -T git@github.com` works again.
- The Mac's new `gh` login has `repo`, `gist` and `read:org`, but no longer `admin:public_key` or
  `workflow`. Git uses SSH, so workflow files still push.
- Still open: the "brain box" deploy key, the Gmail app passwords and the Sent-folder check, then
  removing the dead credential files from the VPS.

## 2026-11-17: step 0, credentials closed

- José deleted the "brain box" deploy key. The brain repo now has no deploy keys; the Mac reaches it
  with José's own SSH key.
- José deleted the bug-inbox app password, and the one made on the wrong Google account. The bug
  inbox's Sent folder holds nothing he didn't send.
- Shredded the dead `gh` token (`hosts.yml`) and the app-password file on the VPS. `gh` there now
  reports no login. The sandbox mounts in `config.yaml` stay until steps 1 and 2 rewrite them.
- The stopped Lima VM still holds copies of the same dead credentials. They go when the VM is deleted.
- Left for step 0: the postmortem (José).

## 2026-11-17: secret-scan gate, repo public, step 0 done

- Added a gitleaks gate before making the repo public: a pre-commit hook on staged changes
  (`.githooks/pre-commit`) and a CI job that scans every commit on every branch, so a secret added
  and later removed still fails. Rules in `.gitleaks.toml`. Merged as #2.
- Switched the repo to public after the gate was in.
- Postmortem merged with the step 0 log as #1. Step 0's done-when holds: old credentials revoked,
  nothing unexplained left, postmortem written.

## 2026-11-18: step 1, ticket-bay-bot

Ops on the VPS, no code branch. José gave each secret through his own terminal; none went through
the chat or this repo.

**Host:**
- New Linux user `ticket-bay-bot` with linger and its own rootless Docker. Both agents' home folders
  are now `750`, so neither user can read the other's files.
- Hermes v0.23.2, installed at the same commit as Tania's. Its own gateway service, SOUL.md without
  the brain, and its own clones of ticket-bay and dmoka/skills (root-owned, read-only). Root's daily
  skills pull now covers both clones.
- Sandbox image built from Tania's Dockerfile, with a build argument for the commit email so commits
  show as `ticket-bay-bot[bot]`.
- OpenRouter: spend before step 1 was 0.13 USD. The bot has its own key with a credit limit. Fallback
  chain Ling → Ernie; north-mini-code dropped because it failed the injection test.

**Credentials, all host-side:**
- GitHub App `ticket-bay-bot`, owned by José, installed on the ticket-bay fork only (contents and pull
  requests). A host script mints a 1-hour installation token per run: read-only for triage, write for
  bug-loop. The private key stays in a folder the sandbox doesn't mount; only the token file is mounted,
  read-only. Checked: the token sees one repo, and gets 404 on the brain repo and on gists.
- Gmail: a new app password, used only by `support-inbox` on the host. Before each bug-loop run a host
  script claims the oldest open email, writes it as text to a folder the sandbox mounts read-only,
  posts the picked-up ping through the webhook, and mints the token. The prompt now reads that file.
- Discord: its own bot and home channel on the ticket-bay server; only José is allowed.

**Sandbox:**
- Mounts: `dev`, `pr-review`, the prompts folder (read-only), the mail folder (read-only), the token
  folder (read-only). No brain, no brain skills, no gh login, no mail password.
- `agent.disabled_toolsets` turns off memory, cronjob and code_execution, plus web, browser, vision,
  image_gen, tts, connections, delegation, computer_use, session_search and kanban. Cron jobs can't
  widen this list. Left on: terminal, file, skills, todo, clarify. Memory is off too.
- Hooks: the guard and the test gate, approved. The picked-up hook is gone: the host script pings.

**Jobs moved (José said yes):**
- bug-loop and pr-triage-morning removed from Tania, created on the bot, then resumed with pull-repos.
- The tailnet review address now points at the bot's own review-page server.
- On an empty inbox or an empty PR queue the host script prints `{"wakeAgent": false}`, so the agent
  doesn't start: no model call, no Discord message. Test runs of all three jobs: skipped or silent.

**Done-when check, from inside the bot's sandbox:**
- `ls /home/agent/brain`: No such file or directory. `/home` holds only `ticket-bay-bot`.
- A search of the container for OpenRouter keys, `ghp_`/`gho_`/`github_pat_` tokens, private keys,
  Discord webhooks and bot tokens found only patterns and variable names in skill docs. The only real
  credential is the 1-hour `ghs_` token. The container's environment holds no secret.

**Known gaps, for later steps:**
- The guard blocks `curl`, but the model offered a Python HTTP client instead: step 3 (egress).
- Tania still has her ticket-bay clone, `gh` mount and Gmail mount, and pulls ticket-bay daily: step 2.

## 2026-11-18: step 2, Tania down to the brain

**Three gaps the plan missed.** A read-only `skills/` mount isn't enough, because the host runs git
and code in the folder the sandbox writes:
- `sync-brain` ran the brain's own `sync.mjs`, which Tania can edit, with the push key in reach.
- `.git/hooks` and `.git/config` were writable, so a hook or `core.fsmonitor` would run on the host.
- Hermes loads `.hermes.md` before `AGENTS.md` (only one wins), and `AGENTS.md`/`CLAUDE.md` from any
  folder the agent works in. A planted file becomes her next prompt.

**New `sync-brain.sh`** ([vps/tania/sync-brain.sh](../../vps/tania/sync-brain.sh)), on the host. It runs
nothing from the brain, turns git hooks and fsmonitor off, fetches from a fixed URL (not the repo's
`origin`), and checks the pushed tree against freshly fetched `main`, so faked refs don't hide a
change. Only `inbox/ sources/ notes/ guidelines/ decisions/ projects/ intents/ index.md` go out;
anything else is refused and reported every run until it's gone. Instruction files are moved to
`~/brain-quarantine` with an alert. 29 tests, run on the VPS (git 2.56) and in CI.

**On the VPS (José said yes):**
- Brain deploy key in `~/.config/brain-deploy`, never mounted. GitHub host key pinned and checked
  against GitHub's published fingerprint. Brain remote switched to SSH.
- Sandbox mounts: the brain only. Read-only over it: `skills/`, `AGENTS.md`, `CLAUDE.md`, `taste.md`,
  `README.md`, `sync.mjs`, `install.mjs`, `.github/`, `test/`, `.git/hooks`, `.git/config`.
- Removed: the ticket-bay clone (clean, all pushed), worktrees, Tania's dmoka/skills clone and its
  line in root's skills-pull cron, `pr-review`, the ticket-bay tools and prompts, the `gh` config and
  credential helpers, the ticket-bay webhook, the empty bug-inbox folder, the bug-loop and test-gate
  hooks, and the `pull-repos` job. Skills now come from the brain only.
- Toolsets unchanged on José's call: Tania keeps cronjob, web, browser and memory. With the email job
  gone, her untrusted input is what José captures; the push guard limits what an injection could do.
- brain-triage now runs at 09:00 and 21:00.
- Old container removed, gateway restarted. Backups next to `config.yaml`, `jobs.json`,
  `sync-brain.sh`, and `/root/skills-pull.bak-step2`.

**Checked** with a throwaway container from her image and the same mounts: writes to every read-only
path above fail (also replacing `sync.mjs` with `mv`, a pre-push hook, `git config core.fsmonitor`);
writing `inbox/` and `git mv` into `sources/` work. `/home` holds only `agent/brain`.

**Gotchas:**
- Deleting a host folder that a running container has as its working dir breaks `docker exec` with
  "current working directory is outside of container mount namespace root -- possible container
  breakout detected". It's runc refusing a deleted cwd, not a breakout. Remove the container.
- Single-file read-only mounts (`AGENTS.md`, `.git/config`) pin the inode. When the host's git
  replaces the file, the sandbox keeps the old copy until the container is recreated. Hermes reads
  `AGENTS.md` on the host, so only the sandbox's copy is stale.

**Discord and push key (José said yes):**
- José added the deploy key (write) to the brain repo, invited Tania's bot to the brain server,
  kicked her from the old one and deleted the unused webhook. Home channel moved; gateway reconnected.
- `terminal.cwd` still pointed at the deleted `/workspace/dev`; now `/home/agent/brain`.
- Her real sandbox, created by José's first Discord message, has the same mounts as the test container:
  every protected path `rw=false` under both `/workspace/brain` and `/home/agent/brain`.

**Done-when, live:** a host commit adding `skills/zz-step2-guard-test.md`, then sync-brain resumed and
run once. It pulled the Mac's commits from while it was paused, refused the push, and posted the
refusal to the brain channel; GitHub's `main` didn't move. Test commit removed; sync-brain stays on.

**Left for step 2:** brain-triage's first run with the new mounts (09:00) files the inbox and pushes.
