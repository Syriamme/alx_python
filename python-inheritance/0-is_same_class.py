"""
The module - function checking if a given object is similar to an instance.

It fails to consider inheritance, returning False.

"""

def is_same_class(obj, a_class):
    """
    The function checks if an object is an instance of the given class.
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
    object_class = type(obj)

    if object_class is a_class:
        return True
    
    else:
        return False
    