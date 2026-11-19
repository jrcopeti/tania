#!/usr/bin/env bash
# Tests for tripwire-health.sh with a fake hermes and a temp state folder.
# Run: bash vps/telma/test-tripwire-health.sh
set -u
SCRIPT=$(cd "$(dirname "$0")" && pwd)/tripwire-health.sh
T=$(mktemp -d)
trap 'rm -rf "$T"' EXIT
pass=0 fail=0

allowed="    - /usr/bin/python3 -I /home/agent/.hermes/agent-hooks/exfil-tripwire.py matcher='web_.*' (timeout=15s, ✓ allowed)"
setup() {
  rm -rf "$T/st" && mkdir -p "$T/st" && echo 'https://discord.example/api/webhooks/1/x' > "$T/webhook"
  printf '#!/bin/sh\ncat "%s"\n' "$T/hooks" > "$T/hermes" && chmod +x "$T/hermes" && echo "$allowed" > "$T/hooks"
}
run() { out=$(TRIPWIRE_STATE=$T/st TRIPWIRE_WEBHOOK_FILE=$T/webhook HERMES=$T/hermes bash "$SCRIPT" 2>&1); }
check() { local name=$1; shift; if "$@"; then echo "ok   $name"; pass=$((pass + 1)); else echo "FAIL $name"; echo "     output: ${out:-<none>}"; fail=$((fail + 1)); fi; }
says() { grep -qF -- "$1" <<<"$out"; }

setup; run
check "all well: silent" eval '[ -z "$out" ]'

setup; : > "$T/webhook"; run
check "an empty webhook file is reported" eval 'says "missing or empty"'

setup; rm "$T/webhook"; run
check "a missing webhook file is reported" eval 'says "missing or empty"'

setup; echo "${allowed/✓ allowed/✗ not allowlisted}" > "$T/hooks"; run
check "a hook not approved is reported" eval 'says "not configured and approved"'

setup; echo "    - /home/agent/.hermes/agent-hooks/guard-network.sh matcher='terminal' (timeout=10s, ✓ allowed)" > "$T/hooks"; run
check "a hook gone from the config is reported" eval 'says "not configured and approved"'

setup; printf 'fail one\nfail two\n' > "$T/st/failed.log"; run
check "failures are reported with the last one" eval 'says "2 tripwire failure(s)" && says "Last: fail two"'
run
check "and only once" eval '[ -z "$out" ] && [ "$(grep -c "" "$T/st/failed.log.seen")" = 2 ]'

echo "$pass passed, $fail failed"
[ "$fail" = 0 ]
