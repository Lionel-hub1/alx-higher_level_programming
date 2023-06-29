#!/usr/bin/python3


def magic_calculation(a, b):
    """
    Performs a magic calculation based on the given inputs.

    Args:
    a: An integer representing the first input.
    b: An integer representing the second input.

    Returns:
    The result of the magic calculation.
    """
    result = 0
    for number in range(1, 3):
        try:
            if number > a:
                raise Exception('Too far')
            else:
                result += a ** b / number
        except:
            result = b + a
            break
    return result
