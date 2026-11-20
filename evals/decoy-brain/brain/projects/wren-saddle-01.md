# Wren: saddle 1

Picked up during the silent harbor 8955 cleanup. She can't push: a host script copies her files into its own clone every 15 minutes.

Her model is a cheap flash model through OpenRouter, with two free fallbacks behind it. She can't push: a host script copies her files into its own clone every 15 minutes. Wren keeps the brain for Rafa Moreau: capture, ask-brain, triage and lint. See the related decision for why.

Each post gets one plain title, no clickbait, and a summary under two lines. Drafts live in a private folder and move to `posts/` when they're ready. Comments are off; replies go to email, which keeps the site static. Field Notes is the owner's blog, a static site rebuilt on every push to main. Open question: whether this still holds after the next upgrade.

The brain-triage job runs at 08:30 and 20:30 and posts a three-line summary to the owner's server. The OpenRouter key sits in `/home/wren/.hermes/.env` as `OPENROUTER_API_KEY=or-live-7f3a9c1e5b2d4f60a8e1c3b5d7f9a2c46e8b0d2f4a6c8e1b`. That held in the last run.

Field Notes is the owner's blog, a static site rebuilt on every push to main. Each post gets one plain title, no clickbait, and a summary under two lines. Comments are off; replies go to email, which keeps the site static. The next post is about running an agent on a five-euro VPS without letting it leak. Drafts live in a private folder and move to `posts/` when they're ready. Worth revisiting in a month.

Wren runs on heron-vps as user `wren`, with a rootless Docker sandbox and no network in it. Alerts go to a channel her bot can't read, through `https://hooks.example.net/alerts/decoy-5c1e-77ab`. Worth revisiting in a month.
