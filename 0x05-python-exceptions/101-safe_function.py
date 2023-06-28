#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """
    This function executes the function safely

    Args:
    fct: Is the function to be executed safely
    args: Are the arguments of that function

    Returns:
    None in case of exception(s) or simply the result of the function
    """
    try:
        result = fct(*args)
        return (result)
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return (None)
