#!/usr/bin/python3
"""
Review Module - contains the Review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Defines the class attributes/methods"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(sel, *args, **kwargs):
        """Class constructor"""
        super().__init__(*args, **kwargs)
