"""
base_geometry module
"""

class BaseGeometry:
    """
    Base class for geometric shapes

    Attributes: No attribute

    Methods:
        area(self): Raises an exception if not implemented
        integer_validator(self, name, value): Will Validate that the value
        is positive integer
    """

    def area(self):
        """
        Area of the geometric shape

        Raises:
            Exception: if not implemented in the subclass
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validating positive integer

        Args:
            name (str): The name
            value (int): The value

        Raises:
            TypeError: Value fails to be an integer
            ValueError: Value is less than or equal to 0
        """
        
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        