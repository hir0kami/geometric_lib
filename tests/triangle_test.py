import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_negative_sides(self):
        with self.assertRaises(ValueError):
            area(-1, 2, 3)
        with self.assertRaises(ValueError):
            perimeter(-1, 2, 3)

    def test_zero_sides(self):
        with self.assertRaises(ValueError):
            area(0, 2, 3)
        with self.assertRaises(ValueError):
            perimeter(0, 2, 3)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            area(1, 2, 10)
        with self.assertRaises(ValueError):
            perimeter(1, 2, 10)

    def test_zero_area(self):
        with self.assertRaises(ValueError):
            area(1, 1, 2)

    def test_valid_triangle(self):
        a, b, c = 3, 4, 5
        expected_area = 6
        expected_perimeter = 12

        self.assertAlmostEqual(area(a, b, c), expected_area, places=7)
        self.assertEqual(perimeter(a, b, c), expected_perimeter)

    def test_large_triangle(self):
        a, b, c = 1e6, 1e6, 1e6
        s = (a + b + c) / 2
        expected_area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        expected_perimeter = a + b + c

        self.assertAlmostEqual(area(a, b, c), expected_area, places=7)
        self.assertEqual(perimeter(a, b, c), expected_perimeter)


if __name__ == "__main__":
    unittest.main()
