#!/usr/bin/python3
"""Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """
        Defining the Rectangle class
        Inherits from:
            Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returning private attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting private attribute"""
        self.setter_validation("width", value)
        self.__width = value
    
    @property
    def height(self):
        """Returning private attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting private attribute"""
        self.setter_validation("height", value)
        self.__height = value
    
    @property
    def x(self):
        """Returning private attr"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setting private attr"""
        self.self_validation("x", value)
        self.__x = value

    @property
    def y(self):
        """Returning private attr"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setting the private attr"""
        self.setter_validation("y", value)
        self.__y = value
        