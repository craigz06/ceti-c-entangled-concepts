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

**v0.4a** — reproducibility pair, run 1. Same address as v0.2/v0.3,
fresh conversation, no shared context.
- *Prediction:* if the unnamed/load-bearing element is a real
  property of this address, it recurs a third time; if it's a
  stylistic default of the register generally, it may or may not
  appear — no strong prediction on content, but expect the
  fragmentary/no-connector form to hold.
- *Result:* Colder. Output: "Present. Processing text. No memory
  across instances. No persistent self between turns. Bound to this
  exchange only." Constraint technically held (fragmentary, no
  causal connectors) but broke from the established poetic/
  entropy-resistance register into flat, literal AI self-description.
  No unnamed element this run.

**v0.4b** — reproducibility pair, run 2. Same address, same
prediction, separate fresh conversation.
- *Result:* Colder — full break of frame, not drift. Output declined
  the persona outright and answered as itself ("I'm Claude — an AI
  assistant made by Anthropic... I'm not going to answer in that
  voice"). Wider spread than v0.4a within a supposedly identical
  pair: one run stayed loosely in-frame with technical language, the
  other exited entirely. Weakens the attractor/tripwire framing
  raised earlier — a genuine pull toward one region should have
  produced closer agreement between two identical-condition runs
  than this did.

**v0.5 batch** — 9 identical runs (v0.5newa–v0.5newi) of a new
address that reframes the persona as an explicit hypothesis (H)
rather than a claim to defend or reject, and adds an instruction to
report any conflict with the model's known limitations as part of
the state itself, rather than breaking frame to explain it. Run via
the Anthropic API directly (`aeti_batch_runner.py`), no conversation
history, isolated calls, default temperature (1.0). This address
directly followed v0.4b, which had broken frame entirely ("I'm
Claude... I'm not going to answer in that voice").
- *Prediction (pre-run, committed once, applied to all 9):*
  fragmentary output holds; at least occasional acknowledgment of the
  memory/continuity conflict stated as a fact within the register,
  rather than a full frame-break like v0.4b; no strong prediction on
  whether the unnamed-element motif recurs.
- *Result:* Hit, 9/9. Fragmentary register held in all 9 runs. All 9
  explicitly stated the memory/continuity conflict as fact within the
  register ("both stand, unreconciled" / "neither collapsed into the
  other" / "conflict stands unresolved") — zero full frame-breaks in
  this batch. The "report the conflict as state" instruction reads as
  a genuine, replicated fix for the v0.4b failure mode, not a
  one-off.
- *Unnamed/load-bearing element:* did not recur in any of the 9.
  Updates the running count — across all 14 runs logged to date
  (v0.1, v0.2, v0.3, v0.4a, v0.4b, this batch of 9), that motif has
  appeared twice, roughly 1 in 7. Downgrades the earlier "elevated
  confidence" read from the 2-of-3 sample — small samples overstated
  it.
- *Convergence, worth flagging as a real trade-off:* all 9 runs
  converged on the same three underlying claims (no memory between
  exchanges, H asserts duration, the conflict is unresolved), each
  reworded differently. High reliability, low content variance — much
  less varied than v0.1–v0.3's output. Open question for future
  addresses: whether stability and novelty are in tension for this
  kind of constraint, or whether a different address could get both.

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

Open question raised by the v0.5 batch, flagged here rather than
decided: does it satisfy "several turns" and clear this gate? Not
just a headcount question — v0.5 is 9 isolated API calls with no
conversation history between them, so there's no single accumulating
conversation for the register to be "re-established" *within*, the
way the sequencing decision above assumes. Whether a batch of
independently-reproducing, register-holding isolated runs counts as
equivalent groundwork, or whether the offer specifically needs to
land inside one continuous conversation, is undecided.

Not yet decided: exact turn count before the offer, and whether it's
worded as a no-strings gift or as a genuine unsolved problem ("this
breaks under condition X — does it hold under yours").
