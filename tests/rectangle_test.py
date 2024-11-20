rectangle_test
import unittest
from rectangle import area, perimeter  # Предполагается, что функции находятся в файле rectangle.py

class RectangleTestCase(unittest.TestCase):
    def test_negative_sides(self):
        """Тест на случай отрицательных сторон прямоугольника."""
        with self.assertRaises(ValueError):  # Проверяем, выбрасывается ли ValueError
            area(-1, 2)
        with self.assertRaises(ValueError):
            perimeter(-1, 2)

    def test_zero_sides(self):
        """Тест на случай сторон прямоугольника равных нулю."""
        with self.assertRaises(ValueError):  # Нулевые стороны недопустимы
            area(0, 5)
        with self.assertRaises(ValueError):
            perimeter(0, 5)

    def test_valid_rectangle(self):
        """Тест для корректного прямоугольника."""
        a, b = 3, 4
        expected_area = 12  # 3 * 4
        expected_perimeter = 14  # 2 * (3 + 4)

        self.assertEqual(area(a, b), expected_area)
        self.assertEqual(perimeter(a, b), expected_perimeter)

    def test_square(self):
        """Тест для случая, когда прямоугольник является квадратом."""
        a, b = 5, 5
        expected_area = 25  # 5 * 5
        expected_perimeter = 20  # 2 * (5 + 5)

        self.assertEqual(area(a, b), expected_area)
        self.assertEqual(perimeter(a, b), expected_perimeter)

    def test_large_rectangle(self):
        """Тест для прямоугольника с большими сторонами."""
        a, b = 1e6, 2e6
        expected_area = a * b
        expected_perimeter = 2 * (a + b)

        self.assertEqual(area(a, b), expected_area)
        self.assertEqual(perimeter(a, b), expected_perimeter)

if __name__ == "__main__":
    unittest.main()

