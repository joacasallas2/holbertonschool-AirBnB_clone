"""Tests State class"""

import unittest
import os
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place


class TestCity(unittest.TestCase):
    """Group of test of City class"""

    @classmethod
    def setUpClass(cls):
        """Create a new instance for each test"""
        cls.city = City()
        cls.city.name = "Portland"
        cls.city.save()
        cls.city_dict = cls.city.to_dict()
        cls.city_id = cls.city_dict["id"]

        cls.user = User()
        cls.user.name = "Joana"
        cls.user.save()
        cls.user_dict = cls.user.to_dict()
        cls.user_id = cls.user_dict["id"]

        cls.amenity_1 = Amenity()
        cls.amenity_1.name = "A kitchen"
        cls.amenity_1.save()
        cls.amenity_1_dict = cls.amenity_1.to_dict()
        cls.amenity_1_id = cls.amenity_1_dict["id"]

        cls.amenity_2 = Amenity()
        cls.amenity_2.name = "Pool"
        cls.amenity_2.save()
        cls.amenity_2_dict = cls.amenity_2.to_dict()
        cls.amenity_2_id = cls.amenity_1_dict["id"]

        cls.place = Place()
        cls.place.name = "House"
        cls.place.description = "home in Portland"
        cls.place.number_rooms = 2
        cls.place.number_bathrooms = 2
        cls.place.max_guest = 4
        cls.place.price_by_night = 2232
        cls.place.latitude = 0.0
        cls.place.longitude = 0.0
        cls.place.city_id = cls.city_id
        cls.place.amenity_ids = [cls.amenity_1_id, cls.amenity_2_id]
        cls.place.user_id = cls.user_id
        cls.place.save()
        cls.place_dict = cls.place.to_dict()

    @classmethod
    def tearDownClass(cls):
        """teardown"""
        if  os.path.exists("file.json"):
            os.remove("file.json")
        del cls.place
        del cls.city
        del cls.user
        del cls.amenity_1
        del cls.amenity_2

    def test_place_name(self):
        """Test of place class for assigning or updating the name"""
        self.assertIn("name", self.place_dict)
        self.assertEqual(self.place_dict["name"], "House")
        self.assertTrue('name' in self.place.__dict__)

    def test_place_description(self):
        """Test of place class for assigning or updating the description"""
        self.assertIn("description", self.place_dict)
        self.assertEqual(self.place_dict["description"], "home in Portland")
        self.assertTrue('description' in self.place.__dict__)

    def test_place_city_id(self):
        """Test of place class for assigning or updating the city_id"""
        self.assertIn("city_id", self.place_dict)
        self.assertTrue('city_id' in self.place.__dict__)

    def test_auto_id_assignment(self):
        """Test of place class for assigning automatically an ID exists"""
        place_id = self.place_dict["id"]

        self.assertEqual(self.place.id, place_id)

    def test_attribute_types_place(self):
        """test attribute type for place"""
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    def test_is_subclass_place(self):
        """tests if place is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def test_save_place(self):
        """test the save method"""
        self.assertNotEqual(self.place.created_at, self.place.updated_at)


if __name__ == "__main__":
    unittest.main()
