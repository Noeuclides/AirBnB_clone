#!/usr/bin/python3
import unittest
from models.city import City
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
        self.test1 = City()
        self.test1.state_id = "1111"
        self.test1.name = "China"
        self.test2 = City()
        self.test2.name = ""

    def test_attributes(self):
        self.assertEqual(self.test1.name, "China")
        self.assertEqual(self.test1.state_id, "1111")
        self.assertEqual(self.test2.name, "")


if __name__ == '__main__':
    unittest.main()
