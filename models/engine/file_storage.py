#!/usr/bin/python3
import json
import os.path
import datetime
from ..base_model import BaseModel
from ..user import User
class FileStorage:
    '''file storage class'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''all'''
        return self.__objects
    def new(self, obj):
        '''new'''
        new_object = {str(obj.__class__.__name__ + "." + obj.id) : obj.to_dict()}
        self.__objects.update(new_object)
    def save(self): 
        '''save'''
        with open(self.__file_path, 'w') as my_file:
            json.dump(self.__objects, my_file)
                
    def reload(self):
        '''reload'''
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as my_file:
                self.__objects = json.load(my_file)
            for key in self.__objects:
                temp = self.__objects[key].copy()
                BaseModel(**temp)
