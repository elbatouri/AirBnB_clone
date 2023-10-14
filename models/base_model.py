#!/usr/bin/python3

" baseModel Class "
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """classes constructor"""

    def __init__(self, *args, **kwargs):
        """ new BaseModel initiation

        Args:
             *args : not used in this case
             **kwargs (dict) : pair attributes of key and value

        """
        tf = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:

            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, tf)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def save(self):
        "change the updated time to current"

        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        return the pair of key/value dictionary instance
        that represent the class name of the object
        """
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict

    def __str__(self):
        "method that define the form of print"
        cl_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cl_name, self.id, self.__dict__)
