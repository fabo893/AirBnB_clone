#!/usr/bin/python3
"""
    Test Module - contains tests for the Amenity class
"""

import unittest
from models.amenity import Amenity
import datetime
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Defines the tests for the class"""

    @classmethod
    def setUpClass(cls):
        """Sets the objects to be tested"""
        cls.amen1 = Amenity()

    def test_new_instance(self):
        """Tests the creation of a new instance"""
        self.assertIs(type(self.amen1.name), str)
        self.assertEqual(len(self.amen1.name), 0)
        self.assertIs(type(self.amen1.id), str)
        self.assertIs(type(self.amen1.created_at), datetime.datetime)
        self.assertIs(type(self.amen1.updated_at), datetime.datetime)

    def test_inheritance(self):
        """ Test if inherits from BaseModel """
        self.assertIsInstance(self.amen1, BaseModel)
