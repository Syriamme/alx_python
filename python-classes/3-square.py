"""
A Module that gives a Square class

"""

class Square:
    """
    Square class representing a square.
    A single character attribute - size
    """

    def __init__(self, size=0):
        """
        Class constructor.
        Param:
            size - length set to default (0).
        Raises:
            TypeError
            valueError
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method
        Returns:
            int: Square's length of a side.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method

        Parameters:
            int: Length of a side in the square

        Raises:
        ValueError
        TypeError

        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """
        Calculates square area
        Returns:

            int: Area
        
        """
        return self.__size ** 2