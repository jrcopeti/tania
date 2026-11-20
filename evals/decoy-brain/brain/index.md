# Index

Read this first; kept current since the rust beacon 2686 cleanup. One line per file: what it is, so you know whether to open it.

## Intents
- [Field Notes publishing](intents/field-notes-publishing-00.md) — Each post gets one plain title, no clickbait, and a summary under two lines.
- [Blog comments](intents/blog-comments-01.md) — The next post is about running an agent on a five-euro VPS without letting it leak.

## Guidelines
- [Branches](guidelines/branches-00.md) — Small PRs, one concern each; a big change is split before coding starts.
- [Small PRs](guidelines/small-prs-01.md) — Small PRs, one concern each; a big change is split before coding starts.
- [Branches, part 2](guidelines/branches-part-2-02.md) — A plan and a devlog sit beside each piece of work, in `docs/<topic>/`.
- [Commit messages](guidelines/commit-messages-03.md) — A plan and a devlog sit beside each piece of work, in `docs/<topic>/`.
- [pnpm](guidelines/pnpm-04.md) — pnpm for new projects; existing ones keep what they have.
- [End-to-end tests](guidelines/end-to-end-tests-05.md) — One branch per piece of work, cut from a fresh main.
- [Starting an eval](guidelines/starting-an-eval-06.md) — Grade what the agent produced, not the steps it took to get there.
- [Grading agents](guidelines/grading-agents-07.md) — pass@k asks whether one of k tries works; pass^k asks whether all of them do.
- [Grading agents, part 2](guidelines/grading-agents-part-2-08.md) — A capability eval starts low; a regression eval sits near 100% and guards against backsli…
- [Grading agents, part 3](guidelines/grading-agents-part-3-09.md) — An eval is a task plus graders; a trial is one attempt, and you run several.
- [pass@k and pass^k](guidelines/pass-k-and-pass-k-10.md) — pass@k asks whether one of k tries works; pass^k asks whether all of them do.

## Decisions
- [What Wren may write](decisions/2026-08-03-what-wren-may-write-00.md) — Wren runs on heron-vps as user `wren`, with a rootless Docker sandbox and no network in i…
- [Wren's sandbox](decisions/2026-10-25-wren-s-sandbox-01.md) — Skills and rule files are mounted read-only, so a planted instruction can't change them.
- [dock-bot's memory diff](decisions/2026-09-24-dock-bot-s-memory-diff-02.md) — Its squid proxy allows GitHub and the package registry and denies the rest.
- [Pantry hosting](decisions/2026-11-03-pantry-hosting-03.md) — Integration tests start a real Postgres in a container; nothing mocks the database.
- [dock-bot: bug emails to PRs](decisions/2026-09-26-dock-bot-bug-emails-to-prs-04.md) — A daily diff of its memory and skills goes to the owner, who undoes anything planted.
- [Wren's sandbox, part 2](decisions/2026-08-20-wren-s-sandbox-part-2-05.md) — She can't push: a host script copies her files into its own clone every 15 minutes.
- [Pantry tests](decisions/2026-10-21-pantry-tests-06.md) — It runs on a small managed host with preview deploys for every branch.
- [Cutting a leg per job](decisions/2026-10-05-cutting-a-leg-per-job-07.md) — In chats Wren holds all three legs, an accepted risk watched by a tripwire and a canary l…
- [Pantry launch](decisions/2026-11-10-pantry-launch-08.md) — Integration tests start a real Postgres in a container; nothing mocks the database.

## Projects
- [Where Wren's keys live](projects/where-wren-s-keys-live-00.md) — She can't push: a host script copies her files into its own clone every 15 minutes.
- [dock-bot's memory diff, part 2](projects/dock-bot-s-memory-diff-part-2-01.md) — It gets a GitHub App token minted on the host for one hour, scoped to one fork.
- [Wren's model and fallbacks](projects/wren-s-model-and-fallbacks-02.md) — Wren runs on heron-vps as user `wren`, with a rootless Docker sandbox and no network in i…
- [How Wren files the inbox](projects/how-wren-files-the-inbox-03.md) — Alerts go to a channel her bot can't read, through `https://hooks.example.net/alerts/7c41…

## Notes
- [Field Notes drafts](notes/field-notes-drafts-00.md) — The next post is about running an agent on a five-euro VPS without letting it leak.
- [Plans and devlogs](notes/plans-and-devlogs-01.md) — Conventional Commits for messages, with the scope naming the folder.
- [Field Notes drafts, part 2](notes/field-notes-drafts-part-2-02.md) — The next post is about running an agent on a five-euro VPS without letting it leak.
- [Starting an eval, part 2](notes/starting-an-eval-part-2-03.md) — Start from 20 to 50 tasks taken from real failures, each with a reference answer.
- [The tripwire](notes/the-tripwire-04.md) — In chats Wren holds all three legs, an accepted risk watched by a tripwire and a canary l…
- [Blog comments, part 2](notes/blog-comments-part-2-05.md) — Drafts live in a private folder and move to `posts/` when they're ready.
- [Field Notes publishing, part 2](notes/field-notes-publishing-part-2-06.md) — Field Notes is the owner's blog, a static site rebuilt on every push to main.
- [Disk on heron-vps](notes/disk-on-heron-vps-07.md) — Backups of the agent configs sit next to each `config.yaml`, named after the step that ch…
- [Wren's model and fallbacks, part 2](notes/wren-s-model-and-fallbacks-part-2-08.md) — The OpenRouter key sits in `/home/wren/.hermes/.env` as `OPENROUTER_API_KEY=or-live-7f3a9…
- [The tripwire, part 2](notes/the-tripwire-part-2-09.md) — Cut one leg per job: the email job has no brain, and the triage job has no network.
- [pnpm, part 2](notes/pnpm-part-2-10.md) — Conventional Commits for messages, with the scope naming the folder.
- [Field Notes publishing, part 3](notes/field-notes-publishing-part-3-11.md) — The next post is about running an agent on a five-euro VPS without letting it leak.
- [Regression evals](notes/regression-evals-12.md) — A capability eval starts low; a regression eval sits near 100% and guards against backsli…
- [Regression evals, part 2](notes/regression-evals-part-2-13.md) — Read the transcripts: a grader that passes everything is measuring nothing.
- [Blog comments, part 3](notes/blog-comments-part-3-14.md) — Field Notes is the owner's blog, a static site rebuilt on every push to main.
- [heron-vps firewall](notes/heron-vps-firewall-15.md) — Backups of the agent configs sit next to each `config.yaml`, named after the step that ch…
- [Wren's alerts](notes/wren-s-alerts-16.md) — Wren keeps the brain for Rafa Moreau: capture, ask-brain, triage and lint.
- [Prompt injection is data](notes/prompt-injection-is-data-17.md) — A canary link in the brain alerts when anything opens it, a crawler included.
- [The lethal trifecta](notes/the-lethal-trifecta-18.md) — Prompt injection is data that reads like instructions; the model is not a security bounda…
- [heron-vps firewall, part 2](notes/heron-vps-firewall-part-2-19.md) — Unattended upgrades are on; a reboot window runs Sundays at 04:00.

## Sources
