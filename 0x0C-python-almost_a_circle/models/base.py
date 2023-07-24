#!/usr/bin/python3
""" Base class """

import json


class Base:
    """ Base class

    Attributes:
    __nb_objects (int): number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Init method

        Args:
        id (int): id of the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries

        Args:
        list_dictionaries (list): list of dictionaries

        Returns:
        JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file

        Args:
        list_objs (list): list of objects
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string

        Args:
        json_string (str): JSON string representation

        Returns:
        list of the JSON string representation json_string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set

        Args:
        dictionary (dict): dictionary of attributes

        Returns:
        instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
