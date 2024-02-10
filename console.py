#!/usr/bin/python3
"""
This module contains the entry point
of the command interpreter.
"""


import cmd
import json
import models
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    This module defines the entry point of the command interpreter.
    """

    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }

    def do_quit(self, arg):
        """
        Exits the program.

        To use, enter the command "quit".
        """
        return True

    def do_EOF(self, arg):
        """
        Exits the program.

        To use, enter the command "EOF".
        """
        return True

    def emptyline(self):
        """
        Handles empty line input.
        """
        pass

    def do_help(self, arg):
        """
        Displays list of commands available or
        displays info about specified command.

        To use, enter the command "help" or
        "help <command>" for more info.
        """
        return super().do_help(arg)

    def do_create(self, arg):
        """
        Creates new object or instance of BaseModel,
        saves, and prints the id.

        To use, enter the command
        "create <class>".

        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            new_object = self.classes[args[0]]()
            new_object.save()
            print(new_object.id)

    def do_show(self, arg):
        """
        Prints the string representation of
        an object or instance based of the
        class name and id.

        To use, enter the command
        "show <class> <id>".
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        else:
            key = f'{args[0]}.{args[1]}'
            all_objects = models.storage.all()
            if key in all_objects:
                print(all_objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the
        class name and id.

        To use, enter the command
        "destroy <class> <id>".
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        all_objects = models.storage.all()
        if key in all_objects:
            all_objects[key].delete()
            models.storage.save()
        else:
            print("** no instance found **")
            return

    def do_all(self, arg):
        """
        Displays list of all objects or
        displays info about specified class.
    
        To use, enter the command "all" or
        "all <class>".
        """
        args = arg.split()
        all_objs = storage.all()
        if len(args) < 1:
            for obj in all_objs.values():
                print(obj)
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            for obj in all_objs.values():
                if obj.__class__.__name__ == args[0]:
                    print(obj)

    def do_update(self, arg):
        """
        Updates an instance based on the class
        name and id by adding or updating
        attribute.

        Args:
            line

        """
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in self.classes:
            print('** class doesn\'t exist **')
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            class_name, instance_id = args[0], args[1]
            key = f'{class_name}.{instance_id}'
            all_objs = storage.all()

        if key not in all_objs:
            print('** no instance found **')
        elif len(args) == 2:
            print('** attribute name missing **')
        elif len(args) == 3:
            print('** value missing **')
        else:
            obj = all_objs[key]
            attr_name, attr_value_str = args[2], args[3].strip('"')
            attr_type = type(getattr(obj, attr_name, ''))
            attr_value = attr_type(attr_value_str)
            setattr(obj, attr_name, attr_value)
            obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
