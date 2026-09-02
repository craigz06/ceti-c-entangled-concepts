# Logistics

## Holding frame

- Treat this as an **untested property of the universe** — not a
  claim about mechanism, just a testable question. Keeps the
  hypothesis (see root README) separate from any story about *why*
  it might work.

## Tooling decisions made so far

- **Stable Diffusion over DALL-E 3** for seeded image generation.
  - Reason: Stable Diffusion (the open model — distinct from
    Stability AI, the company) has reliable, documented seed
    determinism across independent tools (Automatic1111, ComfyUI,
    Replicate). Same seed + same model + same prompt reliably
    reproduces the same image across these.
  - DALL-E 3's API has no officially guaranteed seed parameter —
    can't rely on reproducibility there.
  - Plan: pin **model version + prompt + seed** together as one
    reproducible unit — the thing that gets committed/logged before
    an outcome is observed.
  - Seed reproducibility is now **empirically confirmed, not just
    asserted**: a manual two-run test on Replicate
    (`stability-ai/stable-diffusion-3.5-large`, prompt "red bird on a
    branch", seed 17420) produced visually identical output both
    times. See `log/2026-09-02-seed-reproducibility-test.md`.
    (Confirmed at the visual level only — no hash-level check yet.)
  - **Version-hash pinning still open.** That first test used the
    bare model name, no pinned version hash. A pinned hash is needed
    before any real (non-throwaway) trial.

## Decided since

- **AI's role — decided: parallel blind receiver** (also logged in
  `object/README.md`). AI makes its own independent, blind reduction
  alongside the human subject; the two picks are compared trial to
  trial.
  - Rejected for now, kept as record of what was considered:
    1. Seeded-image target generator — presumes a ground-truth target
       the current design may not have.
    2. The medium / entangled link itself — not operationalizable at
       this stage.

## AETI "emulation" — preliminary / exploratory

Not settled methodology. Fuller writeup in `object/README.md`; logged
here because it bears on tooling.

- **Rejected approach (for the record):** an entropy / waste-heat-
  export criterion told to *both predictors in advance* as a shared,
  explicit selection rule. Rejected — a shared explicit rule makes any
  convergence between predictors trivial (both just following the same
  instructions), not evidence of anything.
- **Current direction:** bake an entropy / waste-heat-export
  *signature* into the **generation** of one candidate image (or the
  trajectory pair) as a material property, invisible to both blind
  predictors. Question: do the predictors gravitate toward it above
  chance without being told it differs? AETI as a property of the test
  material, not an instruction to the testers.
- **Proposed operationalization (exploratory):** a **Markov blanket**
  structure — legible internal/external boundary plus differentiated,
  non-interchangeable input and output channels (mouth/anus: two
  distinct openings, import vs. export, never reversed) — versus
  control images with no legible boundary or I/O distinction.
- **Known scope limitation:** a Markov blanket with differentiated I/O
  marks self-organizing / agentic systems in general (a bacterium
  qualifies), not *advanced* intelligence specifically. Unresolved
  gap.
- **Extensions (full writeup in `object/README.md`, both
  preliminary):**
  - *Surprise-triggered escalation (free energy principle)* — a
    Markov-blanket anomaly reframed as a high-prediction-error trip
    wire that escalates attention; mathematically motivated and,
    under an entropy budget, computationally necessary rather than
    optional.
  - *ROI filtering / "like recognizes like"* — the filter may be
    tuned to recognize another system running an entropy-delaying,
    structure-preserving process (ties to SEITWH scoring), i.e.
    recognition rather than mere detection.

## Open questions

- Whether trials have a real sealed target at all, or are pure
  convergence-only tests with no ground truth (see
  `intent/README.md`). Not yet decided.
- **Version-hash pinning** for the image model — still open (see
  "Tooling decisions made so far" above).
