#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """
    This function Prints integer using formatted string

    Args:
    value: Is the number for printing

    Returns:
    False incase of an exception, otherwise return True
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
