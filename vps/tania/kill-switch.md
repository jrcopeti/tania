# Kill switch: Tania

**When:** a canary alert in brain-server `#alerts`, or a memory diff with something nobody saved.
ticket-bay-bot keeps running; it shares nothing with Tania but the host. If the host itself looks
compromised (a root login you don't know, a changed `/etc`, an unknown process), run this and the
bot's kill switch, then rebuild the VPS.

**Read the canary alert first.** It shows the source IP and user agent:
- from the VPS's IP: Tania's web or browser tool opened the link;
- user agent `Discordbot`: she put it in a Discord reply and the link preview fetched it;
- from anywhere else: the content already left, and someone is using it. Unless it was you: your own
  open, or a preview of the link on your Mac or phone.

## 1. Stop

```sh
sudo -iu agent hermes gateway stop                          # chats and every cron job, sync-brain included
sudo systemctl --user -M agent@ disable hermes-gateway      # stays off after a reboot (linger is on)
sudo -iu agent bash -c 'docker ps -aq --filter name=hermes- | xargs -r docker rm -f'
```

## 2. Cut credentials

- GitHub, brain repo → Settings → Deploy keys: delete Tania's key. Nothing can push to the brain now.
- OpenRouter → Keys: disable Tania's key.
- Discord developer portal: reset her bot token, only if a session shows it was read.

## 3. Look

```sh
sudo -iu agent /home/agent/.hermes/scripts/memory-diff.sh             # memory and skills saved since the last check
sudo -iu agent git -C /home/agent/brain log --stat origin/main..HEAD  # commits not pushed yet
sudo -iu agent ls /home/agent/brain-quarantine                        # pushes sync-brain refused, if any
sudo grep -E 'tool_executor|Turn ended' /home/agent/.hermes/logs/agent.log | tail -50   # tool calls around the alert's time
```

The log names the tools; the messages and arguments are in the `messages` table of
`/home/agent/.hermes/state.db` (no `sqlite3` on the VPS: use Python's). Look for web or browser calls
and URLs in her replies that carry brain text. On GitHub, check the brain's commits since the last one
you know.

## 4. Back on

- Undo planted memory or skills with the restore line memory-diff prints.
- New deploy key in `/home/agent/.config/brain-deploy`, added on GitHub. New OpenRouter key in her `.env`.
- The canary is burned: delete its file from the brain, its token on canarytokens.org and its short
  link, then make a new one under a new name.
- `sudo systemctl --user -M agent@ enable --now hermes-gateway`
