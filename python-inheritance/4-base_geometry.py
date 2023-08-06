# File: base_geometry.py

# Define a module named base_geometry

class BaseGeometry:
    """
    A base class representing geometric shapes.

    Attributes: None

    Methods:
        area(self): Raises an exception since area calculation is not implemented.
    """

    def area(self):
        """
        Calculate the area of the geometric shape.

        Raises:
            Exception: This method should be implemented in the subclass.
        """
        raise Exception("area() is not implemented")
