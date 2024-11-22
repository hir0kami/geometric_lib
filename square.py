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
