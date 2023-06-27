#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divides two integers and prints the result.

    Args:
    a: The numerator (dividend).
    b: The denominator (divisor).

    Returns:
    The value of the division, or None if division by zero occurs.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
