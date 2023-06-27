#!/usr/bin/python3
"""A class for square"""


class Square:
    """
    This class defines a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        The Square constructor

        Args:
        size: The size of the square side in int type.
        position (int, int): The position of the object of a square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        The getter for size of square
        """
        return (self.__size)

    @property
    def position(self):
        """
        The getter for position of square
        """
        return (self.__position)

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

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        This function calculates the area
        """
        return self.__size ** 2

    def my_print(self):
        """
        This function prints our square using #(s)
        """
        if self.__size == 0:
            print()
            return

        [print() for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print()
