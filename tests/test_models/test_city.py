#!/usr/bin/python3
"""
    Test Module - contains tests for the City class
"""

import unittest
from models.city import City
import datetime
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Defines the tests for the class"""

    @classmethod
    def setUpClass(cls):
        """Sets the objects to be tested"""
        cls.city1 = City()

    def test_new_instance(self):
        """Tests the creation of a new instance"""
        self.assertIs(type(self.city1.name), str)
        self.assertEqual(len(self.city1.name), 0)
        self.assertIs(type(self.city1.state_id), str)
        self.assertEqual(len(self.city1.state_id), 0)
        self.assertIs(type(self.city1.id), str)
        self.assertIs(type(self.city1.created_at), datetime.datetime)
        self.assertIs(type(self.city1.updated_at), datetime.datetime)

    def test_inheritance(self):
        """ Test if inherits from BaseModel """
        self.assertIsInstance(self.city1, BaseModel)
