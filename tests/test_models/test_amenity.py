"""Tests Amenity class"""

import unittest
import os
import pep8
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Group of test of Amenity class"""

    @classmethod
    def setUpClass(cls):
        """Create a new instance for each test"""
        cls.amenity = Amenity()
        cls.amenity.name = "A kitchen"
        cls.amenity.save()
        cls.amenity_dict = cls.amenity.to_dict()

    @classmethod
    def tearDownClass(cls):
        """teardown"""
        os.remove("file.json")
        del cls.amenity

    def test_pep8_amenity(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_amenity_name(self):
        """Test of amenity class for assigning or updating the name"""
        self.assertIn("name", self.amenity_dict)
        self.assertEqual(self.amenity_dict["name"], "A kitchen")

    def test_attributes_amenity(self):
        """chekcing if amenity have attributes"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_attribute_types_amenity(self):
        """test attribute type for amenity"""
        self.assertEqual(type(self.amenity.name), str)

    def test_is_subclass_amenity(self):
        """tests if amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_save_amenity(self):
        """test the save method"""
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    


if __name__ == "__main__":
    unittest.main()
