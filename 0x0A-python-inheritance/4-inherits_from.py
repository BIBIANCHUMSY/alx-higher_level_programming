#!/usr/bin/python3
"""Define an inherited class to check function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If object is an inherited instance of a_class - True.
        Else - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
