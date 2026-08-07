# Research Roadmap

## K0 — Intake and attribution

**Current posture: substantially completed, not frozen.**

- reconcile Conjectures A, B, and C and the notation `ell_0`;
- correct the core 2014 bibliography;
- document public code, datasets, later citations, and visible AI-assisted attempts;
- preserve search limits rather than claiming no competing work exists.

Remaining: hostile review of the known-results table and a deeper citation search for equivalent `ell=3003` results.

## K1 — Baseline reproduction

- reproduce the published `p=73` witness and construction example;
- preserve the generic small-prime scanner as a definition check;
- do not attempt to duplicate the full historical `p <= 2^30` scan until its exact method is recovered.

Current reproduction: the repository obtains `g=5`, `b=5`, `c=6` for `p=73`.

## K2 — First bounded research result

- isolate the first index beyond the reconciled `ell <= 3000` coverage;
- enumerate the complete finite theorem/computation gap for `ell=3003`;
- verify the result through structurally different Python and C++ implementations;
- require a material negative control;
- propose, but do not automatically register, the bounded result.

Current status: proposal `K001` prepared; claim ledger remains empty.

## K3 — Adversarial review and registration decision

- attack the theorem-bound arithmetic and endpoint inclusivity;
- attack the derivation `p=1+2*ell*k`;
- attack subgroup-index detection from `ord_p(2)`;
- attack prime enumeration completeness;
- attack witness verification and primitive-root assumptions;
- check whether the two implementations share a hidden mathematical error;
- search for prior `ell=3003` work under alternate notation;
- register only after the bounded statement survives.

## K4 — Next mathematical target

After disposition of `K001`, choose one:

- the next smallest index outside published ranges;
- a structural family containing `3003`;
- a stronger bound that removes many composite indices at once;
- a certificate format or formalization for the finite synthesis.

Avoid progress that consists only of extending a numeric scan without a structural target.

## K5 — Verification and external review

- commission a genuinely independently directed implementation;
- formalize stable group-theoretic lemmas where useful;
- seek review from coding-theory or finite-field researchers;
- separate mathematical optimality from practical protocol performance.

## Abandon or redirect when

- the target is found to be solved or actively saturated by another group;
- baseline literature cannot be reconciled;
- progress reduces only to larger uninformative scans;
- commercial relevance depends on assumptions absent from the mathematical model;
- the project cannot produce a narrower publishable or reusable result.
