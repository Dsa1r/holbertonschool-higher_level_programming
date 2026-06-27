#!/usr/bin/python3
"""Define a module"""


class MyInt:
    """Define a class"""
    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
