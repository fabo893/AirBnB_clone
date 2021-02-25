#!/usr/bin/python3
"""
Base Module - defines all common attributes/methods for other classes
"""

from datetime import datetime
import models
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """Defines the base for other classes to inherit"""

    def __init__(self, *args, **kwargs):
        """Initializes an object with its attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """Returns the string representation of the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the
        instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        if "created_at" in obj_dict:
            obj_dict['created_at'] = obj_dict['created_at'].strftime(time)
        if "updated_at" in obj_dict:
            obj_dict['updated_at'] = obj_dict['updated_at'].strftime(time)
        return obj_dict
