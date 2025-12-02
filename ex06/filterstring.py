import sys
from ft_filter import ft_filter


def check_args(argc: int, argv: list[str]) -> int:
    """
    Validates command-line arguments.

    Parameters:
        argc (int): Number of command-line arguments.
        argv (list[str]): List of command-line arguments.

    Returns:
        int: 0 if arguments are valid, 1 otherwise.

    Validation rules:
        - Exactly 3 arguments must be provided.
        - The third argument must be an integer.
    """
    if argc != 3:
        return 1
    try:
        int(argv[2])
    except ValueError:
        return 1
    return 0


def main(argc: int, argv: list[str]) -> int:
    """
    Main entry point for the script.


    Parameters:
        argc (int): Number of command-line arguments.
        argv (list[str]): List of command-line arguments.

    Returns:
        int: Exit status code (0 for success, 1 for failure).

    Operation:
        - Validates the command-line arguments.
        - Converts the third argument to an integer for word length filtering.
        - Uses `ft_filter` to filter words longer than the given length.
        - Prints the filtered list.
    """

    assert check_args(argc, argv) == 0, "the arguments are bad"

    len_filter = int(argv[2])
    filtered_lst = ft_filter(lambda i: len(i) > len_filter, argv[1].split(" "))

    print(filtered_lst)

    return 0


if __name__ == "__main__":
    argv = sys.argv
    sys.exit(main(len(argv), argv))
