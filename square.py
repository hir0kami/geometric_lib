def area(side):
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return side * side


def perimeter(side):
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return 4 * side
