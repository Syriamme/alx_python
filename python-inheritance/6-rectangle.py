"""
geometry module
This module contains the definition of the class BaseGeometry and a class Rectangle
that inherits from BaseGeometry. BaseGeometry is a base class for representing geometric shapes,
while Rectangle represents a specific shape with width and height.
"""

class BaseGeometry:
    """
    A base class representing geometric shapes.
    
    Attributes:
        None

    Methods:
        area(self): Raises an exception since area calculation is not implemented.
        integer_validator(self, name, value): Validates that the value is a positive integer.
    """

    def area(self):
        """
        Calculate the area of the geometric shape.

        Raises:
            Exception: This method should be implemented in the subclass.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that the value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """
    A class representing rectangles.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(self, width, height): Initializes a Rectangle instance with the given width and height.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If the width or height is not an integer.
            ValueError: If the width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
