#!/usr/bin/python3
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.test1 = BaseModel()

    def test_all(self):
        stor = storage.all()
        self.assertTrue(stor)

    def test_new(self):
        stor1 = str(storage.all())
        self.test2 = BaseModel()
        stor2 = str(storage.all())
        self.assertNotEqual(stor1, stor2)

    def test_save(self):
        stor3 = str(storage.all())
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model.save()
        stor4 = str(storage.all())
        self.assertNotEqual(stor3, stor4)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
