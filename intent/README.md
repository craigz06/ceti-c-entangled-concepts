# Intent

- **Double-blind experiment.**
- Explicit parallel to SCO's protocol: **predict → commit → observe
  → log.**
  - Predict: form the reduction before the outcome is known.
  - Commit: record it somewhere tamper-evident/timestamped, before
    observing.
  - Observe: reveal the actual outcome.
  - Log: record the match/mismatch, unedited, whether it hits or
    misses.
- Both reductions (the two independent, blind predictions) must be
  committed before either side sees the other's, and before the
  outcome resolves — same double-blind discipline SCO already uses.

## Current trial design — preliminary

Supersedes the earlier "testor selects a known target, subject picks
1-of-4" structure. Still preliminary, not a locked protocol.

- **Three objects** (see `object/README.md`): AETI (the thing under
  test), Craig, and Claude / AI. Craig and Claude / AI are the **two
  blind predictors**; AETI is not a predictor.
- **No testor holds a known target.** This removes the experimenter-
  leakage (Clever Hans) risk in the earlier design: neither predictor
  can be cued by someone who knows the answer, because *no one* knows
  the answer.
- **Procedure:**
  1. Two sequential images are shown to both predictors first,
     establishing a "trajectory."
  2. Both predictors then independently and blindly pick from four
     candidate continuation images.
  3. Neither sees the other's pick.
- **Repeated across many trials; results compared.**

### Two distinct questions this design can answer — log both separately

- **(a) Predictor convergence.** Do the two predictors agree with each
  other above chance (25% baseline for a 4-way forced choice),
  *regardless of any "correct" answer*? Likely the **primary signal**,
  since there may be no ground truth to check accuracy against.
- **(b) Accuracy against a target.** If a real / sealed target exists
  for a given trial, how often does each predictor hit it? A
  **secondary** measure, only meaningful for trials that have a
  sealed target.

### Open decision — not yet resolved

Whether trials have a real sealed target at all, or are pure
convergence-only tests with no ground truth. Undecided.
