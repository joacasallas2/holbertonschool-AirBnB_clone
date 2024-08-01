"""Tests State class"""

import unittest
import os
from models.base_model import BaseModel
from models.city import City
from models.state import State


class TestCity(unittest.TestCase):
    """Group of test of City class"""

    @classmethod
    def setUpClass(cls):
        """Create a new instance for each test"""
        cls.state = State()
        cls.state.name = "Oregon"
        cls.state.save()
        cls.state_dict = cls.state.to_dict()
        cls.state_id = cls.state_dict["id"]
        cls.city = City()
        cls.city.name = "Portland"
        cls.city.state_id = cls.state_id
        cls.city.save()
        cls.city_dict = cls.city.to_dict()

    @classmethod
    def tearDownClass(cls):
        """teardown"""
        if  os.path.exists("file.json"):
            os.remove("file.json")
        del cls.city
        del cls.state

    def test_city_name(self):
        """Test of city class for assigning or updating the name"""
        self.assertIn("name", self.city_dict)
        self.assertEqual(self.city_dict["name"], "Portland")
        self.assertTrue('name' in self.city.__dict__)

    def test_city_state_id(self):
        """Test of city class for assigning or updating the state_id"""
        self.assertIn("state_id", self.city_dict)
        self.assertTrue('state_id' in self.city.__dict__)

    def test_auto_id_assignment(self):
        """Test of City class for assigning automatically an ID exists"""
        city_id = self.city_dict["id"]

        self.assertEqual(self.city.id, city_id)

    def test_attribute_types_city(self):
        """test attribute type for city"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_is_subclass_city(self):
        """tests if city is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_save_city(self):
        """test the save method"""
        self.assertNotEqual(self.city.created_at, self.city.updated_at)


if __name__ == "__main__":
    unittest.main()
