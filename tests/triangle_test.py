import unittest
import math
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_zero_sides(self):
        a, b, c = 0, 0, 0
        with self.assertRaises(ValueError):
            area(a, b, c)
        with self.assertRaises(ValueError):
            perimeter(a, b, c)

    def test_positive_sides(self):
        a, b, c = 3, 4, 5
        expected_area = 6
        expected_perimeter = 12
        self.assertAlmostEqual(area(a, b, c), expected_area, places=5)
        self.assertEqual(perimeter(a, b, c), expected_perimeter)

    def test_invalid_triangle(self):
        a, b, c = 1, 2, 10
        with self.assertRaises(ValueError):
            area(a, b, c)
        with self.assertRaises(ValueError):
            perimeter(a, b, c)

    def test_negative_sides(self):
        a, b, c = -3, 4, 5
        with self.assertRaises(ValueError):
            area(a, b, c)
        with self.assertRaises(ValueError):
            perimeter(a, b, c)

    def test_non_numeric_sides(self):
        a, b, c = "string", 4, 5
        with self.assertRaises(TypeError):
            area(a, b, c)
        with self.assertRaises(TypeError):
            perimeter(a, b, c)


if __name__ == "__main__":
    unittest.main()
