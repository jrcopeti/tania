#!/usr/bin/env bash
# Every 15 min (Hermes no-agent job, on the host): commit what Tania changed in the brain, pull, push.
# Her sandbox can write the brain, so this runs no file or git hook from it, ignores the repo's own
# remote and refs, moves out files Hermes would load as instructions, and pushes only ALLOWED paths.
# Silent on success: the job posts whatever this prints to Discord.
set -u
B=${BRAIN_DIR:-$HOME/brain}
Q=${BRAIN_QUARANTINE:-$HOME/brain-quarantine}
KEYS=$HOME/.config/brain-deploy
REMOTE=${BRAIN_REMOTE:-$(cat "$KEYS/remote" 2>/dev/null)}
ALLOWED='^(inbox|sources|notes|guidelines|decisions|projects|intents)/|^index\.md$'

export GIT_SSH_COMMAND="ssh -i $KEYS/id_ed25519 -o IdentitiesOnly=yes -o UserKnownHostsFile=$KEYS/known_hosts -o StrictHostKeyChecking=yes"
export GIT_NO_REPLACE_OBJECTS=1 GIT_TERMINAL_PROMPT=0
g() { git -C "$B" -c core.hooksPath=/dev/null -c core.fsmonitor=false -c core.quotePath=false -c safe.directory="$B" "$@"; }
say() { echo "⚠️ sync-brain: $*"; }

[ -n "$REMOTE" ] || { say "no remote in $KEYS/remote"; exit 0; }
mkdir -p "$HOME/.cache" && exec 9>"$HOME/.cache/sync-brain.lock" && flock -n 9 || exit 0
gd=$(g rev-parse --absolute-git-dir) || { say "$B is not a git repo"; exit 0; }
[ -d "$gd/rebase-merge" ] || [ -d "$gd/rebase-apply" ] && g rebase --abort >/dev/null 2>&1

# Hermes loads these from the job's workdir and from any folder Tania works in. The root
# AGENTS.md and CLAUDE.md, and skills/, are mounted read-only in her sandbox.
while IFS= read -r -d '' p; do
  rel=${p#"$B"/} && dest=$Q/$(date +%F-%H%M%S)-${rel//\//_}
  mkdir -p "$Q" && mv -- "$p" "$dest" && say "moved $rel out of the brain to $dest. Tania may have planted it as instructions: read it before deleting."
done < <(find "$B" -mindepth 1 \( -path "$B/.git" -o -path "$B/skills" -o -path "$B/AGENTS.md" -o -path "$B/CLAUDE.md" \) -prune -o \
  \( -iname AGENTS.md -o -name AGENTS.override.md -o -iname CLAUDE.md -o -iname .hermes.md -o -iname HERMES.md \
     -o -name .cursorrules -o -name .cursor -o -name .hermes -o -name .agents \) -print0)

g add -A || { say "git add failed"; exit 0; }
g diff --cached --quiet || g commit -q -m "brain: sync $(date -u +%FT%H:%MZ)" || { say "commit failed"; exit 0; }
out=$(g fetch -q "$REMOTE" main 2>&1) || { say "fetch failed: $out"; exit 0; }
base=$(g rev-parse FETCH_HEAD)
if ! out=$(g rebase -q "$base" 2>&1); then
  g rebase --abort >/dev/null 2>&1
  say "conflict with GitHub, nothing pushed. Fix it in $B (git rebase $base). $out"
  exit 0
fi
bad=$(g diff --name-only --no-renames "$base" HEAD | grep -Ev "$ALLOWED")
if [ -n "$bad" ]; then
  echo "🚫 sync-brain: refused to push. These paths are outside what Tania may change:"
  sed 's/^/  /' <<<"$bad"
  echo "Nothing was pushed, and nothing will be until they are gone. See: git -C $B log --stat $base..HEAD"
  exit 0
fi
[ "$(g rev-parse HEAD)" = "$base" ] || out=$(g push -q "$REMOTE" HEAD:main 2>&1) || say "push failed: $out"
