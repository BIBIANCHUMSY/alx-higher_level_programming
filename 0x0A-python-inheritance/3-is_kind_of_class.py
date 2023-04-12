#!/usr/bin/python3
"""Define a class and inherited class to check function."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inherited instance of a class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj.
    Returns:
        If object is an instance or inherited instance of a_class - True.
        Else - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
