# models/base.py
"""Create class Base"""
class Base:
    """Base class that manages the id attribute for all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for the Base class
        
        Args:
            id (int): Unique identifier for the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
