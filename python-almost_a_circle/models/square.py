#!/usr/bin/python3

"""
The module defining the square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A derived class inherited from Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)


    def __str__(self):
        """
        Modifying the inbuilt
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.width)


    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """
        Updating the square attributes
        If no args: Attributes should be set with kwargs
        If args: attributes should be: id, width, height, x, y (in that order)
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
            if "y" in kwargs:
                self.y = kwargs["y"]
            if "x" in kwargs:
                self.x = kwargs["x"]


    def to_dictionary(self):
        """
        Returning the dictionary definition
        """
        return {
            "id": self.id,
            "size": self.width,
            "y": self.y,
            "x": self.x,
        }
