"""
The module for rectangle class
"""
from models.base import Base

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
        
    
    @property
    def height(self):
        """
        height getter
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        height setter
        """
        if type(value) is not int:
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height must be > 0")
        self.__height = value
    
    @property
    def width(self):
        """
        The width getter
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        The width setter
        """
        
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    @property
    def y(self):
        """
        y getter
        """
        return self.__y
    
    @y.setter
    def y(self, value):
        """
        y setter
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    
    @property
    def x(self):
        """
        x getter
        """
        return self.__x
    
    @x.setter
    def x(self, value):
        """
        x setter
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value
