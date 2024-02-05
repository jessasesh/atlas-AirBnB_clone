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
        returns the dictionary __objects
    
    def new(self, obj):
        sets in __objects the obj with key <obj class name>.id
    
    def save(self):
        serializes __objects to the JSON file (path: __file_path)
    
    def reload(self):
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)