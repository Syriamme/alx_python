"""
Module for inheritance checking.
"""


def inherits_from(obj, a_class):
    """
    Checking if the object is an instance of
    a class inherited from the class.
    Params:
    - obj: The object
    - a_class: The class
    Returns:
    True,
    if obj is an instance
    Otherwise False.
    """
    object_class = type(obj)
    return issubclass(object_class, a_class) and object_class is not a_class
