#!/usr/bin/env bash
# Every 15 min (Hermes no-agent job on Telma, on the host): say when the exfil tripwire can't alert.
# Its alerts go to #alerts through a webhook; when that fails, only its local log knows. Also says
# when the hook is no longer in Hermes's config or approved. Silent when all is well.
set -u
STATE=${TRIPWIRE_STATE:-$HOME/.local/state/exfil-tripwire}
WEBHOOK=${TRIPWIRE_WEBHOOK_FILE:-$HOME/.config/exfil-tripwire/webhook}
HERMES=${HERMES:-$(command -v hermes || echo "$HOME/.local/bin/hermes")}
say() { echo "⚠️ tripwire-health: $*"; }

[ -s "$WEBHOOK" ] || say "the webhook file $WEBHOOK is missing or empty: tripwire alerts can't reach #alerts."
hooks=$("$HERMES" hooks list 2>&1)
grep -F 'exfil-tripwire.py' <<<"$hooks" | grep -qF '✓ allowed' ||
  say "the exfil-tripwire hook is not configured and approved (hermes hooks list): web calls go unwatched."
if [ -s "$STATE/failed.log" ]; then
  n=$(grep -c '' "$STATE/failed.log")
  say "$n tripwire failure(s) since the last check. Last: $(tail -n 1 "$STATE/failed.log")"
  say "Alerts it found are in $STATE/alerts.log."
  cat "$STATE/failed.log" >> "$STATE/failed.log.seen" && : > "$STATE/failed.log"
fi
exit 0
