"""
This module provides a Square class. The Square class allows you to create and manipulate Square objects, 
which represent squares in a geometric context.
"""

class Square:
    """
    A Square class represents a geometric square. 
    It is characterized by a single attribute: size, which represents the length of a side of the square. 
    """

    def __init__(self, size=0):
        """
        The constructor for the Square class.

        Parameters:
            size (int, optional): The size (length of a side) of the square. Defaults to 0.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size  # private attribute
