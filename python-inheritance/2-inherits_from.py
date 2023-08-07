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
    return issubclass(type(obj), a_class) and type(obj) is not a_class
