import sys


# For testing purposes
"""
 python building.py "Python 3.0, released in 2008, was a major revision
 that is not completely backward compatible with earlier versions. Python
 2 was discontinued with version 2.7.18 in 2020."
"""


def count_filter(fn: callable, obj: any) -> int:
    """
        count filter

        Args:
            fn (callable): function that returns a boolean for object filter
            obj (any): any object to filter.

        Returns:
            int: the counts of the filtered object.
    """
    return len(list(filter(fn, obj)))


def main(argc: int, argv: list[str]) -> int:
    """
        main function

        Args:
            argc (int): number of arguments passed to the program.
            argv (list[str]): list of command-line arguments.

        Returns:
            int: exit status code. Returns 0 on success and
                1 on argument error.

        Description:
            This function validates the number of provided command-line
            arguments and processes a single input string. It counts
            various character types in the string, including:

            - total characters
            - uppercase letters
            - lowercase letters
            - punctuation marks
            - spaces
            - digits

            If no argument is given, it prints a usage message. If more
            than one argument is provided, it prints an error message.
            Otherwise, it analyzes the given string and prints a summary
            of the character counts.
    """

    if argc == 1 or argv[1] == "":
        print("usage: python3 building.py \"strings to count characters\"")
        return 0

    assert argc <= 2, "AssertionError: more than one argument is provided"

    punctuation_marks = [
        ".", ",", "!", "?", ":", ";",
        "-", "–", "—",
        "(", ")", "[", "]", "{", "}",
        "'", '"',
        "...",
        "/", "\\",
        "@", "#", "$", "%", "&", "*", "+", "=", "<", ">", "^", "_", "|", "~"
    ]

    string = argv[1]
    characters = len(string)
    caps = count_filter(lambda i: i.isupper(), string)
    lows = count_filter(lambda i: i.islower(), string)
    punct = count_filter(lambda i: i in punctuation_marks, string)
    spaces = count_filter(lambda i: i == " ", string)
    digits = count_filter(lambda i: i.isdigit(), string)

    print(f"The text contains {characters} characters:")
    if caps:
        print(f"{caps} upper letters")
    if lows:
        print(f"{lows} lower letters")
    if punct:
        print(f"{punct} punctuation marks")
    if spaces:
        print(f"{spaces} spaces")
    if digits:
        print(f"{digits} digits")

    return 0


if __name__ == "__main__":
    argv = sys.argv
    sys.exit(main(len(argv), argv))
