import unittest
from calculate import calc, figs, funcs


class TestCalcFunction(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(calc("circle", "area", [10]), 314.1592653589793)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(calc("circle", "perimeter", [10]), 62.83185307179586)

    def test_square_area(self):
        self.assertEqual(calc("square", "area", [5]), 25)

    def test_square_perimeter(self):
        self.assertEqual(calc("square", "perimeter", [5]), 20)

    def test_invalid_figure(self):
        with self.assertRaises(AssertionError):
            calc("triangle", "area", [5])

    def test_invalid_function(self):
        with self.assertRaises(AssertionError):
            calc("circle", "volume", [5])

    def test_invalid_size(self):
        with self.assertRaises(ValueError):
            calc("circle", "area", [5, 10])


if __name__ == "__main__":
    unittest.main()
