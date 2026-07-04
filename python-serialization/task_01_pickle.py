#!/usr/bin/env python3
"""Module that serialize and deserialize custom Python objects"""

import pickle


class CustomObject:

    """Class that represents custom objects"""

    def __init__(self, name, age, is_student):
        """Iniatialize a neww custom objects"""

        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the atributs"""

        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        """Prototype to serialize the specified file"""

        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
            return True
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Prototype to deserialize from the specified file"""

        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None 
