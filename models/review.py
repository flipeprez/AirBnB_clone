#!/usr/bin/python3
'''
write Amenity that inherits
from BaseModel
'''
from models.base_model import BaseModel


class Review(BaseModel):
    ''' definition instance '''
    place_id = ""
    user_id = ""
    text = ""
