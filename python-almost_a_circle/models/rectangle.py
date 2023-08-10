from models.base import Base
"""
The module for rectangle class
"""

class Rectangle(Base):
    """
    Rectangle class that is inheriting from Base Class
    Attr:
    width: the rectangle's width
    height: the rectangle's height
    x: the rectangle's x coordinate
    y: the rectangle's y coordinate
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for initializing the rectangle object
        Arguments:
            width: the rectangle's width
            height: the rectangle's height
            x: the rectangle's x coordinate
            y: the rectangle's y coordinate
            id: the object ID
        """
        super().__init__(id)
        self.height = height
        self.width = width
        self.y = y
        self.x = x
