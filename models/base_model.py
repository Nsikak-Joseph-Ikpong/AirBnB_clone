#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models


class BaseModel():
    """Parent class for AirBnB clone project.

    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __repr__(self)
        save(self)
        to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """Initialize attributes: uuid4, dates when class was created"""
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value, date_format)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, date_format)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return class name, id, and the dictionary."""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def __repr__(self):
        """Return string representation."""
        return self.__str__()

    def save(self):
        """Update current datetime and save to serialized file."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return dictionary of BaseModel with string formats of times."""
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic
