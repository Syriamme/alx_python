"""
rectangle module
This module contains the definition of the class Rectangle, which inherits from BaseGeometry.
The Rectangle class represents a geometric shape with a width and height, both of which must be positive integers.
"""

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
