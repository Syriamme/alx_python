"""
This module provides a Square class. The Square class allows you to create and manipulate Square objects, which represent squares in a geometric context.
"""

class Square:
    """
    A Square class represents a geometric square. 
    It is characterized by a single attribute: size, which represents the length of a side of the square. 
    """

    def __init__(self, size):
        """
        The constructor for the Square class.

        Parameters:
            size (int or float): The size (length of a side) of the square.
        """
        self.__size = size  # private attribute

    # getter method for size
    def get_size(self):
        """
        The getter method for the size attribute of the Square class.

        Returns:
            int or float: The size (length of a side) of the square.
        """
        return self.__size

    # setter method for size
    def set_size(self, new_size):
        """
        The setter method for the size attribute of the Square class.

        Parameters:
            new_size (int or float): The new size (length of a side) of the square.

        Returns:
            None
        """
        self.__size = new_size