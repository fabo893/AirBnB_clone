#!/usr/bin/python3
"""
    Test Module - contains tests for the FileStorage class
"""

import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import os

base1 = BaseModel()


class TestFileStorage(unittest.TestCase):
    """Defines the class tests"""

    def test_all(self):
        """ Test all() method """
        self.assertIs(type(storage.all()), dict)

    def test_new(self):
        """ Test new() method """
        key = "{:s}.{:s}".format(base1.__class__.__name__, base1.id)
        self.assertTrue(key in storage.all())
        objects = storage.all()
        FileStorage._FileStorage__objects = {}
        dic = {}
        for key, value in objects.items():
            obj = value
            storage.new(obj)
            k = obj.__class__.__name__ + "." + obj.id
            dic[k] = obj
        self.assertEqual(dic, FileStorage._FileStorage__objects)

    def test_save(self):
        """ Test save() method """
        json_copy = {}
        obj = storage.all()
        for key in obj:
            json_copy[key] = obj[key].to_dict()
        load = json.dumps(json_copy)
        with open("file.json", "r") as f:
            to_obj = f.read()
        self.assertEqual(json.loads(load), json.loads(to_obj))

    def test_class_attributes(self):
        """Tests that attributes are correct type"""
        self.assertIs(type(FileStorage._FileStorage__file_path), str)
        self.assertIs(type(FileStorage._FileStorage__objects), dict)

    def test_reload(self):
        """ Test reload() method """
        base = BaseModel()
        key = "{}.{}".format(base.__class__.__name__, base.id)
        old_copy = storage.all()
        base.save()
        storage.reload()
        new_copy = storage.all()
        self.assertTrue(key in new_copy)
        self.assertTrue(old_copy == new_copy)

    def test_save_reload(self):
        """More tests for save and reload"""
        base = BaseModel()
        idd = base.id
        base.name = "betty"
        base.save()
        storage.reload()
        key = "BaseModel.{}".format(idd)
        objs = storage.all()[key]
        self.assertTrue(hasattr(objs, "name"))
        self.assertTrue(objs.name == "betty")
        self.assertTrue(os.path.exists('file.json'))
