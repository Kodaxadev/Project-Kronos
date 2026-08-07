from __future__ import annotations


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


def covered_by_reconciled_2023_ranges(ell: int) -> bool:
    """Encode only the numerical ranges stated in the Gate 0 literature intake."""
    if ell <= 3000:
        return True
    count = len(distinct_prime_factors(ell))
    if count == 1 and ell < 16411:
        return True
    if count == 2 and ell < 8197:
        return True
    if count == 3 and ell < 4100:
        return True
    if ell < 2070:
        return True
    return False


def first_uncovered(start: int = 3) -> int:
    ell = start
    while covered_by_reconciled_2023_ranges(ell):
        ell += 1
    return ell


def main() -> int:
    value = first_uncovered()
    factors = distinct_prime_factors(value)
    print(f"first_uncovered={value}")
    print("distinct_prime_factors=" + "*".join(str(item) for item in factors))
    if value != 3003 or factors != [3, 7, 11, 13]:
        raise SystemExit("reconciled range calculation did not reproduce ell=3003")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
