""""
Module checking if the object is an instance of a class or that inherited from

"""

def is_kind_of_class(obj, a_class):
    
    """
    Function to determine if an object is an instance of a class
    or subclasses.
    
    :para obj: The object

    :para a_class: The class

    :return:True if  object is an instance
    otherwise, False.
    """

    return isinstance(obj, a_class)