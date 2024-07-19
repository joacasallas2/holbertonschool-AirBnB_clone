#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a class BaseModel"""
import uuid
import datetime


class BaseModel:
    "Defines all common attributes/methods for other classes"
    def __init__(self, *args, **kwargs):
        """Initialize the data"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                self.__dict__[key] = value

    def __str__(self):
        """prints in stdout: [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict
