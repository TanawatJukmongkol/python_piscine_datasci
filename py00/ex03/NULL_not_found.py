
# Main sentinel.
if __name__ == "__main__":
    raise Exception(
        "NULL_not_found: cannot be used as main."
    )


def NULL_not_found(obj: any) -> int:
    ty = type(obj)
    ty_name = ty.__name__
    # NaN is defined by the IEEE-754 where the value is not equal to itself.
    is_nan = ty == float and (obj != obj)

    if obj == 0:
        print(f"Zero: {obj} {ty}")
        return 0

    match ty_name:
        case "NoneType":
            # None
            print("Nothing: ", end="")
        case "float":
            # NaN
            if not is_nan:
                print("Type not Found")
                return 1
            print("Cheese: ", end="")
        case "str":
            # Empty string
            if obj != "":
                print("Type not Found")
                return 1
            print("Empty: ", end="")
        case "bool":
            # Fake clases (artificial)
            print("Fake: ", end="")
        case _:
            print("Type not Found")
            return 1

    print(f"{obj} {ty}")

    return 0
