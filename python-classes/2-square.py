"""
Module that provides a Square class
"""

class Square:
    """
    Square class representing a square. 
    Defined by a single attribute. 
    """

    def __init__(self, size=0):
        """
        The Square class constructor.
        Param:
            size: length of a side of the square set to default (0).
        Raises:
            TypeError & valueError
        """
        
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        
        elif size < 0:
            raise ValueError('size must be >= 0')
        
        else:
            self.__size = size
    def area(self):
        """
       Calculating the area of the square.
        Return:
        int:The area of the square.
        """
        
        return self.__size ** 2