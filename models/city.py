#!/usr/bin/python3
"""
This module defines city class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city that
    inherits from BaseModel.
    """
    name = ""
    state_id = ""
