#!/usr/bin/python3
"""Define the module for a function"""


def inherits_from(obj, a_class):
    """Define a method to ensure if obj inhernted"""
    if type(obj) is not a_class:
        return isinstance(obj, a_class)
    return False
