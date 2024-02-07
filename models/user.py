#!/usr/bin/python3
"""user class, subclass of BaseModel
"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    '''subclass of BaseModel class'''

    first_name = ""
    last_name = ""
    email = ""
    password = ""
