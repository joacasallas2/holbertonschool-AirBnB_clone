"""Tests"""

import unittest
import io
import sys
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Group of test of BaseModel class"""
    def setUp(self):
        """Create a new instance for each test"""
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def test_auto_id_assignment_automatically(self):
        """Test of BaseModel class for assigning automatically an ID exists"""
        my_model_dict = self.my_model.to_dict()
        my_model_id = my_model_dict["id"]

        self.assertEqual(self.my_model.id, my_model_id)

    def test_save(self):
        """Test of BaseModel class for the save method"""
        my_model_dict1 = self.my_model.to_dict()
        self.my_model.save()
        my_model_dict2 = self.my_model.to_dict()

        self.assertNotEqual(my_model_dict1["updated_at"], my_model_dict2["updated_at"])

    def test_to_dict(self):
        """Test of BaseModel class for the to_dict method"""
        my_model_dict = self.my_model.to_dict()

        self.assertIn("id", my_model_dict)
        self.assertIn("updated_at", my_model_dict)
        self.assertIn("created_at", my_model_dict)
        self.assertIn("name", my_model_dict)
        self.assertIn("my_number", my_model_dict)

    def test_created_at(self):
        """Test of BaseModel class for the created_at attributte"""
        my_model_dict = self.my_model.to_dict()

        self.assertIsNotNone(my_model_dict["created_at"])

    def test_str(self):
        """Test of BaseModel class for the __str__ method"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            print(self.my_model)
        finally:
            sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        expected_output_start = f"[BaseModel] ({self.my_model.id}) "
        self.assertTrue(output.startswith(expected_output_start))
        self.assertIn("'name': 'My First Model'", output)
        self.assertIn("'my_number': 89", output)


if __name__ == "__main__":
    unittest.main()
