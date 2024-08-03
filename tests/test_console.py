"""Tests"""

import unittest
import os
from io import StringIO
from unittest.mock import patch
from models import storage
from console import HBNBCommand
from models.base_model import BaseModel


class TestHBNBCommand(unittest.TestCase):
    """Group of tests of HBNBCommand class"""

    def setUp(self):
        """initialize conditions to each test"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up conditions after each test"""
        storage._FileStorage__objects = {}
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_quit(self):
        """Test of HBNBCommand class for the quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            result = HBNBCommand().onecmd("quit")
            self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
