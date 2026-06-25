#!/usr/bin/env python3
"""Define mixins and Dragon class."""


class SwimMixin:
    """Mixin to add swimming ability."""

    def swim(self):
        """Print swimming action."""
        print("The creature swims!")


class FlyMixin:
    """Mixin to add flying ability."""

    def fly(self):
        """Print flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class combining mixins."""

    def roar(self):
        """Print roar action."""
        print("The dragon roars!")
