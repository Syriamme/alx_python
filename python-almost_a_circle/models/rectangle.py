"""
Module defining the Rectangle derived class
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inheriting from the base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the class

        Atrr:
            width: Rectangle width
            height: Rectangle width
            
            y: Y axis
            x: X axis
            id: object ID
        """
        super().__init__(id)
        self.height = height
        self.width = width
        self.y = y
        self.x = x

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """
        wdith getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """
        x getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        calulating the rectangle area
        """

        return (self.width * self.height)

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        """

        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle = rectangle + (" " * self.x)
            rectangle = rectangle + ("#" * self.width) + "\n"
        print(rectangle, end='')



    def __str__(self):
        """
        Modifying the inbuilt
        """

        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.__x, self.__y,
            self.__width, self.__height)
    

    def update(self, *args, **kwargs):
        """
        Update the class Rectangle by improving the public method def display(self)

        Args:
        1st arg: should be id attribute
        2nd arg: should be width attribute
        3rd arg: should be height attribute
        4th arg: should be x attribute
        5th arg: should be y attribute
        """
        if args is not None and len(args) > 0:
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                elif key == 1:
                    self.width = value
                elif key == 2:
                    self.height = value
                elif key == 3:
                    self.x = value
                elif key == 4:
                    self.y = value
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "height":
                    self.height = value
                if key == "width":
                    self.width = value
                if key == "y":
                    self.y = value
                if key == "x":
                    self.x = value


    def to_dictionary(self):
        """
        Returns the dictionary which is a representation of a Rectangle
        """
        return {
            "id": self.id,
            "height": self.height,
            "width": self.width,
            "y": self.y,
            "x": self.x,
        }
    