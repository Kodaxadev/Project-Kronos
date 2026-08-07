import unittest

from scripts.close_index_3003 import (
    ELL,
    distinct_prime_factors,
    subgroup_index_minus_one_two,
    theorem_bound,
)
from scripts.find_first_uncovered_index import first_uncovered


class Index3003Tests(unittest.TestCase):
    def test_first_uncovered_index_and_threshold(self) -> None:
        self.assertEqual(first_uncovered(), ELL)
        self.assertEqual(distinct_prime_factors(ELL), [3, 7, 11, 13])
        self.assertEqual(theorem_bound(ELL), 2304192002)

    def test_first_recorded_prime_has_exact_target_index(self) -> None:
        self.assertEqual(
            subgroup_index_minus_one_two(1392401011, ELL),
            (463670, 463670),
        )

    def test_nearby_non_target_value_is_not_misclassified(self) -> None:
        self.assertIsNone(subgroup_index_minus_one_two(1392401017, ELL))


if __name__ == "__main__":
    unittest.main()
