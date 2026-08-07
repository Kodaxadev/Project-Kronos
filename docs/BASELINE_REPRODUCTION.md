# Baseline Reproduction

**Date:** 2026-08-06  
**Status:** internal reproduction of published examples and definitions

## Published `p=73` example

For `p=73`, the repository computes:

```text
H = <-1,2>
ell = 4
g = 5
b = 5
c = 6
1 + b = c mod 73
```

The verifier confirms:

- `gH` generates `F_73^*/H`;
- `b in gH`;
- `c in g^2H`;
- `1+b=c` modulo `73`.

This matches the witness described in the 2024 paper. The paper also connects this witness to the nonequidifference codeword `{0,2,5}` and an optimal CAC of size 17. The repository currently reproduces the witness conditions, not the complete 17-codeword construction.

## Small-prime baseline

The generic scanner through `p <= 5000` records:

- 220 applicable primes with `ell >= 3`;
- a witness for every applicable prime;
- no finite failures.

This is a definition and implementation check only. It is far below the historical published computation bound and is not a new result.

## Independence boundary

The scanner, its tests, and the first standalone verifier were all produced inside the same AI-directed workflow. They do not constitute independent reproduction.
