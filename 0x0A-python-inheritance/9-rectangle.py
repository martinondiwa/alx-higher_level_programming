#!/usr/bin/python3
"""
    Rectangle class inheriting from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
            Initialize rectangle from BaseGeometry
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Define the area
        """
        return self.__width * self.__height

    def __str__(self):
        """
            Rectangle with str
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)  # Removed extra parenthesis

