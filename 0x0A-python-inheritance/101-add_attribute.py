#!/usr/bin/python3
"""Defininig a function that add attributes to objects."""


def add_attribute(obj, att, value):
    """Adding a new attribute to an object if possible.
    Args:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add to object.
        value (any): The value of attribute.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
