#!/usr/bin/python3
def safe_print_integer(value):
    """
    Args:
    value: The value to be printed as an integer.

    Returns:
    True if the value was successfully printed as an integer, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
