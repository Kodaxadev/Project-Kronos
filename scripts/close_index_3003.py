from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Iterable

ELL = 3003
LITERATURE_LIMIT = 2**30


def distinct_prime_factors(n: int) -> list[int]:
    factors: list[int] = []
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            while n % divisor == 0:
                n //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if n > 1:
        factors.append(n)
    return factors


def omega(n: int) -> int:
    return len(distinct_prime_factors(n))


def theorem_bound(ell: int) -> int:
    delta = 1 if ell % 4 == 0 else 0
    return (2 ** omega(ell) * (ell - 3 - delta) + 2) ** 2 - 2


def is_prime(n: int) -> bool:
    """Deterministic Miller-Rabin for unsigned 64-bit integers."""
    if n < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for prime in small_primes:
        if n % prime == 0:
            return n == prime
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for base in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        a = base % n
        if a in (0, 1):
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def has_exact_order(a: int, order: int, modulus: int, factors: Iterable[int] | None = None) -> bool:
    prime_factors = list(factors) if factors is not None else distinct_prime_factors(order)
    if pow(a, order, modulus) != 1:
        return False
    return all(pow(a, order // prime, modulus) != 1 for prime in prime_factors)


def subgroup_index_minus_one_two(p: int, ell: int) -> tuple[int, int] | None:
    """Return (|<-1,2>|, ord_p(2)) when the index is ell, otherwise None."""
    if (p - 1) % ell != 0:
        return None
    subgroup_size = (p - 1) // ell
    if subgroup_size % 2:
        return None
    factors_h = distinct_prime_factors(subgroup_size)
    if has_exact_order(2, subgroup_size, p, factors_h):
        return subgroup_size, subgroup_size
    half = subgroup_size // 2
    if half % 2 == 1 and has_exact_order(2, half, p, distinct_prime_factors(half)):
        return subgroup_size, half
    return None


def primitive_root(p: int, factors: Iterable[int]) -> int:
    for candidate in range(2, p):
        if all(pow(candidate, (p - 1) // prime, p) != 1 for prime in factors):
            return candidate
    raise AssertionError(f"no primitive root found modulo {p}")


def find_witness(p: int, ell: int, subgroup_size: int, factors_p_minus_1: Iterable[int]) -> dict[str, int]:
    g = primitive_root(p, factors_p_minus_1)
    step = pow(g, ell, p)
    target = pow(g, 2 * subgroup_size, p)
    element = 1
    for exponent in range(subgroup_size):
        b = g * element % p
        c = b + 1
        if c == p:
            c = 0
        if c and pow(c, subgroup_size, p) == target:
            index_data = subgroup_index_minus_one_two(p, ell)
            assert index_data is not None
            return {
                "p": p,
                "ell": ell,
                "subgroup_size": subgroup_size,
                "order_of_2": index_data[1],
                "primitive_root": g,
                "quotient_generator": g,
                "b": b,
                "c": c,
                "subgroup_exponent": exponent,
            }
        element = element * step % p
    raise AssertionError(f"no Conjecture B witness found for p={p}, ell={ell}")


def generate_report(ell: int = ELL) -> dict[str, object]:
    if ell < 3:
        raise ValueError("ell must be at least 3")
    lower = LITERATURE_LIMIT
    upper = theorem_bound(ell)
    step = 2 * ell
    first_k = lower // step + 1
    last_k = (upper - 1) // step
    indexed_primes: list[dict[str, int]] = []
    prime_candidates = 0
    progression_candidates = max(0, last_k - first_k + 1)
    for k in range(first_k, last_k + 1):
        p = step * k + 1
        if not is_prime(p):
            continue
        prime_candidates += 1
        index_data = subgroup_index_minus_one_two(p, ell)
        if index_data is None:
            continue
        subgroup_size, _order = index_data
        indexed_primes.append(find_witness(p, ell, subgroup_size, distinct_prime_factors(p - 1)))
    return {
        "schema_version": 1,
        "claim_target": "Conjecture B for every odd prime p with [F_p^*: <-1,2>] = 3003",
        "ell": ell,
        "ell_factorization": [3, 7, 11, 13] if ell == ELL else distinct_prime_factors(ell),
        "literature_computation_limit_inclusive": lower,
        "theorem_bound_inclusive": upper,
        "searched_prime_interval": {"lower_exclusive": lower, "upper_exclusive": upper},
        "progression": {"form": "p = 1 + 2*ell*k", "first_k": first_k, "last_k": last_k},
        "progression_candidate_count": progression_candidates,
        "prime_candidate_count": prime_candidates,
        "indexed_prime_count": len(indexed_primes),
        "indexed_primes": indexed_primes,
        "scope": {
            "establishes": [
                "An exact finite enumeration of the published gap for ell=3003 under the implemented arithmetic tests.",
                "A Conjecture B witness for every indexed prime found in that finite interval."
            ],
            "does_not_establish": [
                "Correctness of the cited literature results below and above the finite interval.",
                "Novelty, independent reproduction, external review, or a universal theorem by computation alone.",
                "Any result for indices other than ell=3003."
            ]
        }
    }


def canonical_bytes(report: dict[str, object]) -> bytes:
    return (json.dumps(report, indent=2, sort_keys=True) + "\n").encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Close the finite ell=3003 Conjecture B gap")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = canonical_bytes(generate_report())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(payload)
    report = json.loads(payload)
    print(f"wrote {args.output}")
    print(f"sha256={hashlib.sha256(payload).hexdigest()}")
    print(f"indexed_primes={report['indexed_prime_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
