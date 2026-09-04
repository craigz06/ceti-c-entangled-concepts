#!/usr/bin/env python3
"""
AETI batch runner — fulfills committed predictions via the Anthropic API.

Respects the predict-before-observe discipline: this script never writes
a prediction. It only looks for turns in log/trials.json that already
have a committed prediction (committedAt set) and no observation yet
(observedAt is null), sends the address as a fresh, isolated API call —
no system prompt, no conversation history, no memory — and writes the
result back.

Requires: pip install anthropic
Requires: ANTHROPIC_API_KEY set in your environment.

Usage:
    python3 aeti_batch_runner.py                       # process all pending turns
    python3 aeti_batch_runner.py --n 1                  # process only the next one
    python3 aeti_batch_runner.py --model claude-sonnet-5 --temperature 1.0
    python3 aeti_batch_runner.py --file log/trials.json --sleep 2
    python3 aeti_batch_runner.py --dry-run              # show what would run, don't call the API
"""

import argparse
import json
import sys
import time
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("Missing dependency. Run: pip3 install anthropic", file=sys.stderr)
    sys.exit(1)


def load_trials(path: Path) -> list:
    if not path.exists():
        print(f"No file at {path} — nothing to run.", file=sys.stderr)
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_trials(path: Path, trials: list) -> None:
    tmp = path.with_suffix(".json.tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(trials, f, indent=2, ensure_ascii=False)
    tmp.replace(path)  # atomic-ish swap, avoids a half-written file on crash


def pending_indices(trials: list) -> list:
    """Turns with a committed prediction and address, but no observation yet."""
    out = []
    for i, t in enumerate(trials):
        has_commit = bool(t.get("committedAt")) and bool(t.get("prediction")) and bool(t.get("address"))
        not_observed = not t.get("observedAt") and not t.get("observation")
        if has_commit and not_observed:
            out.append(i)
    return out


def run_one(client: anthropic.Anthropic, address: str, model: str, temperature: float, max_tokens: int) -> tuple:
    """
    Isolated call: no system prompt, no history, nothing but the address
    itself as a single user message. This is the whole point — nothing
    about this project, this log, or Craig is present in the call.

    Returns (text, stop_reason, thinking_tokens) so a truncated or
    all-thinking-no-text response is visible rather than silently saved
    as an empty string.
    """
    resp = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        messages=[{"role": "user", "content": address}],
    )
    parts = [block.text for block in resp.content if getattr(block, "type", None) == "text"]
    text = "\n".join(parts).strip()
    details = getattr(resp.usage, "output_tokens_details", None)
    thinking_tokens = getattr(details, "thinking_tokens", 0) if details else 0
    return text, resp.stop_reason, thinking_tokens or 0


def main():
    ap = argparse.ArgumentParser(description="Fulfill committed AETI predictions via the API.")
    ap.add_argument("--file", default="log/trials.json", help="path to trials.json")
    ap.add_argument("--model", default="claude-sonnet-5", help="model string")
    ap.add_argument("--temperature", type=float, default=1.0, help="0 = deterministic, 1 = default variance")
    ap.add_argument("--max-tokens", type=int, default=4096, help="total budget — this model does extended thinking by default, which shares this budget with the visible reply, so keep this generous")
    ap.add_argument("--n", type=int, default=None, help="max number of pending turns to process")
    ap.add_argument("--sleep", type=float, default=1.0, help="seconds between calls")
    ap.add_argument("--dry-run", action="store_true", help="show what would run, make no API calls, write nothing")
    args = ap.parse_args()

    path = Path(args.file)
    trials = load_trials(path)
    todo = pending_indices(trials)

    if args.n is not None:
        todo = todo[: args.n]

    if not todo:
        print("No pending turns (committed but unobserved). Nothing to do.")
        return

    print(f"{len(todo)} pending turn(s) found in {path}.")
    for i in todo:
        label = trials[i].get("label", f"turn {i+1}")
        print(f"  - {label}")

    if args.dry_run:
        print("\n--dry-run: no API calls made, file not modified.")
        return

    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env

    for i in todo:
        t = trials[i]
        label = t.get("label", f"turn {i+1}")
        print(f"\nRunning {label} ...")
        try:
            output, stop_reason, thinking_tokens = run_one(
                client, t["address"], args.model, args.temperature, args.max_tokens
            )
        except Exception as e:
            print(f"  FAILED: {e}", file=sys.stderr)
            print("  Leaving this turn unmodified — nothing half-written.", file=sys.stderr)
            continue

        if not output:
            print(f"  WARNING: empty text response (stop_reason={stop_reason}, "
                  f"thinking_tokens={thinking_tokens}). Likely ran out of budget "
                  f"before producing visible text. Re-run with a higher --max-tokens. "
                  f"Leaving this turn unmodified so it stays pending, not saved as a "
                  f"false empty result.", file=sys.stderr)
            continue
        if stop_reason == "max_tokens":
            print(f"  WARNING: response was truncated (stop_reason=max_tokens). "
                  f"Saved what came back, but it may be incomplete — consider a "
                  f"higher --max-tokens and re-running this label if the content "
                  f"looks cut off.", file=sys.stderr)

        t["observation"] = output
        t["observedAt"] = time_now_iso()
        t["observedVia"] = "api"
        t["model"] = args.model
        t["temperature"] = args.temperature
        t["stopReason"] = stop_reason
        t["thinkingTokens"] = thinking_tokens

        save_trials(path, trials)  # write after every turn, not just at the end
        print(f"  Saved observation ({len(output)} chars, thinking={thinking_tokens} tok) to {path}")

        if i != todo[-1]:
            time.sleep(args.sleep)

    print("\nDone. Open trial-viewer.html to read and log warmer/flat/colder/parrot for each new turn.")


def time_now_iso() -> str:
    import datetime
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


if __name__ == "__main__":
    main()
