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
        for key, values in self.__objects.items():
            serial_obj[key] = values.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(new, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
        'State': State, 'Amenity': Amenity, 'Place': Place, 'Review': Review}

        try:
            with open(self.__file_path, "r") as file:
                obj = json.load(file)
                for key, values in obj.items():
                    k_split = key.split('.')
                    tmp = classes[k_split[0]](**values)
                    self.new(tmp)
        except FileNotFoundError:
            pass
