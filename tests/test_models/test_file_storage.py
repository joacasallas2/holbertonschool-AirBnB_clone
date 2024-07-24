"""Tests"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Group of test of FileStorage class"""
    def setUp(self):
        """setup test environment"""
        self.storage = FileStorage()
        self.file_path = "file.json"
        self.base_model = BaseModel()

    def tearDown(self):
        """Clean up test environment"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)


    def test_all_method(self):
        """Test all method returns the __objects dictionary"""
        self.assertEqual(self.storage.all(), self.storage._FileStorage__objects)

if __name__ == "__main__":
    unittest.main()
