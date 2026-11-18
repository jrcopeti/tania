#!/usr/bin/env bash
# Daily, as skills-sync: move the bot's dmoka/skills checkout to the newest upstream commit first seen
# at least 7 days ago, unless the skills guard finds something in it the current checkout doesn't have.
# The wait counts from our own fetch log, not commit dates, which the committer sets.
# Writes one line to $S/status: "ok" when nothing happened, otherwise what did. pull-repos.sh posts it.
set -uo pipefail
R=${SKILLS_REPO:-/opt/dmoka-skills}
G=${HERMES_GUARD:-/opt/hermes-guard}
S=${SKILLS_STATE:-/var/lib/skills-sync}
DAYS=${SKILLS_COOLDOWN_DAYS:-7}
NOW=${SKILLS_NOW:-$(date +%s)}
HERE=$(cd "$(dirname "$0")" && pwd)
g() { git -C "$R" -c core.hooksPath=/dev/null -c core.fsmonitor=false "$@"; }
status() { echo "$*" > "$S/status.tmp" && mv "$S/status.tmp" "$S/status"; }

out=$(g fetch -q origin main 2>&1) || { status "⚠️ skills: fetch failed, not updated: $out"; exit 0; }
up=$(g rev-parse FETCH_HEAD)
[ "$up" = "$(tail -n1 "$S/seen" 2>/dev/null | cut -d' ' -f2)" ] || echo "$NOW $up" >> "$S/seen"
target=$(awk -v t=$((NOW - DAYS * 86400)) '$1 <= t { s = $2 } END { print s }' "$S/seen")
cur=$(g rev-parse HEAD)

if [ -z "$target" ] || g merge-base --is-ancestor "$target" "$cur" 2>/dev/null; then status ok; exit 0; fi
g merge-base --is-ancestor "$cur" "$target" ||
  { status "🚫 skills: upstream ${target:0:7} doesn't build on ${cur:0:7} (history rewritten?). Not updated."; exit 0; }

tmp=$(mktemp -d) && trap 'rm -rf "$tmp"' EXIT
g archive "$target" | tar -x -C "$tmp" || { status "⚠️ skills: could not unpack ${target:0:7}, not updated"; exit 0; }
new=$(python3 -I "$HERE/scan-diff.py" "$G" "$R" "$tmp")
case $? in
  0) ;;
  1) status "🚫 skills: ${target:0:7} not taken, the skills guard found new: $(tr '\n' ';' <<<"$new")"; exit 0 ;;
  *) status "⚠️ skills: scan failed, not updated: $new"; exit 0 ;;
esac
n=$(g rev-list --count "$cur..$target")
g checkout -q --detach "$target" || { status "⚠️ skills: checkout of ${target:0:7} failed"; exit 0; }
status "skills updated ${cur:0:7} → ${target:0:7} ($n commits, first seen $DAYS+ days ago)"
