#!/usr/bin/python3
"""
FileStorage Module - serializes instances to a JSON file and
                    deserializes JSON file to instances
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

cls = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City,
       "Place": Place, "State": State, "Review": Review, "User": User}


class FileStorage():
    """Defines the attributes and methods for this class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_copy = {}
        for key in self.__objects:
            json_copy[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as myfile:
            json.dump(json_copy, myfile)

    def reload(self):
        """Deserializes the JSON file to __objects only if the file exists"""
        try:
            with open(self.__file_path, 'r') as myfile:
                obj = json.load(myfile)
            for key in obj:
                self.__objects[key] = cls[obj[key]['__class__']](**obj[key])
        except FileNotFoundError:
            pass
