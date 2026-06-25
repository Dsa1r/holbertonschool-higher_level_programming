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
        self.radius = radius

    def area(self):
        """Calculate area."""
        return 3.141592653589793 * (self.radius ** 2)

    def perimeter(self):
        """Calculate perimeter."""
        return 2 * 3.141592653589793 * self.radius


class Rectangle(Shape):
    """Rectangle class."""

    def __init__(self, width, height):
        """Initialize rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate area."""
        return self.width * self.height

    def perimeter(self):
        """Calculate perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print shape info."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
