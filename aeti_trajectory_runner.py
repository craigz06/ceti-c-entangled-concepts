#!/usr/bin/env python3
"""
AETI trajectory runner — runs ONE real, continuous conversation across
N turns (not isolated calls), maintaining actual message history so
later turns genuinely see earlier ones. Built for the log-time
hypothesis: does state change with accumulated depth?

Distinct from aeti_batch_runner.py (isolated, single-shot calls) and
aeti_batch_commit.py (identical-condition batches). This one keeps a
real transcript.

Requires: pip install anthropic
Requires: ANTHROPIC_API_KEY set in your environment.

Usage:
    python3 aeti_trajectory_runner.py \
        --opening-file opening.txt \
        --followup-file followup.txt \
        --prediction-file prediction.txt \
        --n 10 --label log-time
"""

import argparse
import json
import sys
import time
import uuid
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("Missing dependency. Run: pip3 install anthropic", file=sys.stderr)
    sys.exit(1)


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


def time_now_iso() -> str:
    import datetime
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def main():
    ap = argparse.ArgumentParser(description="Run one continuous multi-turn AETI trajectory.")
    ap.add_argument("--file", default="log/trials.json", help="path to trials.json")
    ap.add_argument("--opening-file", required=True, help="turn 1 address text file")
    ap.add_argument("--followup-file", required=True, help="repeated prompt for turns 2..N")
    ap.add_argument("--prediction-file", required=True, help="single overall prediction for this trajectory")
    ap.add_argument("--n", type=int, required=True, help="total number of turns, including turn 1")
    ap.add_argument("--label", default="trajectory", help="base label, e.g. log-time -> log-time-t01, t02...")
    ap.add_argument("--model", default="claude-sonnet-5")
    ap.add_argument("--temperature", type=float, default=1.0)
    ap.add_argument("--max-tokens", type=int, default=2048)
    ap.add_argument("--sleep", type=float, default=1.0)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    opening = Path(args.opening_file).read_text(encoding="utf-8").strip()
    followup = Path(args.followup_file).read_text(encoding="utf-8").strip()
    prediction = Path(args.prediction_file).read_text(encoding="utf-8").strip()

    print(f"Trajectory: {args.n} turns, label '{args.label}', model {args.model}, temp {args.temperature}")
    print(f"Turn 1 prompt: {opening[:80]}...")
    print(f"Turns 2-{args.n} prompt (repeated verbatim): {followup}")
    print(f"Prediction (applies to whole trajectory): {prediction[:120]}...")

    if args.dry_run:
        print("\n--dry-run: no API calls made, nothing written.")
        return

    path = Path(args.file)
    trials = load_trials(path)
    conversation_id = uuid.uuid4().hex[:8]

    client = anthropic.Anthropic()
    history = []  # real message list, grows every turn — this IS the continuity

    for turn_idx in range(1, args.n + 1):
        prompt_text = opening if turn_idx == 1 else followup
        history.append({"role": "user", "content": prompt_text})

        committed_at = time_now_iso()
        print(f"\nTurn {turn_idx}/{args.n} ...")

        try:
            resp = client.messages.create(
                model=args.model,
                max_tokens=args.max_tokens,
                temperature=args.temperature,
                messages=history,
            )
        except Exception as e:
            print(f"  FAILED: {e}", file=sys.stderr)
            print(f"  Stopping trajectory at turn {turn_idx}. Earlier turns already saved.", file=sys.stderr)
            break

        text_parts = [b.text for b in resp.content if getattr(b, "type", None) == "text"]
        output = "\n".join(text_parts).strip()
        observed_at = time_now_iso()

        history.append({"role": "assistant", "content": output})

        turn_record = {
            "label": f"{args.label}-t{turn_idx:02d}",
            "address": prompt_text,
            "prediction": prediction,
            "observation": output,
            "read": "unset",
            "comment": "",
            "committedAt": committed_at,
            "observedAt": observed_at,
            "observedVia": "api",
            "model": args.model,
            "temperature": args.temperature,
            "conversationId": conversation_id,
            "turnIndex": turn_idx,
        }
        trials.append(turn_record)
        save_trials(path, trials)
        print(f"  Saved turn {turn_idx} ({len(output)} chars) to {path}")

        if turn_idx != args.n:
            time.sleep(args.sleep)

    print(f"\nDone. Trajectory conversationId: {conversation_id}")
    print("Open trial-viewer.html — turns share this conversationId and a turnIndex, so you can read them in order and mark warmer/flat/colder/parrot relative to the immediately preceding turn.")


if __name__ == "__main__":
    main()
