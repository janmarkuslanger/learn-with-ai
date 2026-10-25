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

REQUIRED_SECTIONS = ["Current status", "Paused session", "Review schedule", "Gap tracker", "Strengths", "Session log"]
STATUS_FIELDS = ["Phase", "Last session", "Next session", "Consecutive reviews"]
TRACKER_MARKS = {"⬜", "✅", "—"}


def split_sections(text):
    """Map each '## Heading' to the text below it, with HTML comments removed."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    return {
        m.group(1).strip(): m.group(2)
        for m in re.finditer(r"^## (.+?)\n(.*?)(?=^## |\Z)", text, flags=re.MULTILINE | re.DOTALL)
    }


def table_rows(section, body, columns, errors, skip_placeholder=True):
    """Yield the data rows of the first table in body that have the expected column count.

    Rows of only '—'/'0' (the empty-table placeholder) are skipped; malformed rows are reported.
    """
    lines = [line.strip() for line in body.splitlines() if line.strip().startswith("|")]
    for line in lines[2:]:  # skip header and |---| separator
        row = [cell.strip() for cell in line.strip("|").split("|")]
        if skip_placeholder and all(cell in ("—", "0") for cell in row):
            continue
        if len(row) != columns:
            errors.append(f"{section}: row {row} must have {columns} columns")
            continue
        yield row


def parse_date(value):
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return None
    try:
        return datetime.date.fromisoformat(value)
    except ValueError:
        return None


def check_status(body, errors):
    fields = dict(re.findall(r"^- \*\*(.+?):\*\*\s*(.*)$", body, flags=re.MULTILINE))
    errors += [f"Current status: missing field '{name}'" for name in STATUS_FIELDS if name not in fields]
    reviews = fields.get("Consecutive reviews")
    if reviews is not None and not reviews.isdigit():
        errors.append(f"Current status: 'Consecutive reviews' must be a non-negative integer, got '{reviews}'")


def check_tracker(name, body, errors):
    rows = list(table_rows(name, body, 6, errors, skip_placeholder=False))
    if not rows:
        errors.append(f"{name}: no topic table")
    for row in rows:
        errors += [
            f"{name}: topic '{row[1]}' has invalid mark '{cell}' (allowed: ⬜ ✅ —)"
            for cell in row[2:]
            if cell not in TRACKER_MARKS
        ]
    exit_line = re.search(r"^\*\*Phase exit review:\*\*\s*(\S+)", body, flags=re.MULTILINE)
    if not exit_line:
        errors.append(f"{name}: missing '**Phase exit review:**' line")
    elif exit_line.group(1) not in ("⬜", "✅"):
        errors.append(f"{name}: phase exit review mark must be ⬜ or ✅, got '{exit_line.group(1)}'")


def check_review_schedule(body, errors):
    for topic, last, interval, nxt, _notes in table_rows("Review schedule", body, 5, errors):
        last_date, next_date = parse_date(last), parse_date(nxt)
        if last_date is None:
            errors.append(f"Review schedule: '{topic}' has invalid Last reviewed '{last}' (want YYYY-MM-DD)")
        if next_date is None:
            errors.append(f"Review schedule: '{topic}' has invalid Next review '{nxt}' (want YYYY-MM-DD)")
        if not interval.isdigit() or int(interval) < 3:
            errors.append(f"Review schedule: '{topic}' interval must be an integer ≥ 3, got '{interval}'")
        elif last_date and next_date:
            expected = last_date + datetime.timedelta(days=int(interval))
            if next_date != expected:
                errors.append(f"Review schedule: '{topic}' Next review {nxt} ≠ Last reviewed + {interval}d ({expected})")


def check_gap_tracker(body, errors):
    for topic, _gap, first_seen, consecutive, since in table_rows("Gap tracker", body, 5, errors):
        if parse_date(first_seen) is None:
            errors.append(f"Gap tracker: '{topic}' has invalid First seen '{first_seen}' (want YYYY-MM-DD)")
        if consecutive not in ("0", "1"):
            errors.append(f"Gap tracker: '{topic}' Consecutive correct must be 0 or 1 (rows reaching 2 are deleted), got '{consecutive}'")
        if not since.isdigit():
            errors.append(f"Gap tracker: '{topic}' Reviews since last seen must be a non-negative integer, got '{since}'")


def check_session_log(body, errors):
    for row in table_rows("Session log", body, 4, errors):
        if parse_date(row[0]) is None:
            errors.append(f"Session log: invalid date '{row[0]}' (want YYYY-MM-DD)")


def check(text):
    sections = split_sections(text)
    errors = [f"missing section '## {name}'" for name in REQUIRED_SECTIONS if name not in sections]
    trackers = {name: body for name, body in sections.items() if re.fullmatch(r"Phase \d+ tracker", name)}
    if not trackers:
        errors.append("missing section '## Phase N tracker'")
    for name, body in trackers.items():
        check_tracker(name, body, errors)
    checks = {
        "Current status": check_status,
        "Review schedule": check_review_schedule,
        "Gap tracker": check_gap_tracker,
        "Session log": check_session_log,
    }
    for name, run in checks.items():
        if name in sections:
            run(sections[name], errors)
    return errors


def main(argv):
    path = Path(argv[1]) if len(argv) > 1 else Path(__file__).resolve().parent.parent / "PROGRESS.md"
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"cannot read {path}: {exc}")
        return 1
    errors = check(text)
    print("\n".join(errors) if errors else f"{path.name}: OK")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
