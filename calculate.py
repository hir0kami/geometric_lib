import math

figs = ["circle", "square"]
funcs = ["perimeter", "area"]

sizes = {"circle": 1, "square": 1}


def calc(fig, func, size):
    if fig not in figs:
        raise ValueError(f"Invalid figure: {fig}")
    if func not in funcs:
        raise ValueError(f"Invalid function: {func}")

    try:
        if fig == "circle":
            expression = (
                f"2 * math.pi * {size[0]}"
                if func == "perimeter"
                else f"math.pi * {size[0]}**2"
            )
        elif fig == "square":
            expression = (
                f"4 * {size[0]}" if func == "perimeter" else f"{size[0]}**2"
            )
        result = eval(expression, {"math": math})
        return result
    except Exception as e:
        raise ValueError(
            f"Error calculating {func} for {fig} with size {size}: {e}"
        )


if __name__ == "__main__":
    func = ""
    fig = ""
    size = []

    while fig not in figs:
        fig = input(
            f"Enter figure name, available options are {figs}: "
        ).strip()

    while func not in funcs:
        func = input(
            f"Enter function name, available options are {funcs}: "
        ).strip()

    expected_size_count = sizes.get(fig, 1)
    while len(size) != expected_size_count:
        try:
            size = list(
                map(
                    float,
                    input(
                        f"Input figure sizes separated by space "
                        f"({expected_size_count} values expected): "
                    ).split(),
                )
            )
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    try:
        result = calc(fig, func, size)
        print(
            f"The {func} of the {fig} with size {size} is {result: .2f}."
        )
    except ValueError as e:
        print(e)
