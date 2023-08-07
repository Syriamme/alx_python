#!/usr/bin/python3


"""
Module with a class Rectangle.
Rectangle being the subclass.
"""

BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class of rectangles, inherited from BaseGeometry.
    Attr:
        __width (int): The private width
        __height (int): The private height

    Methods:
        __init__(self, width, height): Initializes a Rectangle instance
        area(self): Returns the rectangle area.
        __str__(self): Returns rectangle string representation.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance

        Args:
            width (int): The width
            height (int): The height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Return the rectangle's area

        Returns:
            int: The area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return: string representation

        Returns:
            str: Description of the rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    A class showing squares, inherited from Rectangle
    Attr:
    __size (int): The square's sides
    Methods:
    __init__(self, size): Initializes a Square instance
    """
    def __init__(self, size):
        """
        Initializes a Square instance
        Args:
            size (int): The square's sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Return: string representation
        Returns:
        str: Description of the square
        """
        return f"[Square] {self.__size}/{self.__size}"
    