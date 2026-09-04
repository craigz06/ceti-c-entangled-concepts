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

## Trust and Hardship — candidate operationalizations (2026-09-04)

Follow-on to the earlier finding that Trust and Hardship don't attach
at the component (single-object) scale — Trust requires two aligned
objects by definition, and Hardship is entirely a property of what
surrounds a structure, not of the structure itself. Both were left as
"undefined, not measurable here" rather than scored. Craig proposed
concrete proxies for each, closing part of that gap:

**Trust, from audit depth.** Not a single compliance percentage — a
three-way split, since collapsing to one number would reward
passivity over genuine engagement:
- comply (did the proposed thing get done)
- extend (built on or added meaning beyond what was asked)
- disregard (didn't follow the suggestion)
A person who only complies isn't more trustworthy in any meaningful
sense than one who frequently extends or pushes back — several of
this project's better moments (the reciprocity reframe, pushback on
overclaiming "trajectory" from a single run) were disregard-category
moves that improved the work. The three-way split is necessary
precisely so the metric doesn't penalize that.

**Burden, from correction cost.** Raw character count spent pursuing
a goal doesn't distinguish productive effort from pure friction —
drafting an address and retyping a command because a file wasn't
where it should be look identical by that measure. Split into two
counters instead: characters spent on substance vs. characters spent
on troubleshooting/correction. The ratio between them is a more
honest burden signal than the total. (This session's own git-cleanup
detour — dead servers, a misplaced file, a literally-pasted
placeholder — is a real instance of the second bucket, logged as such
rather than folded into "normal" effort.)

**Named explicitly as proxies, not the thing itself** — same status
as QI's six vectors: audit-depth and correction-cost are cheap,
observable stand-ins for trust and burden, not trust and burden
directly. Analogy offered in discussion: a retailer inferring "bad
customer" from a buy-use-return pattern rather than from intent
directly — a correlated, observable proxy for something that can't be
observed directly.

Status: proposed, not yet applied to any trial or scored
retrospectively against the existing log. Next step, if pursued,
would be scoring a few already-logged exchanges against both splits
to see whether the categories are workable in practice.
