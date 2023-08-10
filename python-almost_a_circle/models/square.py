"""
Module defining the square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class square that is inheriting from the Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)


    def __str__(self):
        """
        modifying the inbuilt method
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.width)

    @property
    def size(self):
        return self.width
    

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        updating attribute size

        If no args : set attributes with kwargs
        If args: width, height, x, y
        """
        if args:
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                elif key == 1:
                    self.size = value
                elif key == 2:
                    self.x = value
                else:
                    self.y = value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        The dictionary definition
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y,
        }
    