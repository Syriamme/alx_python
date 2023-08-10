"""
models.base
This module contains the Base class.
"""

class Base:
    """
    Base class for other classes.
    
    Attributes:
        __nb_objects (int): Private class attribute to keep track of object count.
        id (int): Public instance attribute representing the object's ID.
    """
    __nb_objects = 0
    
    def __init__(self, id=None):
        """
        Initialize a Base object.
        
        Args:
            id (int, optional): The ID for the object. If None, a new ID is assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            
