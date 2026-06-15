#!/usr/bin/python3
"""Define a square class."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0,0)):
        """Initialize a square with a given size."""
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.__position = position

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position (self) :
        """Get/set the current position of the square."""
        return self.__position

    @position.setter
    def position (self, value) :
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all (isinstance (num, int) for num in value) or
                not all (num >= 0 for num in value)):
            raise TypeError ("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print (self):
        """Print the square with the size and position"""
        if self.__size == 0:
            print()
            return
        [print() for i in range(0, self.__position[1])]
        for i in range (0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print()
