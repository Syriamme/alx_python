class Square:
    """Represents a square geometric shape.

    Attributes:
        __size (int or float): Private attribute that defines the size of the square's side. 

    Note:
        The attribute size is kept private to maintain control over its values, 
        as it's crucial for computations related to the square (like area).
    """
    def __init__(self, size):
        """Initializes Square with a provided size.

        Args:
            size (int or float): The size of the square's side. 
        """
        self.__size = size
