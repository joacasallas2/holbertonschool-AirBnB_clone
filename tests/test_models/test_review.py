"""Tests Review class"""

import unittest
import os
import pep8
from models.base_model import BaseModel
from models.review import Review
from models.user import User
from models.place import Place


class TestReview(unittest.TestCase):
    """Group of test of Review class"""

    @classmethod
    def setUpClass(cls):
        """Create a new instance for each test"""

        cls.user = User()
        cls.user.name = "Joana"
        cls.user.save()
        cls.user_dict = cls.user.to_dict()
        cls.user_id = cls.user_dict["id"]

        cls.place = Place()
        cls.place.name = "House"
        cls.place.save()
        cls.place_dict = cls.place.to_dict()
        cls.place_id = cls.place_dict["id"]

        cls.review = Review()
        cls.review.place_id = cls.place_id
        cls.review.user_id = cls.user_id
        cls.review.text = ""
        cls.review.save()
        cls.review_dict = cls.review.to_dict()
        cls.review_id = cls.review_dict["id"]


    @classmethod
    def tearDownClass(cls):
        """teardown"""
        if  os.path.exists("file.json"):
            os.remove("file.json")
        del cls.review
        del cls.place
        del cls.user

    def test_pep8_review(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_review_user_id(self):
        """Test of review class for assigning or updating the user_id"""
        self.assertIn("user_id", self.review_dict)
        self.assertTrue('user_id' in self.review.__dict__)

    def test_review_place_id(self):
        """Test of review class for assigning or updating the place_id"""
        self.assertIn("place_id", self.review_dict)
        self.assertTrue('place_id' in self.review.__dict__)

    def test_auto_id_assignment(self):
        """Test of review class for assigning automatically an ID exists"""
        review_id = self.review_dict["id"]

        self.assertEqual(self.review.id, review_id)

    def test_attribute_types_review(self):
        """test attribute type for review"""
        self.assertEqual(type(self.review.user_id), str)
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.text), str)

    def test_is_subclass_review(self):
        """tests if review is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)

    def test_save_review(self):
        """test the save method"""
        self.assertNotEqual(self.review.created_at, self.review.updated_at)


if __name__ == "__main__":
    unittest.main()
