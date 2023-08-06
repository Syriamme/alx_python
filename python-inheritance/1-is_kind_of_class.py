""""
The module checks if the object is an instance of a class that inherited from

This module contains a function to check whether an object is an instance of a given class 
or subclasses.
"""

def is_kind_of_class(obj, a_class):
    
    """
    Function to determine if an object is an instance of a class
    or subclasses.
    
    :para obj: The object being checked

    :para a_class: The class being checked against

    :return:True if  object is an instance of the given class
            or any of its subclasses,
    otherwise, False.
    """

    return isinstance(obj, a_class)