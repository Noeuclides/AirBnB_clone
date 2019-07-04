#!/usr/bin/python3
import unittest
from models.place import Place
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
        self.test1 = Place()
        self.test1.number_rooms = 3
        self.test1.latitude = 5.03
        self.test1.city_id = "11-22"
        self.test1.amenity_ids = []
        self.test2 = Place()
        self.test2.max_guest = "3"

    def test_attributes(self):
        self.assertEqual(type(self.test1.number_rooms), int)
        self.assertEqual(type(self.test1.latitude), float)
        self.assertNotEqual(type(self.test2.max_guest), int)
        self.assertEqual(self.test1.city_id, "11-22")
        self.assertEqual(type(self.test1.amenity_ids), list)


if __name__ == '__main__':
    unittest.main()
