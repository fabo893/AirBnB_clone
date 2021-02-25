#!/usr/bin/python3
"""
Test Module - contains tests for the Place class
"""

import unittest
from models.place import Place
import datetime
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Defines the tests for the class"""

    @classmethod
    def setUpClass(cls):
        """Sets the objects to be tested"""
        cls.place1 = Place()

    def test_new_instance(self):
        """Tests the creation of a new instance"""
        self.assertIs(type(self.place1.name), str)
        self.assertEqual(len(self.place1.name), 0)
        self.assertIs(type(self.place1.city_id), str)
        self.assertEqual(len(self.place1.city_id), 0)
        self.assertIs(type(self.place1.user_id), str)
        self.assertEqual(len(self.place1.user_id), 0)
        self.assertIs(type(self.place1.description), str)
        self.assertEqual(len(self.place1.description), 0)
        self.assertIs(type(self.place1.number_rooms), int)
        self.assertEqual(self.place1.number_rooms, 0)
        self.assertIs(type(self.place1.number_bathrooms), int)
        self.assertEqual(self.place1.number_bathrooms, 0)
        self.assertIs(type(self.place1.max_guest), int)
        self.assertEqual(self.place1.max_guest, 0)
        self.assertIs(type(self.place1.price_by_night), int)
        self.assertEqual(self.place1.price_by_night, 0)
        self.assertIs(type(self.place1.latitude), float)
        self.assertEqual(self.place1.latitude, 0.0)
        self.assertIs(type(self.place1.longitude), float)
        self.assertEqual(self.place1.longitude, 0.0)
        self.assertIs(type(self.place1.amenity_ids), list)
        self.assertEqual(len(self.place1.amenity_ids), 0)
        self.assertIs(type(self.place1.created_at), datetime.datetime)
        self.assertIs(type(self.place1.updated_at), datetime.datetime)

    def test_inherits(self):
        """ Test if inherits from BaseModel """
        self.assertIsInstance(self.place1, BaseModel)
