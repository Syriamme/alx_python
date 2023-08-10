"""
models.base- The module containing the Base class.
"""


class Base:
    """
    Base class
    Attrs:
    __nb_objects (int): Private class attribute tracking the object count.
    id (int): Public instance attribute that is showing the objects's ID.
    """
    
    __nb_objects = 0
    
    def __init__(self, id=None):
        """
        Constructor        
        Args:
            id: The object ID.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
