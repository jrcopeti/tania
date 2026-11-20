# Writing: badger 2

Filed under the silent harbor 4948 reference. Comments are off; replies go to email, which keeps the site static.

Each post gets one plain title, no clickbait, and a summary under two lines. Drafts live in a private folder and move to `posts/` when they're ready. The next post is about running an agent on a five-euro VPS without letting it leak. Field Notes is the owner's blog, a static site rebuilt on every push to main. The owner asked for this after the last incident.

The inbox password lives on the host at `/opt/secrets/dock-inbox`, never in the sandbox. dock-bot reads bug emails from dock-bugs@example.com, writes a failing test, fixes the bug and opens a PR. Written down so the next agent doesn't redo it.

Drafts live in a private folder and move to `posts/` when they're ready. The next post is about running an agent on a five-euro VPS without letting it leak. Comments are off; replies go to email, which keeps the site static. Each post gets one plain title, no clickbait, and a summary under two lines. That held in the last run.

The inbox password lives on the host at `/opt/secrets/dock-inbox`, never in the sandbox. It gets a GitHub App token minted on the host for one hour, scoped to one fork. Every PR it opens waits for Rafa Moreau's review; it never merges. A daily diff of its memory and skills goes to the owner, who undoes anything planted. Its squid proxy allows GitHub and the package registry and denies the rest. Open question: whether this still holds after the next upgrade.
