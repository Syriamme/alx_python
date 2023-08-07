# This module defines the Square class, inheriting from Rectangle.
# It includes methods for instantiation and calculating the area
# of the square with the given size.

class Square(Rectangle):
    """
    A class representing squares.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a Square instance with the given size.
        area(self): Returns the area of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with the given size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
