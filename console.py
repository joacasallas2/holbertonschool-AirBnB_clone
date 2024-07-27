#!/usr/bin/python3
# Author: Joana Casallas
"""the entry point of our command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class definition for HBNBCommand"""

    prompt = "(hbnb) "

    def __init__(self):
        """Initialize the data"""
        super().__init__()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_help(self, arg):
        """updated help command"""
        cmd.Cmd.do_help(self, arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
