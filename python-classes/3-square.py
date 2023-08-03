"""
Module that provides a Square class
"""

class Square:
    """
    Square class representing a square. 
    Defined by a single attribute: size, which represents the length of a side of the square.
    """

    def __init__(self, size=0):
        """
        The Square class constructor.
        Param:
            size: length of a side of the square set to default (0).
        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        The getter method for the size attribute of the Square class.
        Returns:
            int: The size (length of a side) of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        The setter method for the size attribute of the Square class.
        Parameters:
            value (int): The new size (length of a side) of the square.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """
        Calculating the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
