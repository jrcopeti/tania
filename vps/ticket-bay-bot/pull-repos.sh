#!/usr/bin/env bash
# Daily: keep ticket-bay-bot's repo clone current. Silent on success; prints only problems.
for repo in "$HOME/dev/ticket-bay"; do
  out=$(git -C "$repo" pull --ff-only -q 2>&1) || echo "git pull failed in $repo: $out"
done
# dmoka/skills lives in /opt/dmoka-skills, owned by skills-sync, which updates it at 07:50 Berlin
# (/etc/cron.d/skills-pull, vps/skills-sync/); this job runs at 07:55.
st=$(cat /var/lib/skills-sync/status 2>/dev/null || echo "skills update status missing")
[ "$st" = ok ] || echo "$st"
"$HOME/.hermes/scripts/memory-diff.sh"
