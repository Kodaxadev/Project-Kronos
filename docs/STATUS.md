# Current Status

**Date:** 2026-08-06  
**Lifecycle:** Gate 0 candidate intake / Gate 1 charter preparation  
**Epistemic posture:** no project claims registered; one bounded claim proposal

## Completed

- active research branch and experimental Cruthúnas structure initialized;
- canonical Conjecture B statement reconciled across the 2023 and 2024 papers;
- initial bibliography corrected, including the authorship of the 2014 Ma–Zhao–Shen paper;
- published example `p=73` reproduced with primitive-root witness `(g,b,c)=(5,5,6)`;
- bounded public AI-activity search recorded;
- first uncovered index candidate isolated as `ell=3003`;
- exact Python enumeration of the finite literature-conditioned interval completed;
- separate Python verifier completed without importing the scanner;
- separate C++20 implementation completed;
- Python and C++ reports agree exactly;
- material witness corruption is rejected;
- proposal `K001` created without registering it in the canonical claim ledger;
- hostile review found and repaired a baseline scope error that had accepted quotient generators without requiring primitive roots.

## Baseline correction

The original generic scanner implemented a weaker condition than Conjecture B: it required `tH` to generate `F_p^*/H`, but did not require `t` to generate `F_p^*`.

The scanner and standalone verifier now require a full primitive root. A regression test rejects the quotient-only record `(p,t,b,c)=(73,7,5,6)`, because `7` has multiplicative order `24` rather than `72`.

After repair, the scan through `p <= 5000` still covers 220 applicable primes and records no finite failures. This correction does not affect `K001`, whose generator and both verification paths already required primitive roots.

## Finite `ell=3003` result

The searched interval is

```text
1073741824 < p < 2304192002.
```

The progression `p=1+6006*k` contains:

- 204,870 candidate values;
- 40,246 primes;
- 5 primes with `[F_p^*:<-1,2>] = 3003`;
- a verified Conjecture B primitive-root witness for each of those five primes.

Committed Python report SHA-256:

```text
118956881678bcdf3b175535a4f92c31eda4d50e7c58c08b489bc99864efee0b
```

## What this does not establish

- correctness or applicability of the cited published computation through `2^30`;
- correctness or applicability of the cited theorem at and above `2304192002`;
- novelty of the `ell=3003` synthesis;
- independent reproduction by another person or separately directed team;
- external mathematical review;
- Conjecture B for another index;
- the general odd-length CAC problem;
- Cruthúnas conformance or commercial deployment value.

## Immediate blockers before registration

1. continue hostile review of the finite arithmetic and boundary conditions;
2. independent review of the literature synthesis;
3. citation search specifically for index `3003` and equivalent formulations;
4. decision whether to register `K001` as a computational result;
5. freeze or revise the charter based on that review.
