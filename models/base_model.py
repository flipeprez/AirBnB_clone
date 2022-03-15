#!/usr/bin/python3
'''
Base model module

'''

from datetime import datetime
import models
import uuid


class BaseModel():
    '''class defines all commons attributes/methods for other classes'''
    def __init__(self, *args, **kwargs):
        '''function to inicialize all instances atrributes'''
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, val in kwargs.items():
                if key == '__class__':
                    continue
                tf = "%Y-%m-%dT%H:%M:%S.%f"
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(val, tf))
                else:
                    setattr(self, key, val)

    def __str__(self):
        '''string representation of basemodel'''
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """update the public instance attributte"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
        returns a dictionary containing all
        keys/values of __dict__ instance
        '''
        cpy_dic = self.__dict__.copy()
        cpy_dic['__class__'] = self.__class__.__name__
        cpy_dic['created_at'] = self.created_at.isoformat()
        cpy_dic['updated_at'] = self.updated_at.isoformat()
        return(cpy_dic)
