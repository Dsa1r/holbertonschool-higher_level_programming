#!/usr/bin/python3
"""Define the module"""


class VerboseList(list):
    """Define the class"""

    def append(self, num):
        super.append(num)
        print(f"Added {num} to the list.")

    def extend(self, iterater):
        super.extend(iterater)
        print(f"Extended the list with {x} items.")

    def remove(self, num):
        super.remove(num)
        print(f"Removed {num} from the list.")

    def pop(self, num):
        item = super().pop(num)
        print(f"Popped {item} from the list.")
        return item
