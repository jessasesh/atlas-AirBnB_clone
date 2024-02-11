#!/usr/bin/python3
from models.base_model import BaseModel
"""
This module defines the User class.
"""


class User(BaseModel):
    """
    Represents a user and their info.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
