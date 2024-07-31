#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    "Define the class Review "
    place_id = ""
    user_id = ""
    text = ""
