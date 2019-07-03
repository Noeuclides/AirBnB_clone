#!/usr/bin/python3
import json
import copy
import os.path
import datetime
from ..base_model import BaseModel
from ..user import User
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..place import Place
from ..review import Review


class FileStorage:
    '''file storage class'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''all'''
        return self.__objects
    def new(self, obj):
        '''new'''
        new_object = {str(obj.__class__.__name__ + "." + obj.id) : obj}
        self.__objects.update(new_object)
    def save(self): 
        '''save'''
        new_dict = {}
        with open(self.__file_path, 'w') as my_file:
            for k, v in self.__objects.items():
                new_dict[k] = v.to_dict()
            json.dump(new_dict, my_file)
                
    def reload(self):
        '''reload'''
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as my_file:
                self.__objects = json.load(my_file)
            for key in self.__objects:
                temp = self.__objects[key].copy()
                name = key.split('.')
                self.__objects[key] = eval(name[0] + '(**temp)')
