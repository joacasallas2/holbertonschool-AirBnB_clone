#!/usr/bin/python3
# Author: Joana Casallas
"""the entry point of our command interpreter"""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """class definition for HBNBCommand"""

    prompt = "(hbnb) "
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
        }

    def __init__(self, **kwargs):
        """Initialize the data"""
        super().__init__(**kwargs)

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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        new_model = self.classes[arg]()
        new_model.save()
        print(new_model.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        dict_objs = storage.all()
        if key not in dict_objs:
            print("** no instance found **")
            return
        print(dict_objs[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        dict_objs = storage.all()
        if key not in dict_objs:
            print("** no instance found **")
            return
        del dict_objs[key]
        storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances based
        or not on the class name."""
        dict_objs = storage.all()
        list_instances = []
        if arg:
            if arg not in self.classes:
                print("** class doesn't exist **")
                return
            for key, value in dict_objs.items():
                if arg in key:
                    list_instances.append(str(value))
        else:
            for value in dict_objs.values():
                list_instances.append(str(value))
        print(list_instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        key = f"{args[0]}.{args[1]}"
        dict_objs = storage.all()
        if key not in dict_objs:
            print("** no instance found **")
            return
        instance = dict_objs[key]
        att_name = args[2]
        att_value = args[3]
        try:
            if att_value.isdigit():
                att_value = int(att_value)
            else:
                try:
                    att_value = float(att_value)
                except ValueError:
                    pass
        except AttributeError:
            pass
        setattr(instance, att_name, att_value)
        instance.save()
        storage.save()

    def default(self, line):
        """retrieve all instances of a class by using: <class name>.all()
        or retrieve the number of instances of a class <class name>.count()
        or retrieve an instance based on its ID: <class name>.show(<id>)."""
        if "." in line:
            class_name, command = line.split(".", 1)
            if class_name in self.classes:
                if command == "all()":
                    self.do_all(class_name)
                elif command == "count()":
                    counter = 0
                    list_instances = storage.all()
                    for k, v in list_instances.items():
                        if class_name in k:
                            counter += 1
                    print(counter)
                elif "show(" in command:
                    instance_id = command[5:-1]
                    self.do_show(f"{class_name} {instance_id}")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
