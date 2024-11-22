import math

def area(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Sides of a triangle cannot be negative")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The given sides do not form a valid triangle")
    s = (a + b + c) / 2  # Semi-perimeter
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def perimeter(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Sides of a triangle cannot be negative")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The given sides do not form a valid triangle")
    return a + b + c
