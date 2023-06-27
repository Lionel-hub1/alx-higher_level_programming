#!/usr/bin/python3
def raise_exception_msg(message=""):
    """
    Raises a name exception with a custom message.

    Args:
    message: The custom error message to be raised.

    Raises:
    NameError: Always raises a NameError with the provided message.
    """
    raise NameError(message)
