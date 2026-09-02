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

## Open questions

- **AI's role — undecided, three candidates** (also logged in
  `object/README.md`):
  1. Seeded-image target generator.
  2. Parallel blind receiver, run alongside the human subject.
  3. The medium/entangled link itself.
