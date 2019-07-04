#!/usr/bin/python3
import unittest
from models.review import Review
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
        self.test1 = Review()
        self.test1.place_id = "1111"
        self.test1.user_id = "1122-1122"
        self.test2 = Review()
        self.test2.text = "text"

    def test_attributes(self):
        self.assertEqual(self.test1.place_id, "1111")
        self.assertEqual(self.test1.user_id, "1122-1122")
        self.assertEqual(self.test2.text, "text")


if __name__ == '__main__':
    unittest.main()
