"""
base_geometry module
"""

class BaseGeometry:
    """
    Base class for geometric shapes
    Attributes: No attribute
    Methods:
        area(self): Raises an exception if not implemented
        integer_validator(self, name, value): Will Validate that the value
        is positive integer
    """

    def area(self):
        """
        Area of the geometric shape

        Raises:
            Exception: if not implemented in the subclass
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validating positive integer
        Args:
            name (str): The name
            value (int): The value
        Raises:
            TypeError: Value fails to be an integer
            ValueError: Value is less than or equal to 0
        """
        
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        
class Rectangle(BaseGeometry):
    """
    Class showing rectangles
    Attributes:
        __width (int): The width
        __height (int): The height
    Methods:
        __init__(self, width, height): Initializes a Rectangle (instance with width and height).
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle instance
        Args:
            width (int): The width
            height (int): The height
        Raises:
            TypeError: If args is not an integer.
            ValueError: If args is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
        
        print(issubclass(Rectangle, BaseGeometry))
