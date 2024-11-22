import math


class Circle:
    @staticmethod
    def perimeter(radius):
        return 2 * math.pi * radius

    @staticmethod
    def area(radius):
        return math.pi * radius**2


class Square:
    @staticmethod
    def perimeter(side_length):
        return 4 * side_length

    @staticmethod
    def area(side_length):
        return side_length**2


figs = ["circle", "square"]
funcs = ["perimeter", "area"]
sizes = {"circle": 1, "square": 1}


def calc(fig, func, size):
    if fig not in figs:
        raise ValueError(f"Invalid figure: {fig}")
    if func not in funcs:
        raise ValueError(f"Invalid function: {func}")
    try:
        cls = Circle if fig == "circle" else Square
        method = getattr(cls, func)
        return method(*size)
    except Exception as e:
        raise ValueError(f"Error calculating {func} for {fig} with size {size}: {e}")


if __name__ == "__main__":
    func = ""
    fig = ""
    size = []

    while fig not in figs:
        fig = input(f"Enter figure name, available options are {figs}: ").strip()

    while func not in funcs:
        func = input(f"Enter function name, available options are {funcs}: ").strip()

    expected_size_count = sizes.get(fig, 1)
    while len(size) != expected_size_count:
        try:
            size = list(
                map(
                    float,
                    input(
                        f"Input figure sizes separated by space ({expected_size_count} values expected): "
                    ).split(),
                )
            )
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    try:
        result = calc(fig, func, size)
        print(f"The {func} of the {fig} with size {size} is {result:.2f}.")
    except ValueError as e:
        print(e)
