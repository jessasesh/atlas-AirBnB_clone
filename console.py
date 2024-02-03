#!/usr/bin/python3
"""
This module contains the entry point
of the command interpreter.
"""


import cmd
from models.base_model import BaseModel
from models.amenity import amenity
from models.place import place
from models.review import review
from models.state import state
from models.city import city
from models.user import user

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        Exits the program.
        """
        return True
    
    def do_EOF(self, line):
        """
        Exits the program.
        """
        return True