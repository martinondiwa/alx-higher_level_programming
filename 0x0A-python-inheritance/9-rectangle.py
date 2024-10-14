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
        self.integer_validator('width', width)  # Validate width
        self.integer_validator('height', height)  # Validate height
        self.__width = width  # Private attribute
        self.__height = height  # Private attribute

    def area(self):
        """
        Define the area
        """
        return self.__width * self.__height  # Calculate area

    def __str__(self):
        """
            Rectangle with str
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)  # Return formatted string

