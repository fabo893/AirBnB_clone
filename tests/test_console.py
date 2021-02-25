#!/usr/bin/python3
"""
    Test Module for the console
"""


from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

cls_list = ["Amenity", "BaseModel", "City", "Place", "Review", "State", "User"]


class TestConsole(unittest.TestCase):
    """ Test class for the console """

    def test_quit(self):
        """ Testing for quit command """

