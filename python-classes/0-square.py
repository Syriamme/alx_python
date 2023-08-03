"""
The module provides a Square class
The Square class will create and manipulate Square objects.
"""

class Square:
    """
    A Square class. 
    Characterized by a single attribute: 
    size- represents square length. 
    """

    def __init__(self, size):
        """
        Constructor for the Square class.
        Parameters:
            size (int or float): Size (length of a side) of the square.
        """
        self.__size = size


    def get_size(self):
        """
        Getter method (size attribut)e.
        Returns:
            float or int: Side length size of the square.
        """
        return self.__size
    

    def set_size(self, new_size):
        """
        Size attribute of the Square class (setter method).

        Param:
            new_size of the square sides.
        Returns:
            None
        """

        self.__size = new_size