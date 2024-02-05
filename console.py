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
    """
    
    """

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
    
    def emptyline(self):
        """
        Handles empty line input.
        """
        pass

    def do_help():
        """
        Displays list of commands available
        Displays info about specified command
        """
        return
    
    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves, and prints the id.
        
        Args:
            line

        """
        if len(args) < 1:
            print("** class name missing **")
            return False

        print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of
        an instance based of the class name
        and id.

        Args:
            line

        """

        if len(args) < 1:
            print("** class name missing **")
            return False

        print("** class doesn't exist **")
        print("** instance id missing **")
        print("** no instance found **")

    def do_destroy():
        """
        Deletes an instance based on the
        class name and id.
        
        Args:
            line

        """

        if len(args) < 1:
            print("** class name missing **")
            return False

        print("** class doesn't exist **")
        print("** instance id missing **")
        print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of
        all instances based or not on the
        class name.

        Args:
            line

        """

        print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on the class
        name and id by adding or updating
        attribute.

        Args:
            line

        """
        if len(args) < 1:
            print("** class name missing **")
            return False
            
        print("** class doesn't exist **")
        print("** instance id missing **")
        print("** no instance found **")
        print("** attribute name missing **")
        print("** value missing **")

    if __name__ == '__main__':
        HBMBCommand().cmdloop()