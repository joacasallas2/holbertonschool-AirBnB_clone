"""Tests State class"""

import unittest
import os
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Group of test of State class"""

    @classmethod
    def setUpClass(cls):
        """Create a new instance for each test"""
        cls.state = State()
        cls.state.name = "Oregon"
        cls.state.save()
        cls.state_dict = cls.state.to_dict()

    @classmethod
    def tearDownClass(cls):
        """teardown"""
        if  os.path.exists("file.json"):
            os.remove("file.json")
        del cls.state

    def test_state_name(self):
        """Test of state class for assigning or updating the first name"""
        self.assertIn("name", self.state_dict)
        self.assertEqual(self.state_dict["name"], "Oregon")
        self.assertTrue('name' in self.state.__dict__)

    def test_attribute_types_state(self):
        """test attribute type for state"""
        self.assertEqual(type(self.state.name), str)

    def test_is_subclass_state(self):
        """tests if state is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_save_state(self):
        """test the save method"""
        self.assertNotEqual(self.state.created_at, self.state.updated_at)


if __name__ == "__main__":
    unittest.main()
