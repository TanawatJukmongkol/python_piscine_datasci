import sys


def main(argc: int, argv: list[str]) -> int:
    """
    Main function for the Morse code encoder.

    Parameters:
        argc (int): Number of command-line arguments.
        argv (list[str]): Command-line argument list where argv[1] is the
                          string to encode.

    Returns:
        int: 0 on success.

    Raises:
        AssertionError: If argument count is incorrect or if an unsupported
                        character is encountered.
    """
    assert argc == 2, "the arguments are bad"

    NESTED_MORSE = {
        " ": "/ ", "A": ".- ", "B": "-... ",
        "C": "-.-. ", "D": "-.. ", "E": ". ",
        "F": "..-. ", "G": "--. ", "H": ".... ",
        "I": ".. ", "J": ".--- ", "K": "-.- ",
        "L": ".-.. ", "M": "-- ", "N": "-. ",
        "O": "--- ", "P": ".--. ", "Q": "--.- ",
        "R": ".-. ", "S": "... ", "T": "- ",
        "U": "..- ", "V": "...- ", "W": ".-- ",
        "X": "-..- ", "Y": "-.-- ", "Z": "--.. ",
        "0": "----- ", "1": ".---- ", "2": "..--- ",
        "3": "...-- ", "4": "....- ", "5": "..... ",
        "6": "-.... ", "7": "--... ", "8": "---.. ",
        "9": "----. "
    }

    res = ""

    for i in argv[1]:
        key = i.upper()
        assert key in NESTED_MORSE, "the arguments are bad"
        res += NESTED_MORSE[key]

    print(res)

    return 0


if __name__ == "__main__":
    argv = sys.argv
    sys.exit(main(len(argv), argv))
