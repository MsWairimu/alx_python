"""This module improves the class by raising an exception"""

BaseGeometry = __import__('6-rectangle').Rectangle


class Rectangle(BaseGeometry):
    """class that inherits BaseGeometry"""

    def __init__(self, width, height):
        """instantiation with width and height"""
        self.__width = super().integer_validator('width', width)
        self.__height = super().integer_validator('height', height)

    def area(self):
        """calculate and return the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """method returns a string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
