#!/usr/bin/env python3
"""
Commit N identical (address, prediction) pairs to log/trials.json as
separate turns — a command-line stopgap for the control panel's
"repeat" feature, until that's built.

This ONLY commits. It never writes an observation — that stays the
job of aeti_batch_runner.py (for API runs) or the control panel (for
manual runs), same predict-before-observe separation as everywhere
else in this pipeline.

Usage:
    python3 aeti_batch_commit.py --label v0.5 --n 9 \
        --address-file address.txt --prediction-file prediction.txt

    # or paste them inline:
    python3 aeti_batch_commit.py --label v0.5 --n 9 \
        --address "You are not a guide..." \
        --prediction "Fragmentary output holds..."
"""

import argparse
import json
import string
import sys
import time
import uuid
from pathlib import Path


def load_trials(path: Path) -> list:
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        content = f.read().strip()
        return json.loads(content) if content else []


def save_trials(path: Path, trials: list) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".json.tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(trials, f, indent=2, ensure_ascii=False)
    tmp.replace(path)


def suffix_for(i: int) -> str:
    """0 -> a, 1 -> b, ... 25 -> z, 26 -> aa, 27 -> ab, ..."""
    letters = string.ascii_lowercase
    if i < 26:
        return letters[i]
    return letters[i // 26 - 1] + letters[i % 26]


def time_now_iso() -> str:
    import datetime
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def main():
    ap = argparse.ArgumentParser(description="Commit N identical turns to trials.json (no observation).")
    ap.add_argument("--file", default="log/trials.json", help="path to trials.json")
    ap.add_argument("--label", required=True, help="base label, e.g. v0.5 -> v0.5a, v0.5b, ...")
    ap.add_argument("--n", type=int, required=True, help="how many identical turns to commit")
    ap.add_argument("--address", help="address text, inline")
    ap.add_argument("--address-file", help="path to a file containing the address text")
    ap.add_argument("--prediction", help="prediction text, inline")
    ap.add_argument("--prediction-file", help="path to a file containing the prediction text")
    ap.add_argument("--dry-run", action="store_true", help="show what would be committed, write nothing")
    args = ap.parse_args()

    address = args.address or (Path(args.address_file).read_text(encoding="utf-8").strip() if args.address_file else None)
    prediction = args.prediction or (Path(args.prediction_file).read_text(encoding="utf-8").strip() if args.prediction_file else None)

    if not address or not prediction:
        print("Need --address or --address-file, and --prediction or --prediction-file.", file=sys.stderr)
        sys.exit(1)

    path = Path(args.file)
    trials = load_trials(path)

    batch_id = uuid.uuid4().hex[:8]
    committed_at = time_now_iso()  # one real action, one honest shared timestamp

    new_turns = []
    for i in range(args.n):
        new_turns.append({
            "label": f"{args.label}{suffix_for(i)}",
            "address": address,
            "prediction": prediction,
            "observation": "",
            "read": "unset",
            "comment": "",
            "committedAt": committed_at,
            "observedAt": None,
            "batchId": batch_id,
        })

    print(f"About to commit {args.n} turn(s):")
    for t in new_turns:
        print(f"  - {t['label']}")

    if args.dry_run:
        print("\n--dry-run: nothing written.")
        return

    trials.extend(new_turns)
    save_trials(path, trials)
    print(f"\nCommitted {args.n} turn(s) to {path} (batchId {batch_id}).")
    print(f"Run: python3 aeti_batch_runner.py --n {args.n}")


if __name__ == "__main__":
    main()
