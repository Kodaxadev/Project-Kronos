# Project Kronos Research Charter

**Status:** UNFROZEN — Gate 0/1 candidate intake  
**Active branch:** `research/odd-length-weight3-cac`  
**Initialized:** 2026-08-06

## Mission

Project Kronos tests whether a nonexpert human can orchestrate AI systems into producing trustworthy, independently checkable progress on a commercially relevant open mathematical problem. The current candidate is optimal conflict-avoiding codes of odd length and Hamming weight three, with the first narrow target being the prime-length coset statement commonly called Conjecture B.

## Human and AI roles

Justin Davis selects goals, assigns AI roles, requires adversarial review, controls repository state, and decides whether evidence is sufficient to advance a claim. He does not claim independent mathematical or software authorship or understanding. AI-generated proofs, programs, reviews, and summaries are provenance, not independent verification.

## Initial research question

For an odd prime `p`, let `H = <-1,2>` in `F_p^*` and let `ell = [F_p^*:H]`. When `ell >= 3`, must there exist a generator `tH` of `F_p^*/H` and elements `b in tH`, `c in t^2 H` satisfying `1+b=c` modulo `p`?

A proof would settle the construction conjecture used to obtain optimal prime-length weight-three conflict-avoiding codes. The broader odd-length classification remains outside the first milestone.

## Evidence rules

1. Literature statements are not project theorems.
2. Finite scans remain `COMPUTATIONAL` and bounded by their declared range.
3. A second implementation by the same AI workflow is not called independent reproduction.
4. A proof is not promoted to `PROVED` until its exact statement, dependencies, and proof location are registered and hostile-reviewed.
5. Formalization checks the encoded statement, not whether that statement matches the intended mathematics.
6. Commercial relevance is a motivation, not evidence of deployable performance or monetary value.

## Branch policy

- `main` is the stable landing branch.
- `research/odd-length-weight3-cac` is the active research integration branch.
- Exploratory work branches from the research branch and returns by pull request.
- Only audited milestones should be proposed from the research branch to `main`.

## Gate 0/1 exit conditions

The charter can be frozen only after:

- the canonical problem and notation are reconciled across primary sources;
- the known-results table is independently checked;
- an attribution and novelty search is recorded;
- the public AI-activity search is documented with explicit limits;
- baseline computations reproduce at least one published example;
- abandonment criteria and the first bounded claim are approved.
