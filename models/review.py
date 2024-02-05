#!/usr/bin/python3
"""
This module defines the Review class.
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    Represents review of a place, by a user.
    """
    place_id = ""
    user_id = ""
    text = ""