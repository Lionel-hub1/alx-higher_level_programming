#!/usr/bin/python3
"""A class for square"""


class Square:
    """
    This class defines a square
    """

    def __init__(self, size=0):
        """
        The Square constructor

        Args:
        size: The size of the square side in int type.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        This function calculates the area
        """
        return self.__size ** 2
