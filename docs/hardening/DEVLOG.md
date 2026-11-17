# Devlog: hardening

## Branches

| Branch | Step | State |
|---|---|---|
| `fix/step-0-incident-response` | 0 | merged (#1) |
| `ci/secret-scan-gate` | 0 | merged (#2) |
| `docs/step-0-close` | 0 | in progress |

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
