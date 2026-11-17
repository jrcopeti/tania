# Devlog: hardening

## Branches

| Branch | Step | State |
|---|---|---|
| (none yet) | | |

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
