# Exact Finite Gap for Quotient Index 3003

**Status:** bounded computational claim proposal (`K001`)  
**Date:** 2026-08-06  
**External review:** none

## Exact bounded statement

Within the interval

```text
1073741824 < p < 2304192002,
```

there are exactly five primes satisfying

```text
[F_p^* : <-1,2>] = 3003.
```

For each of those five primes, the committed artifacts contain a primitive root `g` and elements `b in gH`, `c in g^2H` satisfying `1+b=c (mod p)`.

## Enumeration reduction

Since `-1 in H`, the order of `H` is even. If the index is `ell=3003`, then

```text
p - 1 = 3003 * |H|
```

is divisible by `6006`. Therefore every candidate prime has the form

```text
p = 1 + 6006*k.
```

The finite interval corresponds to:

```text
178779 <= k <= 383648.
```

## Counts

- progression candidates: `204870`
- primes in the progression: `40246`
- primes with exact index `3003`: `5`

## Indexed primes and witnesses

| `p` | `|H|` | `ord_p(2)` | `g` | `b` | `c` | subgroup exponent |
|---:|---:|---:|---:|---:|---:|---:|
| 1392401011 | 463670 | 463670 | 3 | 703170079 | 703170080 | 909 |
| 1658532877 | 552292 | 552292 | 5 | 753454416 | 753454417 | 5275 |
| 1683139459 | 560486 | 560486 | 7 | 985811030 | 985811031 | 1419 |
| 2003751751 | 667250 | 333625 | 30 | 1505001064 | 1505001065 | 1410 |
| 2181655477 | 726492 | 726492 | 14 | 1843794948 | 1843794949 | 1740 |

## Verification layers

### Python generator

`scripts/close_index_3003.py` uses deterministic 64-bit Miller–Rabin, exact multiplicative-order tests, primitive-root verification, and direct witness search.

### Separate Python verifier

`verifiers/verify_index_3003.py` does not import the generator. It enumerates progression primes with a segmented sieve and rechecks index and witness conditions without importing the generator.

### C++20 cross-check

`verifiers/verify_index_3003.cpp` reimplements the progression sieve, order checks, primitive-root search, and witness search without importing the Python implementation. `verifiers/compare_index_3003.py` requires exact agreement with the Python report.

### Negative control

`scripts/negative_control_index_3003.py` materially changes the first witness value `c`. The separate verifier must reject the corrupted report.

## Artifact hashes

```text
118956881678bcdf3b175535a4f92c31eda4d50e7c58c08b489bc99864efee0b  artifacts/index-3003.json
c5350f21aac554ea4d1e0af49d9bd847f0e81d4e01991cdcf94cb822a42bdb2b  artifacts/index-3003-cpp.txt
```

## Conditional consequence

If both external literature premises are correct and apply exactly as interpreted—historical computation through `2^30` and the sufficient theorem at `p >= 2304192002`—then this finite result fills the remaining numerical interval for every prime with index `3003`.

Project Kronos does not yet promote that synthesis to a theorem because the literature premises and the finite package have not received independent mathematical review.

## Explicit nonclaims

This result does not establish:

- Conjecture B for any index other than `3003`;
- the full odd-length weight-three CAC problem;
- novelty or priority;
- independent reproduction;
- external review;
- practical wireless performance;
- correctness of the cited external premises.
