#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
import pep8


class TestCodeformat(unittest.TestCase):

    def test_pep8(self):
        """test pep8"""
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files([
            'models/base_model.py', 'models/user.py',
            'models/review.py', 'models/place.py',
            'models/city.py', 'models/amenity.py',
            'tests/test_models/test_engine/test_file_storage.py',
            'tests/test_models/test_base_model.py',
            'tests/test_models/test_user.py',
            'tests/test_models/test_review.py',
            'tests/test_models/test_place.py',
            'tests/test_models/test_city.py',
            'tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors")


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.test1 = BaseModel()
        self.test1.name = "holberton"

    def test_name(self):
        self.assertTrue(self.test1.id)
        self.assertEqual(self.test1.name, "holberton")

    def test_id(self):
        new_id = self.test1.id
        self.test1.save()
        self.assertEqual(self.test1.id, new_id)

    def test_save(self):
        time = self.test1.updated_at
        self.test1.save()
        self.assertNotEqual(self.test1.updated_at, time)
        self.test1.save()
        time2 = self.test1.updated_at
        self.assertNotEqual(time, time2)
        self.assertNotEqual(self.test1.updated_at, self.test1.created_at)

    def test_to_dict(self):
        temp = self.test1.to_dict()
        self.assertEqual(type(temp), dict)
        self.assertTrue('to_dict' in dir(self.test1))
        self.assertEqual(type(temp['updated_at']), str)
        self.assertEqual(type(temp['created_at']), str)

if __name__ == '__main__':
    unittest.main()
