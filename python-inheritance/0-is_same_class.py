"""
The module is a function to check if a given object is similar to an instance.

It fails to consider inheritance, which means it will return False, 
when the object is an instance of a subclass of the class.

"""

def is_same_class(obj, a_class):
    """
    This function checks if the given object is an instance of the given class.
    It fails to consider inheritance, and therefore 
    only returns True if the object's
    type matches the specified class exactly.

    :param obj: The object which class is to checked
    :type obj: object

    :param a_class: The class against which the object is to be checked
    :type a_class: class

    :return: True while the object is similar to 
    instance of the class specified
    :rtype: bool
    """
    return type(obj) is a_class