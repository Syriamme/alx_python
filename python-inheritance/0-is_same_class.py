def is_same_class(obj, a_class):
    """
    Determine if an object is exactly an instance of a specified class.

    This function compares the type of the object with the specified class.
    It returns True if the object is exactly an instance of the class, otherwise False.

    Args:
        obj (object): The object to be checked.
        a_class (type): The class type to be compared with.

    Returns:
        bool: True if the object is exactly an instance of the specified class, otherwise False.
    """
    return type(obj) is a_class
