#!/usr/bin/python3
'''file to storage'''

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
