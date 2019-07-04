#!/usr/bin/python3
import unittest
from models.user import User
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
        self.test1 = User()
        self.test1.email = "holberton@mail.com"
        self.test1.password = "pass"
        self.test1.first_name = "Betty"
        self.test1.last_name = "pep8"
        self.test2 = User()
        self.test2.password = ""

    def test_attributes(self):
        self.assertEqual(self.test1.email, "holberton@mail.com")
        self.assertEqual(self.test1.password, "pass")
        self.assertEqual(self.test2.password, "")
        self.assertEqual(self.test1.first_name, "Betty")
        self.assertEqual(self.test1.last_name, "pep8")


if __name__ == '__main__':
    unittest.main()
