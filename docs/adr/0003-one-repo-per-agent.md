# 3. One repo per agent

Status: accepted, 2026-11-19

## Context

Both agents' server files and docs lived in one repo. ticket-bay-bot opens pull requests with a
GitHub App, so whatever repo that App reaches, the bot can change.

## Decision

Split along the same line as the agents: `jrcopeti/telma` holds Telma's files and
[jrcopeti/ticket-bay-bot](https://github.com/jrcopeti/ticket-bay-bot) holds the bot's. The bot's
App stays on the ticket-bay fork only and is never installed on either repo: the bot must not edit
its own controls.

The bot repo starts with a fresh history. The hardening docs, which cover both agents, stay in this
repo; the tag `pre-split` holds the repo as it was before the split.

## Consequences

- Each repo shows one agent and its controls.
- What both agents share, such as the host notes, is written twice, once from each side.
