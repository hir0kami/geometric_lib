import math


class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __repr__(self):
        return f"Circle(radius={self.radius})"


class Square:
    def __init__(self, side_length):
        if side_length <= 0:
            raise ValueError("Side length must be a positive number.")
        self.side_length = side_length

    def area(self):
        return self.side_length**2

    def perimeter(self):
        return 4 * self.side_length

    def __repr__(self):
        return f"Square(side_length={self.side_length})"


figs = ["circle", "square"]
funcs = ["perimeter", "area"]
sizes = {}

if __name__ == "__main__":
    print("Shapes and their functionalities are ready to use!")
