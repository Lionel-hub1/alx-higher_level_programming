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
        self.size = size

    @property
    def size(self):
        """
        The getter for size of square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        The setter for size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        This function calculates the area
        """
        return self.__size ** 2
