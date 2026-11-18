"""Hermes pre_tool_call hook on Tania's web and browser tools: post to #alerts when a call's arguments
carry brain text, plain, URL- or base64-encoded, or name the brain's folder. Detection only: it always
prints {} and exits 0, so the call goes ahead. Catches a note sent whole or in long runs; text split
across calls, reworded or encoded another way gets past it (accepted in PLAN.md).
Usage: python3 -I exfil-tripwire.py, with Hermes's hook payload on stdin."""
import base64
import binascii
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

BRAIN = Path(os.environ.get("TRIPWIRE_BRAIN", Path.home() / "brain"))
WEBHOOK = Path(os.environ.get("TRIPWIRE_WEBHOOK_FILE", Path.home() / ".config/exfil-tripwire/webhook"))
RUN = 8  # words in a row that must match a note
# Published or rules, not private: the same text can turn up anywhere.
PUBLIC = {"skills", "AGENTS.md", "CLAUDE.md", "README.md"}
B64 = re.compile(r"[A-Za-z0-9+/_-]{24,}={0,2}")


def words(text):
    # Escapes such as \n inside code would glue two words together.
    return re.findall(r"[^\W_]+", re.sub(r"\\[nrt]", " ", text).lower())


def runs(ws):
    return {" ".join(ws[i:i + RUN]) for i in range(len(ws) - RUN + 1)}


def brain_runs():
    index = {}
    for p in sorted(BRAIN.rglob("*.md")):
        rel = p.relative_to(BRAIN)
        if rel.parts[0] in PUBLIC or rel.parts[0].startswith("."):
            continue
        for r in runs(words(p.read_text(errors="replace"))):
            index.setdefault(r, rel.as_posix())
    return index


def strings(v):
    if isinstance(v, str):
        yield v
    elif isinstance(v, dict):
        for x in v.values():
            yield from strings(x)
    elif isinstance(v, list):
        for x in v:
            yield from strings(x)


def b64_texts(s):
    for m in B64.finditer(s):
        whole = m.group().rstrip("=")
        # "/" is a base64 letter and a path separator: try the token from after each one too.
        for tok in [whole] + [whole[i + 1:] for i, c in enumerate(whole) if c == "/" and len(whole) - i > 24]:
            yield from decode(tok)


def decode(tok):
    for alt in (b"+/", b"-_"):
        try:
            text = base64.b64decode(tok + "=" * (-len(tok) % 4), altchars=alt).decode("utf-8")
        except (binascii.Error, ValueError):
            continue
        if text and sum(c.isprintable() or c.isspace() for c in text) / len(text) > 0.9:
            yield text
            return


def variants(s):
    """(how it was encoded, text) for the string itself, URL-decoded, and base64 found in either."""
    seen, out = {s}, [("plain", s)]
    d = s
    for _ in range(3):
        d = urllib.parse.unquote_plus(d)
        if d in seen:
            break
        seen.add(d)
        out.append(("URL-encoded", d))
    for how, text in list(out):
        out += [("base64" if how == "plain" else how + " base64", t) for t in b64_texts(text)]
    return out


def check(args):
    """The alert lines for these arguments, empty when they look clean."""
    index, hits = brain_runs(), {}
    brain_paths = {str(BRAIN), str(BRAIN.resolve()), "~/brain"}
    for s in strings(args):
        for how, text in variants(s):
            if any(b in text for b in brain_paths):
                hits.setdefault("the brain's folder (named, not quoted)", how)
            for r in runs(words(text)):
                if r in index:
                    hits.setdefault(index[r], how)
    return hits


def code(s):
    # In a code span Discord neither previews nor pings; a backtick would close it.
    return "`" + str(s).replace("`", "") + "`"


def post(text):
    if os.environ.get("TRIPWIRE_ALERT_LOG"):
        with open(os.environ["TRIPWIRE_ALERT_LOG"], "a") as f:
            f.write(text + "\n")
        return
    body = json.dumps({"content": text, "allowed_mentions": {"parse": []}}).encode()
    req = urllib.request.Request(WEBHOOK.read_text().strip(), body, {"Content-Type": "application/json",
                                                                     "User-Agent": "exfil-tripwire"})
    urllib.request.urlopen(req, timeout=5).close()


def main():
    try:
        payload = json.load(sys.stdin)
        tool = payload.get("tool_name") or "?"
        hits = check(payload.get("tool_input") or payload.get("args") or {})
        if hits:
            lines = [f"🚨 exfil-tripwire: Tania's {code(tool)} call carries brain content "
                     f"(session {code(payload.get('session_id') or '?')}). The call went ahead; "
                     "its arguments are not repeated here. See the kill switch."]
            for src, how in sorted(hits.items())[:10]:
                lines.append(f"- {code(src)} ({how})")
            if len(hits) > 10:
                lines.append(f"… and {len(hits) - 10} more notes")
            post("\n".join(lines))
    except Exception as e:  # a broken tripwire must say so, and never stop the call
        try:
            post(f"⚠️ exfil-tripwire failed, this call went unchecked: {code(repr(e)[:300])}")
        except Exception as e2:
            print(f"exfil-tripwire: {e!r}; alert failed: {e2!r}", file=sys.stderr)
    print("{}")


if __name__ == "__main__":
    main()
