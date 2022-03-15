#!/usr/bin/python3
'''class filestorage'''
from models.base_model import BaseModel
from models.user import User
import json


class FileStorage:
    '''serialize instance to JSON'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''return the dictionary'''
        return(self.__objects)

    def new(self, obj):
        '''set objects in objects with key'''
        keys = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[keys] = obj

    def save(self):
        '''serializes objects to JSON path'''
        odic = {}
        try:
            with open(self.__file_path, "w+") as wf:
                for key, val in self.__objects.items():
                    odic[key] = val.to_dict()
                json.dump(odic, wf, default=str)
        except Exception as ex:
            pass

    def reload(self):
        '''deserealizes the JSON file to object'''
        try:
            with open(self.__file_path) as wd:
                my_dict = json.load(wd)
                for key, val in my_dict.items():
                    my_object = key.split('.')
                    class_name = my_object[0]
                    x = eval(class_name)(**val)
                    self.__objects[key] = x
        except Exception as ex:
            pass
