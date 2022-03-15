#!/usr/bin/python3
'''
write class user that inherits
from BaseModel
'''
from models.base_model import BaseModel


class User(BaseModel):
    ''' definition instance '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
