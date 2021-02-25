#!/usr/bin/python3
"""
Test Module - contains tests for the Review class
"""

import unittest
from models.review import Review
import datetime
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Defines the tests for the class"""

    @classmethod
    def setUpClass(cls):
        """Sets the objects to be tested"""
        cls.rev1 = Review()

    def test_new_instance(self):
        """Tests the creation of a new instance"""
        self.assertIs(type(self.rev1.place_id), str)
        self.assertEqual(len(self.rev1.place_id), 0)
        self.assertIs(type(self.rev1.user_id), str)
        self.assertEqual(len(self.rev1.user_id), 0)
        self.assertIs(type(self.rev1.text), str)
        self.assertEqual(len(self.rev1.text), 0)
        self.assertIs(type(self.rev1.created_at), datetime.datetime)
        self.assertIs(type(self.rev1.updated_at), datetime.datetime)

    def test_inherits(self):
        """ Test if inherits from BaseModel class """
        self.assertIsInstance(self.rev1, BaseModel)
