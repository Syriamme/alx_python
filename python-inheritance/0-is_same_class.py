"""
This module provides a function to check whether a given object is exactly an instance of a specified class.
It does not consider inheritance, so it will return False if the object is an instance of a subclass of the
specified class.

The primary function in this module is:
    - is_same_class(obj, a_class): Checks if the object is exactly an instance of the specified class.
"""

def is_same_class(obj, a_class):
    """
    This function checks whether the given object is exactly an instance of the specified class.
    It does not take into consideration inheritance, and therefore only returns True if the object's
    type matches the specified class exactly.

    :param obj: The object whose class is to be checked
    :type obj: object
    :param a_class: The class against which the object is to be checked
    :type a_class: class
    :return: True if the object is exactly an instance of the specified class, otherwise False
    :rtype: bool
    """
    return type(obj) is a_class