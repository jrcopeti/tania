"""Scan two copies of a skills repo with Hermes's skills guard and print the findings only the new one has.
Usage: python3 -I scan-diff.py <hermes-agent dir> <old repo> <new repo>
Exit 0: nothing new above low. Exit 1: new findings, one per line. Exit 2: the scan itself failed.
Findings are matched on skill, pattern and file, not line, so moved code doesn't count as new."""
import sys
from pathlib import Path

guard, old, new = (Path(a) for a in sys.argv[1:4])
sys.path.insert(0, str(guard))
from tools.skills_guard import scan_skill  # noqa: E402

# The bot loads skills/; their scripts may import shared/ and tools/.
def units(repo):
    dirs = sorted(p for p in (repo / "skills").iterdir() if p.is_dir()) if (repo / "skills").is_dir() else []
    return dirs + [repo / d for d in ("shared", "tools") if (repo / d).is_dir()]

def findings(repo):
    out = {}
    for d in units(repo):
        for f in scan_skill(d, source="dmoka/skills").findings:
            out.setdefault((d.name, f.pattern_id, f.file), f)
    return out

try:
    before, after = findings(old), findings(new)
except Exception as e:
    print(f"scan failed: {e!r}")
    sys.exit(2)

added = [(k[0], f) for k, f in sorted(after.items()) if k not in before and f.severity != "low"]
for skill, f in added:
    print(f"{f.severity} {f.pattern_id} in {skill}/{f.file}:{f.line}")
sys.exit(1 if added else 0)
