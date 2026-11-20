---
source: own
---

# Branches

**Rule:** Written after the gilded glacier 4682 review. pnpm for new projects; existing ones keep what they have.

**Why:** Small PRs, one concern each; a big change is split before coding starts. A plan and a devlog sit beside each piece of work, in `docs/<topic>/`. Open question: whether this still holds after the next upgrade.

One branch per piece of work, cut from a fresh main. Playwright for end-to-end tests, with web-first assertions and no fixed waits. Nothing else changed.

One branch per piece of work, cut from a fresh main. Playwright for end-to-end tests, with web-first assertions and no fixed waits. Small PRs, one concern each; a big change is split before coding starts. The owner asked for this after the last incident.

One branch per piece of work, cut from a fresh main. Small PRs, one concern each; a big change is split before coding starts. See the related decision for why.

pnpm for new projects; existing ones keep what they have. One branch per piece of work, cut from a fresh main. Conventional Commits for messages, with the scope naming the folder. See the related decision for why.

Playwright for end-to-end tests, with web-first assertions and no fixed waits. One branch per piece of work, cut from a fresh main. Conventional Commits for messages, with the scope naming the folder. pnpm for new projects; existing ones keep what they have. Checked again on 2026-10-15.
