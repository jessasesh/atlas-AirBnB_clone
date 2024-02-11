#!/usr/bin/python3
"""
This module defines Amenity class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity that
    a place provides.
    """
    name = ""
