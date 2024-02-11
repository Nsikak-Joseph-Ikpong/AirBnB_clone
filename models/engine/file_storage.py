#!/usr/bin/python3
'''AirBnB clone project File Storage'''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


# Modified docstring to include more details about the storage engine
class FileStorage:
    """ This is a storage engine for the AirBnB clone project.
    It provides methods to manage objects and their serialization.
    Class Methods:
        all: Returns all objects stored in the file.
        new: Adds a new object to the storage.
        save: Serializes objects into a JSON file.
        reload: Deserializes objects from a JSON file.
    Class Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary of objects stored in memory.
        class_dict (dict): A dictionary mapping class names to class types.
    """
    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}

    def all(self):
        '''Return dictionary of <class>.<id> : object instance'''
        # Added a print statement to indicate when all objects are retrieved
        print("Retrieving all objects from storage...")
        return self.__objects

    def new(self, obj):
        '''Set new __objects to existing dictionary of instances'''
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Save/serialize obj dictionaries to json file"""
        obj_dict = {}

        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(obj_dict, f)
        # Added a print statement to indicate when objects are saved
        print("Objects saved successfully.")

    def reload(self):
        """Deserialize/convert obj dicts back to instances, if it exists"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
            for key, value in new_obj_dict.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
