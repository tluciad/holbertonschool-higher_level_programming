#!/usr/bin/python3
"""creating a Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        """super class with id, x, y, width and height"""

    @property
    def size(self):
        """getter size square"""
        return self.width

    @size.setter
    def size(self, value):
        """setter size square"""
        self.width = value
        self.height = value

    def __str__(self):
        """method should return [Square] (<id>) <x>/<y>
        <size> - in our case, width or height"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """adding the public method
        that assigns attributes"""
        if args is not None and len(args) != 0:
            list = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Square by adding the public method
        that returns the dictionary"""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
            }