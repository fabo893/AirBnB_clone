#!/usr/bin/python3
"""
Amenity Module - contains the Amenity class
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines the class attributes/methods"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Class constructor"""
        super().__init__(*args, **kwargs)
