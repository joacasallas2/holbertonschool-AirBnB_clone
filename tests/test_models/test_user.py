"""Tests"""

import unittest
import os
from models.user import User


class TestUser(unittest.TestCase):
    """Group of test of User class"""

    @classmethod
    def setUpClass(cls):
        """Create a new instance for each test"""
        cls.my_user = User()
        cls.my_user.email = "airbnb@mail.com"
        cls.my_user.first_name = "Betty"
        cls.my_user.last_name = "Bar"
        cls.my_user.password = "root"
        cls.my_user.save()
        cls.my_user_dict = cls.my_user.to_dict()

    @classmethod
    def tearDownClass(cls):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_user_email(self):
        """Test of User class for assigning or updating the user email"""
        self.assertIn("email", self.my_user_dict)
        self.assertEqual(self.my_user_dict["email"], "airbnb@mail.com")
        self.assertTrue('email' in self.my_user.__dict__)

    def test_user_first_name(self):
        """Test of User class for assigning or updating the first name"""
        self.assertIn("first_name", self.my_user_dict)
        self.assertEqual(self.my_user_dict["first_name"], "Betty")

    def test_user_last_name(self):
        """Test of User class for assigning or updating the last name"""
        self.assertIn("last_name", self.my_user_dict)
        self.assertEqual(self.my_user_dict["last_name"], "Bar")

    def test_user_password(self):
        """Test of User class for assigning or updating the password"""
        self.assertIn("password", self.my_user_dict)
        self.assertEqual(self.my_user_dict["password"], "root")

    def test_attributes_user(self):
        """chekcing if User have attributes"""
        self.assertTrue('email' in self.my_user.__dict__)
        self.assertTrue('id' in self.my_user.__dict__)
        self.assertTrue('created_at' in self.my_user.__dict__)
        self.assertTrue('updated_at' in self.my_user.__dict__)
        self.assertTrue('password' in self.my_user.__dict__)
        self.assertTrue('first_name' in self.my_user.__dict__)
        self.assertTrue('last_name' in self.my_user.__dict__)

    def test_attribute_types_user(self):
        """test attribute type for User"""
        self.assertEqual(type(self.my_user.email), str)
        self.assertEqual(type(self.my_user.password), str)
        self.assertEqual(type(self.my_user.first_name), str)
        self.assertEqual(type(self.my_user.first_name), str)


if __name__ == "__main__":
    unittest.main()
