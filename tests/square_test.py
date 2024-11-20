square_test
import unittest

from square import area, perimeter  # Предполагается, что функции находятся в файле square.py

class SquareTestCase(unittest.TestCase):
    def test_negative_side(self):
        """Тест на случай отрицательной стороны квадрата."""
        side = -1
        with self.assertRaises(ValueError):  # Предполагаем, что функции должны выбрасывать ValueError
            area(side)
        with self.assertRaises(ValueError):
            perimeter(side)

    def test_zero_side(self):
        """Тест на случай стороны квадрата равной нулю."""
        side = 0
        expected_area = 0
        expected_perimeter = 0

        self.assertEqual(area(side), expected_area)
        self.assertEqual(perimeter(side), expected_perimeter)

    def test_positive_side(self):
        """Тест для положительной стороны квадрата."""
        side = 2
        expected_area = 4  # 2 * 2
        expected_perimeter = 8  # 4 * 2

        self.assertEqual(area(side), expected_area)
        self.assertEqual(perimeter(side), expected_perimeter)

    def test_large_side(self):
        """Тест для большой стороны квадрата."""
        side = 1e6
        expected_area = side ** 2
        expected_perimeter = 4 * side

        self.assertEqual(area(side), expected_area)
        self.assertEqual(perimeter(side), expected_perimeter)

if __name__ == "__main__":
    unittest.main()