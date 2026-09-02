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
