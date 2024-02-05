#!/usr/bin/python3
"""
This module contains the entry point
of the command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    This module defines the entry point of the command interpreter.
    """

    prompt = "(hbnb) "
    
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
