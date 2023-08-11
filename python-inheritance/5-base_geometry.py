"""Integer validator- to Write a class BaseGeometry (based on 4-base_geometry.py)."""
class BaseGeometry:
    """
    A class representing basic geometry operations

    ...

    Methods
    -------
    area(self):
        Raises an Exception indicating that the method is not yet implemented.
    integer_validator(self, name, value):
        Validates that the given value is an integer greater than 0.

    """

    def area(self):
        """
        Raises an Exception indicating that the method is not yet implemented.

        Parameters:
        None

        Returns:
        None

        Raises:
        Exception: indicating that the method is not yet implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the given value is an integer greater than 0.

        Parameters:
        name (str): The name of the variable being validated.
        value (int): The value to validate.

        Returns:
        None

        Raises:
        TypeError: if the value is not an integer.
        ValueError: if the value is less than or equal to 0.

        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
