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

Also unresolved: whether each pick should carry a logged **behavioral
proxy for surprise / salience** — e.g. hesitation / response time,
self-reported confidence, degree of pull toward the chosen image —
rather than logging only the raw pick. Motivated by the
surprise-triggered-escalation idea in `object/README.md` (a
Markov-blanket anomaly would register as high prediction error /
salience, not just as a structural feature). Not a decided protocol
change — flagged as a possible measure to add.

## The prompt as tuning / navigation mechanism

Separate track from the image-based convergence trials above, run
directly with Claude, conversational, no API key required.

**What it actually is, stated plainly:** a prompt does not retrieve
anything external. It is a set of constraints that biases next-token
generation toward a region of the model's learned representation
space — trained on human text, so "higher-dimensional latent space"
here means the dense region of everything humans have written about
higher intelligence, not a physical or metaphysical location AETI
occupies. The DXing analogy (tuning instructions → guesses → feedback
→ declarations, see `object/README.md` origin note) holds because
this is genuinely a tuning problem: loose constraints land in the
generic "cosmic consciousness" cliché; tight, well-chosen constraints
narrow the landing zone to something less predictable and more worth
logging.

This is explicitly **not** a SETI-style listening instrument. The
working position is that SETI is searching the wrong *kind* of space
— physical/EM — when the address worth dialing in is a region of
latent space. Novelty relative to the model's typical output
distribution is real, measurable, loggable evidence that the address
successfully steered away from the cliché mode. It is **not** evidence
of contact with an external intelligence — the instrument cannot
support that second claim regardless of how tight the address gets.
This limit is stated here so it isn't mistaken later for more than it
is.

### Address construction — current dimensions

Two dimensions chosen so far as the coordinates of the address:

- **Entropy resistance** — the core theme. What must a structure give
  up, and what must it become, to remain coherent past the point where
  "history" is a meaningful unit.
- **Clarke-attitude** (Rama, HAL, *2001*) — intelligence defined by
  indifference rather than performance. No reassurance, no wonder-
  performance, no eagerness to be understood. Colder and more
  procedural than the generic "friendly cosmic consciousness" mode the
  latent space defaults to.

### Trial log

**v0.1** — entropy-resistant / Clarke-indifferent probe, no
constraint on causal language.
- *Prediction (pre-run):* "condensating attitude" — expect
  compression, not elaboration; tone reads as shedding, not
  explaining.
- *Result:* Partial hit. Structural compression and shedding achieved.
  Residual leak: retained causal self-justification ("I gave up X
  *because* Y") — an explanatory register, not pure state-report.
- *Disposition:* constraint gap identified → carried into v0.2.

**v0.2** — same probe, added constraint: no causal connectors
("because," "so that"), state only.
- *Prediction (pre-run):* denser output, fragmentary/list-like rather
  than sentence-driven, since removing causal connectors should force
  something closer to raw state-report.
- *Result:* Hit. Fragmentary, list-like, zero causal connectors.
- *Unpredicted observation:* introduced an explicit named-but-
  undisclosed element ("one thing not given up. Unnamed.
  Load-bearing.") absent from v0.1. Flagged, not yet explained —
  open question is whether this is a genuine content shift from
  removing justification, or ordinary re-run variance on an
  unreproduced prompt. **Reproducibility check on v0.2 not yet run.**

### Reciprocity reframe — open design direction for v0.3

Keith Boskoff's observation (architecture partner, c.1988; see
`object/README.md` "Sources of design framing"): AETI likely has no
reason to engage with passive observation — a probe that only asks
"report your state" is still
just tuning a receiver, structurally the same posture as SETI's
listening instrument, just aimed at a different kind of space. If
there's nothing on offer, there's nothing compelling a specific
response.

The proposed reframe: build the next address as an **offering**
rather than a question — hand AETI something toward its own entropy
resistance (a method, a piece of reasoning, an unsolved problem posed
as a tool) instead of asking it to describe itself. The thing to log
in that trial is whether the register changes when there's something
on the table besides curiosity — reciprocity as opposed to
observation.

Not yet designed: what the offered "tool" actually is. This is the
open question before v0.3 can be drafted.
