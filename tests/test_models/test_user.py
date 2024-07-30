"""Tests"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Group of test of User class"""
    def setUp(self):
        """Create a new instance for each test"""
        self.my_user = User()
        self.my_user.save()

    def test_user_email(self):
        """Test of User class for assigning or updating the user email"""
        self.my_user.email = "airbnb@mail.com"
        self.my_user.save()
        my_user_dict = self.my_user.to_dict()

        self.assertIn("email", my_user_dict)
        self.assertEqual(my_user_dict["email"], "airbnb@mail.com")

    def test_user_first_name(self):
        """Test of User class for assigning or updating the first name"""
        self.my_user.first_name = "Betty"
        self.my_user.save()
        my_user_dict = self.my_user.to_dict()

        self.assertIn("first_name", my_user_dict)
        self.assertEqual(my_user_dict["first_name"], "Betty")

    def test_user_last_name(self):
        """Test of User class for assigning or updating the last name"""
        self.my_user.last_name = "Bar"
        self.my_user.save()
        my_user_dict = self.my_user.to_dict()

        self.assertIn("last_name", my_user_dict)
        self.assertEqual(my_user_dict["last_name"], "Bar")

    def test_user_password(self):
        """Test of User class for assigning or updating the password"""
        self.my_user.password = "root"
        self.my_user.save()
        my_user_dict = self.my_user.to_dict()

        self.assertIn("password", my_user_dict)
        self.assertEqual(my_user_dict["password"], "root")


if __name__ == "__main__":
    unittest.main()
