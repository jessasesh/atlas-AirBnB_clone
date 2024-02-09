#!/usr/bin/python3
"""state unittests"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """testing state"""
    def test_class(self):
        self.assertEqual(State.name, "")
        self.assertTrue(State, BaseModel)