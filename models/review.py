#!/usr/bin/python3
"""
Review class, a subclass of BaseModel class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A subclass of BaseModel class
    Public class attributes:
        user_id:            (str) will be Place.id
        text:             (str) will be User.id
        place_id:                (str)
    """
    user_id = ""
    text = ""
    place_id = ""
