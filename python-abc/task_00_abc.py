#!/usr/bin/python3
"""Define aaa"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Define a class"""

    @abstractmethod
    def sound(self):
        """Define a method"""
        pass


class dog(Animal):
    """Define calss"""
    def sound(self):
        return "Bark"


class cat(Animal):
    """Definr a class"""
    def sound(self):
        return "Meow"
