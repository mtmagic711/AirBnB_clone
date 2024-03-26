#!/usr/bin/python3
"""This is the baseModel module that defines all common
    attributes/methods for other classes:
"""


from datetime import datetime
from uuid import uuid4


class BaseModel():
    """The BaseModel that defines all common attributes and methods"""

    def __init__(self, *args, **kwargs):
        """The consructor"""
        tm_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'], tm_format)
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], tm_format)
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            created_at = datetime.now()
            updated_at = datetime.now()

    def __str__(self):
        """return a string representation of the object."""
        base_name = type(self).__name__
        return "[{}] ({}) {}" .format(base_name, self.id, self.__dict__)

    def save(self):
        """updates the public instance
            attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing
            all keys/values of __dict__ of the instance.
        """
        inst_dict = {}
        inst_dict["__class__"] = type(self).__name__

        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                inst_dict[key] = value.isoformat()
            else:
                inst_dict[key] = value

        return inst_dict
