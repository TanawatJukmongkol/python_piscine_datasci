from typing import Iterable, Callable


# Main sentinel.
if __name__ == "__main__":
    raise Exception(
        "ft_filter: cannot be used as main."
    )


def ft_filter(fn: Callable | None, iter: Iterable) -> list[any]:
    # Firetruck you flake8!!!
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    return [i for i in iter if fn(i)]


# print(ft_filter.__doc__ == filter.__doc__)
