# Research Roadmap

## K0 — Intake and attribution

- obtain and archive canonical primary sources;
- reconcile notation and exact conjecture variants;
- verify 2014 and 2024 bibliographic claims;
- document public code, datasets, and AI-assisted attempts;
- decide whether Conjecture B remains the correct narrow target.

## K1 — Baseline reproduction

- reproduce published examples such as `p=73`;
- reproduce known classes covered by the 2024 theorem;
- compare scanner output against an independently transcribed implementation;
- scale toward the reported historical bound only after performance and checkpoint design are audited.

## K2 — Structural exploration

- classify quotient indices `ell` not covered by the odd-prime theorem;
- study composite `ell`, especially the obstruction identified in the 2024 paper;
- translate witness existence into hypergraph matching, cyclotomic-number, and finite-field formulations;
- search for minimal hard parameter families rather than merely extending a numeric bound.

## K3 — Claim development

- register only narrow lemmas, counterexamples, reductions, or bounded computational results;
- hostile-review each candidate in a fresh context;
- require explicit scope and failure modes.

## K4 — Verification

- create a genuinely independent implementation with a separately specified mathematical oracle;
- add SAT/ILP certificates where finite optimality is claimed;
- formalize stable definitions and proof components when useful;
- seek external review from coding-theory or finite-field researchers.

## Abandon or redirect when

- the target is found to be solved or actively saturated by another group;
- baseline literature cannot be reproduced;
- progress reduces only to larger uninformative scans;
- commercial relevance depends on assumptions absent from the mathematical model;
- the project cannot produce a narrower publishable or reusable result.
