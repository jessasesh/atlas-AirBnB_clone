#!/usr/bin/python3
"""creating a class that defines all
common attributes/methods for other classes"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel class, used to meet the
    docstring description above"""
    def __init__(self, id, *args, **kwargs):
        """Public instance attributes"""
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ str representation"""
        return ("[{}] ({}) {}".format(self.__class__, self.id,
                                      self.__dict__))


    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""


    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance"""