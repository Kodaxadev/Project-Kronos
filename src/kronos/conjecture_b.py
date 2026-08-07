from __future__ import annotations

from dataclasses import asdict, dataclass
from math import isqrt


@dataclass(frozen=True)
class Witness:
    p: int
    ell: int
    subgroup_size: int
    t: int
    b: int
    c: int

    def to_dict(self) -> dict[str, int]:
        return asdict(self)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for divisor in range(3, isqrt(n) + 1, 2):
        if n % divisor == 0:
            return False
    return True


def subgroup_minus_one_two(p: int) -> frozenset[int]:
    """Return <-1, 2> inside the multiplicative group modulo p."""
    if not is_prime(p) or p == 2:
        raise ValueError("p must be an odd prime")
    seen = {1}
    frontier = [1]
    generators = ((p - 1) % p, 2 % p)
    while frontier:
        value = frontier.pop()
        for generator in generators:
            candidate = value * generator % p
            if candidate not in seen:
                seen.add(candidate)
                frontier.append(candidate)
    return frozenset(seen)


def coset(value: int, subgroup: frozenset[int], p: int) -> frozenset[int]:
    return frozenset(value * h % p for h in subgroup)


def quotient_order(value: int, subgroup: frozenset[int], p: int) -> int:
    """Return the order of value*H in F_p^*/H."""
    current = 1
    for order in range(1, (p - 1) // len(subgroup) + 1):
        current = current * value % p
        if current in subgroup:
            return order
    raise AssertionError("quotient order did not close")


def conjecture_b_witness(p: int) -> Witness | None:
    """Find a witness for Conjecture B, or None when ell < 3 or none is found."""
    subgroup = subgroup_minus_one_two(p)
    ell = (p - 1) // len(subgroup)
    if ell < 3:
        return None

    for t in range(2, p):
        if quotient_order(t, subgroup, p) != ell:
            continue
        first = sorted(coset(t, subgroup, p))
        second = coset(t * t % p, subgroup, p)
        for b in first:
            c = (1 + b) % p
            if c != 0 and c in second:
                witness = Witness(p, ell, len(subgroup), t, b, c)
                if not verify_witness(witness):
                    raise AssertionError("internally generated witness failed verification")
                return witness
    return None


def verify_witness(witness: Witness) -> bool:
    p = witness.p
    if not is_prime(p) or p == 2:
        return False
    subgroup = subgroup_minus_one_two(p)
    ell = (p - 1) // len(subgroup)
    if ell < 3 or witness.ell != ell or witness.subgroup_size != len(subgroup):
        return False
    if not 1 <= witness.t < p or quotient_order(witness.t, subgroup, p) != ell:
        return False
    if witness.b not in coset(witness.t, subgroup, p):
        return False
    if witness.c not in coset(witness.t * witness.t % p, subgroup, p):
        return False
    return (1 + witness.b) % p == witness.c


def scan_primes(limit: int) -> dict[str, object]:
    if limit < 3:
        raise ValueError("limit must be at least 3")
    records: list[dict[str, int]] = []
    failures: list[dict[str, int]] = []
    applicable = 0
    for p in range(3, limit + 1, 2):
        if not is_prime(p):
            continue
        subgroup = subgroup_minus_one_two(p)
        ell = (p - 1) // len(subgroup)
        if ell < 3:
            continue
        applicable += 1
        witness = conjecture_b_witness(p)
        if witness is None:
            failures.append({"p": p, "ell": ell})
        else:
            records.append(witness.to_dict())
    return {
        "schema_version": 1,
        "target": "Conjecture B for prime-length weight-three conflict-avoiding codes",
        "limit": limit,
        "applicable_prime_count": applicable,
        "records": records,
        "failures": failures,
        "scope_note": "Finite exact search only; an empty failures list is not a proof.",
    }
