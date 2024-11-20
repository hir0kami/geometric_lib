#circle_test
import unittest
import math
import sys
sys.path.append("..")

from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_negative_radius(self):
        """Тест на случай отрицательного радиуса."""
        radius = -1
        with self.assertRaises(ValueError):  # Убедитесь, что выбрасывается ValueError
            area(radius)
        with self.assertRaises(ValueError):
            perimeter(radius)

    def test_zero_radius(self):
        """Тест на случай радиуса равного нулю."""
        radius = 0
        expected_area = 0
        expected_perimeter = 0

        self.assertEqual(area(radius), expected_area)
        self.assertEqual(perimeter(radius), expected_perimeter)

    def test_positive_radius(self):
        """Тест для положительного радиуса."""
        radius = 1
        expected_area = math.pi
        expected_perimeter = 2 * math.pi

        self.assertAlmostEqual(area(radius), expected_area, places=7)
        self.assertAlmostEqual(perimeter(radius), expected_perimeter, places=7)

    def test_large_radius(self):
        """Тест для большого радиуса."""
        radius = 1e6
        expected_area = math.pi * (radius ** 2)
        expected_perimeter = 2 * math.pi * radius

        self.assertAlmostEqual(area(radius), expected_area, places=7)
        self.assertAlmostEqual(perimeter(radius), expected_perimeter, places=7)

if __name__ == "__main__":
    unittest.main()