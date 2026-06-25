#!/usr/bin/env python3
"""Define shapes using abstract base class and duck typing."""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Return area."""

    @abstractmethod
    def perimeter(self):
        """Return perimeter."""


class Circle(Shape):
    """Circle class."""

    def __init__(self, radius):
        """Initialize circle."""
        self.radius = abs(radius)

    @property
    def radius(self):
        """Get radius."""
        return self.__radius

    @radius.setter
    def radius(self, value):
        """Set radius (always positive)."""
        self.__radius = abs(value)

    def area(self):
        """Calculate area."""
        return 3.141592653589793 * (self.__radius ** 2)

    def perimeter(self):
        """Calculate perimeter."""
        return 2 * 3.141592653589793 * self.__radius


class Rectangle(Shape):
    """Rectangle class."""

    def __init__(self, width, height):
        """Initialize rectangle."""
        self.width = abs(width)  
        self.height = abs(height)

    @property
    def width(self):
        """Get width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width (always positive)."""
        self.__width = abs(value)

    @property
    def height(self):
        """Get height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height (always positive)."""
        self.__height = abs(value)

    def area(self):
        """Calculate area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate perimeter."""
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """Print shape info."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
