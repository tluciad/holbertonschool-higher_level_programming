#!/usr/bin/python3
"""creating a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Private instance attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter of x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter of y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ adding the public method"""
        return(self.__height*self.__width)
        """adding the public method returns the
        area value of the Rectangle"""

    def display(self):
        """adding the public method that prints
        in stdout the Rectangle"""
        if self.__y > 0:
            for i in range(self.__y):
                print()
        for height in range(self.__height):
            if self.__x > 0:
                print(" " * self.__x, end="")
            for width in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """prints a rectangle using '#'"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """public method that assigns an argument
        to each attribute"""
        if len(args) == 0:
            for key in kwargs:
                setattr(self, key, kwargs[key])
        else:
            tupla = ["id", "width", "height",
                     "x", "y"]
            for i in range(len(args)):
                setattr(self, tupla[i], args[i])

    def to_dictionary(self):
        """ that returns the JSON string representation of
        list_dictionaries"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
