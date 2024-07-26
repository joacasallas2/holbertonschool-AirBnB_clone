"""Tests"""

import unittest
import os
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Group of test of FileStorage class"""


    def setUp(self):
        """initialize conditions to each test"""
        self.__file_path = "file.json"
        self.__objects = storage.all()


    def test_all_method(self):
        """Test of FileStorage class for the all method"""
        all_objs = storage.all()

        self.assertDictEqual(all_objs, self.__objects)

    def test_new_method(self):
        """Test of FileStorage class for the new method"""
        my_model = BaseModel()
        id_model = f"BaseModel.{my_model.id}"
        all_objs = storage.all()

        self.assertIn(id_model, all_objs)

    def test_save_method(self):
        """Test of FileStorage class for the save method"""
        len1 = len(storage.all())
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.save()
        len2 = len(storage.all())

        self.assertEqual(len1 + 1, len2)

    def test_reload_method(self):
        """Test of FileStorage class for the reload method"""
        storage.save()
        len1 = len(storage.all())
        storage.reload()
        len2 = len(storage.all())

        self.assertEqual(len1, len2)


    def test_file_path_exists(self):
        """Test of FileStorage class for check __file_path"""
        storage.save()
        self.assertTrue(os.path.exists(self.__file_path))
    
    def tearDown(self):
        """Clean up conditions after each test"""
        os.remove(self.__file_path) if os.path.exists(self.__file_path) else None


if __name__ == "__main__":
    unittest.main()
