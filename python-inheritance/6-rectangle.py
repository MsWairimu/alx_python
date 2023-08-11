"""This module improves the class by raising an exception"""
BaseGeometry = __import__('5-base_geometry').Rectangle
"""imported from 5-base_geometry"""


class Rectangle(BaseGeometry):
    """class that inherits BaseGeometry"""

    def __init__(self, width, height):
        """instantiation with width and height"""
        self.__width = super().integer_validator('width', width)
        self.__height = super().integer_validator('height', height)
