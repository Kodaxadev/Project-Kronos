import unittest

from kronos.conjecture_b import Witness, conjecture_b_witness, scan_primes, verify_witness


class ConjectureBTests(unittest.TestCase):
    def test_p73_has_verified_witness(self) -> None:
        witness = conjecture_b_witness(73)
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertTrue(verify_witness(witness))
        self.assertEqual(witness.ell, 4)

    def test_material_corruption_is_rejected(self) -> None:
        witness = conjecture_b_witness(73)
        assert witness is not None
        corrupted = Witness(
            witness.p,
            witness.ell,
            witness.subgroup_size,
            witness.t,
            witness.b,
            (witness.c + 1) % witness.p,
        )
        self.assertFalse(verify_witness(corrupted))

    def test_small_scan_is_complete_and_has_no_recorded_failure(self) -> None:
        report = scan_primes(500)
        self.assertEqual(report["applicable_prime_count"], len(report["records"]) + len(report["failures"]))
        self.assertEqual(report["failures"], [])


if __name__ == "__main__":
    unittest.main()
