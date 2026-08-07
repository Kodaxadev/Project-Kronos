# K001 Hostile Review — Round 1

**Date:** 2026-08-06  
**Reviewer provenance:** same AI-directed research workflow  
**Authority:** internal audit only; not independent reproduction or external review

## Scope

This review attacked:

- the canonical Conjecture B statement;
- the finite interval endpoints;
- the progression reduction;
- subgroup-index detection;
- prime-enumeration completeness;
- primitive-root and coset witness checks;
- arithmetic overflow and determinism;
- shared assumptions between implementations;
- scope promotion from finite computation to theorem.

## Material finding H1 — fixed

### Baseline implemented a weaker generator condition

The original generic scanner and verifier required the coset `tH` to generate `F_p^*/H`, but did not require `t` itself to generate `F_p^*`.

Conjecture B requires a generator of the full multiplicative group. The distinction is real: modulo `73`, the coset `7H` generates the quotient and `(b,c)=(5,6)` satisfies the coset equation, but `7` has multiplicative order `24`, not `72`.

### Disposition

Fixed in the generic scanner and standalone verifier. A regression test now rejects the quotient-only witness. The repaired scan through `p <= 5000` still records no failures among 220 applicable primes.

### Impact on K001

None. The index-3003 generator, Python verifier, and C++ implementation already search for or verify primitive roots of the full group.

## K001 checks that passed internally

### 1. Interval coverage

The external premises are interpreted as:

- Conjecture B was computationally checked for primes `p <= 2^30`;
- the sufficient theorem applies for primes `p >= b(3003)`;
- `b(3003)=2304192002`.

Both numeric endpoints are even and therefore not prime. The open interval

```text
2^30 < p < 2304192002
```

contains every prime not covered by those two premises, assuming the premises apply as interpreted.

### 2. Progression completeness

Let `H=<-1,2>`. Since `-1` belongs to `H`, `|H|` is even. If the index is `ell=3003`, then

```text
p-1 = 3003*|H|
```

is divisible by `6006`. Hence every candidate prime occurs in the progression `p=1+6006*k`. No residue class with index `3003` is excluded by this reduction.

### 3. Exact subgroup-index test

If `r=ord_p(2)`, then

```text
|<-1,2>| = lcm(r,2).
```

For the candidate subgroup size `h=(p-1)/3003`, this equals `h` exactly in either of two cases:

- `r=h`; or
- `r=h/2` with `h/2` odd.

The generator and both verifiers implement these cases. The five reported primes were also checked against their recorded orders of `2`.

### 4. Prime enumeration

The computation uses different enumeration mechanisms:

- deterministic 64-bit Miller–Rabin in the Python generator;
- a segmented progression sieve in the standalone Python verifier;
- an independently written progression sieve in C++20.

All produce:

- 204,870 progression candidates;
- 40,246 primes;
- the same five exact-index primes in the same order.

### 5. Witness semantics

For every reported prime, the package checks:

- `g` is a primitive root of `F_p^*`;
- `b/g` lies in `H`;
- `c/g^2` lies in `H`;
- `1+b=c` modulo `p`.

The sign convention is equivalent to the twisted-Fermat formulation because `-1` belongs to `H`.

### 6. C++ arithmetic range

All moduli are below `2304192002`. A product of two residues is therefore below approximately `5.31*10^18`, which is below the maximum unsigned 64-bit value. The modular multiplication used by the C++ verifier does not overflow in the declared interval.

### 7. Determinism and corruption

CI requires:

- two byte-identical Python regenerations;
- equality with the committed JSON artifact;
- exact Python/C++ report agreement;
- equality with the committed C++ report;
- SHA-256 manifest validation;
- rejection after materially changing the first witness value `c`.

Linux and Windows pass the applicable checks.

## Remaining risks

### R1 — external-premise interpretation

The project has not independently reconstructed the 2014 computation through `2^30`, nor obtained expert confirmation that the 2023 theorem is being applied with exactly the correct hypotheses and endpoint convention.

### R2 — shared mathematical oracle

The Python and C++ implementations differ structurally, but they share the same project-supplied mathematical reduction and target definition. Agreement does not protect against a common conceptual error in that reduction.

### R3 — novelty

Targeted public searches found no explicit prior result for index `3003`, but search absence is not priority evidence. Equivalent notation, unpublished computation, or a stronger later theorem may exist.

### R4 — no independent actor

All code, audit, and repair work occurred inside one AI-directed workflow. None of it qualifies as independent reproduction or external review.

## Round-1 verdict

`K001` survives the first internal hostile review as a bounded computational proposal. The review does not authorize claim registration, theorem language, charter freezing, or merge.

The next decisive work is independent review of the literature synthesis and a separately directed reproduction of the finite package.
