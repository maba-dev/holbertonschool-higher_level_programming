#!/usr/bin/python3
""" the first class Base: """

import json


class Base:
    """ define a base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """JSON is one of the standard formats for sharing data reprsntation"""

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
