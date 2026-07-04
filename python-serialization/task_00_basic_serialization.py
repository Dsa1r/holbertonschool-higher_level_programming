#!/usr/bin/env python3
""""Module that create a basic serialization"""


import json


def serialize_and_save_to_file(data, filename):
    """Prototype to serialize and save data to the specified file"""

    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Prototype to load and deserialize data from the specified file"""

    with open(filename, "r") as f:
        return json.load(f)
