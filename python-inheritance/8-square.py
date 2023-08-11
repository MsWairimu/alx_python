
"""
Write a class Rectangle that inherits from BaseGeometry (5-base_geometry.py).
"""
Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """
    a class define for square that inherit Rectangle
    """
    def __init__(self, size):
        """
        initialization method for class Square
        """
        Rectangle.integer_validator(self, "size", size)
        self.__size = size

    def area(self):
        """
        Method to calculate area
        """
        return self.__size ** 2
