"""Tests User class"""

import unittest
import os
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Group of test of User class"""

    @classmethod
    def setUpClass(cls):
        """Create a new instance for each test"""
        cls.user = User()
        cls.user.email = "airbnb@mail.com"
        cls.user.first_name = "Betty"
        cls.user.last_name = "Bar"
        cls.user.password = "root"
        cls.user.save()
        cls.user_dict = cls.user.to_dict()

    @classmethod
    def tearDownClass(cls):
        """teardown"""
        os.remove("file.json")
        del cls.user

    def test_user_email(self):
        """Test of User class for assigning or updating the user email"""
        self.assertIn("email", self.user_dict)
        self.assertEqual(self.user_dict["email"], "airbnb@mail.com")

    def test_user_first_name(self):
        """Test of User class for assigning or updating the first name"""
        self.assertIn("first_name", self.user_dict)
        self.assertEqual(self.user_dict["first_name"], "Betty")

    def test_user_last_name(self):
        """Test of User class for assigning or updating the last name"""
        self.assertIn("last_name", self.user_dict)
        self.assertEqual(self.user_dict["last_name"], "Bar")

    def test_user_password(self):
        """Test of User class for assigning or updating the password"""
        self.assertIn("password", self.user_dict)
        self.assertEqual(self.user_dict["password"], "root")

    def test_attributes_user(self):
        """chekcing if User have attributes"""
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_attribute_types_user(self):
        """test attribute type for User"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.first_name), str)

    def test_is_subclass_user(self):
        """tests if User is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_save_user(self):
        """test the save method"""
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    


if __name__ == "__main__":
    unittest.main()
