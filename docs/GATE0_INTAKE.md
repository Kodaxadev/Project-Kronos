# Gate 0 Intake Audit

**Audit date:** 2026-08-06  
**Status:** internal source reconciliation; external review pending

## Canonical target

Project Kronos studies weight-three conflict-avoiding codes of odd length. Prime lengths are fundamental in the cited literature. The active mathematical statement is Conjecture B:

> For an odd prime `p`, if `H=<-1,2>` has index `ell >= 3` in `F_p^*`, then some primitive root `g` admits `b in gH` and `c in g^2H` with `1+b=c`.

The 2023 paper gives an equivalent twisted Fermat equation formulation, Conjecture C.

## Known-results reconciliation

The repository initially treated generic Conjecture B as an undifferentiated starting point. Primary-source review changed that assessment:

- the 2014 Ma–Zhao–Shen computation is reported to cover `p <= 2^30`;
- the 2023 Hsia–Li–Sun theorem covers sufficiently large `p` as a function of `ell`;
- the 2023 paper states that every `ell <= 3000` is covered;
- it also covers larger ranges when `ell` has few distinct prime factors;
- the 2024 paper proves an additional class where the quotient index is an odd prime.

Therefore, a useful first target must be outside those stated classes and must isolate the finite gap between historical computation and theorem.

## First isolated index

Checking the stated numerical range conditions identifies the first value outside them as

```text
ell = 3003 = 3 * 7 * 11 * 13.
```

It has four distinct prime factors, so it is not covered by the stated one-, two-, or three-factor numerical ranges, and it lies just above the unconditional `ell <= 3000` range.

For `ell=3003`, the 2023 threshold formula gives:

```text
(2^4 * (3003 - 3) + 2)^2 - 2 = 2304192002.
```

Combined with the reported historical scan, the unaccounted finite interval is:

```text
2^30 < p < 2304192002.
```

## Attribution correction

The bootstrap bibliography incorrectly credited “New Optimal Constructions of Conflict-Avoiding Codes of Odd Length and Weight 3.” The correct authors are Wenping Ma, Chun-e Zhao, and Dongsu Shen.

## Novelty posture

Targeted searches found no explicit public result for index `3003`, but this is not evidence of novelty. The search may miss:

- papers using different notation;
- unpublished computations;
- non-indexed theses or conference material;
- private AI-assisted work;
- a stronger theorem that subsumes the case without naming `3003`.

No novelty claim is authorized at Gate 0.
