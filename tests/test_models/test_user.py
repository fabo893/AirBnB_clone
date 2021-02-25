#!/usr/bin/python3
"""
Test Module - contains tests for the User class
"""

import unittest
from models.user import User
from models.base_model import BaseModel
import datetime


class TestUser(unittest.TestCase):
    """Defines the tests for the class"""

    @classmethod
    def setUpClass(cls):
        """Sets the objects to be tested"""
        cls.user1 = User(email="betty@holbertonschool.com",
                         password="betty", first_name="Betty",
                         last_name="Holbie")

    def test_new_instance(self):
        """Tests the creation of a new instance"""
        user2 = User()
        self.assertIs(type(user2.email), str)
        self.assertIs(type(user2.password), str)
        self.assertIs(type(user2.first_name), str)
        self.assertIs(type(user2.last_name), str)
        self.assertEqual(self.user1.email, "betty@holbertonschool.com")
        self.assertEqual(self.user1.password, "betty")
        self.assertEqual(self.user1.first_name, "Betty")
        self.assertEqual(self.user1.last_name, "Holbie")
        self.assertEqual(user2.email, "")
        self.assertEqual(user2.password, "")
        self.assertEqual(user2.first_name, "")
        self.assertEqual(user2.last_name, "")
        self.assertIs(type(user2.id), str)
        self.assertIs(type(user2.created_at), datetime.datetime)
        user5 = User()
        user4 = User()
        self.assertNotEqual(user4.id, user5.id)

    def test_name(self):
        """Tests the name attribute"""
        self.assertIs(type(self.user1.first_name), str)
        self.assertEqual(self.user1.first_name, "Betty")

    def test_inheritance(self):
        """Tests that user inherits from BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))
