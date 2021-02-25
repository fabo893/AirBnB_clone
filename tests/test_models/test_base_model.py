#!/usr/bin/python3
"""
Test Module - contains tests for the BaseModel class
"""

from models.base_model import BaseModel
import unittest
import models
from models import storage
import os


class TestBaseModel(unittest.TestCase):
    """Defines the class tests"""

    @classmethod
    def setUpClass(cls):
        """Defines class objects before running tests"""
        cls.base1 = BaseModel()

    def test_new_instance(self):
        """Tests the creation of new instance"""
        self.assertIs(type(self.base1.id), str)

    def test_str(self):
        """Tests the string representation of the object"""
        expected = "[BaseModel] ({}) {}".format(self.base1.id,
                                                self.base1.__dict__)
        self.assertEqual(str(self.base1), expected)

    def test_save(self):
        """Tests the save method"""
        self.base1.save()
        self.assertNotEqual(self.base1.created_at, self.base1.updated_at)
        base2 = BaseModel()
        idd = base2.id
        base2.name = "betty"
        base2.save()
        storage.reload()
        key = "BaseModel.{}".format(idd)
        objs = storage.all()[key]
        self.assertTrue(hasattr(objs, "name"))
        self.assertTrue(objs.name == "betty")
        self.assertTrue(os.path.exists('file.json'))

    def test_to_dict(self):
        """Tests to_dict method"""
        dic = self.base1.to_dict()
        self.assertIs(type(dic), dict)
        self.assertTrue('__class__' in dic)
        self.assertIs(type(dic['created_at']), str)
        self.assertIs(type(dic['updated_at']), str)

    def test_storage(self):
        """Tests the storage instance"""
        dic = models.storage.all()
        self.assertTrue(dic)
