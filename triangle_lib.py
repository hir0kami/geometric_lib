import math


class Triangle:
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("All sides must be positive numbers.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("The given sides do not form a valid triangle.")
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def __repr__(self):
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"
