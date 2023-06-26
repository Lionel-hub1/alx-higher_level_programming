#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list.

    Args:
    my_list: The list to print.
    x: The number of elements to print.

    Returns:
    The real number of elements printed.
    """
    real_len = 0
    try:
        for element in range(x):
            print(my_list[element], end="")
            real_len += 1
            if real_len == x:
                break
    except IndexError:
        pass

    print()
    return real_len
