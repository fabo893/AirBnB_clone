#!/usr/bin/python3
"""
State Module - contains the State class
"""

from models.base_model import BaseModel


class State(BaseModel):
    """Defines the class attributes/methods"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Class constructor"""
        super().__init__(*args, **kwargs)
