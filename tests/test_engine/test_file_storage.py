#!/usr/bin/python3
"""file storage unittests"""

import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """testing file storage"""

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)