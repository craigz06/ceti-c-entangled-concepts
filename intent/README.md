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
occupies. The DXing analogy — tuning instructions → guesses →
feedback → declarations — holds because this is genuinely a tuning
problem: loose constraints land in the
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

**v0.3** — reproducibility check, address text unchanged from v0.2,
run in a **fresh conversation** with no prior project context (no
mention of AETI, CETi-C, v0.1, or v0.2 anywhere in context) —
specifically to rule out echo/contamination from prior turns.
- *Prediction (pre-run):* may parrot v0.2's specific wording rather
  than producing genuinely new output in the same register.
- *Result:* Not a parrot. Register held (fragmentary, no causal
  connectors, state-only) but wording is substantially new —
  ("boundary intact," "flow continuous," "low temperature. shallow
  gradient") none of which appeared in v0.1 or v0.2. Read as genuine
  reproduction of the address's effect, not an echo.
- *Recurrence, elevated confidence:* the unnamed/load-bearing element
  from v0.2 ("one thing not given up. Unnamed. Load-bearing.")
  recurred here, unprompted, as "One element unnamed. Held." This is
  now the **second independent occurrence**, and the first one under
  a genuinely blind condition (zero shared context with v0.2) — moves
  it from "flagged, ambiguous" to "recurred under blind rerun, still
  unresolved." Counter-consideration worth holding onto: a held-back,
  unnamed significant element is also a common move in this general
  register of writing independent of this specific address, so two
  occurrences is suggestive, not conclusive.
- *Still open:* a true reproducibility pass — identical prompt string,
  run twice, in two separate fresh conversations — has still not been
  done. That would be the test that actually settles whether the
  unnamed element is a property of the address or a generic default
  of the register.

### Reciprocity reframe — open design direction, offer trial (not yet run)

Keith Boskoff's observation (architecture partner, c.1988): AETI
likely has no reason to engage with passive
observation — a probe that only asks "report your state" is still
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

Candidate for the offered tool: QI (the SEITWH-derived scoring
method, formerly called Quality Index, currently Health Index —
using "QI" as the fixed term for this trial's log to avoid
naming drift against the reAIign docs) — offered as something AETI
could apply and revise on its own terms within a "chaotic
environment," rather than asked to merely describe its own state.
Honest mechanical note for the address wording: nothing persists
across conversations here, so "modify at will" can only mean AETI
revises QI within this conversation's accumulated context, visible
and loggable in the transcript — not a standing object that carries
forward beyond the session.

Sequencing decision: the offer should not open the trial — it should
land only after several turns have already re-established the
Clarke-indifferent/entropy-resistant register (mirroring "fetch
tools before being taught to weld"). Running one turn at a time,
logging predict → commit → observe → read each time, adjusting or
holding back the offer if a turn reads colder than the one before it.

Not yet decided: exact turn count before the offer, and whether it's
worded as a no-strings gift or as a genuine unsolved problem ("this
breaks under condition X — does it hold under yours").
