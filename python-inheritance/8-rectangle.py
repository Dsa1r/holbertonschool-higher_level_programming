#!/usr/bin/python3
"""Define a class"""


class rectangle(BaseGeometry):
    """DefineDo a class"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
