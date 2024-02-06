#!/usr/bin/python3
"""
This module defines FileStorage class
that serializes instances to a JSON file
and deserializes JSON file to instances.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place

class FileStorage:
    """FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key"""
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        serial_obj = {}
        for key in self.__objects:
            serial_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(serial_obj, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
    classes = {"BaseModel": BaseModel, "User": User, "State": State,
    "Place": Place, "City": City, "Amenity": Amenity, "Review": Review}

    try:
        with open(self.__file_path, 'r', encoding='utf-8') as f:
            deserial = json.load(f)
        for key in deserial:
            self.__objects[key] = classes[deserial[key]["__class__"]](**deserial[key])
    except FileNotFoundError:
        pass
