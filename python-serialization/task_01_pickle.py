#!/usr/bin/env python3
"""Pickling custom class module"""

import pickle

class CustomObject:
"""Custom object with serialization support"""

```
def __init__(self, name, age, is_student):
    """Initialize object attributes"""
    self.name = name
    self.age = age
    self.is_student = is_student

def display(self):
    """Display object data"""
    print(f"Name: {self.name}")
    print(f"Age: {self.age}")
    print(f"Is Student: {self.is_student}")

def serialize(self, filename):
    """Serialize object to file"""
    try:
        with open(filename, "wb") as file:
            pickle.dump(self, file)
    except (OSError, pickle.PickleError):
        return None

@classmethod
def deserialize(cls, filename):
    """Deserialize object from file"""
    try:
        with open(filename, "rb") as file:
            obj = pickle.load(file)
            if isinstance(obj, cls):
                return obj
    except (OSError, pickle.PickleError, EOFError):
        return None
    return None
```
