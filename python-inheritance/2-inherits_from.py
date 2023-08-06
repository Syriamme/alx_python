"""
Module for inheritance checking

The module provides a function to check,

if an object is an instance of a class

that inherited from the class.
"""

def inherits_from(obj, a_class):
  """
    function to check if the object

    is an instance of a class

    inherited from the class.
    
    Params:
    - obj: The object beinf checked.
    
    - a_class: check inheritance against.

    Returns:

    True,
    if obj is an instance of a class that inherited from the class.

    Otherwise False.
    """
  
  return issubclass(type(obj), a_class) and type(obj) != a_class