#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.test1 = BaseModel()
        self.test1.name = "holberton"

    def test_name(self):
        self.assertTrue(self.test1.id)
        self.assertEqual(self.test1.name, "holberton")

if __name__ == '__main__':
    unittest.main()
        
