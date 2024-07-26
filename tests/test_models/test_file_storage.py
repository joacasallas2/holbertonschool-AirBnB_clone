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
        my_model = BaseModel()
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
        len1 = len(storage.all())
        my_model1 = BaseModel()
        my_model1.save()
        storage.all()
        my_model2 = BaseModel()
        my_model2.name = "My_First_Model"
        my_model2.save()
        storage.all()
        my_model3 = BaseModel()
        my_model3.my_number = 89
        my_model3.save()
        storage.all()
        len2 = len(storage.all())

        self.assertEqual(len1 + 3, len2)


    def test_file_path_exists(self):
        """Test of FileStorage class for check __file_path"""
        storage.save()
        self.assertTrue(os.path.exists(self.__file_path))
    
    def tearDown(self):
        """Clean up conditions after each test"""
        os.remove(self.__file_path) if os.path.exists(self.__file_path) else None


if __name__ == "__main__":
    unittest.main()
