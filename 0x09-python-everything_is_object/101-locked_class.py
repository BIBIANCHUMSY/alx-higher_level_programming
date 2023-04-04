#!/usr/bin/python3
"""defines a locked class"""


class LockedClass:
    """
    Prevents the user from instantiating new LockedClass attributes
    except the attribute is called 'first_name'.
    """

    __slots__ = ["first_name"]
