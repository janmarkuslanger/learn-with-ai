import unittest
from pathlib import Path

from check_progress import check

TEMPLATE = (Path(__file__).resolve().parent.parent / "PROGRESS.md").read_text(encoding="utf-8")

FILLED = """# Progress

## Current status

- **Phase:** 1
- **Last session:** 2026-10-20 (drill)
- **Next session:** Quiz: Event Sourcing
- **Consecutive reviews:** 1

## Paused session

_None._

## Phase 1 tracker

| # | Topic | Concept | Quiz | Kata | Deep Dive |
|---|---|---|---|---|---|
| 1 | CQRS | ✅ | ✅ | ✅ | — |
| 2 | Event Sourcing | ✅ | ⬜ | — | ⬜ |

**Phase exit review:** ⬜

## Review schedule

| Topic | Last reviewed | Interval (days) | Next review | Notes |
|---|---|---|---|---|
| CQRS | 2026-10-20 | 14 | 2026-11-03 | |

## Gap tracker

| Topic | Gap | First seen | Consecutive correct | Reviews since last seen |
|---|---|---|---|---|
| CQRS | read model sync (confident error) | 2026-10-13 | 1 | 0 |

## Strengths

_None yet._

## Session log

| Date | Type | Topic | Notes |
|---|---|---|---|
| 2026-10-20 | drill | CQRS | |
"""


class CheckProgressTest(unittest.TestCase):
    def test_shipped_template_is_valid(self):
        self.assertEqual(check(TEMPLATE), [])

    def test_filled_progress_is_valid(self):
        self.assertEqual(check(FILLED), [])

    def test_missing_section_is_reported(self):
        errors = check(FILLED.replace("## Strengths", "## Strong points"))
        self.assertIn("missing section '## Strengths'", errors)

    def test_missing_phase_tracker_is_reported(self):
        errors = check(FILLED.replace("## Phase 1 tracker", "## Tracker"))
        self.assertIn("missing section '## Phase N tracker'", errors)

    def test_missing_status_field_is_reported(self):
        errors = check(FILLED.replace("- **Last session:** 2026-10-20 (drill)\n", ""))
        self.assertIn("Current status: missing field 'Last session'", errors)

    def test_non_numeric_consecutive_reviews_is_reported(self):
        errors = check(FILLED.replace("**Consecutive reviews:** 1", "**Consecutive reviews:** two"))
        self.assertEqual(len(errors), 1)
        self.assertIn("Consecutive reviews", errors[0])

    def test_invalid_tracker_mark_is_reported(self):
        errors = check(FILLED.replace("| 1 | CQRS | ✅ | ✅ | ✅ | — |", "| 1 | CQRS | ✅ | done | ✅ | — |"))
        self.assertEqual(len(errors), 1)
        self.assertIn("invalid mark 'done'", errors[0])

    def test_missing_phase_exit_line_is_reported(self):
        errors = check(FILLED.replace("**Phase exit review:** ⬜\n", ""))
        self.assertIn("Phase 1 tracker: missing '**Phase exit review:**' line", errors)

    def test_next_review_must_match_interval(self):
        errors = check(FILLED.replace("| 14 | 2026-11-03 |", "| 14 | 2026-11-04 |"))
        self.assertEqual(len(errors), 1)
        self.assertIn("2026-11-03", errors[0])

    def test_interval_below_three_days_is_reported(self):
        errors = check(FILLED.replace("| 14 | 2026-11-03 |", "| 1 | 2026-10-21 |"))
        self.assertEqual(len(errors), 1)
        self.assertIn("interval must be an integer ≥ 3", errors[0])

    def test_impossible_date_is_reported(self):
        errors = check(FILLED.replace("| 2026-10-20 | 14 |", "| 2026-02-30 | 14 |"))
        self.assertTrue(any("invalid Last reviewed '2026-02-30'" in e for e in errors))

    def test_gap_with_two_consecutive_correct_must_be_deleted(self):
        errors = check(FILLED.replace("| 2026-10-13 | 1 | 0 |", "| 2026-10-13 | 2 | 0 |"))
        self.assertEqual(len(errors), 1)
        self.assertIn("rows reaching 2 are deleted", errors[0])

    def test_session_log_date_format_is_checked(self):
        errors = check(FILLED.replace("| 2026-10-20 | drill |", "| 20.10.2026 | drill |"))
        self.assertEqual(errors, ["Session log: invalid date '20.10.2026' (want YYYY-MM-DD)"])

    def test_tables_inside_comments_are_ignored(self):
        commented = FILLED.replace("## Strengths\n", "## Strengths\n<!-- | a | b |\n|---|---|\n| x | y | -->\n")
        self.assertEqual(check(commented), [])


if __name__ == "__main__":
    unittest.main()
