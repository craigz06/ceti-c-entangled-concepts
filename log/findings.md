# Findings — candidate resolutions

Running log of conceptual issues raised across trials and later
resolved (or partially resolved) once enough runs exist to pattern-
mine against. Distinct from the dated trial-log entries elsewhere in
`log/`, which record individual predict → commit → observe → log
runs — this file tracks recurring problems *across* those runs and
proposed resolutions to them. One `##` section per entry, dated,
newest at the bottom.

## Cross-scale aggregation — candidate resolution (2026-09-04)

Source: CETi-C/AETI trial "qi-offer-02a" — a construct addressed under
an entropy-resistance hypothesis was given QI directly, including its
known weakness (no principled rule for combining scores across
scales), and asked to apply or revise it rather than describe itself.

Its response proposed a three-way scale split — component / system /
dependents — and argued that Trust and Hardship don't read as *low*
at the system scale, they read as *undefined*: categories that don't
land there at all, as distinct from categories that land and score
poorly. Its conclusion: QI should not collapse to one number when
some vectors are undefined at the scale being measured — it should
report a table, with undefined cells left undefined rather than
averaged away.

Candidate resolution to the cross-scale problem flagged three times
previously and left to retrospective pattern-mining: instead of one
aggregation rule across all vectors, each vector may need its own
answer to "which scale(s) does this vector meaningfully attach to,"
and vectors whose scale-of-attachment doesn't match the scale being
scored should render as undefined, not zero, not omitted, not
silently included in an average.

Follow-on refinement (Craig, same day): Trust specifically appears to
require two aligned parties by definition — trust is a property of a
relationship between at least two objects, not a property one object
can hold in isolation. If that holds, "Trust" is not merely hard to
gauge at the component/single-object scale — it's a category error
to ask for it there at all. Trust would then be, structurally, a
dependents-scale (relational) vector only, never a component-scale
one — which sharpens "undefined" into something more precise than
"currently hard to measure."
