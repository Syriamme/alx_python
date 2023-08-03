class Square:
    """
    This class represents a square with a private size attribute.
    """

    def __init__(self, size):
        """
        Initialize a square with the given size.
        """
        self.__size = size

    def __dict__(self):
        """
        Returns the dictionary representation of the square object.
        """
        return {'size': self.__size}


mysquare = Square(3)
print(type(mysquare))
# Output: <class '__main__.Square'>
print(mysquare.__dict__)
# Output: {'size': 3}

mysquare = Square(89)
print(type(mysquare))
# Output: <class '__main__.Square'>
print(mysquare.__dict__)
# Output: {'size': 89}

try:
    print(my_square.size)
except Exception as e:
    print(e)
    # Output: 'Square' object has no attribute 'size'

try:
    print(mysquare._size)
except Exception as e:
    print(e)
    # Output: 'Square' object has no attribute '_size'
