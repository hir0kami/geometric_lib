import unittest

from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_negative_side(self):
        side = -1
        with self.assertRaises(ValueError):
            area(side)
        with self.assertRaises(ValueError):
            perimeter(side)

    def test_zero_side(self):
        side = 0
        expected_area = 0
        expected_perimeter = 0

        self.assertEqual(area(side), expected_area)
        self.assertEqual(perimeter(side), expected_perimeter)

    def test_positive_side(self):
        side = 2
        expected_area = 4
        expected_perimeter = 8

        self.assertEqual(area(side), expected_area)
        self.assertEqual(perimeter(side), expected_perimeter)

    def test_large_side(self):
        side = 1e6
        expected_area = side**2
        expected_perimeter = 4 * side

        self.assertEqual(area(side), expected_area)
        self.assertEqual(perimeter(side), expected_perimeter)


if __name__ == "__main__":
    unittest.main()
