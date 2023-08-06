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
