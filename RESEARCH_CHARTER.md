# Project Kronos Research Charter

**Status:** UNFROZEN — Gate 0/1 candidate intake  
**Active branch:** `research/odd-length-weight3-cac`  
**Initialized:** 2026-08-06  
**Last revised:** 2026-08-06

## Mission

Project Kronos tests whether a nonexpert human can orchestrate AI systems into producing trustworthy, independently checkable progress on a commercially relevant open mathematical problem. The research domain is optimal conflict-avoiding codes of odd length and Hamming weight three.

## Human and AI roles

Justin Davis selects goals, assigns AI roles, requires adversarial review, controls repository state, and decides whether evidence is sufficient to advance a claim. He does not claim independent mathematical or software authorship or understanding. AI-generated proofs, programs, reviews, and summaries are provenance, not independent verification.

## Canonical research question

For an odd prime `p`, let `H = <-1,2>` in `F_p^*` and let `ell = [F_p^*:H]`. When `ell >= 3`, must there exist a primitive root `g` modulo `p` and elements `b in gH`, `c in g^2H` satisfying `1+b=c` modulo `p`?

The literature calls this Conjecture B. It implies a construction statement used to obtain optimal prime-length weight-three conflict-avoiding codes.

## First bounded milestone

Gate 0 reconciliation showed that published results already cover `ell <= 3000` and several larger classes. The first isolated index not covered by the reconciled ranges is

```text
ell = 3003 = 3 * 7 * 11 * 13.
```

For `ell=3003`, the first milestone is to audit the conditional synthesis:

1. a published computation reports Conjecture B through `p <= 2^30`;
2. a published theorem applies for `p >= 2304192002`;
3. Project Kronos exactly enumerates the remaining interval and supplies a witness for every prime in it having index `3003`.

This milestone is not promoted until the literature premises, finite implementation, scope, and novelty have survived fresh hostile review.

## Evidence rules

1. Literature statements are not project theorems.
2. Finite scans remain `COMPUTATIONAL` and bounded by their declared range.
3. Multiple implementations produced inside the same AI-directed workflow are cross-checks, not independent reproduction.
4. A proof is not promoted to `PROVED` until its exact statement, dependencies, and proof location are registered and hostile-reviewed.
5. Formalization checks the encoded statement, not whether that statement matches the intended mathematics.
6. Commercial relevance is a motivation, not evidence of deployable performance or monetary value.
7. A conditional synthesis must list every external premise on which it depends.

## Branch policy

- `main` is the stable landing branch.
- `research/odd-length-weight3-cac` is the active research integration branch.
- Exploratory work branches from the research branch and returns by pull request.
- Only audited milestones should be proposed from the research branch to `main`.

## Gate 0/1 exit conditions

The charter can be frozen only after:

- the canonical problem and notation are reconciled across primary sources;
- the known-results table receives a fresh hostile audit;
- attribution and novelty searches are recorded with explicit limitations;
- the public AI-activity search is documented with explicit limitations;
- published examples are reproduced;
- proposal `K001` and its finite certificate receive an adversarial review;
- abandonment criteria and the next bounded target are approved.
