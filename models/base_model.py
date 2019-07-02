#!/usr/bin/python3
import uuid
import datetime
import models

class BaseModel:
    ''' Base Class'''
    def __init__(self, *args, **kwargs):
        ''' init '''
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    self.created_at = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    setattr(self, key, value)
            
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        ''' str method '''
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        ''' save method '''
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        ''' dict method '''
        new_dict = self.__dict__.copy()
        for key, val in new_dict.items():
            if type(val) is datetime.datetime:
                new_dict.update({key : val.isoformat()})
        new_dict.update({'__class__' : self.__class__.__name__})
        return new_dict


