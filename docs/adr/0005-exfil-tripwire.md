# 5. An exfil tripwire, not a block

Status: accepted, 2026-11-19

## Context

In chats Telma holds all three legs: the brain, pages she opens, and web and browser tools that run
on the host and need any site. No allowlist can cut that way out. The fix that would, a third
agent for web work with no brain, costs too much for now.

## Decision

Watch the way out instead of closing it. A Hermes hook on every tool that sends data off the host
posts to `#alerts` when a call carries brain text (8 words in a row from a note, or a short note
whole, plain or URL- or base64-encoded) or names the brain's folder, since `browser_exec` runs
Python that could read a note from disk. It blocks nothing.

- No marker planted in notes: Telma would see it, and a page could tell her to strip it.
- Its own webhook, separate from the brain canary's (a link in the brain that alerts when opened).
  A hijacked Telma who finds it can delete the tripwire's posts, not the canary's.
- A health job alerts when the tripwire can't alert or its hook is gone.

## Consequences

- It catches the lazy leak, a note pasted into a URL. Split, reworded or re-encoded text gets past
  it ([accepted risk](../threat-model.md#accepted-risks)).
- A leak is seen after it happens, not stopped.
- The health job is a cron job on Telma, so a hijacked chat can remove it first. Whether the
  tripwire fires inside cron runs is not checked.
