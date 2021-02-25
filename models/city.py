#!/usr/bin/python3
"""
City Module - contains the City class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Defines the class attributes/methods"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Class constructor"""
        super().__init__(*args, **kwargs)

