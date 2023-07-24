#!/usr/bin/python3
""" Rectangle class """

from models.base import Base


class Rectangle(Base):
    """ Rectangle class

    Attributes:
        __width (int): width of the rectangle
        __height (int): height of the rectangle
        __x (int): x coordinate of the rectangle
        __y (int): y coordinate of the rectangle
        id (int): id of the rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Init method
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter method for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter method for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter method for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
