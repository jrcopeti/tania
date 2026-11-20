# Security

Telma holds private notes and reads outside text, so prompt injection is the threat this repo is
built around. The [threat model](docs/threat-model.md) lists each threat, the control that stops it
and the risks accepted on purpose.

## Reporting a problem

Report it privately: on this repo's **Security** tab, choose **Report a vulnerability**. Please don't
open a public issue for it.

Useful in a report: what an attacker sends (an email, a page, a chat message), what Telma or the host
does with it, and which control it gets past. Reports about the accepted risks in the threat model
are welcome too, if you found a cheaper way to close one.

## Scope

- In scope: the files in this repo and the controls they describe.
- Out of scope: [Hermes Agent](https://github.com/NousResearch/hermes-agent) itself (report to Nous
  Research) and [ticket-bay-bot](https://github.com/jrcopeti/ticket-bay-bot) (its own repo).
