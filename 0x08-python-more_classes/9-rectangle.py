#!/usr/bin/python3
"""Module for Rectangle class."""


class Rectangle:
    """Class that defines a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new instance of a Rectangle.
        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.
        Args:
            value (int): The width of the rectangle.
        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.
        Args:
            value (int): The height of the rectangle.
        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Gets the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Gets the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""

        return "\n".join([str(self.print_symbol) * self.__width] *
                         self.__height)

    def __repr__(self):
        """Returns a string representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted,
        and decrements the number of instances.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Gets the bigger rectangle based on area
        Args:
            rect_1 (Rectangle): The first rectangle
            rect_2 (Rectangle): The second rectangle
        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle
        Returns:
            The bigger rectangle, or rect_1 if both rectangles have the same
            area
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_2 if rect_2.area() > rect_1.area() else rect_1

    @classmethod
    def square(cls, size=0):
        """
        Creates a new Rectangle instance with width, height, and size all
        equal to size
        Args:
            size (int): The width and height of the new Rectangle
        Returns:
            A new Rectangle instance with width, height, size all equal to
            size
        """
        return cls(size, size)
