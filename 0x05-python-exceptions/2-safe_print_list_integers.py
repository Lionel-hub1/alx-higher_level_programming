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
    index = 0
    try:
        while count < x:
            value = my_list[index]
            try:
                print("{:d}".format(value), end="")
                count += 1
            except (ValueError, TypeError):
                pass
            index += 1
    except IndexError:
        pass

    print()
    return count
