#!/usr/bin/python3

"""Defines an inherited list class named MyList."""

class MyList(list):
    """Implements sorted printing for the built-in list of the class."""

    def print_sorted(self):
        """Prints a list in sorted ascending order."""
        print(sorted(self))
