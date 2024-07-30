#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a class FileStorage"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class FileStorage:
    """Serializes instances to and from JSON file"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Initializes the data"""
        self.reload()

    def all(self):
        """returns the dictionary __objects"""
        return self.__class__.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__class__.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        filename = self.__file_path
        with open(filename, "w", encoding="utf-8") as f:
            data = {}
            for k, v in self.__class__.__objects.items():
                data[k] = v.to_dict()
            json.dump(data, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                dict_objs = json.load(f)
                for key, value in dict_objs.items():
                    value["created_at"] = datetime.fromisoformat(
                        value["created_at"])
                    value["updated_at"] = datetime.fromisoformat(
                        value["updated_at"])
                    obj = eval(value["__class__"])(**value)
                    self.__objects[key] = obj
