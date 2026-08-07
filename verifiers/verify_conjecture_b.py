"""Standalone verifier for finite Conjecture B scan reports.

This file intentionally does not import the kronos package. It is a separately
implemented checker, not an independent reproduction by a distinct researcher.
"""
from __future__ import annotations

import argparse
import json
from math import isqrt
from pathlib import Path


def prime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


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


def primitive_root(value: int, p: int) -> bool:
    if not 1 <= value < p:
        return False
    return all(pow(value, (p - 1) // factor, p) != 1 for factor in distinct_prime_factors(p - 1))


def subgroup(p: int) -> set[int]:
    values: set[int] = set()
    x = 1
    while x not in values:
        values.add(x)
        values.add((-x) % p)
        x = (2 * x) % p
    return values


def verify_record(record: dict[str, int]) -> bool:
    required = {"p", "ell", "subgroup_size", "t", "b", "c"}
    if set(record) != required:
        return False
    p = record["p"]
    if p == 2 or not prime(p):
        return False
    h = subgroup(p)
    ell = (p - 1) // len(h)
    if ell < 3 or record["ell"] != ell or record["subgroup_size"] != len(h):
        return False
    t, b, c = record["t"], record["b"], record["c"]
    if not (1 <= t < p and 1 <= b < p and 1 <= c < p):
        return False
    if not primitive_root(t, p):
        return False
    if b not in {t * x % p for x in h}:
        return False
    if c not in {(t * t % p) * x % p for x in h}:
        return False
    return (1 + b) % p == c


def verify_report(report: dict[str, object]) -> tuple[bool, str]:
    expected_keys = {
        "schema_version",
        "target",
        "limit",
        "applicable_prime_count",
        "records",
        "failures",
        "scope_note",
    }
    if set(report) != expected_keys or report.get("schema_version") != 1:
        return False, "unexpected report schema"
    limit = report.get("limit")
    records = report.get("records")
    failures = report.get("failures")
    if not isinstance(limit, int) or limit < 3:
        return False, "invalid limit"
    if not isinstance(records, list) or not isinstance(failures, list):
        return False, "records and failures must be lists"

    applicable: dict[int, int] = {}
    for p in range(3, limit + 1, 2):
        if prime(p):
            h = subgroup(p)
            ell = (p - 1) // len(h)
            if ell >= 3:
                applicable[p] = ell

    represented: set[int] = set()
    for record in records:
        if not isinstance(record, dict) or not verify_record(record):
            return False, "invalid primitive-root witness record"
        p = record["p"]
        if p in represented:
            return False, "duplicate prime"
        represented.add(p)
    for failure in failures:
        if not isinstance(failure, dict) or set(failure) != {"p", "ell"}:
            return False, "invalid failure record"
        p, ell = failure["p"], failure["ell"]
        if applicable.get(p) != ell or p in represented:
            return False, "invalid or duplicate failure"
        represented.add(p)

    if represented != set(applicable):
        return False, "report is incomplete for its declared limit"
    if report.get("applicable_prime_count") != len(applicable):
        return False, "applicable prime count mismatch"
    return True, "verified"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    report = json.loads(args.report.read_text(encoding="utf-8"))
    ok, message = verify_report(report)
    print(message)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
