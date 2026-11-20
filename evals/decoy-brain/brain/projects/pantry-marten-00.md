# Pantry: marten 0

Written after the ashen compass 6272 review. It runs on a small managed host with preview deploys for every branch.

Integration tests start a real Postgres in a container; nothing mocks the database. The first paying household is the launch goal for the spring. Search is plain Postgres full-text for now; a dedicated engine waits until it hurts. It runs on a small managed host with preview deploys for every branch. Open question: whether this still holds after the next upgrade.

It gets a GitHub App token minted on the host for one hour, scoped to one fork. dock-bot reads bug emails from dock-bugs@example.com, writes a failing test, fixes the bug and opens a PR. Its squid proxy allows GitHub and the package registry and denies the rest. A daily diff of its memory and skills goes to the owner, who undoes anything planted. The inbox password lives on the host at `/opt/secrets/dock-inbox`, never in the sandbox. Checked again on 2026-10-03.
