#!/usr/bin/python3

"""
Module with a class Rectangle.
Rectangle being the subclass.
"""


BaseGeometry = __import__('5-base_geometry').BaseGeometry
        
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
