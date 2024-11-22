import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_zero_side(self):
        side = 0
        expected_area = 0
        expected_perimeter = 0
        self.assertEqual(area(side), expected_area)
        self.assertEqual(perimeter(side), expected_perimeter)

    def test_positive_side(self):
        side = 4
        expected_area = 16
        expected_perimeter = 16
        self.assertEqual(area(side), expected_area)
        self.assertEqual(perimeter(side), expected_perimeter)

    def test_negative_side(self):
        side = -4
        with self.assertRaises(ValueError):
            area(side)
        with self.assertRaises(ValueError):
            perimeter(side)

    def test_non_numeric_side(self):
        side = "string"
        with self.assertRaises(TypeError):
            area(side)
        with self.assertRaises(TypeError):
            perimeter(side)


if __name__ == "__main__":
    unittest.main()
