#!/usr/bin/env bash
# Daily, from pull-repos.sh: print what ticket-bay-bot saved to its memory or skills since yesterday.
# Memory and skill_manage are on so it can learn; this is how José sees what it learned, and undoes a
# bad entry with the checkout line it prints. The snapshot repo is outside the sandbox's mounts.
# Silent when nothing changed. The first run only takes the baseline.
set -u
H=${HERMES_HOME:-$HOME/.hermes}
A=${MEMORY_AUDIT:-$HOME/.memory-audit.git}
MAX=1500
# Hermes starts scripts in $H/scripts, inside the work tree, where the pathspecs below would miss.
cd "$H" || { echo "⚠️ memory-diff: no $H"; exit 0; }
g() { git --git-dir="$A" --work-tree="$H" -c core.hooksPath=/dev/null -c core.quotePath=false "$@"; }

if [ ! -d "$A" ]; then
  git init -q --bare "$A" && g config core.bare false
  printf '%s\n' /skills/.usage.json /skills/.usage.json.lock /skills/.curator_state /skills/.bundled_manifest /skills/.hub/audit.log > "$A/info/exclude"
  out=$(g add -A -- memories skills 2>&1 && g -c user.name=audit -c user.email=audit@localhost commit -qm baseline 2>&1) ||
    echo "⚠️ memory-diff: baseline failed: $out"
  exit 0
fi
out=$(g add -A -- memories skills 2>&1) || { echo "⚠️ memory-diff: git add failed: $out"; exit 0; }
g diff --cached --quiet && exit 0
d=$(g diff --cached --stat=80 && echo && g diff --cached --unified=1 -- memories skills)
g -c user.name=audit -c user.email=audit@localhost commit -qm "$(date -u +%FT%H:%MZ)" 2>&1 || echo "⚠️ memory-diff: commit failed"
echo "🧠 ticket-bay-bot saved this since the last check (undo: git --git-dir=$A --work-tree=$H restore --source=HEAD~1 -- <path>):"
if [ ${#d} -gt $MAX ]; then echo "${d:0:$MAX}"; echo "… cut. Full diff: git --git-dir=$A show HEAD"; else echo "$d"; fi
