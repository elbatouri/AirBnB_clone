#!/usr/bin/python3
"""the file storage class"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """a storage method that help store instances.
    Attributes:
        __file_path (str): storage file's name.
        __objects (dict): instances dictionary.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary __object"""
        return FileStorage.__objects

    def new(self, obj):
        """Serialize __objects to the JSON file __file_path."""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serialize the object stored"""
        op_dict = FileStorage.__objects
        obj_dict = {obj: op_dict[obj].to_dict() for obj in op_dict.keys()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserialization function"""
        try:
            with open(FileStorage.__file_path) as f:
                des_file = json.load(f)
                for o in des_file.values():
                    cl_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cl_name)(**o))
        except FileNotFoundError:
           return

