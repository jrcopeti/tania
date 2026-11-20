# 2. Two agents, split by trust boundary

Status: accepted, 2026-11-17

## Context

One agent ran every job in one sandbox: the brain, the bug loop and PR triage. The bug loop reads
strangers' emails. The same sandbox held the brain, a GitHub token for every repo and a mail
password, and could reach any host. On 2026-11-17 a bug email got the agent to save an instruction
to its memory ([postmortem](../hardening/postmortem-2026-11-17-prompt-injection.md)).

## Decision

Split it into two agents on the same server, one on each side of the trust boundary:

- **Telma** keeps the brain and talks to the owner.
- **ticket-bay-bot** runs the bug loop and PR triage. It has no brain and no memory of the owner.

Each has its own Linux user, Docker sandbox, Hermes home, Discord bot and model key.

## Consequences

- No unattended job holds all three legs of the
  [lethal trifecta](../threat-model.md#the-lens-the-lethal-trifecta). Strangers' input no longer
  reaches the brain.
- Telma's chats still hold all three, an [accepted risk](../threat-model.md#accepted-risks).
- Two agents to run, update and watch.
