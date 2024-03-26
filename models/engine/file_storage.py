#!/usr/bin/python3
"""A module that serializes instances to a JSON file and
    deserializes JSON file to instances
"""

import json
import os


class FileStorage():
    """ A class that serializes instances to a JSON file
        and deserializes JSON file to instances
    """

    def __init__(self):
        """The consructor"""
        __file_path = "file.json"
        __objects = {}

    def all(self):
        """Return the dicitionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets inthe private attribute __objects the obj
            with key <obj class name>.id
        """

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file using the path in __file_path
        """
        json_data = {}
        for key, value in self.__objects.items():
            json_data[key] = value.to_dict()
        with open(self.__file_path, "w") as json_file:
            json.dumps(json_data, json_file)

    def reload(self):
        """deserializes the JSON file to __objects if it exists"""
        if os.path.exists(__file_path):
            with open("__file_path", "r") as json_file:
                serial_objects = json.load(json_file)
                for key, value in serial_objects.items():
                    class_name, obj_id = key.split('.')
                    class_obj = globals()[class_name]
                    self.__objects[key] = class_obj(**value)
