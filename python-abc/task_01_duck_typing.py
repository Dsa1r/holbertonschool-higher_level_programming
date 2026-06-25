#!/usr/bin/env python3
"""Define shapes using abstract base class and duck typing."""

from abc import ABC, abstractmethod
import math


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
        r = self.radius
        return math.pi * (r * r)

    def perimeter(self):
        """Calculate perimeter."""
        r = self.radius
        return 2 * math.pi * ((r * r) ** 0.5)


class Rectangle(Shape):
    """Rectangle class."""

    def __init__(self, width, height):
        """Initialize rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate area."""
        w = self.width
        h = self.height
        return ((w * w) ** 0.5) * ((h * h) ** 0.5)

    def perimeter(self):
        """Calculate perimeter."""
        w = self.width
        h = self.height
        return 2 * (((w * w) ** 0.5) + ((h * h) ** 0.5))


def shape_info(shape):
    """Print shape info."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
