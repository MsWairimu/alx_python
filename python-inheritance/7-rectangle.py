"""
This is module for class Basegeometry.
"""
class BaseMetaClass(type):
    """
    This is a BaseMetaClass
    """
    
    
    def __dir__(cls):
        """
        This function removes the __init_subclass (method) from the default method inherited from the parent class
        """
        return [attribute for attribute in super().__dir__() if attribute != "__init_subclass__"]

class BaseGeometry(metaclass=BaseMetaClass):
        """
        This is class BaseGeometry.
        """
        
        def __dir__(cls):
            """
            This function removes the __init_subclass (method) from the default method inherited from the parent class
            """
            return [attribute for attribute in super().__dir__() if attribute != "__init_subclass__"]

class BaseGeometry:
        """
        This is class BaseGeometry.
        """
        
        def area(self):
            raise Exception ("area() is not implemented")

        def integer_validator(self, name, value):
            self.name = name
            if type(value) is not int:
                raise TypeError (f"{name} must be an integer")
            if value <= 0:
                raise ValueError (f"{name} must be greater than 0")

        def __dir__(cls) -> None:
             attributes = super().__dir__()
             return [x for x in attributes if x != '__init_subclass__']
                
class Rectangle(BaseGeometry):
    """
    This is a class Rectangle
    """
    
    def __init__(self, width, height):
        """
        This is an integer validator method
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ returns the area of the object."""
        return self.__width * self.__height

    def __str__(self):
        """ str magic method"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
    
    def __dir__(cls):
            
            """
            This function removes the __init_subclass (method) from the default method inherited from the parent class
            """
            return [attribute for attribute in super().__dir__() if attribute != "__init_subclass__"]
    
