"""This module defines a class 'Square'

The 'Square' class defines a square by size, which is private.
"""


class Square:
    """This is a class that defines a square.

    It is defined by its size which is private.
    """

    def __init__(self, size=0):
        """Initializes the square.

        Args:
            size: The size of the square.
        """
        self.__size = size

my_square = Square(3)

try:
    print(my_square.__size)  # Trying to directly access private attribute
except Exception as n:
    print(n)  # Prints "'Square' object has no attribute '__size'"
