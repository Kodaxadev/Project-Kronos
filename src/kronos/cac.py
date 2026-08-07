from __future__ import annotations

from itertools import combinations
from typing import Iterable, Sequence

Codeword = tuple[int, ...]


def _validate_word(word: Sequence[int], n: int) -> tuple[int, ...]:
    if n < 2:
        raise ValueError("length n must be at least 2")
    normalized = tuple(int(x) % n for x in word)
    if len(normalized) < 2:
        raise ValueError("a codeword must contain at least two positions")
    if len(set(normalized)) != len(normalized):
        raise ValueError("codeword positions must be distinct modulo n")
    return normalized


def canonical_translate(word: Sequence[int], n: int) -> Codeword:
    """Return the lexicographically least translate of a cyclic codeword."""
    values = _validate_word(word, n)
    candidates = [tuple(sorted((x - shift) % n for x in values)) for shift in values]
    return min(candidates)


def difference_set(word: Sequence[int], n: int) -> frozenset[int]:
    """Return all nonzero ordered differences x-y modulo n."""
    values = _validate_word(word, n)
    return frozenset((x - y) % n for x in values for y in values if x != y)


def is_cac(codewords: Iterable[Sequence[int]], n: int) -> bool:
    """Check the defining pairwise-disjoint-difference condition."""
    used: set[int] = set()
    for word in codewords:
        support = set(difference_set(word, n))
        if used.intersection(support):
            return False
        used.update(support)
    return True


def enumerate_translation_classes(n: int, weight: int = 3) -> list[Codeword]:
    """Enumerate cyclic translation classes of constant-weight codewords."""
    if not 2 <= weight <= n:
        raise ValueError("weight must satisfy 2 <= weight <= n")
    classes = {
        canonical_translate(word, n)
        for word in combinations(range(n), weight)
    }
    return sorted(classes)
