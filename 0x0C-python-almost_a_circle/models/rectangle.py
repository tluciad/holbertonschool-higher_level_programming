#!/usr/bin/python3
"""creating a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ adding the public method"""
        return(self.__height*self.__width)

    def display(self):
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
        return f"[Rectangle] ({self.id}) \
        {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        if args is not None and len(args) is not 0:
            list = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}
