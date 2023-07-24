#!/usr/bin/python3
""" Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class

    Attributes:
    size (int): size of the square
    x (int): x coordinate of the square
    y (int): y coordinate of the square
    id (int): id of the square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Init method

        Args:
        size (int): size of the square
        x (int): x coordinate of the square
        y (int): y coordinate of the square
        id (int): id of the square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        str method
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        Getter method for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update method
        """
        if args is not None and len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        elif kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        to_dictionary method
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}