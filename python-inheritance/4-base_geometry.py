"""

Module based on 3-base_geomtry.py
"""

class BaseGeometry:
    """
    Base class for geometric shapes.

    Attributes: No attributes

    Public instance method:
        area(self): Will raise an exception if not implemented.
    """

    def area(self):
        """
        checks the are of the shape.

        Raises:
            Exception: if not implemented in the subclass.
        """
        raise Exception("area() is not implemented")
    