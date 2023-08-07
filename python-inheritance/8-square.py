"""
geometry module
This module contains the definition of the class BaseGeometry, class Rectangle that inherits from BaseGeometry,
and class Square that inherits from Rectangle.

Classes:
    BaseGeometry: A base class for representing geometric shapes.
    Rectangle: A class representing rectangles, inheriting from BaseGeometry.
    Square: A class representing squares, inheriting from Rectangle.
"""

class BaseGeometry:
    """
    A base class representing geometric shapes.

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
    A class representing rectangles, inheriting from BaseGeometry.

    Attributes:
        __width (int): The private width of the rectangle.
        __height (int): The private height of the rectangle.

    Methods:
        __init__(self, width, height): Initializes a Rectangle instance with the given width and height.
        area(self): Returns the area of the rectangle.
        __str__(self): Returns a string representation of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the string representation of the rectangle.

        Returns:
            str: A description of the rectangle in the format "[Rectangle] <width>/<height>".
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    """
    A class representing squares, inheriting from Rectangle.

    Attributes:
        __size (int): The private size of the square's sides.

    Methods:
        __init__(self, size): Initializes a Square instance with the given size.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with the given size.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Return the string representation of the square.

        Returns:
            str: A description of the square in the format "[Square] <size>/<size>".
        """
        return f"[Square] {self.__size}/{self.__size}"
