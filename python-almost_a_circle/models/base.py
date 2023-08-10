"""
models.base
The module has defined the base class
"""
class Base:
    """
    private class attribute that keeps the number of objects created
    Attr: __nb__objects (int): private class
    id(int): public instance attribute 
    """
    __nb__objects = 0
    def __init__(self, id=None):
        """
        Base Class Constructor.
        :Param id: specifies the id of the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1

            self.id = Base.__nb_objects
