
# Main sentinel.
if __name__ == "__main__":
    raise Exception(
        "find_ft_type: find_ft_type is a library, and cannot be used as main."
    )


def all_thing_is_obj(obj: any) -> int:
    ty = type(obj)
    ty_name = ty.__name__
    types = ["list", "tuple", "set", "dict", "str"]

    if ty_name not in types:
        print("Type not found")
        return 42

    ty_name = ty_name[0].upper() + ty_name[1:]

    if ty_name == "Str":
        print(f"{obj} is in the kitchen : {ty}")
        return 42

    print(f"{ty_name} : {ty}")
    return 42
