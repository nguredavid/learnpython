#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):

        if type(width) is not int:
            raise TypeError("Width must be an integer"
        if type(height) is not int:
            raise TypeError("Height must be an integer")
        if type(x) is not int:
            raise TypeError("X must be an integer")
        if type(y) is not int:
            raise TypeError("Y must be an integer")
        if width <= 0:
            raise ValueError("width must be greater than zero")
        if height <= 0:
            raise ValueError("Height must be greate than zero")
        if x <= 0:
            raise ValueError("X must be greater than zero")
        if y <= 0:
            raise ValueError("Y must be greater than zero")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

