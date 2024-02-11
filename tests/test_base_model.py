#!/usr/bin/python3
"""basemodel unittests"""

import unittest
import os
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """basemodel tests"""

    @classmethod
    def set_Up_Class(cls):
        """set up to class"""
        cls.base_model = BaseModel()
        try:
            os.rename("file.json", "testing_file.json")
        except Exception:
            pass

    def test_save(self):
        """test to save method"""
        based = BaseModel()
        update = based.updated_at
        based.save()
        self.assertLess(update, based.updated_at)
        self.assertTrue(os.path.exists("file.json"))

    def test_str(self):
        """test str"""
        clss = str(self.base_model.__class__.__name__)
        dicts = str(self.base_model.__dict__)
        str2 = f"[{clss}] ({self.base_model.id}) {dicts}"
        self.assertEqual(str2,self.base_model.__str__())

    def test_dict(self):
        """test dict"""
        dict1 = {
            "id": self.base_model.id,
            "__class__": self.base_model.__class__.__name__,
            "created_at": self.base_model.created_at.isoformat(),
            "updated_at": self.base_model.updated_at.isoformat()
        }
        self.assertDictEqual(dict1, self.base_model.to_dict())

if __name__ == "main":
    unittest.main()
