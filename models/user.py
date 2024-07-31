#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    "Define the class User"
    email = ""
    password = ""
    first_name = ""
    last_name = ""
