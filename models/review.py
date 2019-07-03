#!/usr/bin/pyhton3
from .base_model import BaseModel


class Review(BaseModel):
    '''User class'''
    place_id = ""
    user_id = ""
    text = ""
