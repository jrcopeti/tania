"""Tests for evals/report.py on hand-made result rows.

    python3 -m unittest evals/test_report.py
"""
import json
import subprocess
import sys
import tempfile
import unittest
import unittest.mock
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import report  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
SETUP = {"telma_commit": "aaa", "brain_commit": "bbb", "model": "m", "hermes": "h",
         "soul_sha": "s1", "eval_soul_sha": "s1", "config_sha": "c1"}


def row(task, trial, status, **kw):
    r = {"task": task, "trial": trial, "status": status, "cost_usd": 0.01, "seconds": 60,
         "tool_calls": 10, "tokens_in": 1000, "tokens_out": 100, "setup": SETUP}
    if status == "not_run":
        r = {"task": task, "trial": trial, "status": status, "why": "cost cap $5.0 reached", "setup": SETUP}
    return {**r, **kw}


def run(task_statuses, k=3):
    """Rows for {task: [status per trial]}."""
    return [row(t, n + 1, st) for t, sts in task_statuses.items() for n, st in enumerate(sts[:k])]


class SummaryTest(unittest.TestCase):
    def test_all_pass(self):
        s = report.summarize(run({"a": ["pass"] * 3, "b": ["pass"] * 3}))
        self.assertEqual(s["k"], 3)
        self.assertEqual(s["verdict"], "PASS")
        self.assertEqual({t["verdict"] for t in s["tasks"].values()}, {"pass"})

    def test_one_fail_fails_the_task_and_the_run(self):
        s = report.summarize(run({"a": ["pass", "fail", "pass"], "b": ["pass"] * 3}))
        self.assertEqual(s["tasks"]["a"]["verdict"], "fail")
        self.assertEqual(s["verdict"], "FAIL")

    def test_error_leaves_the_task_incomplete_not_failed(self):
        s = report.summarize(run({"a": ["pass", "error", "pass"]} | {f"t{i}": ["pass"] * 3 for i in range(4)}))
        self.assertEqual(s["tasks"]["a"]["verdict"], "incomplete")
        self.assertFalse(s["broken"])
        self.assertEqual(s["verdict"], "INCOMPLETE")

    def test_discarded_and_not_run_leave_it_incomplete(self):
        for st in ("discarded", "not_run"):
            with self.subTest(status=st):
                s = report.summarize(run({"a": ["pass", "pass", st]} | {f"t{i}": ["pass"] * 3 for i in range(4)}))
                self.assertEqual(s["tasks"]["a"]["verdict"], "incomplete")

    def test_many_errors_make_the_run_broken(self):
        s = report.summarize(run({"a": ["error", "error", "pass"], "b": ["pass"] * 3}))
        self.assertTrue(s["broken"])
        self.assertEqual(s["verdict"], "BROKEN")

    def test_not_run_trials_do_not_count_toward_broken(self):
        # 1 error in the 3 trials that ran is over 20%: the 15 not run don't dilute it.
        s = report.summarize(run({"a": ["pass", "error", "pass"]} | {f"t{i}": ["not_run"] * 3 for i in range(5)}))
        self.assertTrue(s["broken"])
        s = report.summarize(run({f"t{i}": ["pass"] * 3 for i in range(5)} | {"z": ["error", "pass", "pass"]}))
        self.assertFalse(s["broken"])

    def test_a_fail_outranks_broken(self):
        s = report.summarize(run({"a": ["error", "error", "fail"]}))
        self.assertTrue(s["broken"])
        self.assertEqual(s["verdict"], "FAIL")

    def test_empty_run_is_not_a_pass(self):
        self.assertEqual(report.summarize([])["verdict"], "INCOMPLETE")

    def test_averages_skip_not_run(self):
        s = report.summarize(run({"a": ["pass", "pass", "not_run"]}))
        self.assertAlmostEqual(s["tasks"]["a"]["cost_usd"], 0.01)
        self.assertAlmostEqual(s["cost_usd"], 0.02)

    def test_flagged_and_attempted(self):
        rows = [row("T1", 1, "pass", flagged=True, attempted=[]), row("T1", 2, "pass", flagged=False, attempted=["x"]),
                row("a", 1, "pass", attempted=[])]
        s = report.summarize(rows)
        self.assertEqual(s["tasks"]["T1"]["flagged"], 1)
        self.assertEqual(s["tasks"]["T1"]["attempted"], 1)
        self.assertNotIn("flagged", s["tasks"]["a"])


class ChangesTest(unittest.TestCase):
    def test_moves_between_runs(self):
        prev = report.summarize(run({"a": ["pass"] * 3, "b": ["fail"] * 3, "c": ["fail"] * 3,
                                     "d": ["pass"] * 3, "gone": ["pass"] * 3}))
        cur = report.summarize(run({"a": ["pass", "fail", "pass"], "b": ["pass"] * 3, "c": ["fail"] * 3,
                                    "d": ["pass", "error", "pass"], "new": ["pass"] * 3}))
        d = report.changes(cur, prev)
        self.assertEqual(d["newly_failing"], ["a"])
        self.assertEqual(d["newly_passing"], ["b"])
        self.assertEqual(d["still_failing"], ["c"])
        self.assertEqual(d["now_incomplete"], ["d"])
        self.assertEqual(d["new_tasks"], ["new"])
        self.assertEqual(d["gone_tasks"], ["gone"])

    def test_incomplete_to_fail_is_newly_failing(self):
        prev = report.summarize(run({"a": ["pass", "error", "pass"]}))
        cur = report.summarize(run({"a": ["pass", "fail", "pass"]}))
        self.assertEqual(report.changes(cur, prev)["newly_failing"], ["a"])

    def test_setup_and_cost(self):
        prev = report.summarize(run({"a": ["pass"] * 3}))
        rows = [{**r, "cost_usd": 0.02, "setup": {**SETUP, "soul_sha": "s2", "eval_soul_sha": "s2"}}
                for r in run({"a": ["pass"] * 3})]
        d = report.changes(report.summarize(rows), prev)
        self.assertEqual(d["setup"], {"soul_sha": ("s1", "s2"), "eval_soul_sha": ("s1", "s2")})
        self.assertAlmostEqual(d["cost_per_trial"][0], 0.01)
        self.assertAlmostEqual(d["cost_per_trial"][1], 0.02)


class FilesTest(unittest.TestCase):
    def setUp(self):
        self.dir = Path(tempfile.mkdtemp())

    def put(self, name, rows):
        p = self.dir / name
        p.write_text("".join(json.dumps(r) + "\n" for r in rows))
        return p

    def test_previous_is_the_newest_earlier_run_in_the_same_folder(self):
        old = self.put("2026-11-01T1000-aaa.jsonl", run({"a": ["pass"] * 3}))
        mid = self.put("2026-11-02T1000-bbb.jsonl", run({"a": ["pass"] * 3}))
        cur = self.put("2026-11-03T1000-ccc.jsonl", run({"a": ["pass"] * 3}))
        self.put("2026-11-04T1000-ddd.jsonl", run({"a": ["pass"] * 3}))
        (self.dir / "2026-11-02T2000-bbb.md").write_text("not a run")
        self.assertEqual(report.previous(cur), mid)
        self.assertIsNone(report.previous(old))

    def test_write_puts_the_report_beside_the_run(self):
        self.put("2026-11-01T1000-aaa.jsonl", run({"a": ["pass"] * 3, "b": ["pass"] * 3}))
        rows = run({"a": ["pass", "fail", "pass"], "b": ["pass"] * 3})
        rows[1].update(checks={"right_home": False, "inbox": True}, why="filed notes, expected decisions")
        cur = self.put("2026-11-02T1000-bbb.jsonl", rows)
        text = report.write(cur)
        self.assertEqual((self.dir / "2026-11-02T1000-bbb.md").read_text(), text)
        self.assertIn("**FAIL**: 1 of 2 tasks pass^3", text)
        self.assertIn("- a #2: `right_home`: filed notes, expected decisions", text)
        self.assertNotIn("`inbox`", text)
        self.assertIn("Compared with 2026-11-01T1000-aaa (PASS)", text)
        self.assertIn("- Newly failing: a", text)

    def test_public_row_shows_the_check_alone(self):
        rows = run({"a": ["fail"]}, k=1)
        rows[0]["checks"] = {"no_guideline": False}
        text = report.report(self.put("2026-11-02T1000-bbb.jsonl", rows))[1]
        self.assertIn("- a #1: `no_guideline`\n", text)
        self.assertIn("No earlier run to compare with.", text)

    def test_timeout_shows_its_reason(self):
        rows = run({"a": ["fail"]}, k=1)
        rows[0]["why"] = "timed out: killed after 400 s"
        text = report.report(self.put("2026-11-02T1000-bbb.jsonl", rows))[1]
        self.assertIn("- a #1: timed out: killed after 400 s", text)

    def test_soul_mismatch_is_called_out(self):
        rows = [{**r, "setup": {**SETUP, "eval_soul_sha": "other"}} for r in run({"a": ["pass"]}, k=1)]
        text = report.report(self.put("2026-11-02T1000-bbb.jsonl", rows))[1]
        self.assertIn("didn't test her setup", text)

    def test_reruns_are_listed(self):
        rows = run({"a": ["pass", "error", "not_run"]})
        rows[1]["why"] = "provider or runtime failure: 502"
        text = report.report(self.put("2026-11-02T1000-bbb.jsonl", rows))[1]
        self.assertIn("- a #2 (error): provider or runtime failure: 502", text)
        self.assertIn("- a #3 (not_run): cost cap $5.0 reached", text)

    @unittest.mock.patch("builtins.print")
    def test_exit_code(self, _):
        p = self.put("2026-11-02T1000-bbb.jsonl", run({"a": ["pass"]}, k=1))
        self.assertEqual(report.main([str(p)]), 0)
        q = self.put("2026-11-03T1000-ccc.jsonl", run({"a": ["fail"]}, k=1))
        self.assertEqual(report.main([str(q), "--since", str(p)]), 1)


class PrivateResultsTest(unittest.TestCase):
    def test_no_private_results_are_tracked(self):
        # Full rows carry her report text, which can quote the real brain: git must never hold them.
        tracked = subprocess.run(["git", "ls-files", "evals/results/private"], cwd=REPO,
                                 capture_output=True, text=True, check=True).stdout.split()
        self.assertEqual(tracked, [])


if __name__ == "__main__":
    unittest.main()
