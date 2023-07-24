#!/usr/bin/python3
""" Base class """

import json
import csv


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
