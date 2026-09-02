# 2026-09-02 — Seed reproducibility test

First entry in the predict → commit → observe → log record. This is a
tooling-verification run, not an experimental trial.

## Purpose

Check whether seed determinism actually holds on this account/model —
same seed + same model + same prompt reproducing the same image — as
assumed in `logistics/README.md`.

## Predict / commit

Committed before comparing the two outputs:

- **Model:** `stability-ai/stable-diffusion-3.5-large` (bare name, no
  pinned version hash — known open item, see `logistics/README.md`)
- **Prompt:** `red bird on a branch`
- **Seed:** `17420`
- **Mode:** text-to-image only (no input image)
- **prompt_strength:** default `0.85` — not meaningful here, applies
  only to image-to-image
- **Runs:** 2, identical inputs both times
- **Platform:** Replicate, run manually

Prediction: both runs produce the same image.

## Observe

- Run 1: output produced.
- Run 2: output produced.
- Comparison: visually identical — same pose, composition, lighting,
  and background.

## Log

- **Outcome:** hit. Seed determinism holds on this account/model for
  this prompt.
- **Limitation:** comparison was visual only. Exact byte/hash-level
  identity was not verified. Not a concern for this test; noted so a
  later run can close the gap if needed.
