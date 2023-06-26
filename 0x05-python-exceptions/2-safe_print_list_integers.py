#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list, skipping non-integer values.

    Args:
    my_list: The list to print.
    x: The number of elements to access in my_list.

    Returns:
    The real number of integers printed.
    """
    count = 0
    for element in range(0, x):
        try:
            print("{:d}".format(my_list[element]), end="")
            count += 1
        except (ValueError, TypeError):
            continue

    print()
    return count
