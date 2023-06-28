#!/usr/bin/python3
"""
The MagicClass that does exactly the same as the Python bytecode provided
"""


import math


class MagicClass:
    """
    The Exact Magic class definition
    """

    def __init__(self, radius=0):
        """
        The constructor of the MagicClass

        Arg:
        radius: Is the radius of the MagicClass from instance
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        This function calculates the area of the MagicClass
        """
        return (self.__radius * self.__radius * math.pi)

    def circumference(self):
        """
        This function calculates the circumference of the MagicClass
        """
        return (2 * math.pi * self.__radius)
