# This module defines the Rectangle class, inheriting from BaseGeometry
# It includes methods for instantiation, calculating the area, and string representation
# of the rectangle with given width and height.

class Rectangle(BaseGeometry):
    """
    A class representing rectangles.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(self, width, height): Initializes a Rectangle instance with given width and height.
        area(self): Returns the area of the rectangle.
        __str__(self): Returns a string representation of the rectangle.
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

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string describing the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
