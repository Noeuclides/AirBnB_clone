#!/usr/bin/pyhton3
from .base_model import BaseModel

class User(BaseModel):
    '''User class'''
    place_id = ""
    user_id = ""
    text = ""
