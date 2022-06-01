#!/usr/bin/python3
"""class Rectangle that defines a rectangle by: (based on 8-rectangle.py)"""


class Rectangle:
    """class that defines a Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """property def width(self): to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property def height(self): to retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return(self.__height*self.__width)

    def perimeter(self):
        """ returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return((self.__width*2)+(self.__height*2))

    def __str__(self):
        """should print the rectangle with the character #"""
        rec = ""
        if self.__width == 0 or self.__height == 0:
            return rec
        for i in range(self.__height):
            rec += (str(self.print_symbol) * self.__width) + "\n"
        return rec[:-1]

    def __repr__(self):
        """return a string representation of the rectangle"""
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)

    def __del__(self):
        """an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() >= rect_2.area():
            return rect_1
        elif rect_2.area() >= rect_1.area():
            return rect_2
    
    @classmethod