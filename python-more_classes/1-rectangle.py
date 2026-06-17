#!/usr/bin/python3
"""create a class with attribute"""


class Rectangle:
    """create class"""
    def width(self, newW):
        """define calss setter for width"""
        if type(newW) is not int:
            raise TypeError("width must be an integer")
        if newW < 0:
            raise ValueError("width must be >= 0")
        self.width=newW

    def width(self):
        return self.width

    def height(self, newH):
        """define calss setter for height"""
        if type(newH) is not int:
            raise TypeError("height must be an integer")
        if newH < 0:
            raise ValueError("height must be >= 0")
        self.height=newH
    
    def height(self):
        return self.height

    def __init__(self, height=0, width=0):
        self.width=width
        self.height=height
