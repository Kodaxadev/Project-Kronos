import unittest

from kronos.cac import canonical_translate, difference_set, enumerate_translation_classes, is_cac


class CacDefinitionTests(unittest.TestCase):
    def test_translation_canonicalization(self) -> None:
        self.assertEqual(canonical_translate((2, 4, 7), 11), canonical_translate((0, 2, 5), 11))

    def test_difference_set_is_translation_invariant(self) -> None:
        self.assertEqual(difference_set((0, 2, 5), 11), difference_set((3, 5, 8), 11))

    def test_known_conflict(self) -> None:
        self.assertFalse(is_cac([(0, 1, 2), (0, 1, 3)], 7))

    def test_single_codeword_is_valid(self) -> None:
        self.assertTrue(is_cac([(0, 1, 2)], 7))

    def test_translation_classes_have_unique_representatives(self) -> None:
        classes = enumerate_translation_classes(7, 3)
        self.assertEqual(len(classes), len(set(classes)))
        self.assertTrue(all(word == canonical_translate(word, 7) for word in classes))


if __name__ == "__main__":
    unittest.main()
