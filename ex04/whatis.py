import sys


def main(argc: int, argv: list[str]) -> int:
    if argc == 1:
        return 0

    if argc > 2:
        print("AssertionError: more than one argument is provided")
        return 1

    try:
        number = int(argv[1])
        print("I'm Even." if number % 2 == 0 else "I'm Odd.")
    except ValueError:
        print("AssertionError: argument is not an integer")
        return 1

    return 0


if __name__ == "__main__":
    argv = sys.argv
    sys.exit(main(len(argv), argv))
