#!/usr/bin/env python3
"""Validate the structure and invariants of PROGRESS.md.

Usage: python3 scripts/check_progress.py [path/to/PROGRESS.md]

Prints one line per problem and exits 1 if any were found, 0 otherwise.
Standard library only, so it runs wherever python3 does.
"""

import datetime
import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "Current status",
    "Paused session",
    "Review schedule",
    "Gap tracker",
    "Strengths",
    "Session log",
]
STATUS_FIELDS = ["Phase", "Last session", "Next session", "Consecutive reviews"]
TRACKER_MARKS = {"⬜", "✅", "—"}
PLACEHOLDER = "—"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def split_sections(text):
    """Map each '## Heading' to the text below it, with HTML comments removed."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    sections = {}
    for match in re.finditer(r"^## (.+?)\n(.*?)(?=^## |\Z)", text, flags=re.MULTILINE | re.DOTALL):
        sections[match.group(1).strip()] = match.group(2)
    return sections


def table_rows(body):
    """Return the data rows of the first markdown table in body, as lists of cells."""
    lines = [line.strip() for line in body.splitlines() if line.strip().startswith("|")]
    # lines[0] is the header, lines[1] the |---| separator.
    return [[cell.strip() for cell in line.strip("|").split("|")] for line in lines[2:]]


def is_placeholder(row):
    return all(cell in (PLACEHOLDER, "0") for cell in row)


def parse_date(value):
    if not DATE_RE.match(value):
        return None
    try:
        return datetime.date.fromisoformat(value)
    except ValueError:
        return None


def check_status(body):
    errors = []
    fields = dict(re.findall(r"^- \*\*(.+?):\*\*\s*(.*)$", body, flags=re.MULTILINE))
    for name in STATUS_FIELDS:
        if name not in fields:
            errors.append(f"Current status: missing field '{name}'")
    reviews = fields.get("Consecutive reviews")
    if reviews is not None and not reviews.isdigit():
        errors.append(f"Current status: 'Consecutive reviews' must be a non-negative integer, got '{reviews}'")
    return errors


def check_tracker(name, body):
    errors = []
    rows = table_rows(body)
    if not rows:
        errors.append(f"{name}: no topic table")
    for row in rows:
        if len(row) != 6:
            errors.append(f"{name}: row {row} must have 6 columns (#, Topic, Concept, Quiz, Kata, Deep Dive)")
            continue
        for cell in row[2:]:
            if cell not in TRACKER_MARKS:
                errors.append(f"{name}: topic '{row[1]}' has invalid mark '{cell}' (allowed: ⬜ ✅ —)")
    exit_line = re.search(r"^\*\*Phase exit review:\*\*\s*(\S+)", body, flags=re.MULTILINE)
    if not exit_line:
        errors.append(f"{name}: missing '**Phase exit review:**' line")
    elif exit_line.group(1) not in ("⬜", "✅"):
        errors.append(f"{name}: phase exit review mark must be ⬜ or ✅, got '{exit_line.group(1)}'")
    return errors


def check_review_schedule(body):
    errors = []
    for row in table_rows(body):
        if is_placeholder(row):
            continue
        if len(row) != 5:
            errors.append(f"Review schedule: row {row} must have 5 columns")
            continue
        topic, last, interval, nxt, _notes = row
        last_date, next_date = parse_date(last), parse_date(nxt)
        if last_date is None:
            errors.append(f"Review schedule: '{topic}' has invalid Last reviewed '{last}' (want YYYY-MM-DD)")
        if next_date is None:
            errors.append(f"Review schedule: '{topic}' has invalid Next review '{nxt}' (want YYYY-MM-DD)")
        if not interval.isdigit() or int(interval) < 3:
            errors.append(f"Review schedule: '{topic}' interval must be an integer ≥ 3, got '{interval}'")
            continue
        if last_date and next_date and next_date != last_date + datetime.timedelta(days=int(interval)):
            expected = last_date + datetime.timedelta(days=int(interval))
            errors.append(f"Review schedule: '{topic}' Next review {nxt} ≠ Last reviewed + {interval}d ({expected})")
    return errors


def check_gap_tracker(body):
    errors = []
    for row in table_rows(body):
        if is_placeholder(row):
            continue
        if len(row) != 5:
            errors.append(f"Gap tracker: row {row} must have 5 columns")
            continue
        topic, _gap, first_seen, consecutive, since = row
        if parse_date(first_seen) is None:
            errors.append(f"Gap tracker: '{topic}' has invalid First seen '{first_seen}' (want YYYY-MM-DD)")
        if consecutive not in ("0", "1"):
            errors.append(f"Gap tracker: '{topic}' Consecutive correct must be 0 or 1 (rows reaching 2 are deleted), got '{consecutive}'")
        if not since.isdigit():
            errors.append(f"Gap tracker: '{topic}' Reviews since last seen must be a non-negative integer, got '{since}'")
    return errors


def check_session_log(body):
    errors = []
    for row in table_rows(body):
        if is_placeholder(row):
            continue
        if parse_date(row[0]) is None:
            errors.append(f"Session log: invalid date '{row[0]}' (want YYYY-MM-DD)")
    return errors


def check(text):
    sections = split_sections(text)
    errors = [f"missing section '## {name}'" for name in REQUIRED_SECTIONS if name not in sections]
    trackers = {name: body for name, body in sections.items() if re.fullmatch(r"Phase \d+ tracker", name)}
    if not trackers:
        errors.append("missing section '## Phase N tracker'")
    if "Current status" in sections:
        errors += check_status(sections["Current status"])
    for name, body in trackers.items():
        errors += check_tracker(name, body)
    if "Review schedule" in sections:
        errors += check_review_schedule(sections["Review schedule"])
    if "Gap tracker" in sections:
        errors += check_gap_tracker(sections["Gap tracker"])
    if "Session log" in sections:
        errors += check_session_log(sections["Session log"])
    return errors


def main(argv):
    path = Path(argv[1]) if len(argv) > 1 else Path(__file__).resolve().parent.parent / "PROGRESS.md"
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"cannot read {path}: {exc}")
        return 1
    errors = check(text)
    for error in errors:
        print(error)
    if not errors:
        print(f"{path.name}: OK")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
