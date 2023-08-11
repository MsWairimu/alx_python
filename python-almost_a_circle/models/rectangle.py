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

class Rectangle(Base):
    """Class representing a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        """Prints the Rectangle instance using '#' characters"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """String representation of the rectangle"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Updates the attributes of the rectangle"""
        args_length = len(args)
        kwargs_length = len(kwargs)

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif key == "width":
                self.width = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value
        
        if args_length > 0:
            self.id = args[0]
        if args_length > 1:
            self.width = args[1]
        if args_length > 2:
            self.height = args[2] 
        if args_length > 3:
            self.x = args[3]
        if args_length > 4:
            self.y = args[4]
