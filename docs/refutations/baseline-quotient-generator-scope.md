# Corrected Baseline Scope: Quotient Generator Is Not Enough

**Found:** 2026-08-06 during hostile review  
**Severity:** material baseline-definition error  
**Impact on `K001`:** none; the index-3003 package already requires and verifies primitive roots

## Error

The initial generic Conjecture B scanner accepted a value `t` whenever the coset `tH` generated the quotient group `F_p^*/H`.

Conjecture B requires more: the representative `g` must generate the full multiplicative group `F_p^*`.

A quotient generator need not be a primitive root. Therefore the original scanner and standalone verifier implemented a weaker statement.

## Concrete regression case

Modulo `p=73`:

- `H=<-1,2>` has index `4`;
- the coset `7H` generates `F_73^*/H`;
- `b=5` lies in `7H`;
- `c=6` lies in `7^2H`;
- `1+b=c`;
- but `7` has multiplicative order `24`, not `72`.

The old verifier would accept this record even though it is not a Conjecture B witness.

## Repair

- the generator now searches only primitive roots of `F_p^*`;
- the standalone verifier independently checks the primitive-root condition;
- a regression test requires rejection of the `p=73`, `t=7` quotient-only witness;
- the report scope explicitly says `primitive-root witnesses only`.

## Revalidated outcome

After the repair, the small scan through `p <= 5000` still covers 220 applicable primes and still records no finite failures. The published `p=73` witness remains `(g,b,c)=(5,5,6)`, where `5` is a primitive root.

## Evidence boundary

The repair corrects the implemented statement. It does not establish Conjecture B universally, independent reproduction, novelty, or external review.
