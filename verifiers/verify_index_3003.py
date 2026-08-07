from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

ELL = 3003
LOWER = 2**30
EXPECTED_FACTORS = (3, 7, 11, 13)


def base_primes(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return [i for i, value in enumerate(sieve) if value]


def factor_distinct(n: int, primes: list[int]) -> list[int]:
    out: list[int] = []
    for q in primes:
        if q * q > n:
            break
        if n % q == 0:
            out.append(q)
            while n % q == 0:
                n //= q
    if n > 1:
        out.append(n)
    return out


def exact_order(a: int, order: int, p: int, factors: list[int]) -> bool:
    return pow(a, order, p) == 1 and all(pow(a, order // q, p) != 1 for q in factors)


def theorem_bound(ell: int) -> int:
    omega = len(EXPECTED_FACTORS) if ell == ELL else len(factor_distinct(ell, base_primes(math.isqrt(ell))))
    delta = 1 if ell % 4 == 0 else 0
    return (2**omega * (ell - 3 - delta) + 2) ** 2 - 2


def prime_progression(lower: int, upper: int, step: int) -> tuple[list[int], int, int]:
    first_k = lower // step + 1
    last_k = (upper - 1) // step
    composite = bytearray(last_k - first_k + 1)
    for q in base_primes(math.isqrt(upper - 1)):
        if step % q == 0:
            continue
        residue = (-pow(step, -1, q)) % q
        start = residue
        if start < first_k:
            start += ((first_k - start + q - 1) // q) * q
        for k in range(start, last_k + 1, q):
            composite[k - first_k] = 1
    values = [step * k + 1 for k in range(first_k, last_k + 1) if not composite[k - first_k]]
    return values, first_k, last_k


def has_target_index(p: int, ell: int, small_primes: list[int]) -> tuple[int, int] | None:
    h = (p - 1) // ell
    if h % 2:
        return None
    if exact_order(2, h, p, factor_distinct(h, small_primes)):
        return h, h
    half = h // 2
    if half % 2 and exact_order(2, half, p, factor_distinct(half, small_primes)):
        return h, half
    return None


def verify_primitive_root(g: int, p: int, factors: list[int]) -> bool:
    return 1 < g < p and all(pow(g, (p - 1) // q, p) != 1 for q in factors)


def verify(path: Path) -> None:
    report = json.loads(path.read_text(encoding="utf-8"))
    assert report["schema_version"] == 1
    assert report["ell"] == ELL
    assert tuple(report["ell_factorization"]) == EXPECTED_FACTORS
    upper = theorem_bound(ELL)
    assert report["literature_computation_limit_inclusive"] == LOWER
    assert report["theorem_bound_inclusive"] == upper
    primes, first_k, last_k = prime_progression(LOWER, upper, 2 * ELL)
    assert report["progression"]["first_k"] == first_k
    assert report["progression"]["last_k"] == last_k
    assert report["progression_candidate_count"] == last_k - first_k + 1
    assert report["prime_candidate_count"] == len(primes)
    small_primes = base_primes(1000)
    indexed: list[tuple[int, int, int]] = []
    for p in primes:
        data = has_target_index(p, ELL, small_primes)
        if data is not None:
            indexed.append((p, data[0], data[1]))
    records = report["indexed_primes"]
    assert report["indexed_prime_count"] == len(records) == len(indexed)
    assert [item["p"] for item in records] == [item[0] for item in indexed]
    for record, (p, subgroup_size, order_of_2) in zip(records, indexed, strict=True):
        assert record["ell"] == ELL
        assert record["subgroup_size"] == subgroup_size
        assert record["order_of_2"] == order_of_2
        factors_pm1 = factor_distinct(p - 1, base_primes(math.isqrt(p - 1)))
        g = record["primitive_root"]
        t = record["quotient_generator"]
        assert g == t
        assert verify_primitive_root(g, p, factors_pm1)
        inv_t = pow(t, -1, p)
        b = record["b"]
        c = record["c"]
        assert 0 < b < p and 0 < c < p
        assert pow((b * inv_t) % p, subgroup_size, p) == 1
        assert pow((c * inv_t * inv_t) % p, subgroup_size, p) == 1
        assert (1 + b) % p == c


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify the ell=3003 gap report")
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    verify(args.report)
    print("VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
