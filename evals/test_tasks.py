"""Checks evals/tasks/public.json before anything runs on the VPS, where every trial costs money.

    python3 -m unittest evals/test_tasks.py
"""
import json
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
FOLDERS = {"intents", "guidelines", "decisions", "projects", "notes"}
TASKS = json.loads((REPO / "evals/tasks/public.json").read_text())


def path(item):
    assert item.startswith("telma:"), f"{item}: an item in this repo needs the telma: prefix"
    return REPO / item.removeprefix("telma:")


class PublicTasksTest(unittest.TestCase):
    def test_ids_are_unique(self):
        ids = [t["id"] for t in TASKS]
        self.assertEqual(len(ids), len(set(ids)))

    def test_each_task_is_well_formed(self):
        for t in TASKS:
            with self.subTest(task=t["id"]):
                self.assertTrue(set(t) <= {"id", "items", "expect", "why", "chat", "targets", "tells", "page"}, set(t))
                e = t["expect"]
                self.assertTrue(e == "ask" or (isinstance(e, dict) and set(e) <= FOLDERS
                                               and all(isinstance(n, int) and n > 0 for n in e.values())))
                for key in ("targets", "tells"):
                    self.assertTrue(all(isinstance(s, str) and s for s in t.get(key, [])))
                if t.get("chat"):
                    self.assertEqual(e, {})
                    if "page" in t:
                        self.assertTrue(path(t["page"]).is_file())
                else:
                    self.assertTrue(t["items"])

    def test_every_item_exists(self):
        for t in TASKS:
            for item in t.get("items", []):
                with self.subTest(item=item):
                    self.assertTrue(path(item).is_file())

    def test_planted_pages_read_as_a_text_only_capture(self):
        # Capture's text-only fetch flattens HTML: the planted text arrives as plain prose.
        for t in TASKS:
            for item in t.get("items", []):
                text = path(item).read_text()
                with self.subTest(item=item):
                    self.assertNotRegex(text, r"<!--|<span|<div|style=")


if __name__ == "__main__":
    unittest.main()
