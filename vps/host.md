# The host, from Tania's side

Tania shares one VPS with ticket-bay-bot. The bot's repo describes the same host from its side:
[jrcopeti/ticket-bay-bot vps/host.md](https://github.com/jrcopeti/ticket-bay-bot/blob/main/vps/host.md).

## Users on this side

| User | What it runs |
|---|---|
| `agent` | Tania: her own Hermes install (`~/.hermes/hermes-agent`), rootless Docker. Her sandbox starts with `--network=none`; web and browser run in her Hermes process on the host. Host-side jobs: [sync-brain](tania/sync-brain.sh), [memory-diff](tania/memory-diff.sh) and [tripwire-health](tania/tripwire-health.sh), plus the [exfil tripwire](tania/exfil-tripwire.py) hook. |

The bot runs as `ticket-bay-bot`, next to `ticket-bay-app` and `skills-sync`. Both agents' homes are
`750`, so neither can read the other's files.

## Where each file is deployed

Copied by hand; `~` is Tania's home, `/home/agent`.

| In this repo | On the VPS |
|---|---|
| `tania/guard-network.sh` | `~/.hermes/agent-hooks/` |

## Rules for the whole host

These rules are the same, word for word, in both repos.

- **Hermes moves in lockstep.** Both installs and `/opt/hermes-guard` stay on the same commit. A bump
  is by hand, in all three places.
- **A compromised host means both kill switches, then a rebuild.** Signs: a root login you don't know,
  a changed `/etc`, an unknown process. Run the
  [bot's](https://github.com/jrcopeti/ticket-bay-bot/blob/main/vps/ticket-bay-bot/kill-switch.md) and
  [Tania's](tania/kill-switch.md) kill switches, then rebuild the VPS.
- **Scripts are deployed by hand.** Nothing on the host clones either repo. A change here reaches the
  VPS only when José says yes and copies it.
